from ai_assistant.assistant import Assistant


def test_assistant_ask(monkeypatch):
    class FakeResponse:
        class Message:
            content = "Simulated Response"

        message = Message()

    def fake_chat(**kwargs):
        return FakeResponse()

    monkeypatch.setattr(
        "ai_assistant.assistant.chat",
        fake_chat,
    )

    assistant = Assistant()

    response = assistant.ask("Explique-moi Git")

    assert response == "Simulated Response"