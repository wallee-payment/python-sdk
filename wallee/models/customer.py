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
import re
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class Customer(BaseModel):
    """
    Customer
    """
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Allow to store additional information about the object.", alias="metaData")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, description="The customer's email address.", alias="emailAddress")
    family_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The customer's family or last name.", alias="familyName")
    given_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The customer's given or first name.", alias="givenName")
    preferred_currency: Optional[StrictStr] = Field(default=None, description="The customer's preferred currency.", alias="preferredCurrency")
    customer_id: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The customer's ID in the merchant's system.", alias="customerId")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "metaData", "emailAddress", "familyName", "givenName", "preferredCurrency", "customerId", "language", "id", "createdOn", "version"]

    @field_validator('customer_id')
    def customer_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

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
        """Create an instance of Customer from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "meta_data",
            "email_address",
            "family_name",
            "given_name",
            "preferred_currency",
            "customer_id",
            "language",
            "id",
            "created_on",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Customer from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "metaData": obj.get("metaData"),
            "emailAddress": obj.get("emailAddress"),
            "familyName": obj.get("familyName"),
            "givenName": obj.get("givenName"),
            "preferredCurrency": obj.get("preferredCurrency"),
            "customerId": obj.get("customerId"),
            "language": obj.get("language"),
            "id": obj.get("id"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version")
        })
        return _obj


