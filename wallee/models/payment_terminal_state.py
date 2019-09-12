# coding: utf-8
from enum import Enum, unique


@unique
class PaymentTerminalState(Enum):
    
    PREPARING = "PREPARING"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DECOMMISSIONING = "DECOMMISSIONING"
    DECOMMISSIONED = "DECOMMISSIONED"

