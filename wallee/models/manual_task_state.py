# coding: utf-8
from enum import Enum, unique


@unique
class ManualTaskState(Enum):
    
    OPEN = "OPEN"
    DONE = "DONE"
    EXPIRED = "EXPIRED"

