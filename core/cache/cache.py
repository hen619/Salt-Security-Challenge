from typing import List

from dacite import from_dict
from flask import session

from core.dataclasses.model_schema import ModelSchema


def add_model(model: ModelSchema):
    session.pop('models')
    if 'models' not in session.keys():
        session['models'] = []
    session['models'].append(model)
# to do - check if model already exists


def get_models() -> List[ModelSchema]:
    models: List[ModelSchema] = []
    for model in session['models']:
        models.append(from_dict(ModelSchema, model))
    return models
