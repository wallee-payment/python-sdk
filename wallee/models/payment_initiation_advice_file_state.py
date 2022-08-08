# coding: utf-8
from enum import Enum, unique


@unique
class PaymentInitiationAdviceFileState(Enum):
    
    PENDING = "PENDING"
    PROCESSED = "PROCESSED"

