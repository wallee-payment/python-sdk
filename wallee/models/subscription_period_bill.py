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
from wallee.models.subscription_period_bill_state import SubscriptionPeriodBillState
from wallee.models.subscription_version import SubscriptionVersion
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionPeriodBill(BaseModel):
    """
    SubscriptionPeriodBill
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    period_start_date: Optional[datetime] = Field(default=None, description="The date and time when the period started.", alias="periodStartDate")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    subscription_version: Optional[SubscriptionVersion] = Field(default=None, alias="subscriptionVersion")
    effective_period_end_date: Optional[datetime] = Field(default=None, description="The date and time when the period actually ended.", alias="effectivePeriodEndDate")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionPeriodBillState] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the period bill was created.", alias="createdOn")
    planned_period_end_date: Optional[datetime] = Field(default=None, description="The date and time when the period is planned to end.", alias="plannedPeriodEndDate")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "periodStartDate", "plannedPurgeDate", "subscriptionVersion", "effectivePeriodEndDate", "language", "id", "state", "createdOn", "plannedPeriodEndDate", "version"]

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
        """Create an instance of SubscriptionPeriodBill from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "period_start_date",
            "planned_purge_date",
            "effective_period_end_date",
            "language",
            "id",
            "created_on",
            "planned_period_end_date",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of subscription_version
        if self.subscription_version:
            _dict['subscriptionVersion'] = self.subscription_version.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionPeriodBill from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "periodStartDate": obj.get("periodStartDate"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "subscriptionVersion": SubscriptionVersion.from_dict(obj["subscriptionVersion"]) if obj.get("subscriptionVersion") is not None else None,
            "effectivePeriodEndDate": obj.get("effectivePeriodEndDate"),
            "language": obj.get("language"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "createdOn": obj.get("createdOn"),
            "plannedPeriodEndDate": obj.get("plannedPeriodEndDate"),
            "version": obj.get("version")
        })
        return _obj


