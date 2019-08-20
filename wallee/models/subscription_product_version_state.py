# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionProductVersionState(Enum):
    
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    OBSOLETE = "OBSOLETE"
    RETIRING = "RETIRING"
    RETIRED = "RETIRED"

