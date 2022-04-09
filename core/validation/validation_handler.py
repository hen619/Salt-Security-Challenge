from typing import List

from core.api.responses.validation_response import ValidatorResponse, ValidationProcessResponse
from core.validation.validators.missing_required_params_validator import MissingRequiredParamsValidator
from core.validation.validators.type_mismatch_validator import TypeMismatchValidator
from core.validation.validators.validator import Validator
from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema


class ValidationHandler:
    def __init__(self, model: ModelSchema, request: RequestSchema):
        self.__validators: List[Validator] = [MissingRequiredParamsValidator(model=model, request=request),
                                              TypeMismatchValidator(model=model, request=request)]

    def validate_request(self) -> ValidationProcessResponse:
        valid = True
        details = {}
        for validator in self.__validators:
            response: ValidatorResponse = validator.validate()
            if not response.valid:
                valid = False
                details.update(response.get_details())
        if not valid:
            return ValidationProcessResponse(status='abnormal', details=details)
        return ValidationProcessResponse(status='valid')
