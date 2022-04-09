from core.validation.type_validation import ParamType
from core.validation.type_validation.string_validator import StringValidator
import uuid


class UUIDValidator(StringValidator):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def validate(self, value: any) -> bool:
        try:
            uuid.UUID(value)
            return True
        except ValueError:
            return False
