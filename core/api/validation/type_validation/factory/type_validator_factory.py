from typing import List, Dict

from core.api.validation.type_validation import ParamType
from core.api.validation.type_validation.auth_token_validator import AuthTokenValidator
from core.api.validation.type_validation.boolean_validator import BooleanValidator
from core.api.validation.type_validation.date_validator import DateValidator
from core.api.validation.type_validation.email_validator import EmailValidator
from core.api.validation.type_validation.int_validator import IntValidator
from core.api.validation.type_validation.list_validator import ListValidator
from core.api.validation.type_validation.string_validator import StringValidator
from core.api.validation.type_validation.type_validator import TypeValidator
from core.api.validation.type_validation.uuid_validator import UUIDValidator

validators: Dict[str: TypeValidator] = {
    ParamType.STRING.name: StringValidator(name=ParamType.STRING),
    ParamType.UUID.name: UUIDValidator(name=ParamType.UUID),
    ParamType.EMAIL.name: EmailValidator(name=ParamType.EMAIL),
    ParamType.DATE.name: DateValidator(name=ParamType.DATE),
    ParamType.LIST.name: ListValidator(name=ParamType.LIST),
    ParamType.INTEGER.name: IntValidator(name=ParamType.INTEGER),
    ParamType.BOOLEAN.name: BooleanValidator(name=ParamType.BOOLEAN),
    ParamType.AUTH_TOKEN.name: AuthTokenValidator(name=ParamType.AUTH_TOKEN)}


def get_type_validators(types: List[str]) -> List[TypeValidator]:
    required_validators: List[TypeValidator] = []
    for value_type in types:
        required_validators.append(validators[value_type])
    return required_validators
