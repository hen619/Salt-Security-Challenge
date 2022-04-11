from dacite import from_dict, MissingValueError
from flask import request, jsonify
from flask_restful import Resource

from core.api.responses.validation_response import ValidationProcessResponse
from core.cache.cache import get_matching_model
from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema
from core.validation.validation_handler import ValidationHandler


class ApiRequests(Resource):
    def post(self):
        request_data: dict = request.get_json()
        try:
            api_request: RequestSchema = from_dict(RequestSchema, request_data)
            model: ModelSchema = get_matching_model(api_request)
            if model:
                validation_handler = ValidationHandler(request=api_request, model=model)
                response: ValidationProcessResponse = validation_handler.validate_request()
            else:
                return "No Matching model found for the request"
        except MissingValueError as e:
            return str(e)
        return jsonify(response)
