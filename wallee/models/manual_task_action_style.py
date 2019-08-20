# coding: utf-8
from enum import Enum, unique


@unique
class ManualTaskActionStyle(Enum):
    
    DEFAULT = "DEFAULT"
    PRIMARY = "PRIMARY"
    DANGER = "DANGER"

