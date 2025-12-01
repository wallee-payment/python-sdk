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
from wallee.models.charge_state import ChargeState
from wallee.models.charge_type import ChargeType
from wallee.models.failure_reason import FailureReason
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class Charge(BaseModel):
    """
    Charge
    """ # noqa: E501
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that this object is associated with.", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    type: Optional[ChargeType] = None
    user_failure_message: Optional[StrictStr] = Field(default=None, description="The message that can be displayed to the customer explaining why the charge failed, in the customer's language.", alias="userFailureMessage")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the charge will expire.", alias="timeoutOn")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[ChargeState] = None
    transaction: Optional[Transaction] = None
    __properties: ClassVar[List[str]] = ["plannedPurgeDate", "timeZone", "language", "spaceViewId", "type", "userFailureMessage", "createdOn", "version", "linkedSpaceId", "timeoutOn", "failureReason", "id", "state", "transaction"]

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
        """Create an instance of Charge from a JSON string"""
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
            "planned_purge_date",
            "time_zone",
            "language",
            "space_view_id",
            "user_failure_message",
            "created_on",
            "version",
            "linked_space_id",
            "timeout_on",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Charge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "spaceViewId": obj.get("spaceViewId"),
            "type": obj.get("type"),
            "userFailureMessage": obj.get("userFailureMessage"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


