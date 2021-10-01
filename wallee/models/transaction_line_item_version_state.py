# coding: utf-8
from enum import Enum, unique


@unique
class TransactionLineItemVersionState(Enum):
    
    CREATE = "CREATE"
    SCHEDULED = "SCHEDULED"
    PENDING = "PENDING"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

