from dataclasses import dataclass
from enum import Enum

from core.dataclasses.request_schema import RequestParamSchema


class Scope(Enum):
    HEADERS = 'headers'
    BODY = 'body'
    QUERY_PARAMS = 'query_params'


@dataclass
class RequiredMissingParameter:
    name: str
    scope: str


@dataclass
class TypeMismatchParameter:
    parameter: RequestParamSchema
    scope: str
    expected_type: str
