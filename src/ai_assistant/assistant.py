#from openai import OpenAI
from ollama import chat
from ai_assistant.history import ConversationHistory

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
    def __init__(self):
        self.history = ConversationHistory()

    def ask(self, prompt: str) -> str:
        self.history.add_user_message(prompt)

        response = chat(
            model="gemma3",
            messages=self.history.get_messages(),
        )

        answer = response.message.content
        self.history.add_assistant_message(answer)
        return answer