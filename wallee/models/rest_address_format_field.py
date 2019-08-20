# coding: utf-8
from enum import Enum, unique


@unique
class RestAddressFormatField(Enum):
    
    GIVEN_NAME = "GIVEN_NAME"
    FAMILY_NAME = "FAMILY_NAME"
    ORGANIZATION_NAME = "ORGANIZATION_NAME"
    STREET = "STREET"
    DEPENDENT_LOCALITY = "DEPENDENT_LOCALITY"
    CITY = "CITY"
    POSTAL_STATE = "POSTAL_STATE"
    POST_CODE = "POST_CODE"
    SORTING_CODE = "SORTING_CODE"
    COUNTRY = "COUNTRY"

