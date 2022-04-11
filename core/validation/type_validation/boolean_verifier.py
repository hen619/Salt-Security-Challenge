from core.validation.type_validation import ParamType
from core.validation.type_validation.type_verifier import TypeVerifier


class BooleanVerifier(TypeVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any):
        return isinstance(value, bool)
