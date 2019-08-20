# coding: utf-8
from enum import Enum, unique


@unique
class DebtCollectionCaseState(Enum):
    
    CREATE = "CREATE"
    PREPARING = "PREPARING"
    REVIEWING = "REVIEWING"
    PENDING = "PENDING"
    PROCESSING = "PROCESSING"
    CLOSED = "CLOSED"
    FAILED = "FAILED"

