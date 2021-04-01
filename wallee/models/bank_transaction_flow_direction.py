# coding: utf-8
from enum import Enum, unique


@unique
class BankTransactionFlowDirection(Enum):
    
    INFLOW = "INFLOW"
    OUTFLOW = "OUTFLOW"

