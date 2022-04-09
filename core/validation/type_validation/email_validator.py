from core.validation.type_validation import ParamType
from core.validation.type_validation.string_validator import StringValidator
import re


class EmailValidator(StringValidator):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def validate(self, value: any) -> bool:
        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(re.fullmatch(regex, value))
