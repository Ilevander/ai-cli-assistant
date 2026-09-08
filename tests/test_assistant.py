from ai_assistant.assistant import Assistant


class FakeResponse:
    output_text = "Similated Response"


class FakeResponses:
    def create(self, **kwargs):
        return FakeResponse()


class FakeClient:
    def __init__(self):
        self.responses = FakeResponses()


def test_assistant_ask():
    assistant = Assistant.__new__(Assistant)
    assistant.client = FakeClient()

    response = assistant.ask("Explique-moi Git")

    assert response == "Simulated Response"