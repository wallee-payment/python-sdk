# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppChargeAttemptTargetState(Enum):
    
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

