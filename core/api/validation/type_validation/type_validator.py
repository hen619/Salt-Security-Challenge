from abc import ABC, abstractmethod


class TypeValidator(ABC):
    @abstractmethod
    def __init__(self, name):
        self.name = name

    def validate(self, value: any):
        pass
