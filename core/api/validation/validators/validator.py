from abc import ABC, abstractmethod

from core.api.responses.validation_response import ValidatorResponse
from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema


class Validator(ABC):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        self.__model: ModelSchema = model
        self.__request: RequestSchema = request

    @abstractmethod
    def validate(self) -> ValidatorResponse:
        pass
