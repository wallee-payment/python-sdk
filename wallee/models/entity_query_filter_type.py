# coding: utf-8
from enum import Enum, unique


@unique
class EntityQueryFilterType(Enum):
    
    LEAF = "LEAF"
    OR = "OR"
    AND = "AND"

