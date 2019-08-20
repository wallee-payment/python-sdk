# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionProductState(Enum):
    
    CREATE = "CREATE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    RETIRING = "RETIRING"
    RETIRED = "RETIRED"

