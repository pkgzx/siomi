from src.app.domain.enum.technical_message import TechnicalMessage


class ProcessorException(Exception):
    """Process all exceptions of application that can be managed"""
    technical_message: TechnicalMessage

    def __init__(self, exception: Exception, technical_message: TechnicalMessage):
        super(exception)
        self.technical_message = technical_message

    def __init__(self, message: str, technical_message: TechnicalMessage):
        super(message)
        self.technical_message == technical_message

    def get_technical_message(self) -> TechnicalMessage:
        return self.technical_message