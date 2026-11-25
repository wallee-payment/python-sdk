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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.address import Address
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.express_checkout_session_state import ExpressCheckoutSessionState
from wallee.models.express_checkout_shipping_option import ExpressCheckoutShippingOption
from wallee.models.express_checkout_wallet_type import ExpressCheckoutWalletType
from wallee.models.failure_reason import FailureReason
from wallee.models.line_item import LineItem
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class ExpressCheckoutSession(BaseModel):
    """
    ExpressCheckoutSession
    """ # noqa: E501
    merchant_shipping_callback_url: Optional[StrictStr] = Field(default=None, description="The URL to fetch the shipping options from.", alias="merchantShippingCallbackUrl")
    authorization_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of the session.", alias="authorizationAmount")
    wallet_type: Optional[ExpressCheckoutWalletType] = Field(default=None, alias="walletType")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    time_zone: Optional[StrictStr] = Field(default=None, description="Customer time zone for presentation and cutoffs (same semantics as on Transaction).", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="Preferred language for customer-facing content (same semantics as on Transaction).")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the session was created.", alias="createdOn")
    line_items: Optional[List[LineItem]] = Field(default=None, alias="lineItems")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The spaceId linked to the entity.", alias="linkedSpaceId")
    merchant_redirect_url: Optional[StrictStr] = Field(default=None, description="The base URL on the merchant shop used to create the order.", alias="merchantRedirectUrl")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, alias="metaData")
    authorization_environment: Optional[ChargeAttemptEnvironment] = Field(default=None, alias="authorizationEnvironment")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    shipping_address: Optional[Address] = Field(default=None, alias="shippingAddress")
    currency: Optional[StrictStr] = Field(default=None, description="The currency of the session.")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    id: Optional[StrictInt] = Field(default=None, description="Id of the entity.")
    state: Optional[ExpressCheckoutSessionState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    shipping_options: Optional[List[ExpressCheckoutShippingOption]] = Field(default=None, alias="shippingOptions")
    transaction: Optional[Transaction] = None
    __properties: ClassVar[List[str]] = ["merchantShippingCallbackUrl", "authorizationAmount", "walletType", "plannedPurgeDate", "timeZone", "language", "createdOn", "lineItems", "linkedSpaceId", "merchantRedirectUrl", "metaData", "authorizationEnvironment", "failureReason", "shippingAddress", "currency", "billingAddress", "id", "state", "linkedTransaction", "shippingOptions", "transaction"]

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
        """Create an instance of ExpressCheckoutSession from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "merchant_shipping_callback_url",
            "authorization_amount",
            "planned_purge_date",
            "time_zone",
            "language",
            "created_on",
            "line_items",
            "linked_space_id",
            "merchant_redirect_url",
            "meta_data",
            "currency",
            "id",
            "linked_transaction",
            "shipping_options",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of wallet_type
        if self.wallet_type:
            _dict['walletType'] = self.wallet_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in shipping_options (list)
        _items = []
        if self.shipping_options:
            for _item_shipping_options in self.shipping_options:
                if _item_shipping_options:
                    _items.append(_item_shipping_options.to_dict())
            _dict['shippingOptions'] = _items
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExpressCheckoutSession from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "merchantShippingCallbackUrl": obj.get("merchantShippingCallbackUrl"),
            "authorizationAmount": obj.get("authorizationAmount"),
            "walletType": ExpressCheckoutWalletType.from_dict(obj["walletType"]) if obj.get("walletType") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "createdOn": obj.get("createdOn"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "merchantRedirectUrl": obj.get("merchantRedirectUrl"),
            "metaData": obj.get("metaData"),
            "authorizationEnvironment": obj.get("authorizationEnvironment"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "shippingAddress": Address.from_dict(obj["shippingAddress"]) if obj.get("shippingAddress") is not None else None,
            "currency": obj.get("currency"),
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "shippingOptions": [ExpressCheckoutShippingOption.from_dict(_item) for _item in obj["shippingOptions"]] if obj.get("shippingOptions") is not None else None,
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


