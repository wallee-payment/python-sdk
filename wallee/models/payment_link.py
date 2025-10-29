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
import re
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.line_item import LineItem
from wallee.models.payment_link_address_handling_mode import PaymentLinkAddressHandlingMode
from wallee.models.payment_link_protection_mode import PaymentLinkProtectionMode
from wallee.models.payment_method_configuration import PaymentMethodConfiguration
from typing import Optional, Set
from typing_extensions import Self

class PaymentLink(BaseModel):
    """
    PaymentLink
    """
    shipping_address_handling_mode: Optional[PaymentLinkAddressHandlingMode] = Field(default=None, alias="shippingAddressHandlingMode")
    allowed_redirection_domains: Optional[Annotated[List[StrictStr], Field(min_length=1)]] = Field(default=None, description="The domains to which the user is allowed to be redirected after the payment is completed. The following options can be configured: Exact domain: enter a full domain, e.g. (https://example.com). Wildcard domain: use to allow subdomains, e.g. (https://*.example.com). All domains: use (ALL) to allow redirection to any domain (not recommended for security reasons). No domains : use (NONE) to disallow any redirection. Only one option per line is allowed. Invalid entries will be rejected. ", alias="allowedRedirectionDomains")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    language: Optional[StrictStr] = Field(default=None, description="The language for displaying the payment page. If not specified, it can be supplied via the 'language' request parameter.")
    available_from: Optional[datetime] = Field(default=None, description="The earliest date the payment link can be used to initiate a transaction. If no date is provided, the link will be available immediately.", alias="availableFrom")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    url: Optional[StrictStr] = Field(default=None, description="The public URL to share with customers for making payments.")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The line items representing what is being sold. If not specified, they can be supplied via request parameters.", alias="lineItems")
    protection_mode: Optional[PaymentLinkProtectionMode] = Field(default=None, alias="protectionMode")
    available_until: Optional[datetime] = Field(default=None, description="The latest date the payment link can be used to initiate a transaction. If no date is provided, the link will remain available indefinitely.", alias="availableUntil")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the payment link.")
    currency: Optional[StrictStr] = Field(default=None, description="The three-letter currency code (ISO 4217). If not specified, it must be provided in the 'currency' request parameter.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    maximal_number_of_transactions: Optional[StrictInt] = Field(default=None, description="The maximum number of transactions that can be initiated using the payment link.", alias="maximalNumberOfTransactions")
    allowed_payment_method_configurations: Optional[List[PaymentMethodConfiguration]] = Field(default=None, description="The payment method configurations that customers can use for making payments.", alias="allowedPaymentMethodConfigurations")
    applied_space_view: Optional[StrictInt] = Field(default=None, description="The payment link can be used within a specific space view, which may apply a customized design to the payment page.", alias="appliedSpaceView")
    billing_address_handling_mode: Optional[PaymentLinkAddressHandlingMode] = Field(default=None, alias="billingAddressHandlingMode")
    __properties: ClassVar[List[str]] = ["shippingAddressHandlingMode", "allowedRedirectionDomains", "plannedPurgeDate", "externalId", "language", "availableFrom", "version", "url", "lineItems", "protectionMode", "availableUntil", "linkedSpaceId", "name", "currency", "id", "state", "maximalNumberOfTransactions", "allowedPaymentMethodConfigurations", "appliedSpaceView", "billingAddressHandlingMode"]

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
        """Create an instance of PaymentLink from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "allowed_redirection_domains",
            "planned_purge_date",
            "external_id",
            "language",
            "available_from",
            "version",
            "url",
            "line_items",
            "available_until",
            "linked_space_id",
            "name",
            "currency",
            "id",
            "maximal_number_of_transactions",
            "allowed_payment_method_configurations",
            "applied_space_view",
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
        # override the default output from pydantic by calling `to_dict()` of each item in allowed_payment_method_configurations (list)
        _items = []
        if self.allowed_payment_method_configurations:
            for _item_allowed_payment_method_configurations in self.allowed_payment_method_configurations:
                if _item_allowed_payment_method_configurations:
                    _items.append(_item_allowed_payment_method_configurations.to_dict())
            _dict['allowedPaymentMethodConfigurations'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shippingAddressHandlingMode": obj.get("shippingAddressHandlingMode"),
            "allowedRedirectionDomains": obj.get("allowedRedirectionDomains"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "language": obj.get("language"),
            "availableFrom": obj.get("availableFrom"),
            "version": obj.get("version"),
            "url": obj.get("url"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "protectionMode": obj.get("protectionMode"),
            "availableUntil": obj.get("availableUntil"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "name": obj.get("name"),
            "currency": obj.get("currency"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "maximalNumberOfTransactions": obj.get("maximalNumberOfTransactions"),
            "allowedPaymentMethodConfigurations": [PaymentMethodConfiguration.from_dict(_item) for _item in obj["allowedPaymentMethodConfigurations"]] if obj.get("allowedPaymentMethodConfigurations") is not None else None,
            "appliedSpaceView": obj.get("appliedSpaceView"),
            "billingAddressHandlingMode": obj.get("billingAddressHandlingMode")
        })
        return _obj


