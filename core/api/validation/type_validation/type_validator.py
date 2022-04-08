from abc import ABC, abstractmethod


class TypeValidator(ABC):
    @abstractmethod
    def validate(self, value: any):
        pass
