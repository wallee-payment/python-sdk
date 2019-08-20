# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionLedgerEntryState(Enum):
    
    OPEN = "OPEN"
    SCHEDULED = "SCHEDULED"
    PAID = "PAID"

