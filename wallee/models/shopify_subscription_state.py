# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionState(Enum):
    
    INITIATING = "INITIATING"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"

