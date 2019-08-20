# coding: utf-8
from enum import Enum, unique


@unique
class OneClickPaymentMode(Enum):
    
    DISABLED = "DISABLED"
    ALLOW = "ALLOW"
    FORCE = "FORCE"

