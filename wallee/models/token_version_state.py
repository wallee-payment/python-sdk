# coding: utf-8
from enum import Enum, unique


@unique
class TokenVersionState(Enum):
    
    UNINITIALIZED = "UNINITIALIZED"
    ACTIVE = "ACTIVE"
    OBSOLETE = "OBSOLETE"

