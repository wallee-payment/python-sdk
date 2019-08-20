# coding: utf-8
from enum import Enum, unique


@unique
class ChargeAttemptEnvironment(Enum):
    
    PRODUCTION = "PRODUCTION"
    TEST = "TEST"

