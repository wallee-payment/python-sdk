# coding: utf-8
from enum import Enum, unique


@unique
class TransactionCompletionMode(Enum):
    
    DIRECT = "DIRECT"
    ONLINE = "ONLINE"
    OFFLINE = "OFFLINE"

