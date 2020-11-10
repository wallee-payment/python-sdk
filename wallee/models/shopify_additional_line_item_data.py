# coding: utf-8
from enum import Enum, unique


@unique
class ShopifyAdditionalLineItemData(Enum):
    
    VENDOR = "VENDOR"
    WEIGHT = "WEIGHT"

