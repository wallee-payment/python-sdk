# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionPeriodBillState(Enum):
    
    PENDING = "PENDING"
    BILLED = "BILLED"

