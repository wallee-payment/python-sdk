# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionVersionItemPriceStrategy(Enum):
    
    INITIALLY_CALCULATED = "INITIALLY_CALCULATED"
    RECALCULATE = "RECALCULATE"

