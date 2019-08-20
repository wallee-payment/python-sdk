# coding: utf-8
from enum import Enum, unique


@unique
class ChargeAttemptState(Enum):
    
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

