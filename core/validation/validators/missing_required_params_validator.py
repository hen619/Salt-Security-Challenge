from typing import List

from core.api.responses.validation_response import MissingRequiredParamsValidatorResponse
from core.dataclasses.parameters import RequiredMissingParameter, Scope
from core.validation.validators.validator import Validator
from core.dataclasses.model_schema import ModelSchema, ModelParamSchema
from core.dataclasses.request_schema import RequestSchema, RequestParamSchema


class MissingRequiredParamsValidator(Validator):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        super().__init__(model, request)

    def validate(self) -> MissingRequiredParamsValidatorResponse:
        missing_required_parameters: List[RequiredMissingParameter] = []
        missing_required_parameters.extend(self.__get_missing_required_parameters(scope=Scope.HEADERS,
                                                                                  model_parameters=self._model.headers,
                                                                                  request_parameters=self._request.headers))
        missing_required_parameters.extend(self.__get_missing_required_parameters(scope=Scope.QUERY_PARAMS,
                                                                                  model_parameters=self._model.query_params,
                                                                                  request_parameters=self._request.query_params))
        missing_required_parameters.extend(self.__get_missing_required_parameters(scope=Scope.BODY,
                                                                                  model_parameters=self._model.body,
                                                                                  request_parameters=self._request.body))
        if not missing_required_parameters:
            return MissingRequiredParamsValidatorResponse(valid=True)
        return MissingRequiredParamsValidatorResponse(valid=False,
                                                      missing_parameters=missing_required_parameters)

    def __get_missing_required_parameters(self, scope: Scope, model_parameters: List[ModelParamSchema],
                                          request_parameters: List[RequestParamSchema]) -> \
            List[RequiredMissingParameter]:
        missing_parameters: List[RequiredMissingParameter] = []
        for model_param in model_parameters:
            if model_param.required:
                if not self.__is_parameter_exists(model_param.name, request_parameters):
                    missing_parameters.append(RequiredMissingParameter(name=model_param.name, scope=scope.name))
        return missing_parameters

    def __is_parameter_exists(self, required_param_name: str, parameters: List[RequestParamSchema]) -> bool:
        for parameter in parameters:
            if parameter.name == required_param_name:
                return True
        return False
