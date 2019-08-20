# coding: utf-8
from enum import Enum, unique


@unique
class TransactionState(Enum):
    
    CREATE = "CREATE"
    PENDING = "PENDING"
    CONFIRMED = "CONFIRMED"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    AUTHORIZED = "AUTHORIZED"
    VOIDED = "VOIDED"
    COMPLETED = "COMPLETED"
    FULFILL = "FULFILL"
    DECLINE = "DECLINE"

