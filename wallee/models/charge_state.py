# coding: utf-8
from enum import Enum, unique


@unique
class ChargeState(Enum):
    
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

