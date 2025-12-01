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
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.document_template_type import DocumentTemplateType
from typing import Optional, Set
from typing_extensions import Self

class DocumentTemplate(BaseModel):
    """
    A document template contains the customizations for a particular document template type.
    """ # noqa: E501
    delivery_enabled: Optional[StrictBool] = Field(default=None, description="Whether documents of this template should be delivered.", alias="deliveryEnabled")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="spaceId")
    default_template: Optional[StrictBool] = Field(default=None, description="Whether this is the default document template which is used whenever no specific template is specified for the same template type.", alias="defaultTemplate")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the document template.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    template_resource: Optional[StrictStr] = Field(default=None, description="The resource path to a custom template to be used to generate PDF documents.", alias="templateResource")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    type: Optional[DocumentTemplateType] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["deliveryEnabled", "linkedSpaceId", "spaceId", "defaultTemplate", "name", "plannedPurgeDate", "templateResource", "id", "state", "type", "version"]

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
        """Create an instance of DocumentTemplate from a JSON string"""
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
            "delivery_enabled",
            "linked_space_id",
            "space_id",
            "default_template",
            "name",
            "planned_purge_date",
            "template_resource",
            "id",
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
        """Create an instance of DocumentTemplate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "deliveryEnabled": obj.get("deliveryEnabled"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "spaceId": obj.get("spaceId"),
            "defaultTemplate": obj.get("defaultTemplate"),
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "templateResource": obj.get("templateResource"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "type": DocumentTemplateType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "version": obj.get("version")
        })
        return _obj


