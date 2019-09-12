# coding: utf-8
from enum import Enum, unique


@unique
class PaymentTerminalLocationVersionState(Enum):
    
    PENDING = "PENDING"
    SCHEDULING = "SCHEDULING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

