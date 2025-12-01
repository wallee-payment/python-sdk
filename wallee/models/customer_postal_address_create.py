# coding: utf-8

"""
Wallee AG Python SDK

This library allows to interact with the Wallee AG payment service.

Copyright owner: Wallee AG
Website: https://en.wallee.com
Developer email: ecosystem-team@wallee.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


from __future__ import annotations
import pprint
import re  # noqa: F401
import json

from datetime import date
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.gender import Gender
from typing import Optional, Set
from typing_extensions import Self

class CustomerPostalAddressCreate(BaseModel):
    """
    CustomerPostalAddressCreate
    """ # noqa: E501
    country: Optional[StrictStr] = Field(default=None, description="The two-letter country code (ISO 3166 format).")
    mobile_phone_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The phone number of a mobile phone.", alias="mobilePhoneNumber")
    gender: Optional[Gender] = None
    organization_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The organization's name.", alias="organizationName")
    city: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The city, town or village.")
    commercial_register_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The commercial registration number of the organization.", alias="commercialRegisterNumber")
    social_security_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The social security number.", alias="socialSecurityNumber")
    given_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The given or first name.", alias="givenName")
    postcode: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The postal code, also known as ZIP, postcode, etc.")
    legal_organization_form: Optional[StrictInt] = Field(default=None, description="The legal form of the organization.", alias="legalOrganizationForm")
    sales_tax_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The sales tax number of the organization.", alias="salesTaxNumber")
    date_of_birth: Optional[date] = Field(default=None, description="The date of birth.", alias="dateOfBirth")
    dependent_locality: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The dependent locality which is a sub-division of the state.", alias="dependentLocality")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, description="The email address.", alias="emailAddress")
    phone_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The phone number.", alias="phoneNumber")
    sorting_code: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The sorting code identifying the post office where the PO Box is located.", alias="sortingCode")
    street: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(default=None, description="The street or PO Box.")
    family_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The family or last name.", alias="familyName")
    postal_state: Optional[StrictStr] = Field(default=None, description="The name of the region, typically a state, county, province or prefecture.", alias="postalState")
    salutation: Optional[Annotated[str, Field(strict=True, max_length=20)]] = Field(default=None, description="The salutation e.g. Mrs, Mr, Dr.")
    __properties: ClassVar[List[str]] = ["country", "mobilePhoneNumber", "gender", "organizationName", "city", "commercialRegisterNumber", "socialSecurityNumber", "givenName", "postcode", "legalOrganizationForm", "salesTaxNumber", "dateOfBirth", "dependentLocality", "emailAddress", "phoneNumber", "sortingCode", "street", "familyName", "postalState", "salutation"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of CustomerPostalAddressCreate from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of CustomerPostalAddressCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "country": obj.get("country"),
            "mobilePhoneNumber": obj.get("mobilePhoneNumber"),
            "gender": obj.get("gender"),
            "organizationName": obj.get("organizationName"),
            "city": obj.get("city"),
            "commercialRegisterNumber": obj.get("commercialRegisterNumber"),
            "socialSecurityNumber": obj.get("socialSecurityNumber"),
            "givenName": obj.get("givenName"),
            "postcode": obj.get("postcode"),
            "legalOrganizationForm": obj.get("legalOrganizationForm"),
            "salesTaxNumber": obj.get("salesTaxNumber"),
            "dateOfBirth": obj.get("dateOfBirth"),
            "dependentLocality": obj.get("dependentLocality"),
            "emailAddress": obj.get("emailAddress"),
            "phoneNumber": obj.get("phoneNumber"),
            "sortingCode": obj.get("sortingCode"),
            "street": obj.get("street"),
            "familyName": obj.get("familyName"),
            "postalState": obj.get("postalState"),
            "salutation": obj.get("salutation")
        })
        return _obj


