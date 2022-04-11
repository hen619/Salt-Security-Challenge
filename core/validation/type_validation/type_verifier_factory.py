from typing import List, Dict
from core.validation.type_validation import ParamType
from core.validation.type_validation.auth_token_verifier import AuthTokenVerifier
from core.validation.type_validation.boolean_verifier import BooleanVerifier
from core.validation.type_validation.date_verifier import DateVerifier
from core.validation.type_validation.email_verifier import EmailValidator
from core.validation.type_validation.int_verifier import IntVerifier
from core.validation.type_validation.list_verifier import ListVerifier
from core.validation.type_validation.string_verifier import StringVerifier
from core.validation.type_validation.type_verifier import TypeVerifier
from core.validation.type_validation.uuid_verifier import UUIDValidator

validators: Dict[str, TypeVerifier] = {
    ParamType.STRING.value: StringVerifier(name=ParamType.STRING),
    ParamType.UUID.value: UUIDValidator(name=ParamType.UUID),
    ParamType.EMAIL.value: EmailValidator(name=ParamType.EMAIL),
    ParamType.DATE.value: DateVerifier(name=ParamType.DATE),
    ParamType.LIST.value: ListVerifier(name=ParamType.LIST),
    ParamType.INTEGER.value: IntVerifier(name=ParamType.INTEGER),
    ParamType.BOOLEAN.value: BooleanVerifier(name=ParamType.BOOLEAN),
    ParamType.AUTH_TOKEN.value: AuthTokenVerifier(name=ParamType.AUTH_TOKEN)
}


def get_type_validators(types: List[str]) -> List[TypeVerifier]:
    required_validators: List[TypeVerifier] = []
    for value_type in types:
        required_validators.append(validators[value_type])
    return required_validators
