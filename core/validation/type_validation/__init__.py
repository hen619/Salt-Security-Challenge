from enum import Enum


class ParamType(Enum):
    STRING = 'String'
    INTEGER = 'Int'
    BOOLEAN = 'Boolean'
    UUID = 'UUID'
    AUTH_TOKEN = 'Auth-Token'
    EMAIL = 'Email'
    LIST = 'List'
    DATE = 'Date'

