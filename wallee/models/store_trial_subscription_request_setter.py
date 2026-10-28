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
from wallee.models.subscription_component_group_configuration_request_setter import SubscriptionComponentGroupConfigurationRequestSetter
from typing import Optional, Set
from typing_extensions import Self

class StoreTrialSubscriptionRequestSetter(BaseModel):
    """
    Model used to store a Trial Subscription, assigning it to an Account
    """ # noqa: E501
    coupon_codes: Optional[List[StrictStr]] = Field(default=None, alias="couponCodes")
    component_configurations: Optional[List[SubscriptionComponentGroupConfigurationRequestSetter]] = Field(default=None, alias="componentConfigurations")
    product_id: StrictInt = Field(description="ID of the product that will be used for the Trial Subscription assigned to the Account.", alias="productId")
    currency: StrictStr
    affiliate_id: Optional[StrictInt] = Field(default=None, description="ID of the affiliate to be added in the subscription assignment.", alias="affiliateId")
    __properties: ClassVar[List[str]] = ["couponCodes", "componentConfigurations", "productId", "currency", "affiliateId"]

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
        """Create an instance of StoreTrialSubscriptionRequestSetter from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in component_configurations (list)
        _items = []
        if self.component_configurations:
            for _item_component_configurations in self.component_configurations:
                if _item_component_configurations:
                    _items.append(_item_component_configurations.to_dict())
            _dict['componentConfigurations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of StoreTrialSubscriptionRequestSetter from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "couponCodes": obj.get("couponCodes"),
            "componentConfigurations": [SubscriptionComponentGroupConfigurationRequestSetter.from_dict(_item) for _item in obj["componentConfigurations"]] if obj.get("componentConfigurations") is not None else None,
            "productId": obj.get("productId"),
            "currency": obj.get("currency"),
            "affiliateId": obj.get("affiliateId")
        })
        return _obj


