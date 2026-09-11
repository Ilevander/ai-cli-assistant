#from openai import OpenAI
from ollama import chat
from ai_assistant.history import ConversationHistory
from ai_assistant.tools.datetime import (
    get_current_date,
    get_current_datetime,
    get_current_time,
    get_day_of_week,
)
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

        self.available_tools = {
            "get_current_date": get_current_date,
            "get_current_datetime": get_current_datetime,
            "get_current_time": get_current_time,
            "get_day_of_week": get_day_of_week,
        }

        self.tools = list(self.available_tools.values())


    def ask(self, prompt: str) -> str:
        self.history.add_user_message(prompt)

        response = chat(
            #model="gemma3",
            model="qwen3:8b",
            messages=self.history.get_messages(),
            tools=self.tools,
        )

        if response.message.tool_calls:
            self.history.messages.append(response.message)

            for tool_call in response.message.tool_calls:
                function_name = tool_call.function.name
                function_args = tool_call.function.arguments

                function_to_call = self.available_tools.get(function_name)

                if function_to_call is None:
                    result = f"Unknown tool: {function_name}"
                else:
                    result = function_to_call(**function_args)

                self.history.messages.append(
                    {
                        "role": "tool",
                        "tool_name": function_name,
                        "content": str(result),
                    }
                )

            final_response = chat(
                #model="gemma3",
                model="qwen3:8b",
                messages=self.history.get_messages(),
                tools=self.tools,
            )

            answer = final_response.message.content
        else:
            answer = response.message.content
            
        self.history.add_assistant_message(answer)
        
        return answer