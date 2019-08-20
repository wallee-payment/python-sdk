# coding: utf-8
from enum import Enum, unique


@unique
class LabelDescriptorCategory(Enum):
    
    HUMAN = "HUMAN"
    APPLICATION = "APPLICATION"

