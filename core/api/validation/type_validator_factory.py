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
    ParamType.STRING: StringValidator(),
    ParamType.UUID: UUIDValidator(),
    ParamType.EMAIL: EmailValidator(),
    ParamType.DATE: DateValidator(),
    ParamType.LIST: ListValidator(),
    ParamType.INTEGER: IntValidator(),
    ParamType.BOOLEAN: BooleanValidator(),
    ParamType.AUTH_TOKEN: AuthTokenValidator()}


def get_type_validators(types: List[str]):
    required_validators: List[TypeValidator] = []
    for value_type in types:
        required_validators.append(validators[value_type])
    return validators
