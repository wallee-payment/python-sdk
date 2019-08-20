# coding: utf-8
from enum import Enum, unique


@unique
class LineItemType(Enum):
    
    SHIPPING = "SHIPPING"
    DISCOUNT = "DISCOUNT"
    FEE = "FEE"
    PRODUCT = "PRODUCT"

