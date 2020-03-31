# coding: utf-8
from enum import Enum, unique


@unique
class ShopifyTransactionState(Enum):
    
    PENDING = "PENDING"
    AUTHORIZED = "AUTHORIZED"
    COMPLETED = "COMPLETED"
    FAILED = "FAILED"
    CONFLICTING = "CONFLICTING"

