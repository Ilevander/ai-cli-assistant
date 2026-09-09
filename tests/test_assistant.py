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

    assert assistant.history.get_messages() == [
        {
            "role": "user",
            "content": "Explique-moi Git",
        },
        {
            "role": "assistant",
            "content": "Simulated Response",
        },
    ]


def test_assistant_keeps_conversation_history(monkeypatch):
    calls = []

    class FakeResponse:
        class Message:
            content = "Simulated Response"

        message = Message()

    def fake_chat(**kwargs):
        calls.append(list(kwargs["messages"]))
        return FakeResponse()

    monkeypatch.setattr(
        "ai_assistant.assistant.chat",
        fake_chat,
    )

    assistant = Assistant()

    assistant.ask("Bonjour")
    assistant.ask("Comment vas-tu ?")

    assert len(calls) == 2

    assert calls[0] == [
        {
            "role": "user",
            "content": "Bonjour",
        }
    ]

    assert calls[1] == [
        {
            "role": "user",
            "content": "Bonjour",
        },
        {
            "role": "assistant",
            "content": "Simulated Response",
        },
        {
            "role": "user",
            "content": "Comment vas-tu ?",
        },
    ]