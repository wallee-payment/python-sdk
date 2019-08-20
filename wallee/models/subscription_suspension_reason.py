# coding: utf-8
from enum import Enum, unique


@unique
class SubscriptionSuspensionReason(Enum):
    
    FAILED_CHARGE = "FAILED_CHARGE"
    SUBSCRIBER_INITIATED_REFUND = "SUBSCRIBER_INITIATED_REFUND"
    MANUAL = "MANUAL"

