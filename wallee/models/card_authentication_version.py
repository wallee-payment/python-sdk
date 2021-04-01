# coding: utf-8
from enum import Enum, unique


@unique
class CardAuthenticationVersion(Enum):
    
    V1 = "V1"
    V2 = "V2"

