# coding: utf-8
from enum import Enum, unique


@unique
class TransactionUserInterfaceType(Enum):
    
    IFRAME = "IFRAME"
    PAYMENT_PAGE = "PAYMENT_PAGE"
    MOBILE_SDK = "MOBILE_SDK"

