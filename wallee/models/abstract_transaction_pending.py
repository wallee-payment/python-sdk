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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.address_create import AddressCreate
from wallee.models.line_item_create import LineItemCreate
from wallee.models.tokenization_mode import TokenizationMode
from wallee.models.transaction_completion_behavior import TransactionCompletionBehavior
from typing import Optional, Set
from typing_extensions import Self

class AbstractTransactionPending(BaseModel):
    """
    AbstractTransactionPending
    """ # noqa: E501
    customer_email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, description="The customer's email address.", alias="customerEmailAddress")
    shipping_method: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The name of the shipping method used to ship the products.", alias="shippingMethod")
    invoice_merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the invoice.", alias="invoiceMerchantReference")
    success_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=2000)]] = Field(default=None, description="The URL to redirect the customer back to after they successfully authenticated their payment.", alias="successUrl")
    time_zone: Optional[StrictStr] = Field(default=None, description="The customer's time zone, which affects how dates and times are formatted when communicating with the customer.", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    tokenization_mode: Optional[TokenizationMode] = Field(default=None, alias="tokenizationMode")
    allowed_payment_method_brands: Optional[List[StrictInt]] = Field(default=None, description="The payment method brands that can be used to authorize the transaction.", alias="allowedPaymentMethodBrands")
    completion_behavior: Optional[TransactionCompletionBehavior] = Field(default=None, alias="completionBehavior")
    token: Optional[StrictInt] = Field(default=None, description="The payment token that should be used to charge the customer.")
    line_items: Optional[List[LineItemCreate]] = Field(default=None, description="The line items purchased by the customer.", alias="lineItems")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Allow to store additional information about the object.", alias="metaData")
    customer_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the customer in the external system.", alias="customerId")
    shipping_address: Optional[AddressCreate] = Field(default=None, alias="shippingAddress")
    currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the transaction's currency.")
    billing_address: Optional[AddressCreate] = Field(default=None, alias="billingAddress")
    merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the transaction.", alias="merchantReference")
    allowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="The payment method configurations that can be used to authorize the transaction.", alias="allowedPaymentMethodConfigurations")
    failed_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=2000)]] = Field(default=None, description="The URL to redirect the customer back to after they canceled or failed to authenticated their payment.", alias="failedUrl")
    __properties: ClassVar[List[str]] = ["customerEmailAddress", "shippingMethod", "invoiceMerchantReference", "successUrl", "timeZone", "language", "tokenizationMode", "allowedPaymentMethodBrands", "completionBehavior", "token", "lineItems", "metaData", "customerId", "shippingAddress", "currency", "billingAddress", "merchantReference", "allowedPaymentMethodConfigurations", "failedUrl"]

    @field_validator('invoice_merchant_reference')
    def invoice_merchant_reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

    @field_validator('merchant_reference')
    def merchant_reference_validate_regular_expression(cls, value):
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
        """Create an instance of AbstractTransactionPending from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AbstractTransactionPending from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "customerEmailAddress": obj.get("customerEmailAddress"),
            "shippingMethod": obj.get("shippingMethod"),
            "invoiceMerchantReference": obj.get("invoiceMerchantReference"),
            "successUrl": obj.get("successUrl"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "tokenizationMode": obj.get("tokenizationMode"),
            "allowedPaymentMethodBrands": obj.get("allowedPaymentMethodBrands"),
            "completionBehavior": obj.get("completionBehavior"),
            "token": obj.get("token"),
            "lineItems": [LineItemCreate.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "metaData": obj.get("metaData"),
            "customerId": obj.get("customerId"),
            "shippingAddress": AddressCreate.from_dict(obj["shippingAddress"]) if obj.get("shippingAddress") is not None else None,
            "currency": obj.get("currency"),
            "billingAddress": AddressCreate.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "merchantReference": obj.get("merchantReference"),
            "allowedPaymentMethodConfigurations": obj.get("allowedPaymentMethodConfigurations"),
            "failedUrl": obj.get("failedUrl")
        })
        return _obj


