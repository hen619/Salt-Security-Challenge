from dacite import from_dict, MissingValueError
from flask import request, session
from flask_restful import Resource

from core.cache.cache import add_model
from core.dataclasses.model_schema import ModelSchema


class Models(Resource):
    def post(self):
        request_data: dict = request.get_json()
        try:
            model: ModelSchema = from_dict(ModelSchema, request_data)
            add_model(model=model)
        except MissingValueError as e:
            return str(e), 400
        return 200
