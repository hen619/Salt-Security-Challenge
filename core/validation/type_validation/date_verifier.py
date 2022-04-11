from core.validation.type_validation import ParamType
from core.validation.type_validation.type_verifier import TypeVerifier
from datetime import datetime


class DateVerifier(TypeVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        format = "%d-%m-%Y"
        return bool(datetime.strptime(value, format))
