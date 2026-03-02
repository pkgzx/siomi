from src.app.domain.exception.processor_exception import ProcessorException
from src.app.domain.enum.technical_message import TechnicalMessage

class BusinessException(ProcessorException):
    param_value: str

    def __init__(self, exception, technical_message=None, param_value: str = None):
        super().__init__(exception, technical_message)
        self.param_value = param_value
        
        if isinstance(technical_message, TechnicalMessage) and param_value is None:
            param_value= technical_message.get_param()

    def get_param_value(self) -> str:
        return self.param_value