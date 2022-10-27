# coding: utf-8
from enum import Enum, unique


@unique
class PaymentInitiationAdviceFileState(Enum):
    
    CREATED = "CREATED"
    UPLOADED = "UPLOADED"
    DOWNLOADED = "DOWNLOADED"
    PROCESSED = "PROCESSED"

