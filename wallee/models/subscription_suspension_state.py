# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionSuspensionState(Enum):
    
    RUNNING = "RUNNING"
    ENDED = "ENDED"

