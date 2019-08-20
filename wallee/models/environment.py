# coding: utf-8
from enum import Enum, unique


@unique
class Environment(Enum):
    
    LIVE = "LIVE"
    PREVIEW = "PREVIEW"

