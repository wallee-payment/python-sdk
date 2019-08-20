# coding: utf-8
from enum import Enum, unique


@unique
class ResourceState(Enum):
    
    ACTIVE = "ACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

