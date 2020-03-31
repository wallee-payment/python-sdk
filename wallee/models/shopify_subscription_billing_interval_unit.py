# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionBillingIntervalUnit(Enum):
    
    MINUTES = "MINUTES"
    HOURS = "HOURS"
    DAYS = "DAYS"
    WEEKS = "WEEKS"
    MONTHS = "MONTHS"
    YEARS = "YEARS"

