from datetime import datetime

from core.validation.type_verification import ParamType
from core.validation.type_verification.type_verifier import TypeVerifier


class DateVerifier(TypeVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        try:
            datetime.strptime(value, "%d-%m-%Y")
            return True
        except ValueError:
            return False
