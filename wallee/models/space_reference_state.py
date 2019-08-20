# coding: utf-8
from enum import Enum, unique


@unique
class SpaceReferenceState(Enum):
    
    RESTRICTED_ACTIVE = "RESTRICTED_ACTIVE"
    ACTIVE = "ACTIVE"
    INACTIVE = "INACTIVE"
    DELETING = "DELETING"
    DELETED = "DELETED"

