from ai_assistant.history import ConversationHistory


def test_history_starts_empty():
    history = ConversationHistory()

    assert history.get_messages() == []


def test_history_stores_user_message():
    history = ConversationHistory()

    history.add_user_message("Hello")

    assert history.get_messages() == [
        {
            "role": "user",
            "content": "Hello",
        }
    ]


def test_history_stores_conversation():
    history = ConversationHistory()

    history.add_user_message("Hello")
    history.add_assistant_message("Hello !")

    assert history.get_messages() == [
        {
            "role": "user",
            "content": "Hello",
        },
        {
            "role": "assistant",
            "content": "Hello !",
        },
    ]