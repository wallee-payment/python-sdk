# coding: utf-8
from enum import Enum, unique


@unique
class InstallmentPaymentState(Enum):
    
    CREATE = "CREATE"
    CONFIRMED = "CONFIRMED"
    AUTHORIZED = "AUTHORIZED"
    REJECTED = "REJECTED"
    COMPLETED = "COMPLETED"
    RUNNING = "RUNNING"
    DONE = "DONE"
    DEFAULTED = "DEFAULTED"

