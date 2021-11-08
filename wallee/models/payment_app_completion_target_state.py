# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppCompletionTargetState(Enum):
    
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

