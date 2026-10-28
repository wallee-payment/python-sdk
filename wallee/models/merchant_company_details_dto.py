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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.basic_address import BasicAddress
from wallee.models.legal_form import LegalForm
from typing import Optional, Set
from typing_extensions import Self

class MerchantCompanyDetailsDto(BaseModel):
    """
    MerchantCompanyDetailsDto
    """ # noqa: E501
    business_sector: Optional[StrictStr] = Field(default=None, description="The business sector code or category of the merchant.", alias="businessSector")
    extract: Optional[StrictStr] = Field(default=None, description="The commercial register extract or reference.")
    incorporation_year: Optional[StrictStr] = Field(default=None, description="The year in which the merchant company was incorporated.", alias="incorporationYear")
    organization_name: Optional[StrictStr] = Field(default=None, description="The registered legal name of the merchant company.", alias="organizationName")
    business_description: Optional[StrictStr] = Field(default=None, description="A short description of the merchant's business activity.", alias="businessDescription")
    sales_tax_number: Optional[StrictStr] = Field(default=None, description="The sales tax or VAT number of the merchant company.", alias="salesTaxNumber")
    business_identification_number: Optional[StrictStr] = Field(default=None, description="The official business identification number of the merchant company.", alias="businessIdentificationNumber")
    incorporation_address: Optional[BasicAddress] = Field(default=None, alias="incorporationAddress")
    legal_form: Optional[LegalForm] = Field(default=None, alias="legalForm")
    __properties: ClassVar[List[str]] = ["businessSector", "extract", "incorporationYear", "organizationName", "businessDescription", "salesTaxNumber", "businessIdentificationNumber", "incorporationAddress", "legalForm"]

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
        """Create an instance of MerchantCompanyDetailsDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of incorporation_address
        if self.incorporation_address:
            _dict['incorporationAddress'] = self.incorporation_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantCompanyDetailsDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "businessSector": obj.get("businessSector"),
            "extract": obj.get("extract"),
            "incorporationYear": obj.get("incorporationYear"),
            "organizationName": obj.get("organizationName"),
            "businessDescription": obj.get("businessDescription"),
            "salesTaxNumber": obj.get("salesTaxNumber"),
            "businessIdentificationNumber": obj.get("businessIdentificationNumber"),
            "incorporationAddress": BasicAddress.from_dict(obj["incorporationAddress"]) if obj.get("incorporationAddress") is not None else None,
            "legalForm": obj.get("legalForm")
        })
        return _obj


