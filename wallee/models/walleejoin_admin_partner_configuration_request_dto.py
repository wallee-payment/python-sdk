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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.walleejoin_admin_pricing_type import WalleejoinAdminPricingType
from wallee.models.walleejoin_partnership_type import WalleejoinPartnershipType
from typing import Optional, Set
from typing_extensions import Self

class WalleejoinAdminPartnerConfigurationRequestDto(BaseModel):
    """
    WalleejoinAdminPartnerConfigurationRequestDto
    """ # noqa: E501
    allowed_to_sell_scope_products: Optional[StrictBool] = Field(default=None, alias="allowedToSellScopeProducts")
    pricing_profile_sell_rate_ids: Optional[List[StrictInt]] = Field(default=None, alias="pricingProfileSellRateIds")
    revenue_share: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="revenueShare")
    one_off_referral: Optional[StrictInt] = Field(default=None, alias="oneOffReferral")
    partner_account_id: Optional[StrictInt] = Field(default=None, alias="partnerAccountId")
    subscription_product_ids: Optional[List[StrictInt]] = Field(default=None, alias="subscriptionProductIds")
    pricing_profile_buy_rate_id: Optional[StrictInt] = Field(default=None, alias="pricingProfileBuyRateId")
    partnership_types: Optional[List[WalleejoinPartnershipType]] = Field(default=None, alias="partnershipTypes")
    pricing_type: Optional[WalleejoinAdminPricingType] = Field(default=None, alias="pricingType")
    __properties: ClassVar[List[str]] = ["allowedToSellScopeProducts", "pricingProfileSellRateIds", "revenueShare", "oneOffReferral", "partnerAccountId", "subscriptionProductIds", "pricingProfileBuyRateId", "partnershipTypes", "pricingType"]

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
        """Create an instance of WalleejoinAdminPartnerConfigurationRequestDto from a JSON string"""
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
        """Create an instance of WalleejoinAdminPartnerConfigurationRequestDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "allowedToSellScopeProducts": obj.get("allowedToSellScopeProducts"),
            "pricingProfileSellRateIds": obj.get("pricingProfileSellRateIds"),
            "revenueShare": obj.get("revenueShare"),
            "oneOffReferral": obj.get("oneOffReferral"),
            "partnerAccountId": obj.get("partnerAccountId"),
            "subscriptionProductIds": obj.get("subscriptionProductIds"),
            "pricingProfileBuyRateId": obj.get("pricingProfileBuyRateId"),
            "partnershipTypes": obj.get("partnershipTypes"),
            "pricingType": obj.get("pricingType")
        })
        return _obj


