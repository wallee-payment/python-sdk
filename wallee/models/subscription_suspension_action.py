# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionSuspensionAction(Enum):
    
    TERMINATE = "TERMINATE"
    REACTIVATE = "REACTIVATE"

