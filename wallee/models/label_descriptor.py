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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.feature import Feature
from wallee.models.label_descriptor_category import LabelDescriptorCategory
from wallee.models.label_descriptor_group import LabelDescriptorGroup
from typing import Optional, Set
from typing_extensions import Self

class LabelDescriptor(BaseModel):
    """
    LabelDescriptor
    """ # noqa: E501
    features: Optional[List[Feature]] = Field(default=None, description="The features that this label belongs to.")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the object.")
    weight: Optional[StrictInt] = Field(default=None, description="When listing labels, they can be sorted by this number.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    category: Optional[LabelDescriptorCategory] = None
    type: Optional[StrictInt] = Field(default=None, description="The type of the label's value.")
    group: Optional[LabelDescriptorGroup] = None
    __properties: ClassVar[List[str]] = ["features", "name", "description", "weight", "id", "category", "type", "group"]

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
        """Create an instance of LabelDescriptor from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "features",
            "name",
            "description",
            "weight",
            "id",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LabelDescriptor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "features": [Feature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "weight": obj.get("weight"),
            "id": obj.get("id"),
            "category": obj.get("category"),
            "type": obj.get("type"),
            "group": LabelDescriptorGroup.from_dict(obj["group"]) if obj.get("group") is not None else None
        })
        return _obj


