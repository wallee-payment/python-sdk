# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppRefundTargetState(Enum):
    
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

