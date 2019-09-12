# coding: utf-8
from enum import Enum, unique


@unique
class PaymentTerminalDeviceState(Enum):
    
    CREATE = "CREATE"
    PREPARING = "PREPARING"
    REGISTERED = "REGISTERED"
    DECOMMISSIONING = "DECOMMISSIONING"
    DECOMMISSIONED = "DECOMMISSIONED"

