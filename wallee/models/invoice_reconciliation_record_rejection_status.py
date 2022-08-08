# coding: utf-8
from enum import Enum, unique


@unique
class InvoiceReconciliationRecordRejectionStatus(Enum):
    
    NONE = "NONE"
    REJECTED = "REJECTED"
    BULK_REJECTED = "BULK_REJECTED"

