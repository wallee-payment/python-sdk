# coding: utf-8
from enum import Enum, unique


@unique
class TransactionVoidState(Enum):
    
    CREATE = "CREATE"
    PENDING = "PENDING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

