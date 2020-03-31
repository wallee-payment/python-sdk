# coding: utf-8
from enum import Enum, unique


@unique
class ShopifyRecurringOrderState(Enum):
    
    PENDING = "PENDING"
    ONHOLD = "ONHOLD"
    PROCESSING = "PROCESSING"
    CANCELED = "CANCELED"
    BILLED = "BILLED"
    FAILED = "FAILED"

