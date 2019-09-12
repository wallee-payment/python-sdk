# coding: utf-8
from enum import Enum, unique


@unique
class ChargeType(Enum):
    
    ASYNCHRONOUS = "ASYNCHRONOUS"
    SYNCHRONOUS = "SYNCHRONOUS"
    TOKEN = "TOKEN"
    TERMINAL = "TERMINAL"

