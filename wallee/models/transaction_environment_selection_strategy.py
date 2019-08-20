# coding: utf-8
from enum import Enum, unique


@unique
class TransactionEnvironmentSelectionStrategy(Enum):
    
    FORCE_TEST_ENVIRONMENT = "FORCE_TEST_ENVIRONMENT"
    FORCE_PRODUCTION_ENVIRONMENT = "FORCE_PRODUCTION_ENVIRONMENT"
    USE_CONFIGURATION = "USE_CONFIGURATION"

