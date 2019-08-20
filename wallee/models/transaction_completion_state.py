# coding: utf-8
from enum import Enum, unique


@unique
class TransactionCompletionState(Enum):
    
    CREATE = "CREATE"
    SCHEDULED = "SCHEDULED"
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

