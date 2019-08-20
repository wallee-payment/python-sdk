# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionChargeState(Enum):
    
    SCHEDULED = "SCHEDULED"
    DISCARDED = "DISCARDED"
    PROCESSING = "PROCESSING"
    SUCCESSFUL = "SUCCESSFUL"
    FAILED = "FAILED"

