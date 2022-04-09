from typing import List

from core.api.responses.validation_response import MissingRequiredParamsValidatorResponse
from core.dataclasses.parameters import RequiredMissingParameter, Scope
from core.validation.validators.validator import Validator
from core.dataclasses.model_schema import ModelSchema, ModelParamSchema
from core.dataclasses.request_schema import RequestSchema, RequestParamSchema


class MissingRequiredParamsValidator(Validator):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        super().__init__(model, request)
        self.name = "MissingRequiredParamsValidator"

    def validate(self) -> MissingRequiredParamsValidatorResponse:
        missing_required_parameters: List[RequiredMissingParameter] = []
        missing_required_parameters.extend(self.__get_missing_required_params(scope=Scope.HEADERS,
                                                                              model_params=self._model.headers,
                                                                              request_params=self._request.headers))
        missing_required_parameters.extend(self.__get_missing_required_params(scope=Scope.QUERY_PARAMS,
                                                                              model_params=self._model.query_params,
                                                                              request_params=self._request.query_params))
        missing_required_parameters.extend(self.__get_missing_required_params(scope=Scope.BODY,
                                                                              model_params=self._model.body,
                                                                              request_params=self._request.body))
        if not missing_required_parameters:
            return MissingRequiredParamsValidatorResponse(valid=True)
        return MissingRequiredParamsValidatorResponse(valid=False,
                                                      missing_parameters=missing_required_parameters)

    def __get_missing_required_params(self, scope: Scope, model_params: List[ModelParamSchema],
                                      request_params: List[RequestParamSchema]) -> \
            List[RequiredMissingParameter]:
        missing_params: List[RequiredMissingParameter] = []
        for model_param in model_params:
            if model_param.required:
                if not self.__is_param_exists(model_param.name, request_params):
                    missing_params.append(RequiredMissingParameter(name=model_param.name, scope=scope.name))
        return missing_params

    def __is_param_exists(self, required_param_name: str, params: List[RequestParamSchema]) -> bool:
        for param in params:
            if param.name == required_param_name:
                return True
        return False
