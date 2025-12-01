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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.account_state import AccountState
from wallee.models.account_type import AccountType
from wallee.models.scope import Scope
from typing import Optional, Set
from typing_extensions import Self

class Account(BaseModel):
    """
    Account
    """ # noqa: E501
    active_or_restricted_active: Optional[StrictBool] = Field(default=None, description="Whether this account and all its parent accounts are active or restricted active.", alias="activeOrRestrictedActive")
    deleted_on: Optional[datetime] = Field(default=None, description="The date and time when the account was deleted.", alias="deletedOn")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    active: Optional[StrictBool] = Field(default=None, description="Whether this account and all its parent accounts are active.")
    parent_account: Optional[Account] = Field(default=None, alias="parentAccount")
    type: Optional[AccountType] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the account was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    deleted_by: Optional[StrictInt] = Field(default=None, description="The ID of a user the account was deleted by.", alias="deletedBy")
    restricted_active: Optional[StrictBool] = Field(default=None, description="Whether this account and all its parent accounts are active or restricted active. There is at least one account that is restricted active.", alias="restrictedActive")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the account was created by.", alias="createdBy")
    scope: Optional[Scope] = None
    name: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=200)]] = Field(default=None, description="The name used to identify the account.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[AccountState] = None
    subaccount_limit: Optional[StrictInt] = Field(default=None, description="The number of sub-accounts that can be created within this account.", alias="subaccountLimit")
    __properties: ClassVar[List[str]] = ["activeOrRestrictedActive", "deletedOn", "plannedPurgeDate", "active", "parentAccount", "type", "createdOn", "version", "deletedBy", "restrictedActive", "createdBy", "scope", "name", "id", "state", "subaccountLimit"]

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
        """Create an instance of Account from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "active_or_restricted_active",
            "deleted_on",
            "planned_purge_date",
            "active",
            "created_on",
            "version",
            "deleted_by",
            "restricted_active",
            "created_by",
            "name",
            "id",
            "subaccount_limit",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of parent_account
        if self.parent_account:
            _dict['parentAccount'] = self.parent_account.to_dict()
        # override the default output from pydantic by calling `to_dict()` of scope
        if self.scope:
            _dict['scope'] = self.scope.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Account from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeOrRestrictedActive": obj.get("activeOrRestrictedActive"),
            "deletedOn": obj.get("deletedOn"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "active": obj.get("active"),
            "parentAccount": Account.from_dict(obj["parentAccount"]) if obj.get("parentAccount") is not None else None,
            "type": obj.get("type"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "deletedBy": obj.get("deletedBy"),
            "restrictedActive": obj.get("restrictedActive"),
            "createdBy": obj.get("createdBy"),
            "scope": Scope.from_dict(obj["scope"]) if obj.get("scope") is not None else None,
            "name": obj.get("name"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "subaccountLimit": obj.get("subaccountLimit")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
Account.model_rebuild(raise_errors=False)

