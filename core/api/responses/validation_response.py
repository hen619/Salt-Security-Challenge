from abc import ABC, abstractmethod
from dataclasses import dataclass
from typing import List, Dict

from core.dataclasses.parameters import TypeMismatchParameter, RequiredMissingParameter


@dataclass
class ValidationProcessResponse(ABC):
    status: str
    details: str = ""


@dataclass
class ValidatorResponse(ABC):
    valid: bool

    @abstractmethod
    def get_details(self) -> Dict:
        pass


@dataclass
class MissingRequiredParamsValidatorResponse(ValidatorResponse):
    missing_parameters: List[RequiredMissingParameter] = None

    def get_details(self) -> Dict:
        if self.missing_parameters:
            return {'missing_required_params': self.missing_parameters}


@dataclass
class TypeMismatchValidatorResponse(ValidatorResponse):
    type_mismatch_params: List[TypeMismatchParameter] = None

    def get_details(self) -> Dict:
        return {'type_mismatch_params': self.type_mismatch_params}
