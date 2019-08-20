# coding: utf-8
from enum import Enum, unique


@unique
class ChargeFlowLevelState(Enum):
    
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

