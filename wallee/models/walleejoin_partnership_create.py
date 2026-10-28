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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.walleejoin_partnership_state import WalleejoinPartnershipState
from wallee.models.walleejoin_partnership_type import WalleejoinPartnershipType
from typing import Optional, Set
from typing_extensions import Self

class WalleejoinPartnershipCreate(BaseModel):
    """
    WalleejoinPartnershipCreate
    """ # noqa: E501
    terminated_on: Optional[datetime] = Field(default=None, description="The date and time when the partnership was terminated.", alias="terminatedOn")
    pricing_profile_sell_rate: Optional[Dict[str, Any]] = Field(default=None, alias="pricingProfileSellRate")
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the partnership was activated.", alias="activatedOn")
    merchant_account: Optional[StrictInt] = Field(default=None, description="The ID of the merchant account.", alias="merchantAccount")
    invitation_email_address: Optional[StrictStr] = Field(default=None, description="The email address the merchant was invited with.", alias="invitationEmailAddress")
    partnership_type: Optional[WalleejoinPartnershipType] = Field(default=None, alias="partnershipType")
    state: Optional[WalleejoinPartnershipState] = None
    subscription_product_id: Optional[StrictInt] = Field(default=None, description="The ID of the product.", alias="subscriptionProductId")
    partner_account: Optional[StrictInt] = Field(default=None, description="The ID of the partner account.", alias="partnerAccount")
    __properties: ClassVar[List[str]] = ["terminatedOn", "pricingProfileSellRate", "activatedOn", "merchantAccount", "invitationEmailAddress", "partnershipType", "state", "subscriptionProductId", "partnerAccount"]

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
        """Create an instance of WalleejoinPartnershipCreate from a JSON string"""
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
        """Create an instance of WalleejoinPartnershipCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "terminatedOn": obj.get("terminatedOn"),
            "pricingProfileSellRate": obj.get("pricingProfileSellRate"),
            "activatedOn": obj.get("activatedOn"),
            "merchantAccount": obj.get("merchantAccount"),
            "invitationEmailAddress": obj.get("invitationEmailAddress"),
            "partnershipType": obj.get("partnershipType"),
            "state": obj.get("state"),
            "subscriptionProductId": obj.get("subscriptionProductId"),
            "partnerAccount": obj.get("partnerAccount")
        })
        return _obj


