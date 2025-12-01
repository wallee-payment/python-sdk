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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class PaymentProcessor(BaseModel):
    """
    Payment processors serve as intermediaries that establish connections with third-party companies, known as payment service providers. These providers are responsible for managing the technical aspects of payment transactions, ensuring seamless and secure payment processing.
    """ # noqa: E501
    company_name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The name of the company to which the processor belongs.", alias="companyName")
    headquarters_location: Optional[Dict[str, StrictStr]] = Field(default=None, description="Where the processor's headquarters are located.", alias="headquartersLocation")
    logo_path: Optional[StrictStr] = Field(default=None, description="The path to the logo image of the processor.", alias="logoPath")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    product_name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The name of the processor's product.", alias="productName")
    __properties: ClassVar[List[str]] = ["companyName", "headquartersLocation", "logoPath", "name", "description", "id", "productName"]

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
        """Create an instance of PaymentProcessor from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "company_name",
            "headquarters_location",
            "logo_path",
            "name",
            "description",
            "id",
            "product_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentProcessor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "companyName": obj.get("companyName"),
            "headquartersLocation": obj.get("headquartersLocation"),
            "logoPath": obj.get("logoPath"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "productName": obj.get("productName")
        })
        return _obj


