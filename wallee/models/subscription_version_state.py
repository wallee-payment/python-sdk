# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionVersionState(Enum):
    
    PENDING = "PENDING"
    INITIALIZING = "INITIALIZING"
    FAILED = "FAILED"
    ACTIVE = "ACTIVE"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"

