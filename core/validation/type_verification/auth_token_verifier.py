from core.validation.type_verification import ParamType
from core.validation.type_verification.string_verifier import StringVerifier
import re


class AuthTokenVerifier(StringVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any):
        if not super(AuthTokenVerifier, self).verify(value):
            return False

        regex = "^Bearer *"
        return bool(re.search(regex, value))
