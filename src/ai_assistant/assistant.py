#from openai import OpenAI
from ollama import chat

#class Assistant:
    #def __init__(self):
        #self.client = OpenAI()

    #def ask(self, prompt: str) -> str:
     #   response = self.client.responses.create(
      #      model="gpt-5.6-luna",
       #     input=prompt,
        #)

      #  return response.output_text

class Assistant:
    def ask(self, prompt: str) -> str:
        response = chat(
            model="gemma3",
            messages=[
                {
                    "role": "user",
                    "content": prompt,
                }
            ],
        )
        return response.message.content