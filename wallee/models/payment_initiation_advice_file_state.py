# coding: utf-8
from enum import Enum, unique


@unique
class PaymentInitiationAdviceFileState(Enum):
    
    CREATING = "CREATING"
    FAILED = "FAILED"
    CREATED = "CREATED"
    OVERDUE = "OVERDUE"
    UPLOADED = "UPLOADED"
    DOWNLOADED = "DOWNLOADED"
    PROCESSED = "PROCESSED"

