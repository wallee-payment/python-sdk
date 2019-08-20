# coding: utf-8
from enum import Enum, unique


@unique
class DataCollectionType(Enum):
    
    ONSITE = "ONSITE"
    OFFSITE = "OFFSITE"

