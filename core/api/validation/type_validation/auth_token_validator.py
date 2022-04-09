from core.api.validation.type_validation.string_validator import StringValidator


class AuthTokenValidator(StringValidator):
    def __init__(self, name):
        super().__init__(name)

    def validate(self, value: any):
        pass
