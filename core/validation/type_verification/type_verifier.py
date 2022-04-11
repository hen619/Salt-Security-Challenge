from abc import ABC, abstractmethod

from core.validation.type_verification import ParamType


class TypeVerifier(ABC):
    @abstractmethod
    def __init__(self, name: ParamType):
        self.name = name

    def verify(self, value: any) -> bool:
        pass
