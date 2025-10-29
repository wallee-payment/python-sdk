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
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.dunning_flow_type import DunningFlowType
from typing import Optional, Set
from typing_extensions import Self

class DunningFlow(BaseModel):
    """
    DunningFlow
    """
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    name: Optional[StrictStr] = Field(default=None, description="The dunning flow name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    conditions: Optional[List[StrictInt]] = Field(default=None, description="If a dunning flow meets all selected conditions, the dunning flow will be used to process the dunning case. If the conditions are not met the next dunning flow in line will be chosen according to the priorities.")
    priority: Optional[StrictInt] = Field(default=None, description="The priority orders the dunning flows. As such the priority determines together with the conditions the dunning flow the selection mechanism for a particular invoice. A change of the priority affects all future selections.")
    type: Optional[DunningFlowType] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "name", "plannedPurgeDate", "id", "state", "conditions", "priority", "type", "version"]

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
        """Create an instance of DunningFlow from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "name",
            "planned_purge_date",
            "id",
            "conditions",
            "priority",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DunningFlow from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "conditions": obj.get("conditions"),
            "priority": obj.get("priority"),
            "type": DunningFlowType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "version": obj.get("version")
        })
        return _obj


