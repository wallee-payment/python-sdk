# coding: utf-8
from enum import Enum, unique


@unique
class CustomerAddressType(Enum):
    
    BILLING = "BILLING"
    SHIPPING = "SHIPPING"
    BOTH = "BOTH"

