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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.dunning_case import DunningCase
from wallee.models.dunning_case_level_state import DunningCaseLevelState
from wallee.models.environment import Environment
from typing import Optional, Set
from typing_extensions import Self

class DunningCaseLevel(BaseModel):
    """
    DunningCaseLevel
    """ # noqa: E501
    canceled_on: Optional[datetime] = Field(default=None, alias="canceledOn")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    flow_level: Optional[StrictInt] = Field(default=None, alias="flowLevel")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, alias="timeoutOn")
    environment: Optional[Environment] = None
    succeeded_on: Optional[datetime] = Field(default=None, alias="succeededOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    invoice: Optional[StrictInt] = None
    state: Optional[DunningCaseLevelState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    failed_on: Optional[datetime] = Field(default=None, alias="failedOn")
    most_recent_level: Optional[StrictBool] = Field(default=None, alias="mostRecentLevel")
    dunning_case: Optional[DunningCase] = Field(default=None, alias="dunningCase")
    __properties: ClassVar[List[str]] = ["canceledOn", "plannedPurgeDate", "language", "createdOn", "version", "flowLevel", "linkedSpaceId", "timeoutOn", "environment", "succeededOn", "id", "invoice", "state", "linkedTransaction", "failedOn", "mostRecentLevel", "dunningCase"]

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
        """Create an instance of DunningCaseLevel from a JSON string"""
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
            "canceled_on",
            "planned_purge_date",
            "language",
            "created_on",
            "version",
            "flow_level",
            "linked_space_id",
            "timeout_on",
            "succeeded_on",
            "id",
            "invoice",
            "linked_transaction",
            "failed_on",
            "most_recent_level",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of dunning_case
        if self.dunning_case:
            _dict['dunningCase'] = self.dunning_case.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DunningCaseLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canceledOn": obj.get("canceledOn"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "language": obj.get("language"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "flowLevel": obj.get("flowLevel"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "environment": obj.get("environment"),
            "succeededOn": obj.get("succeededOn"),
            "id": obj.get("id"),
            "invoice": obj.get("invoice"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "failedOn": obj.get("failedOn"),
            "mostRecentLevel": obj.get("mostRecentLevel"),
            "dunningCase": DunningCase.from_dict(obj["dunningCase"]) if obj.get("dunningCase") is not None else None
        })
        return _obj


