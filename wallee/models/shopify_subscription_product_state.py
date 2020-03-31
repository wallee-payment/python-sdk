# coding: utf-8
from enum import Enum, unique


@unique
class ShopifySubscriptionProductState(Enum):
    
    CREATE = "CREATE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    OBSOLETE = "OBSOLETE"
    DELETING = "DELETING"
    DELETED = "DELETED"

