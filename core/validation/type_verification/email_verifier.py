from core.validation.type_verification import ParamType
from core.validation.type_verification.string_verifier import StringVerifier
import re


class EmailValidator(StringVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        if not super(EmailValidator, self).verify(value):
            return False

        regex = '^[a-z0-9]+[\._]?[a-z0-9]+[@]\w+[.]\w{2,3}$'
        return bool(re.search(regex, value))
