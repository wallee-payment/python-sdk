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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.payment_facilitator_pricing_profile_dto import PaymentFacilitatorPricingProfileDto
from wallee.models.subscription_product_dto import SubscriptionProductDto
from wallee.models.walleejoin_admin_pricing_type import WalleejoinAdminPricingType
from wallee.models.walleejoin_partnership_type import WalleejoinPartnershipType
from typing import Optional, Set
from typing_extensions import Self

class WalleejoinAdminPartnerConfigurationResponseDto(BaseModel):
    """
    WalleejoinAdminPartnerConfigurationResponseDto
    """ # noqa: E501
    pricing_profile_sell_rates: Optional[List[PaymentFacilitatorPricingProfileDto]] = Field(default=None, alias="pricingProfileSellRates")
    revenue_share: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="revenueShare")
    subscription_products: Optional[List[SubscriptionProductDto]] = Field(default=None, alias="subscriptionProducts")
    one_off_referral: Optional[StrictInt] = Field(default=None, alias="oneOffReferral")
    pricing_profile_buy_rate: Optional[PaymentFacilitatorPricingProfileDto] = Field(default=None, alias="pricingProfileBuyRate")
    partnership_types: Optional[List[WalleejoinPartnershipType]] = Field(default=None, alias="partnershipTypes")
    partner_account: Optional[StrictInt] = Field(default=None, alias="partnerAccount")
    pricing_type: Optional[WalleejoinAdminPricingType] = Field(default=None, alias="pricingType")
    __properties: ClassVar[List[str]] = ["pricingProfileSellRates", "revenueShare", "subscriptionProducts", "oneOffReferral", "pricingProfileBuyRate", "partnershipTypes", "partnerAccount", "pricingType"]

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
        """Create an instance of WalleejoinAdminPartnerConfigurationResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in pricing_profile_sell_rates (list)
        _items = []
        if self.pricing_profile_sell_rates:
            for _item_pricing_profile_sell_rates in self.pricing_profile_sell_rates:
                if _item_pricing_profile_sell_rates:
                    _items.append(_item_pricing_profile_sell_rates.to_dict())
            _dict['pricingProfileSellRates'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in subscription_products (list)
        _items = []
        if self.subscription_products:
            for _item_subscription_products in self.subscription_products:
                if _item_subscription_products:
                    _items.append(_item_subscription_products.to_dict())
            _dict['subscriptionProducts'] = _items
        # override the default output from pydantic by calling `to_dict()` of pricing_profile_buy_rate
        if self.pricing_profile_buy_rate:
            _dict['pricingProfileBuyRate'] = self.pricing_profile_buy_rate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalleejoinAdminPartnerConfigurationResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "pricingProfileSellRates": [PaymentFacilitatorPricingProfileDto.from_dict(_item) for _item in obj["pricingProfileSellRates"]] if obj.get("pricingProfileSellRates") is not None else None,
            "revenueShare": obj.get("revenueShare"),
            "subscriptionProducts": [SubscriptionProductDto.from_dict(_item) for _item in obj["subscriptionProducts"]] if obj.get("subscriptionProducts") is not None else None,
            "oneOffReferral": obj.get("oneOffReferral"),
            "pricingProfileBuyRate": PaymentFacilitatorPricingProfileDto.from_dict(obj["pricingProfileBuyRate"]) if obj.get("pricingProfileBuyRate") is not None else None,
            "partnershipTypes": obj.get("partnershipTypes"),
            "partnerAccount": obj.get("partnerAccount"),
            "pricingType": obj.get("pricingType")
        })
        return _obj


