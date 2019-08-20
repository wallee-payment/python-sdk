# coding: utf-8
from enum import Enum, unique


@unique
class UserType(Enum):
    
    HUMAN_USER = "HUMAN_USER"
    SINGLE_SIGNON_USER = "SINGLE_SIGNON_USER"
    APPLICATION_USER = "APPLICATION_USER"
    ANONYMOUS_USER = "ANONYMOUS_USER"
    SERVER_USER = "SERVER_USER"

