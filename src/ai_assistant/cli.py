import argparse


def main(args=None):
    parser = argparse.ArgumentParser(
        description="A command-line AI assistant"
    )

    parser.add_argument(
        "--version",
        action="version",
        version="ai-cli-assistant 0.1.0"
    )

    parser.parse_args(args)

    print("AI Assistant")


if __name__ == "__main__":
    main()