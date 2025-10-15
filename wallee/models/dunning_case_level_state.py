# coding: utf-8
from enum import Enum, unique


@unique
class DunningCaseLevelState(Enum):
    
    INITIALIZING = "INITIALIZING"
    PENDING = "PENDING"
    FAILED = "FAILED"
    CANCELED = "CANCELED"
    SUCCEEDED = "SUCCEEDED"

