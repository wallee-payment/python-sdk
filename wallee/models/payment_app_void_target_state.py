# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppVoidTargetState(Enum):
    
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

