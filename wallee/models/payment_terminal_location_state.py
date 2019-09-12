# coding: utf-8
from enum import Enum, unique


@unique
class PaymentTerminalLocationState(Enum):
    
    CREATE = "CREATE"
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

