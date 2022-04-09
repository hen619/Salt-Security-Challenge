from core.api.validation.type_validation.type_validator import TypeValidator


class IntValidator(TypeValidator):
    def __init__(self, name):
        super().__init__(name)

    def validate(self, value: any):
        pass