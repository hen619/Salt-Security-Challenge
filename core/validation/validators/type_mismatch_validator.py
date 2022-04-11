from typing import List

from core.api.responses.validation_response import TypeMismatchValidatorResponse
from core.dataclasses.model_schema import ModelSchema, ModelParamSchema
from core.dataclasses.parameters import TypeMismatchParameter, Scope
from core.dataclasses.request_schema import RequestSchema, RequestParamSchema
from core.validation.type_verification.factory import get_type_validators
from core.validation.type_verification.type_verifier import TypeVerifier
from core.validation.validators.validator import Validator


class TypeMismatchValidator(Validator):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        super().__init__(model, request)

    def validate(self) -> TypeMismatchValidatorResponse:
        type_mismatch_parameters: List[TypeMismatchParameter] = []
        type_mismatch_parameters.extend(
            self.find_type_mismatch(scope=Scope.HEADERS, model_parameters=self._model.headers,
                                    request_parameters=self._request.headers))

        type_mismatch_parameters.extend(
            self.find_type_mismatch(scope=Scope.QUERY_PARAMS, model_parameters=self._model.query_params,
                                    request_parameters=self._request.query_params))

        type_mismatch_parameters.extend(self.find_type_mismatch(scope=Scope.BODY, model_parameters=self._model.body,
                                                                request_parameters=self._request.body))
        if not type_mismatch_parameters:
            return TypeMismatchValidatorResponse(valid=True)
        return TypeMismatchValidatorResponse(valid=False, type_mismatch_params=type_mismatch_parameters)

    def find_type_mismatch(self, scope: Scope, model_parameters: List[ModelParamSchema],
                           request_parameters: List[RequestParamSchema]) -> List[TypeMismatchParameter]:
        type_mismatch_parameters: List[TypeMismatchParameter] = []
        for expected_parameter in model_parameters:
            request_parameter = self.get_parameter_from_request(model_param=expected_parameter,
                                                                request_parameters=request_parameters)
            if request_parameter:
                types_validators: List[TypeVerifier] = get_type_validators(expected_parameter.types)
                for type_validator in types_validators:
                    if not type_validator.verify(request_parameter.value):
                        type_mismatch_parameters.append(
                            TypeMismatchParameter(parameter=request_parameter, scope=scope.name,
                                                  expected_type=type_validator.name.value))
        return type_mismatch_parameters

    def get_parameter_from_request(self, model_param: ModelParamSchema,
                                   request_parameters: List[RequestParamSchema]) -> RequestParamSchema:
        for param in request_parameters:
            if param.name == model_param.name:
                return param
