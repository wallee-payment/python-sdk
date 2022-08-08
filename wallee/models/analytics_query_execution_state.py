# coding: utf-8
from enum import Enum, unique


@unique
class AnalyticsQueryExecutionState(Enum):
    
    PROCESSING = "PROCESSING"
    PROCESSED = "PROCESSED"
    FAILED = "FAILED"
    CANCELED = "CANCELED"

