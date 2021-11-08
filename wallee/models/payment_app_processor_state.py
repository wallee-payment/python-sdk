# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppProcessorState(Enum):
    
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

