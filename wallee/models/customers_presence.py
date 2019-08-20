# coding: utf-8
from enum import Enum, unique


@unique
class CustomersPresence(Enum):
    
    NOT_PRESENT = "NOT_PRESENT"
    VIRTUAL_PRESENT = "VIRTUAL_PRESENT"
    PHYSICAL_PRESENT = "PHYSICAL_PRESENT"

