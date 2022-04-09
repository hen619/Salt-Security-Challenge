from dataclasses import dataclass
from typing import List

from core.dataclasses.request_schema import RequestParamSchema


@dataclass
class Parameters:
    header: List[str]
    query: List[str]
    body: List[str]


@dataclass
class TypeMismatchParameter:
    parameter: RequestParamSchema
    scope: str
    expected_type: str


