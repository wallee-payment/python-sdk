# coding: utf-8
from enum import Enum, unique


@unique
class FailureCategory(Enum):
    
    TEMPORARY_ISSUE = "TEMPORARY_ISSUE"
    INTERNAL = "INTERNAL"
    END_USER = "END_USER"
    CONFIGURATION = "CONFIGURATION"
    DEVELOPER = "DEVELOPER"

