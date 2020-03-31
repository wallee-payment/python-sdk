# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionSuspensionInitiator(Enum):
    
    MERCHANT = "MERCHANT"
    CUSTOMER = "CUSTOMER"

