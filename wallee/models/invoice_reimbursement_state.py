# coding: utf-8
from enum import Enum, unique


@unique
class InvoiceReimbursementState(Enum):
    
    PENDING = "PENDING"
    MANUAL_REVIEW = "MANUAL_REVIEW"
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    DISCARDED = "DISCARDED"

