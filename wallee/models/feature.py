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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.feature_category import FeatureCategory
from typing import Optional, Set
from typing_extensions import Self

class Feature(BaseModel):
    """
    Feature
    """ # noqa: E501
    required_features: Optional[List[StrictInt]] = Field(default=None, description="The features that must be enabled for this feature to work properly.", alias="requiredFeatures")
    visible: Optional[StrictBool] = Field(default=None, description="Whether the feature is visible to the user.")
    logo_path: Optional[StrictStr] = Field(default=None, description="The path to the feature's logo image.", alias="logoPath")
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing features, they can be sorted by this number.", alias="sortOrder")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    category: Optional[FeatureCategory] = None
    beta: Optional[StrictBool] = Field(default=None, description="Whether the feature is in beta stage and there may still be some issues.")
    __properties: ClassVar[List[str]] = ["requiredFeatures", "visible", "logoPath", "sortOrder", "name", "description", "id", "category", "beta"]

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
        """Create an instance of Feature from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "required_features",
            "visible",
            "logo_path",
            "sort_order",
            "name",
            "description",
            "id",
            "beta",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of category
        if self.category:
            _dict['category'] = self.category.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Feature from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requiredFeatures": obj.get("requiredFeatures"),
            "visible": obj.get("visible"),
            "logoPath": obj.get("logoPath"),
            "sortOrder": obj.get("sortOrder"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "category": FeatureCategory.from_dict(obj["category"]) if obj.get("category") is not None else None,
            "beta": obj.get("beta")
        })
        return _obj


