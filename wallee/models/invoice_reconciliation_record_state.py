# coding: utf-8
from enum import Enum, unique


@unique
class InvoiceReconciliationRecordState(Enum):
    
    CREATE = "CREATE"
    PENDING = "PENDING"
    UNRESOLVED = "UNRESOLVED"
    RESOLVED = "RESOLVED"
    DISCARDED = "DISCARDED"

