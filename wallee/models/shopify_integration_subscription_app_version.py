# coding: utf-8
from enum import Enum, unique


@unique
class ShopifyIntegrationSubscriptionAppVersion(Enum):
    
    BASIC = "BASIC"
    SUBSCRIPTION = "SUBSCRIPTION"
    API_2019_07 = "API_2019_07"

