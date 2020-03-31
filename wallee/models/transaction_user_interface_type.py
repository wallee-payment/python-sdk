# coding: utf-8
from enum import Enum, unique


@unique
class TransactionUserInterfaceType(Enum):
    
    IFRAME = "IFRAME"
    LIGHTBOX = "LIGHTBOX"
    PAYMENT_PAGE = "PAYMENT_PAGE"
    MOBILE_SDK = "MOBILE_SDK"
    TERMINAL = "TERMINAL"

