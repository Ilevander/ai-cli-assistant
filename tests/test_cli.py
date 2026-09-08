from ai_assistant.cli import main


def test_cli_runs(capsys):
    main([])

    captured = capsys.readouterr()

    assert "AI Assistant" in captured.out


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