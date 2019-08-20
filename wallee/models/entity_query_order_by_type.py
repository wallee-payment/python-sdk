# coding: utf-8
from enum import Enum, unique


@unique
class EntityQueryOrderByType(Enum):
    
    DESC = "DESC"
    ASC = "ASC"

