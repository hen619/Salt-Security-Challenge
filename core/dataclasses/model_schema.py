from dataclasses import dataclass
from typing import List


@dataclass
class ModelParamSchema:
    name: str
    types: List[str]
    required: bool


@dataclass
class ModelSchema:
    path: str
    method: str
    query_params: List[ModelParamSchema]
    headers: List[ModelParamSchema]
    body: List[ModelParamSchema]
