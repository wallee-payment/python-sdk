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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.address import Address
from wallee.models.creation_entity_state import CreationEntityState
from typing import Optional, Set
from typing_extensions import Self

class Subscriber(BaseModel):
    """
    A subscriber represents everyone who is subscribed to a product.
    """ # noqa: E501
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    description: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The description used to identify the subscriber.")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    language: Optional[StrictStr] = Field(default=None, description="The language that is used when communicating with the subscriber via emails and documents.")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the subscriber.")
    additional_allowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="Allow the subscriber to use these payment methods even if subscription products do not accept them.", alias="additionalAllowedPaymentMethodConfigurations")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Allow to store additional information about the object.", alias="metaData")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, description="The email address that is used to communicate with the subscriber. There can be only one subscriber per space with the same email address.", alias="emailAddress")
    disallowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="Prevent the subscriber from using these payment methods even if subscription products do accept them.", alias="disallowedPaymentMethodConfigurations")
    shipping_address: Optional[Address] = Field(default=None, alias="shippingAddress")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    __properties: ClassVar[List[str]] = ["plannedPurgeDate", "description", "externalId", "language", "version", "reference", "additionalAllowedPaymentMethodConfigurations", "linkedSpaceId", "metaData", "emailAddress", "disallowedPaymentMethodConfigurations", "shippingAddress", "billingAddress", "id", "state"]

    @field_validator('reference')
    def reference_validate_regular_expression(cls, value):
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
        """Create an instance of Subscriber from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "planned_purge_date",
            "description",
            "external_id",
            "language",
            "version",
            "reference",
            "additional_allowed_payment_method_configurations",
            "linked_space_id",
            "meta_data",
            "email_address",
            "disallowed_payment_method_configurations",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Subscriber from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "description": obj.get("description"),
            "externalId": obj.get("externalId"),
            "language": obj.get("language"),
            "version": obj.get("version"),
            "reference": obj.get("reference"),
            "additionalAllowedPaymentMethodConfigurations": obj.get("additionalAllowedPaymentMethodConfigurations"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "metaData": obj.get("metaData"),
            "emailAddress": obj.get("emailAddress"),
            "disallowedPaymentMethodConfigurations": obj.get("disallowedPaymentMethodConfigurations"),
            "shippingAddress": Address.from_dict(obj["shippingAddress"]) if obj.get("shippingAddress") is not None else None,
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state")
        })
        return _obj


