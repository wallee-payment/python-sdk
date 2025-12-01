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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.subscription_product_state import SubscriptionProductState
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProductActive(BaseModel):
    """
    A subscription product represents a product to which a subscriber can subscribe to. A product defines how much the subscription costs and in what cycles the subscribe is charged.
    """ # noqa: E501
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing products, they can be sorted by this number.", alias="sortOrder")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the product.")
    product_locked: Optional[StrictBool] = Field(default=None, description="Whether subscriptions can be switched to or from this product, or whether they are locked in.", alias="productLocked")
    state: Optional[SubscriptionProductState] = None
    failed_payment_suspension_period: Optional[StrictStr] = Field(default=None, description="The period after which a subscription that has been suspended due to a failed payment is terminated.", alias="failedPaymentSuspensionPeriod")
    allowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="The payment methods that can be used to subscribe to this product. If none are selected, no restriction is applied.", alias="allowedPaymentMethodConfigurations")
    version: StrictInt = Field(description="The version number indicates the version of the entity. The version is incremented whenever the entity is changed.")
    __properties: ClassVar[List[str]] = ["sortOrder", "name", "productLocked", "state", "failedPaymentSuspensionPeriod", "allowedPaymentMethodConfigurations", "version"]

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
        """Create an instance of SubscriptionProductActive from a JSON string"""
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
        """Create an instance of SubscriptionProductActive from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sortOrder": obj.get("sortOrder"),
            "name": obj.get("name"),
            "productLocked": obj.get("productLocked"),
            "state": obj.get("state"),
            "failedPaymentSuspensionPeriod": obj.get("failedPaymentSuspensionPeriod"),
            "allowedPaymentMethodConfigurations": obj.get("allowedPaymentMethodConfigurations"),
            "version": obj.get("version")
        })
        return _obj


