# coding: utf-8
from enum import Enum, unique


@unique
class AccountType(Enum):
    
    MASTER = "MASTER"
    REGULAR = "REGULAR"
    SUBACCOUNT = "SUBACCOUNT"

