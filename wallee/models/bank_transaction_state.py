# coding: utf-8
from enum import Enum, unique


@unique
class BankTransactionState(Enum):
    
    UPCOMING = "UPCOMING"
    SETTLED = "SETTLED"

