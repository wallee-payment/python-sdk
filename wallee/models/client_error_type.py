# coding: utf-8
from enum import Enum, unique


@unique
class ClientErrorType(Enum):
    
    END_USER_ERROR = "END_USER_ERROR"
    CONFIGURATION_ERROR = "CONFIGURATION_ERROR"
    DEVELOPER_ERROR = "DEVELOPER_ERROR"

