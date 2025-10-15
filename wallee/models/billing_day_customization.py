# coding: utf-8
from enum import Enum, unique


@unique
class BillingDayCustomization(Enum):
    
    DEFAULT = "DEFAULT"
    SPECIFIC = "SPECIFIC"

