import argparse


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

    if parsed_args.prompt:
        print(f"You asked: {parsed_args.prompt}")
    else:
        print("AI Assistant")


if __name__ == "__main__":
    main()