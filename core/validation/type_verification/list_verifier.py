from core.validation.type_verification import ParamType
from core.validation.type_verification.type_verifier import TypeVerifier


class ListVerifier(TypeVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        return isinstance(value, list)
