from mirascope.core import openai, prompt_template
from openai.types.chat import ChatCompletionMessageParam
from pydantic import BaseModel


class Chatbot(BaseModel):
    history: list[ChatCompletionMessageParam] = []

    @openai.call(model="gpt-4o-mini", stream=True)
    @prompt_template(
        """
        SYSTEM: You are a helpful assistant.
        MESSAGES: {self.history}
        USER: {question}
        """
    )
    def _call(self, question: str): ...

    def run(self):
        while True:
            question = input("(User): ")
            if question in ["quit", "exit"]:
                print("(Assistant): Have a great day!")
                break
            stream = self._call(question)
            print("(Assistant): ", end="", flush=True)
            for chunk, _ in stream:
                print(chunk.content, end="", flush=True)
            print("")
            if stream.user_message_param:
                self.history.append(stream.user_message_param)
            self.history.append(stream.message_param)


Chatbot().run()
