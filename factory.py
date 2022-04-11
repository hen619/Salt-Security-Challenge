from flask import Flask, g
from flask_restful import Api

from core.api.resources.api_requests import ApiRequests
from core.api.resources.models import Models


def create_app():
    app = Flask(__name__)
    api = Api(app)
    add_resources(api=api)
    return app


def add_resources(api: Api):
    api.add_resource(Models, '/models/model')
    api.add_resource(ApiRequests, '/api')
