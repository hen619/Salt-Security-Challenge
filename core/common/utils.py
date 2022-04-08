from typing import List

from core.schema.model_schema import ModelSchema
from core.schema.request_schema import RequestSchema


def get_matching_model(api_request: RequestSchema, models: List[ModelSchema]):
    for model in models:
        if api_request.path == model.path and api_request.method == model.method:
            return model
