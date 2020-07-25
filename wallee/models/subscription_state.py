# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionState(Enum):
    
    PENDING = "PENDING"
    INITIALIZING = "INITIALIZING"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"
    SUSPENDED = "SUSPENDED"
    TERMINATION_SCHEDULED = "TERMINATION_SCHEDULED"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"

