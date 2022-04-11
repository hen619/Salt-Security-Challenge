from core.validation.type_validation import ParamType
from core.validation.type_validation.type_verifier import TypeVerifier


class ListVerifier(TypeVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        return isinstance(value, list)
