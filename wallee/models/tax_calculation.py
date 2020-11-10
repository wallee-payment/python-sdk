# coding: utf-8
from enum import Enum, unique


@unique
class TaxCalculation(Enum):
    
    INCLUDED = "TAX_INCLUDED"
    NOT_INCLUDED = "TAX_NOT_INCLUDED"

