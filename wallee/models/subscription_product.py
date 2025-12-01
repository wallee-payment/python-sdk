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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.subscription_product_state import SubscriptionProductState
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProduct(BaseModel):
    """
    A subscription product represents a product to which a subscriber can subscribe to. A product defines how much the subscription costs and in what cycles the subscribe is charged.
    """ # noqa: E501
    reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the product, e.g. the SKU.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="spaceId")
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing products, they can be sorted by this number.", alias="sortOrder")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the product.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    product_locked: Optional[StrictBool] = Field(default=None, description="Whether subscriptions can be switched to or from this product, or whether they are locked in.", alias="productLocked")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionProductState] = None
    failed_payment_suspension_period: Optional[StrictStr] = Field(default=None, description="The period after which a subscription that has been suspended due to a failed payment is terminated.", alias="failedPaymentSuspensionPeriod")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    allowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="The payment methods that can be used to subscribe to this product. If none are selected, no restriction is applied.", alias="allowedPaymentMethodConfigurations")
    __properties: ClassVar[List[str]] = ["reference", "linkedSpaceId", "spaceId", "sortOrder", "name", "plannedPurgeDate", "productLocked", "id", "state", "failedPaymentSuspensionPeriod", "version", "allowedPaymentMethodConfigurations"]

    @field_validator('reference')
    def reference_validate_regular_expression(cls, value):
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
        """Create an instance of SubscriptionProduct from a JSON string"""
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
            "reference",
            "linked_space_id",
            "space_id",
            "sort_order",
            "name",
            "planned_purge_date",
            "product_locked",
            "id",
            "failed_payment_suspension_period",
            "version",
            "allowed_payment_method_configurations",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionProduct from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "spaceId": obj.get("spaceId"),
            "sortOrder": obj.get("sortOrder"),
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "productLocked": obj.get("productLocked"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "failedPaymentSuspensionPeriod": obj.get("failedPaymentSuspensionPeriod"),
            "version": obj.get("version"),
            "allowedPaymentMethodConfigurations": obj.get("allowedPaymentMethodConfigurations")
        })
        return _obj


