# coding: utf-8
from enum import Enum, unique


@unique
class TerminalReceiptFormat(Enum):
    
    PDF = "PDF"
    TXT = "TXT"

