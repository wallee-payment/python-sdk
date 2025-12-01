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
from typing_extensions import Annotated
from wallee.models.address import Address
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.label import Label
from wallee.models.payment_connector_configuration import PaymentConnectorConfiguration
from wallee.models.payment_information_hash import PaymentInformationHash
from wallee.models.payment_method import PaymentMethod
from wallee.models.payment_method_brand import PaymentMethodBrand
from wallee.models.token import Token
from wallee.models.token_version_retry_strategy import TokenVersionRetryStrategy
from wallee.models.token_version_state import TokenVersionState
from wallee.models.token_version_type import TokenVersionType
from typing import Optional, Set
from typing_extensions import Self

class TokenVersion(BaseModel):
    """
    TokenVersion
    """ # noqa: E501
    payment_information_hashes: Optional[List[PaymentInformationHash]] = Field(default=None, description="The hashed payment information that the token version represents.", alias="paymentInformationHashes")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    type: Optional[TokenVersionType] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    retry_in: Optional[StrictStr] = Field(default=None, description="Retry interval when the strategy advises retrying later.", alias="retryIn")
    payment_connector_configuration: Optional[PaymentConnectorConfiguration] = Field(default=None, alias="paymentConnectorConfiguration")
    obsoleted_on: Optional[datetime] = Field(default=None, description="The date and time when the token version was marked obsolete.", alias="obsoletedOn")
    expires_on: Optional[datetime] = Field(default=None, description="The date and time when the token version is set to expire, after which it will be marked as obsolete.", alias="expiresOn")
    icon_url: Optional[StrictStr] = Field(default=None, description="The URL to the token's icon displayed to the customer.", alias="iconUrl")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[TokenVersionState] = None
    processor_token: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="The token name as specified by the processor.", alias="processorToken")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    payment_method_brand: Optional[PaymentMethodBrand] = Field(default=None, alias="paymentMethodBrand")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    last_retried_on: Optional[datetime] = Field(default=None, description="The date and time when the system last attempted a retry for this token version.", alias="lastRetriedOn")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    token: Optional[Token] = None
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    environment: Optional[ChargeAttemptEnvironment] = None
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the token version was activated.", alias="activatedOn")
    name: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="The name used to identify the token.")
    payment_method: Optional[PaymentMethod] = Field(default=None, alias="paymentMethod")
    shipping_address: Optional[Address] = Field(default=None, alias="shippingAddress")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    retry_strategy: Optional[TokenVersionRetryStrategy] = Field(default=None, alias="retryStrategy")
    __properties: ClassVar[List[str]] = ["paymentInformationHashes", "language", "type", "createdOn", "retryIn", "paymentConnectorConfiguration", "obsoletedOn", "expiresOn", "iconUrl", "id", "state", "processorToken", "plannedPurgeDate", "paymentMethodBrand", "version", "lastRetriedOn", "labels", "token", "linkedSpaceId", "environment", "activatedOn", "name", "paymentMethod", "shippingAddress", "billingAddress", "retryStrategy"]

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
        """Create an instance of TokenVersion from a JSON string"""
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
            "payment_information_hashes",
            "language",
            "created_on",
            "retry_in",
            "obsoleted_on",
            "expires_on",
            "icon_url",
            "id",
            "processor_token",
            "planned_purge_date",
            "version",
            "last_retried_on",
            "labels",
            "linked_space_id",
            "activated_on",
            "name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in payment_information_hashes (list)
        _items = []
        if self.payment_information_hashes:
            for _item_payment_information_hashes in self.payment_information_hashes:
                if _item_payment_information_hashes:
                    _items.append(_item_payment_information_hashes.to_dict())
            _dict['paymentInformationHashes'] = _items
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_connector_configuration
        if self.payment_connector_configuration:
            _dict['paymentConnectorConfiguration'] = self.payment_connector_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method_brand
        if self.payment_method_brand:
            _dict['paymentMethodBrand'] = self.payment_method_brand.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TokenVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentInformationHashes": [PaymentInformationHash.from_dict(_item) for _item in obj["paymentInformationHashes"]] if obj.get("paymentInformationHashes") is not None else None,
            "language": obj.get("language"),
            "type": TokenVersionType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "createdOn": obj.get("createdOn"),
            "retryIn": obj.get("retryIn"),
            "paymentConnectorConfiguration": PaymentConnectorConfiguration.from_dict(obj["paymentConnectorConfiguration"]) if obj.get("paymentConnectorConfiguration") is not None else None,
            "obsoletedOn": obj.get("obsoletedOn"),
            "expiresOn": obj.get("expiresOn"),
            "iconUrl": obj.get("iconUrl"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "processorToken": obj.get("processorToken"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "paymentMethodBrand": PaymentMethodBrand.from_dict(obj["paymentMethodBrand"]) if obj.get("paymentMethodBrand") is not None else None,
            "version": obj.get("version"),
            "lastRetriedOn": obj.get("lastRetriedOn"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "token": Token.from_dict(obj["token"]) if obj.get("token") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "environment": obj.get("environment"),
            "activatedOn": obj.get("activatedOn"),
            "name": obj.get("name"),
            "paymentMethod": PaymentMethod.from_dict(obj["paymentMethod"]) if obj.get("paymentMethod") is not None else None,
            "shippingAddress": Address.from_dict(obj["shippingAddress"]) if obj.get("shippingAddress") is not None else None,
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "retryStrategy": obj.get("retryStrategy")
        })
        return _obj


