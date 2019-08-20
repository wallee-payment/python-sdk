# coding: utf-8
from enum import Enum, unique


@unique
class TransactionVoidMode(Enum):
    
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

