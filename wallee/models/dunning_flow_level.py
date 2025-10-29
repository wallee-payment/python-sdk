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
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.document_template import DocumentTemplate
from wallee.models.dunning_flow import DunningFlow
from typing import Optional, Set
from typing_extensions import Self

class DunningFlowLevel(BaseModel):
    """
    DunningFlowLevel
    """
    period: Optional[StrictStr] = Field(default=None, description="The duration of the level before switching to the next one.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    reminder_template: Optional[DocumentTemplate] = Field(default=None, alias="reminderTemplate")
    priority: Optional[StrictInt] = Field(default=None, description="The priority indicates the sort order of the level. A low value indicates that the level is executed before any level with a higher value. Any change to this value affects future level selections. The value has to pe unique per dunning flow.")
    title: Optional[Dict[str, StrictStr]] = Field(default=None, description="The title is used to communicate the dunning level to the customer within the reminder.")
    processor: Optional[StrictInt] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    document_text: Optional[Dict[str, StrictStr]] = Field(default=None, description="This text is put in the reminder document of this dunning flow level.", alias="documentText")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The dunning flow level name is used internally to identify the dunning flow level. For example the name is used within search fields and hence it should be distinct and descriptive.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    flow: Optional[DunningFlow] = None
    __properties: ClassVar[List[str]] = ["period", "plannedPurgeDate", "reminderTemplate", "priority", "title", "processor", "version", "linkedSpaceId", "documentText", "name", "id", "state", "flow"]

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
        """Create an instance of DunningFlowLevel from a JSON string"""
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
            "period",
            "planned_purge_date",
            "priority",
            "title",
            "processor",
            "version",
            "linked_space_id",
            "document_text",
            "name",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of reminder_template
        if self.reminder_template:
            _dict['reminderTemplate'] = self.reminder_template.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flow
        if self.flow:
            _dict['flow'] = self.flow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DunningFlowLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "period": obj.get("period"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "reminderTemplate": DocumentTemplate.from_dict(obj["reminderTemplate"]) if obj.get("reminderTemplate") is not None else None,
            "priority": obj.get("priority"),
            "title": obj.get("title"),
            "processor": obj.get("processor"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "documentText": obj.get("documentText"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "flow": DunningFlow.from_dict(obj["flow"]) if obj.get("flow") is not None else None
        })
        return _obj


