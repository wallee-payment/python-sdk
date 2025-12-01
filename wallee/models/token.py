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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from typing import Optional, Set
from typing_extensions import Self

class Token(BaseModel):
    """
    Token
    """ # noqa: E501
    enabled_for_one_click_payment: Optional[StrictBool] = Field(default=None, description="Whether the token is enabled for one-click payments, which simplify the payment process for the customer. One-click tokens are linked to customers via the customer ID.", alias="enabledForOneClickPayment")
    customer_email_address: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="The customer's email address.", alias="customerEmailAddress")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    time_zone: Optional[StrictStr] = Field(default=None, description="The customer's time zone, which affects how dates and times are formatted when communicating with the customer.", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    token_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The reference used to identify the payment token (e.g. the customer's ID or email address).", alias="tokenReference")
    customer_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the customer in the external system.", alias="customerId")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    __properties: ClassVar[List[str]] = ["enabledForOneClickPayment", "customerEmailAddress", "plannedPurgeDate", "externalId", "timeZone", "language", "createdOn", "version", "linkedSpaceId", "tokenReference", "customerId", "id", "state"]

    @field_validator('token_reference')
    def token_reference_validate_regular_expression(cls, value):
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
        """Create an instance of Token from a JSON string"""
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
            "enabled_for_one_click_payment",
            "customer_email_address",
            "planned_purge_date",
            "external_id",
            "time_zone",
            "language",
            "created_on",
            "version",
            "linked_space_id",
            "token_reference",
            "customer_id",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Token from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "enabledForOneClickPayment": obj.get("enabledForOneClickPayment"),
            "customerEmailAddress": obj.get("customerEmailAddress"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "tokenReference": obj.get("tokenReference"),
            "customerId": obj.get("customerId"),
            "id": obj.get("id"),
            "state": obj.get("state")
        })
        return _obj


