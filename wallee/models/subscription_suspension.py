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
from wallee.models.subscription import Subscription
from wallee.models.subscription_suspension_action import SubscriptionSuspensionAction
from wallee.models.subscription_suspension_reason import SubscriptionSuspensionReason
from wallee.models.subscription_suspension_state import SubscriptionSuspensionState
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionSuspension(BaseModel):
    """
    SubscriptionSuspension
    """ # noqa: E501
    effective_end_date: Optional[datetime] = Field(default=None, description="The date and time when the suspension ended.", alias="effectiveEndDate")
    note: Optional[Annotated[str, Field(strict=True, max_length=300)]] = Field(default=None, description="A note that contains details about the suspension. It is not disclosed to the subscriber.")
    reason: Optional[SubscriptionSuspensionReason] = None
    period_bill: Optional[StrictInt] = Field(default=None, description="The period bill that led to the suspension of the subscription.", alias="periodBill")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    subscription: Optional[Subscription] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    planned_end_date: Optional[datetime] = Field(default=None, description="The date and time when the suspension is planned to end.", alias="plannedEndDate")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    end_action: Optional[SubscriptionSuspensionAction] = Field(default=None, alias="endAction")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionSuspensionState] = None
    __properties: ClassVar[List[str]] = ["effectiveEndDate", "note", "reason", "periodBill", "plannedPurgeDate", "language", "subscription", "createdOn", "version", "plannedEndDate", "linkedSpaceId", "endAction", "id", "state"]

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
        """Create an instance of SubscriptionSuspension from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "effective_end_date",
            "note",
            "period_bill",
            "planned_purge_date",
            "language",
            "created_on",
            "version",
            "planned_end_date",
            "linked_space_id",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionSuspension from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "effectiveEndDate": obj.get("effectiveEndDate"),
            "note": obj.get("note"),
            "reason": obj.get("reason"),
            "periodBill": obj.get("periodBill"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "language": obj.get("language"),
            "subscription": Subscription.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "plannedEndDate": obj.get("plannedEndDate"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "endAction": obj.get("endAction"),
            "id": obj.get("id"),
            "state": obj.get("state")
        })
        return _obj


