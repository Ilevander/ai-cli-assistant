from ai_assistant.cli import main


def test_cli_runs(capsys):
    main([])

    captured = capsys.readouterr()

    assert "AI Assistant" in captured.out


def test_cli_prompt(capsys):
    main(["Explique-moi Git"])

    captured = capsys.readouterr()

    assert "Explique-moi Git" in captured.out