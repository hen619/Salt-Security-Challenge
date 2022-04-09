from core.validation.type_validation import ParamType
from core.validation.type_validation.type_validator import TypeValidator


class StringValidator(TypeValidator):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def validate(self, value: any) -> bool:
        return isinstance(value, str)
