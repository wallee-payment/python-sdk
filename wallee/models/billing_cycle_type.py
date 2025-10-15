# coding: utf-8
from enum import Enum, unique


@unique
class BillingCycleType(Enum):
    
    DAILY = "DAILY"
    WEEKLY = "WEEKLY"
    MONTHLY = "MONTHLY"
    YEARLY = "YEARLY"

