# coding: utf-8
from enum import Enum, unique


@unique
class PaymentPrimaryRiskTaker(Enum):
    
    CUSTOMER = "CUSTOMER"
    MERCHANT = "MERCHANT"
    THIRD_PARTY = "THIRD_PARTY"

