# coding: utf-8
from enum import Enum, unique


@unique
class DunningCaseState(Enum):
    
    RUNNING = "RUNNING"
    SUSPENDED = "SUSPENDED"
    CANCELED = "CANCELED"
    DERECOGNIZED = "DERECOGNIZED"
    FAILED = "FAILED"
    SUCCEEDED = "SUCCEEDED"

