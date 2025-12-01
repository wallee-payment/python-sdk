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
from wallee.models.account import Account
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.space_address import SpaceAddress
from wallee.models.tenant_database import TenantDatabase
from typing import Optional, Set
from typing_extensions import Self

class Space(BaseModel):
    """
    Space
    """ # noqa: E501
    active_or_restricted_active: Optional[StrictBool] = Field(default=None, description="Whether this space and all its parent accounts are active or restricted active.", alias="activeOrRestrictedActive")
    deleted_on: Optional[datetime] = Field(default=None, description="The date and time when the space was deleted.", alias="deletedOn")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    active: Optional[StrictBool] = Field(default=None, description="Whether this space and all its parent accounts are active.")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that is used to schedule and run background processes. This does not affect the formatting of dates in the user interface.", alias="timeZone")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the space was created.", alias="createdOn")
    primary_currency: Optional[StrictStr] = Field(default=None, description="The currency that is used to display aggregated amounts in the space.", alias="primaryCurrency")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    deleted_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the space was deleted by.", alias="deletedBy")
    request_limit: Optional[StrictInt] = Field(default=None, description="The maximum number of API requests that are accepted within two minutes. This limit can only be changed with special privileges.", alias="requestLimit")
    database: Optional[TenantDatabase] = None
    postal_address: Optional[SpaceAddress] = Field(default=None, alias="postalAddress")
    restricted_active: Optional[StrictBool] = Field(default=None, description="Whether this space and all its parent accounts are active or restricted active. There is least one parent account that is restricted active.", alias="restrictedActive")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the space was created by.", alias="createdBy")
    name: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=200)]] = Field(default=None, description="The name used to identify the space.")
    technical_contact_addresses: Optional[List[StrictStr]] = Field(default=None, description="The email address that will receive messages about technical issues and errors that occur in the space.", alias="technicalContactAddresses")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    account: Optional[Account] = None
    __properties: ClassVar[List[str]] = ["activeOrRestrictedActive", "deletedOn", "plannedPurgeDate", "active", "timeZone", "createdOn", "primaryCurrency", "version", "deletedBy", "requestLimit", "database", "postalAddress", "restrictedActive", "createdBy", "name", "technicalContactAddresses", "id", "state", "account"]

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
        """Create an instance of Space from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "active_or_restricted_active",
            "deleted_on",
            "planned_purge_date",
            "active",
            "time_zone",
            "created_on",
            "primary_currency",
            "version",
            "deleted_by",
            "request_limit",
            "restricted_active",
            "created_by",
            "name",
            "technical_contact_addresses",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of database
        if self.database:
            _dict['database'] = self.database.to_dict()
        # override the default output from pydantic by calling `to_dict()` of postal_address
        if self.postal_address:
            _dict['postalAddress'] = self.postal_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of account
        if self.account:
            _dict['account'] = self.account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Space from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "activeOrRestrictedActive": obj.get("activeOrRestrictedActive"),
            "deletedOn": obj.get("deletedOn"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "active": obj.get("active"),
            "timeZone": obj.get("timeZone"),
            "createdOn": obj.get("createdOn"),
            "primaryCurrency": obj.get("primaryCurrency"),
            "version": obj.get("version"),
            "deletedBy": obj.get("deletedBy"),
            "requestLimit": obj.get("requestLimit"),
            "database": TenantDatabase.from_dict(obj["database"]) if obj.get("database") is not None else None,
            "postalAddress": SpaceAddress.from_dict(obj["postalAddress"]) if obj.get("postalAddress") is not None else None,
            "restrictedActive": obj.get("restrictedActive"),
            "createdBy": obj.get("createdBy"),
            "name": obj.get("name"),
            "technicalContactAddresses": obj.get("technicalContactAddresses"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "account": Account.from_dict(obj["account"]) if obj.get("account") is not None else None
        })
        return _obj


