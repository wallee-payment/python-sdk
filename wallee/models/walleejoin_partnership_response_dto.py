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
from wallee.models.pricing_history_dto import PricingHistoryDto
from wallee.models.walleejoin_admin_pricing_type import WalleejoinAdminPricingType
from wallee.models.walleejoin_partnership import WalleejoinPartnership
from wallee.models.walleejoin_partnership_state import WalleejoinPartnershipState
from wallee.models.walleejoin_partnership_type import WalleejoinPartnershipType
from typing import Optional, Set
from typing_extensions import Self

class WalleejoinPartnershipResponseDto(BaseModel):
    """
    WalleejoinPartnershipResponseDto
    """ # noqa: E501
    partnership: Optional[WalleejoinPartnership] = None
    merchant_account: Optional[StrictInt] = Field(default=None, alias="merchantAccount")
    allowed_to_sell_scope_products: Optional[StrictBool] = Field(default=None, alias="allowedToSellScopeProducts")
    pricing_history: Optional[PricingHistoryDto] = Field(default=None, alias="pricingHistory")
    partnership_type: Optional[WalleejoinPartnershipType] = Field(default=None, alias="partnershipType")
    state: Optional[WalleejoinPartnershipState] = None
    updated_on: Optional[datetime] = Field(default=None, alias="updatedOn")
    allowed_pricing_type: Optional[WalleejoinAdminPricingType] = Field(default=None, alias="allowedPricingType")
    created_on: Optional[datetime] = Field(default=None, alias="createdOn")
    subscription_product_id: Optional[StrictInt] = Field(default=None, alias="subscriptionProductId")
    partner_account: Optional[StrictInt] = Field(default=None, alias="partnerAccount")
    __properties: ClassVar[List[str]] = ["partnership", "merchantAccount", "allowedToSellScopeProducts", "pricingHistory", "partnershipType", "state", "updatedOn", "allowedPricingType", "createdOn", "subscriptionProductId", "partnerAccount"]

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
        """Create an instance of WalleejoinPartnershipResponseDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of partnership
        if self.partnership:
            _dict['partnership'] = self.partnership.to_dict()
        # override the default output from pydantic by calling `to_dict()` of pricing_history
        if self.pricing_history:
            _dict['pricingHistory'] = self.pricing_history.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WalleejoinPartnershipResponseDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "partnership": WalleejoinPartnership.from_dict(obj["partnership"]) if obj.get("partnership") is not None else None,
            "merchantAccount": obj.get("merchantAccount"),
            "allowedToSellScopeProducts": obj.get("allowedToSellScopeProducts"),
            "pricingHistory": PricingHistoryDto.from_dict(obj["pricingHistory"]) if obj.get("pricingHistory") is not None else None,
            "partnershipType": obj.get("partnershipType"),
            "state": obj.get("state"),
            "updatedOn": obj.get("updatedOn"),
            "allowedPricingType": obj.get("allowedPricingType"),
            "createdOn": obj.get("createdOn"),
            "subscriptionProductId": obj.get("subscriptionProductId"),
            "partnerAccount": obj.get("partnerAccount")
        })
        return _obj


