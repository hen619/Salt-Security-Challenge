from dataclasses import dataclass
from typing import List, Any


@dataclass
class RequestParamSchema:
    name: str
    value: Any


@dataclass
class RequestSchema:
    path: str
    method: str
    query_params: List[RequestParamSchema]
    headers: List[RequestParamSchema]
    body: List[RequestParamSchema]
