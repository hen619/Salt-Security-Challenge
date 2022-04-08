from typing import List

from core.schema.model_schema import ModelSchema, ModelParamSchema
from core.schema.request_schema import RequestSchema, RequestParamSchema


class MissingRequiredParamsFetcher:
    def __init__(self, model: ModelSchema, request: RequestSchema):
        self.__model: ModelSchema = model
        self.__request: RequestSchema = request

    def find_missing_required_params(self) -> dict:
        header_missing_params = self.__get_missing_required_params(model_params=self.__model.headers,
                                                                   request_params=self.__request.headers)
        query_missing_params = self.__get_missing_required_params(model_params=self.__model.query_params,
                                                                  request_params=self.__request.query_params)
        body_missing_params = self.__get_missing_required_params(model_params=self.__model.body,
                                                                 request_params=self.__request.body)
        return {'header_params': header_missing_params,
                'query_params': query_missing_params,
                'body_params': body_missing_params}

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
