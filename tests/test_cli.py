from ai_assistant.cli import main


def test_cli_runs(monkeypatch,capsys):
    inputs = iter(["exit"])
    monkeypatch.setattr("builtins.input", lambda _: next(inputs))

    main([])

    captured = capsys.readouterr()

    assert "AI Assistant" in captured.out
    assert "Goodbye!" in captured.out


def test_cli_prompt(monkeypatch, capsys):
    class FakeAssistant:
        def ask(self, prompt):
            return "Simulated Response"

    monkeypatch.setattr(
        "ai_assistant.cli.Assistant",
        FakeAssistant,
    )

    main(["Explique-moi Git"])

    captured = capsys.readouterr()

    assert "Simulated Response" in captured.out


def test_cli_conversation(monkeypatch, capsys):
    class FakeAssistant:
        def __init__(self):
            self.prompts = []

        def ask(self, prompt):
            self.prompts.append(prompt)
            return f"Response to: {prompt}"

    fake_assistant = FakeAssistant()

    monkeypatch.setattr(
        "ai_assistant.cli.Assistant",
        lambda: fake_assistant,
    )

    inputs = iter([
        "Bonjour",
        "Comment vas-tu ?",
        "exit",
    ])

    monkeypatch.setattr(
        "builtins.input",
        lambda _: next(inputs),
    )

    main([])

    captured = capsys.readouterr()

    assert fake_assistant.prompts == [
        "Bonjour",
        "Comment vas-tu ?",
    ]

    assert "Response to: Bonjour" in captured.out
    assert "Response to: Comment vas-tu ?" in captured.out
    assert "Goodbye!" in captured.out