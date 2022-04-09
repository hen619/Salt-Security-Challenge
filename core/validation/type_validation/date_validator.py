from core.validation.type_validation import ParamType
from core.validation.type_validation.type_validator import TypeValidator
from datetime import datetime


class DateValidator(TypeValidator):
    def __init__(self, name: ParamType):
        super().__init__(name)

    def validate(self, value: any)->bool:
        format = "%d-%m-%Y"
        return bool(datetime.strptime(value, format))
