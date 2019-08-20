# coding: utf-8
from enum import Enum, unique


@unique
class PaymentContractState(Enum):
    
    PENDING = "PENDING"
    ACTIVE = "ACTIVE"
    TERMINATING = "TERMINATING"
    TERMINATED = "TERMINATED"
    REJECTED = "REJECTED"

