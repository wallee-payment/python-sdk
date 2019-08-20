# coding: utf-8
from enum import Enum, unique


@unique
class TransactionInvoiceState(Enum):
    
    CREATE = "CREATE"
    OPEN = "OPEN"
    OVERDUE = "OVERDUE"
    CANCELED = "CANCELED"
    PAID = "PAID"
    DERECOGNIZED = "DERECOGNIZED"
    NOT_APPLICABLE = "NOT_APPLICABLE"

