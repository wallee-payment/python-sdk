# coding: utf-8
from enum import Enum, unique


@unique
class RefundState(Enum):
    
    CREATE = "CREATE"
    SCHEDULED = "SCHEDULED"
    PENDING = "PENDING"
    MANUAL_CHECK = "MANUAL_CHECK"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

