# coding: utf-8
from enum import Enum, unique


@unique
class DeliveryIndicationState(Enum):
    
    PENDING = "PENDING"
    NOT_SUITABLE = "NOT_SUITABLE"
    MANUAL_CHECK_REQUIRED = "MANUAL_CHECK_REQUIRED"
    SUITABLE = "SUITABLE"

