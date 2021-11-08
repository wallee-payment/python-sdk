# coding: utf-8
from enum import Enum, unique


@unique
class PaymentAppConnectorState(Enum):
    
    ACTIVE = "ACTIVE"
    DELETED = "DELETED"

