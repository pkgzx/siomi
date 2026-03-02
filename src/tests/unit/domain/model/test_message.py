import pytest

from src.app.domain.model.message import Message

class TestMessage:
    """Tests of message model"""

    def test_create_success(self):
        """Test create a message with content valid"""

        message = Message(content="Hello")

        assert message is not None
        assert message.content is not None
        assert message.content == "Hello"
    
    def test_create_with_error_empty(self):
        """Test create a message with content invalid"""
        with pytest.raises(Exception):
            message = Message(content=None)
     