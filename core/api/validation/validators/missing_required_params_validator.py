from typing import List

from core.api.responses.validation_response import MissingRequiredParamsValidatorResponse
from core.api.validation.validators.validator import Validator
from core.dataclasses.parameters import Parameters
from core.dataclasses.model_schema import ModelSchema, ModelParamSchema
from core.dataclasses.request_schema import RequestSchema, RequestParamSchema


class MissingRequiredParamsValidator(Validator):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        super().__init__(model, request)

    def validate(self) -> MissingRequiredParamsValidatorResponse:
        header_missing_params = self.__get_missing_required_params(model_params=self.__model.headers,
                                                                   request_params=self.__request.headers)
        query_missing_params = self.__get_missing_required_params(model_params=self.__model.query_params,
                                                                  request_params=self.__request.query_params)
        body_missing_params = self.__get_missing_required_params(model_params=self.__model.body,
                                                                 request_params=self.__request.body)
        if not header_missing_params and not query_missing_params and not body_missing_params:
            return MissingRequiredParamsValidatorResponse(valid=True)
        return MissingRequiredParamsValidatorResponse(valid=False,
                                                      missing_parameters=Parameters(header=header_missing_params,
                                                                                    query=query_missing_params,
                                                                                    body=body_missing_params))

    def __get_missing_required_params(self, model_params: List[ModelParamSchema],
                                      request_params: List[RequestParamSchema]) -> \
            List[str]:
        missing_params: List[str] = []
        for model_param in model_params:
            if model_param.required:
                if not self.__is_param_exists(model_param.name, request_params):
                    missing_params.append(model_param.name)
        return missing_params

    def __is_param_exists(self, required_param_name: str, params: List[RequestParamSchema]) -> bool:
        for param in params:
            if param.name == required_param_name:
                return True
        return False
