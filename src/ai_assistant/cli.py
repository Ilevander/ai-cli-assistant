import argparse

from ai_assistant.assistant import Assistant

def main(args=None):
    parser = argparse.ArgumentParser(
        description="A command-line AI assistant"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ai-cli-assistant 0.1.0",
    )

    parser.add_argument(
        "prompt",
        nargs="?",
        help="Question or instruction for the assistant",
    )

    parsed_args = parser.parse_args(args)

    assistant = Assistant()

    if parsed_args.prompt:

        response = assistant.ask(parsed_args.prompt)
        print(response)
        #print(f"You asked: {parsed_args.prompt}")
        return
    
    print("AI Assistant -conversation mode")
    print("Type 'exit' to quit.")

    while True:
        prompt = input("\nYou  > ")

        if prompt.lower() == "exit":
            print("Goodbye!")
            break

        if not prompt.strip():
            continue

        response = assistant.ask(prompt)
        print(f"AI  > {response}")
    
    
if __name__ == "__main__":
    main()