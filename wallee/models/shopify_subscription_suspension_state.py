# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionSuspensionState(Enum):
    
    ACTIVE = "ACTIVE"
    ENDED = "ENDED"

