# coding: utf-8
from enum import Enum, unique


@unique
class PaymentLinkProtectionMode(Enum):
    
    NO_PROTECTION = "NO_PROTECTION"
    ACCESS_KEY = "ACCESS_KEY"

