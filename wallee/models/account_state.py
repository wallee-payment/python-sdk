# coding: utf-8
from enum import Enum, unique


@unique
class AccountState(Enum):
    
    CREATE = "CREATE"
    RESTRICTED_ACTIVE = "RESTRICTED_ACTIVE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

