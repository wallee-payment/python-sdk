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
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.line_item import LineItem
from typing import Optional, Set
from typing_extensions import Self

class ExpressCheckoutSessionCreate(BaseModel):
    """
    ExpressCheckoutSessionCreate
    """ # noqa: E501
    line_items: List[LineItem] = Field(alias="lineItems")
    merchant_shipping_callback_url: Optional[StrictStr] = Field(default=None, description="The URL to fetch the shipping options from.", alias="merchantShippingCallbackUrl")
    merchant_redirect_url: StrictStr = Field(description="The base URL on the merchant shop used to create the order.", alias="merchantRedirectUrl")
    authorization_environment: ChargeAttemptEnvironment = Field(alias="authorizationEnvironment")
    time_zone: Optional[StrictStr] = Field(default=None, description="Customer time zone for presentation and cutoffs (same semantics as on Transaction).", alias="timeZone")
    currency: StrictStr = Field(description="The currency of the session.")
    language: Optional[StrictStr] = Field(default=None, description="Preferred language for customer-facing content (same semantics as on Transaction).")
    __properties: ClassVar[List[str]] = ["lineItems", "merchantShippingCallbackUrl", "merchantRedirectUrl", "authorizationEnvironment", "timeZone", "currency", "language"]

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
        """Create an instance of ExpressCheckoutSessionCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExpressCheckoutSessionCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "merchantShippingCallbackUrl": obj.get("merchantShippingCallbackUrl"),
            "merchantRedirectUrl": obj.get("merchantRedirectUrl"),
            "authorizationEnvironment": obj.get("authorizationEnvironment"),
            "timeZone": obj.get("timeZone"),
            "currency": obj.get("currency"),
            "language": obj.get("language")
        })
        return _obj


