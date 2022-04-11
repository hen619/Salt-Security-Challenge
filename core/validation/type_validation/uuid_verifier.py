from core.validation.type_validation import ParamType
from core.validation.type_validation.string_verifier import StringVerifier
import uuid


class UUIDValidator(StringVerifier):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def verify(self, value: any) -> bool:
        if not super(UUIDValidator, self).verify(value):
            return False

        try:
            uuid.UUID(value)
            return True
        except ValueError:
            return False
