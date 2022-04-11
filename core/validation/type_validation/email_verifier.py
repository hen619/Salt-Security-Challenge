from core.validation.type_validation import ParamType
from core.validation.type_validation.string_verifier import StringVerifier
import re


class EmailValidator(StringVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        if not super(EmailValidator, self).verify(value):
            return False

        regex = re.compile(r'([A-Za-z0-9]+[.-_])*[A-Za-z0-9]+@[A-Za-z0-9-]+(\.[A-Z|a-z]{2,})+')
        return bool(re.fullmatch(regex, value))
