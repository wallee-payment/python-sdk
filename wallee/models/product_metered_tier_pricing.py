# coding: utf-8
from enum import Enum, unique


@unique
class ProductMeteredTierPricing(Enum):
    
    CHEAPEST_TIER_PRICING = "CHEAPEST_TIER_PRICING"
    INCREMENTAL_DISCOUNT_PRICING = "INCREMENTAL_DISCOUNT_PRICING"

