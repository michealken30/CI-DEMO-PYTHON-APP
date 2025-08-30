from app.main import get_message

def test_get_message_returns_hello():
    assert get_message() == "Hello"