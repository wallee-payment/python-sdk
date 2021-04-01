# coding: utf-8
from enum import Enum, unique


@unique
class BankAccountEnvironment(Enum):
    
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"

