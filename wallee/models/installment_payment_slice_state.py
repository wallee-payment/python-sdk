# coding: utf-8
from enum import Enum, unique


@unique
class InstallmentPaymentSliceState(Enum):
    
    CREATE = "CREATE"
    SCHEDULED = "SCHEDULED"
    CANCELED = "CANCELED"
    PREPARE_PROCESSING = "PREPARE_PROCESSING"
    PROCESSING = "PROCESSING"
    FAILED = "FAILED"
    SUCCESSFUL = "SUCCESSFUL"

