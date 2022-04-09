from core.validation.type_validation import ParamType
from core.validation.type_validation.string_validator import StringValidator
import re


class AuthTokenValidator(StringValidator):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def validate(self, value: any):
        regex = re.compile('Bearer *')
        return bool(re.search(regex, value))
