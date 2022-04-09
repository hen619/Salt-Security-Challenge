from flask import session

from core.dataclasses.model_schema import ModelSchema


def add_model(model: ModelSchema):
    if 'models' not in session.keys():
        session['models'] = []
    session['models'].append(model)


def get_models():
    return session['models']
