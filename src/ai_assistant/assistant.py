from openai import OpenAI


class Assistant:
    def __init__(self):
        self.client = OpenAI()

    def ask(self, prompt: str) -> str:
        response = self.client.responses.create(
            model="gpt-5.6-luna",
            input=prompt,
        )

        return response.output_text