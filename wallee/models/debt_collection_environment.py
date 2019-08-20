# coding: utf-8
from enum import Enum, unique


@unique
class DebtCollectionEnvironment(Enum):
    
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"

