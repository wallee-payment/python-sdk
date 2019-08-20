# coding: utf-8
from enum import Enum, unique


@unique
class ProductFeeType(Enum):
    
    METERED_FEE = "METERED_FEE"
    SETUP_FEE = "SETUP_FEE"
    PERIOD_FEE = "PERIOD_FEE"

