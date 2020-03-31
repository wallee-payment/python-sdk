# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionSuspensionType(Enum):
    
    REACTIVATE = "REACTIVATE"
    TERMINATE = "TERMINATE"

