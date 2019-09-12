# coding: utf-8
from enum import Enum, unique


@unique
class PaymentTerminalConfigurationVersionState(Enum):
    
    PENDING = "PENDING"
    SCHEDULING = "SCHEDULING"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

