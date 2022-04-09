from abc import ABC, abstractmethod

from core.api.responses.validation_response import ValidatorResponse
from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema


class Validator(ABC):
    def __init__(self, model: ModelSchema, request: RequestSchema):
        self._model: ModelSchema = model
        self._request: RequestSchema = request
        self.name = "Base Validator"

    @abstractmethod
    def validate(self) -> ValidatorResponse:
        pass
