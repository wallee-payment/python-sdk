# coding: utf-8
from enum import Enum, unique


@unique
class CreationEntityState(Enum):
    
    CREATE = "CREATE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

