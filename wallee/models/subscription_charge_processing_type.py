# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionChargeProcessingType(Enum):
    
    SYNCHRONOUS = "SYNCHRONOUS"
    CHARGE_FLOW = "CHARGE_FLOW"

