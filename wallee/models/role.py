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
from wallee.models.account import Account
from wallee.models.permission import Permission
from wallee.models.role_state import RoleState
from typing import Optional, Set
from typing_extensions import Self

class Role(BaseModel):
    """
    Role
    """ # noqa: E501
    permissions: Optional[List[Permission]] = Field(default=None, description="The permissions granted to users with this role.")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The name used to identify the role.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[RoleState] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    account: Optional[Account] = None
    two_factor_required: Optional[StrictBool] = Field(default=None, description="Whether users with this role are required to use two-factor authentication.", alias="twoFactorRequired")
    __properties: ClassVar[List[str]] = ["permissions", "name", "plannedPurgeDate", "id", "state", "version", "account", "twoFactorRequired"]

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
        """Create an instance of Role from a JSON string"""
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
            "permissions",
            "name",
            "planned_purge_date",
            "id",
            "version",
            "two_factor_required",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in permissions (list)
        _items = []
        if self.permissions:
            for _item_permissions in self.permissions:
                if _item_permissions:
                    _items.append(_item_permissions.to_dict())
            _dict['permissions'] = _items
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Role from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "permissions": [Permission.from_dict(_item) for _item in obj["permissions"]] if obj.get("permissions") is not None else None,
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "version": obj.get("version"),
            "account": Account.from_dict(obj["account"]) if obj.get("account") is not None else None,
            "twoFactorRequired": obj.get("twoFactorRequired")
        })
        return _obj


