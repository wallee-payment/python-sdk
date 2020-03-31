# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionVersionState(Enum):
    
    CREATE = "CREATE"
    ACTIVE = "ACTIVE"
    DISCHARGED = "DISCHARGED"

