from typing import List

from dacite import from_dict, MissingValueError
from flask import request
from flask_restful import Resource

from core.api.validation.validation import validate_request
from core.cache.cache import get_models
from core.common.utils import get_matching_model
from core.schema.model_schema import ModelSchema
from core.schema.request_schema import RequestSchema


class ApiRequests(Resource):
    def post(self):
        request_data: dict = request.get_json()
        try:
            api_request: RequestSchema = from_dict(RequestSchema, request_data)
            model: ModelSchema = get_matching_model(api_request, get_models())
            if model:
                response = validate_request(request=api_request, model=model)
            else:
                return "No Matching model found for the request"
        except MissingValueError as e:
            return str(e)
        return response
