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
from wallee.models.subscriber import Subscriber
from wallee.models.subscription_affiliate import SubscriptionAffiliate
from wallee.models.subscription_product_version import SubscriptionProductVersion
from wallee.models.subscription_state import SubscriptionState
from wallee.models.token import Token
from typing import Optional, Set
from typing_extensions import Self

class Subscription(BaseModel):
    """
    Subscription
    """ # noqa: E501
    subscriber: Optional[Subscriber] = None
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    terminated_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the subscription was terminated by.", alias="terminatedBy")
    description: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="A description used to identify the subscription.")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    initialized_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription was initialized.", alias="initializedOn")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    token: Optional[Token] = None
    reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the subscription.")
    terminated_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription was terminated.", alias="terminatedOn")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription was activate.", alias="activatedOn")
    terminating_on: Optional[datetime] = Field(default=None, description="The date and time when the termination of the subscription started.", alias="terminatingOn")
    current_product_version: Optional[SubscriptionProductVersion] = Field(default=None, alias="currentProductVersion")
    planned_termination_date: Optional[datetime] = Field(default=None, description="The date and time when the subscription is planned to be terminated.", alias="plannedTerminationDate")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionState] = None
    affiliate: Optional[SubscriptionAffiliate] = None
    termination_scheduled_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription was scheduled to be terminated.", alias="terminationScheduledOn")
    __properties: ClassVar[List[str]] = ["subscriber", "plannedPurgeDate", "terminatedBy", "description", "language", "initializedOn", "createdOn", "version", "token", "reference", "terminatedOn", "linkedSpaceId", "activatedOn", "terminatingOn", "currentProductVersion", "plannedTerminationDate", "id", "state", "affiliate", "terminationScheduledOn"]

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
        """Create an instance of Subscription from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "planned_purge_date",
            "terminated_by",
            "description",
            "language",
            "initialized_on",
            "created_on",
            "version",
            "reference",
            "terminated_on",
            "linked_space_id",
            "activated_on",
            "terminating_on",
            "planned_termination_date",
            "id",
            "termination_scheduled_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of subscriber
        if self.subscriber:
            _dict['subscriber'] = self.subscriber.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of current_product_version
        if self.current_product_version:
            _dict['currentProductVersion'] = self.current_product_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of affiliate
        if self.affiliate:
            _dict['affiliate'] = self.affiliate.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Subscription from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "subscriber": Subscriber.from_dict(obj["subscriber"]) if obj.get("subscriber") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "terminatedBy": obj.get("terminatedBy"),
            "description": obj.get("description"),
            "language": obj.get("language"),
            "initializedOn": obj.get("initializedOn"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "token": Token.from_dict(obj["token"]) if obj.get("token") is not None else None,
            "reference": obj.get("reference"),
            "terminatedOn": obj.get("terminatedOn"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "activatedOn": obj.get("activatedOn"),
            "terminatingOn": obj.get("terminatingOn"),
            "currentProductVersion": SubscriptionProductVersion.from_dict(obj["currentProductVersion"]) if obj.get("currentProductVersion") is not None else None,
            "plannedTerminationDate": obj.get("plannedTerminationDate"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "affiliate": SubscriptionAffiliate.from_dict(obj["affiliate"]) if obj.get("affiliate") is not None else None,
            "terminationScheduledOn": obj.get("terminationScheduledOn")
        })
        return _obj


