# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionProductPricingOption(Enum):
    
    CURRENT_PRICE = "CURRENT_PRICE"
    ORIGINAL_PRICE = "ORIGINAL_PRICE"
    FIXED_PRICE = "FIXED_PRICE"
    RELATIVE_ADJUSTMENT = "RELATIVE_ADJUSTMENT"
    ABSOLUTE_ADJUSTMENT = "ABSOLUTE_ADJUSTMENT"

