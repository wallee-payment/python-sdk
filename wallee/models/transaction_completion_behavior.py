# coding: utf-8
from enum import Enum, unique


@unique
class TransactionCompletionBehavior(Enum):
    
    COMPLETE_IMMEDIATELY = "COMPLETE_IMMEDIATELY"
    COMPLETE_DEFERRED = "COMPLETE_DEFERRED"
    USE_CONFIGURATION = "USE_CONFIGURATION"

