from abc import ABC, abstractmethod

from core.validation.type_validation import ParamType


class TypeValidator(ABC):
    @abstractmethod
    def __init__(self, name: ParamType):
        self.name = name

    def validate(self, value: any) -> bool:
        pass
