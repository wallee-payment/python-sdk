# coding: utf-8
from enum import Enum, unique


@unique
class TaxCalculation(Enum):
    
    TAX_INCLUDED = "TAX_INCLUDED"
    TAX_NOT_INCLUDED = "TAX_NOT_INCLUDED"

