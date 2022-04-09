from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List

from core.dataclasses.parameters import Parameters, TypeMismatchParameter


@dataclass
class ValidationProcessResponse(ABC):
    status: str
    details: str = ""


@dataclass
class ValidatorResponse(ABC):
    valid: bool

    @abstractmethod
    def get_details(self) -> str:
        pass


@dataclass
class MissingRequiredParamsValidatorResponse(ValidatorResponse):
    missing_parameters: Parameters = None

    def get_details(self):
        if self.missing_parameters:
            return repr(self.missing_parameters)


@dataclass
class TypeMismatchValidatorResponse(ValidatorResponse):
    type_mismatch_params: List[TypeMismatchParameter] = None

    def get_details(self):
        return '\n'.join(map(repr, self.type_mismatch_params))
