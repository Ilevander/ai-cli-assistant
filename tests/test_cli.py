from ai_assistant.cli import main


def test_cli_runs(capsys):
    main([])

    captured = capsys.readouterr()

    assert "AI Assistant" in captured.out