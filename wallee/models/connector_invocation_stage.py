# coding: utf-8
from enum import Enum, unique


@unique
class ConnectorInvocationStage(Enum):
    
    PAYMENT_METHOD_LIST = "PAYMENT_METHOD_LIST"
    FORM_GENERATION = "FORM_GENERATION"
    VALIDATION = "VALIDATION"
    AUTHORIZATION = "AUTHORIZATION"

