from core.dataclasses.model_schema import ModelSchema
from core.dataclasses.request_schema import RequestSchema

'''
-- Real life solution -- 
In real life production I would use Redis as a key value dataBase.
The key will be a hash of the path and method, and the value will be the model object it self
This way i can access the models in O(1) complexity. 

-- Trade offs --
All Redis data resides in memory, which enables low latency and high performance 
But large amount of models can require a lot of memory.
In case we lack memory I would consider using Another Database.
'''

models: dict = {}


def add_model(model: ModelSchema):
    model_hash = model.path + model.method
    models[model_hash] = model


def get_matching_model(api_request: RequestSchema):
    model_hash = api_request.path + api_request.method
    if model_hash in models.keys():
        return models[model_hash]
