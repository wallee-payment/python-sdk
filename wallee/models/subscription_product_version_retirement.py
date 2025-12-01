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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.subscription_product import SubscriptionProduct
from wallee.models.subscription_product_version import SubscriptionProductVersion
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProductVersionRetirement(BaseModel):
    """
    SubscriptionProductVersionRetirement
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    respect_termination_periods: Optional[StrictBool] = Field(default=None, description="Whether the subscriptions' termination periods should be respected.", alias="respectTerminationPeriods")
    product_version: Optional[SubscriptionProductVersion] = Field(default=None, alias="productVersion")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    target_product: Optional[SubscriptionProduct] = Field(default=None, alias="targetProduct")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "respectTerminationPeriods", "productVersion", "id", "createdOn", "version", "targetProduct"]

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
        """Create an instance of SubscriptionProductVersionRetirement from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "respect_termination_periods",
            "id",
            "created_on",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of product_version
        if self.product_version:
            _dict['productVersion'] = self.product_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_product
        if self.target_product:
            _dict['targetProduct'] = self.target_product.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionProductVersionRetirement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "respectTerminationPeriods": obj.get("respectTerminationPeriods"),
            "productVersion": SubscriptionProductVersion.from_dict(obj["productVersion"]) if obj.get("productVersion") is not None else None,
            "id": obj.get("id"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "targetProduct": SubscriptionProduct.from_dict(obj["targetProduct"]) if obj.get("targetProduct") is not None else None
        })
        return _obj


