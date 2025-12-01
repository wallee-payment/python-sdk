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
from wallee.models.feature import Feature
from typing import Optional, Set
from typing_extensions import Self

class Permission(BaseModel):
    """
    Permission
    """ # noqa: E501
    parent: Optional[StrictInt] = Field(default=None, description="The group that this permission belongs to.")
    feature: Optional[Feature] = None
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    path_to_root: Optional[List[StrictInt]] = Field(default=None, description="All parents of this permission up to the root of the permission tree.", alias="pathToRoot")
    web_app_enabled: Optional[StrictBool] = Field(default=None, alias="webAppEnabled")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    leaf: Optional[StrictBool] = Field(default=None, description="Whether this is a leaf in the tree of permissions, and not a group.")
    title: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    group: Optional[StrictBool] = Field(default=None, description="Whether this is a permission group.")
    two_factor_required: Optional[StrictBool] = Field(default=None, description="Whether users with this permission are required to enable two-factor authentication.", alias="twoFactorRequired")
    __properties: ClassVar[List[str]] = ["parent", "feature", "name", "pathToRoot", "webAppEnabled", "description", "id", "leaf", "title", "group", "twoFactorRequired"]

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
        """Create an instance of Permission from a JSON string"""
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
            "parent",
            "name",
            "path_to_root",
            "web_app_enabled",
            "description",
            "id",
            "leaf",
            "title",
            "group",
            "two_factor_required",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of feature
        if self.feature:
            _dict['feature'] = self.feature.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Permission from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parent": obj.get("parent"),
            "feature": Feature.from_dict(obj["feature"]) if obj.get("feature") is not None else None,
            "name": obj.get("name"),
            "pathToRoot": obj.get("pathToRoot"),
            "webAppEnabled": obj.get("webAppEnabled"),
            "description": obj.get("description"),
            "id": obj.get("id"),
            "leaf": obj.get("leaf"),
            "title": obj.get("title"),
            "group": obj.get("group"),
            "twoFactorRequired": obj.get("twoFactorRequired")
        })
        return _obj


