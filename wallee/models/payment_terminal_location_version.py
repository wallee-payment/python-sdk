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
from wallee.models.payment_terminal_address import PaymentTerminalAddress
from wallee.models.payment_terminal_location import PaymentTerminalLocation
from wallee.models.payment_terminal_location_version_state import PaymentTerminalLocationVersionState
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalLocationVersion(BaseModel):
    """
    PaymentTerminalLocationVersion
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    address: Optional[PaymentTerminalAddress] = None
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the payment terminal location version was created by.", alias="createdBy")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    contact_address: Optional[PaymentTerminalAddress] = Field(default=None, alias="contactAddress")
    location: Optional[PaymentTerminalLocation] = None
    version_applied_immediately: Optional[StrictBool] = Field(default=None, description="Whether payment terminals are immediately updated to this configuration version. If not, it will be applied during the maintenance window.", alias="versionAppliedImmediately")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentTerminalLocationVersionState] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "address", "createdBy", "plannedPurgeDate", "contactAddress", "location", "versionAppliedImmediately", "id", "state", "createdOn", "version"]

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
        """Create an instance of PaymentTerminalLocationVersion from a JSON string"""
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
            "created_by",
            "planned_purge_date",
            "version_applied_immediately",
            "id",
            "created_on",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address
        if self.address:
            _dict['address'] = self.address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contact_address
        if self.contact_address:
            _dict['contactAddress'] = self.contact_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of location
        if self.location:
            _dict['location'] = self.location.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalLocationVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "address": PaymentTerminalAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "createdBy": obj.get("createdBy"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "contactAddress": PaymentTerminalAddress.from_dict(obj["contactAddress"]) if obj.get("contactAddress") is not None else None,
            "location": PaymentTerminalLocation.from_dict(obj["location"]) if obj.get("location") is not None else None,
            "versionAppliedImmediately": obj.get("versionAppliedImmediately"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version")
        })
        return _obj


