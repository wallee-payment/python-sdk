# coding: utf-8
from enum import Enum, unique


@unique
class PaymentLinkAddressHandlingMode(Enum):
    
    NOT_REQUIRED = "NOT_REQUIRED"
    REQUIRED_IN_URL = "REQUIRED_IN_URL"
    REQUIRED_ON_PAYMENT_PAGE = "REQUIRED_ON_PAYMENT_PAGE"

