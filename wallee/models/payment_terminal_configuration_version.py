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
from wallee.models.payment_terminal_configuration import PaymentTerminalConfiguration
from wallee.models.payment_terminal_configuration_version_state import PaymentTerminalConfigurationVersionState
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalConfigurationVersion(BaseModel):
    """
    PaymentTerminalConfigurationVersion
    """ # noqa: E501
    maintenance_window_start: Optional[StrictStr] = Field(default=None, description="The start time of the terminal's maintenance window.", alias="maintenanceWindowStart")
    configuration: Optional[PaymentTerminalConfiguration] = None
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone of the payment terminal used to determine the maintenance window.", alias="timeZone")
    version_applied_immediately: Optional[StrictBool] = Field(default=None, description="Whether payment terminals are immediately updated to this configuration version. If not, it will be applied during the maintenance window.", alias="versionAppliedImmediately")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    connector_configurations: Optional[List[StrictInt]] = Field(default=None, description="The payment connector configurations that are available on the payment terminal.", alias="connectorConfigurations")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the payment terminal configuration version was created by.", alias="createdBy")
    default_currency: Optional[StrictStr] = Field(default=None, description="The default currency that is used if none is set on the payment terminal itself. If it is empty, the currency is derived from the location of the terminal.", alias="defaultCurrency")
    maintenance_window_duration: Optional[StrictStr] = Field(default=None, description="The permitted duration of the terminal's maintenance window.", alias="maintenanceWindowDuration")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentTerminalConfigurationVersionState] = None
    __properties: ClassVar[List[str]] = ["maintenanceWindowStart", "configuration", "plannedPurgeDate", "timeZone", "versionAppliedImmediately", "createdOn", "version", "linkedSpaceId", "connectorConfigurations", "createdBy", "defaultCurrency", "maintenanceWindowDuration", "id", "state"]

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
        """Create an instance of PaymentTerminalConfigurationVersion from a JSON string"""
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
            "maintenance_window_start",
            "planned_purge_date",
            "time_zone",
            "version_applied_immediately",
            "created_on",
            "version",
            "linked_space_id",
            "connector_configurations",
            "created_by",
            "default_currency",
            "maintenance_window_duration",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalConfigurationVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "maintenanceWindowStart": obj.get("maintenanceWindowStart"),
            "configuration": PaymentTerminalConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "timeZone": obj.get("timeZone"),
            "versionAppliedImmediately": obj.get("versionAppliedImmediately"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "connectorConfigurations": obj.get("connectorConfigurations"),
            "createdBy": obj.get("createdBy"),
            "defaultCurrency": obj.get("defaultCurrency"),
            "maintenanceWindowDuration": obj.get("maintenanceWindowDuration"),
            "id": obj.get("id"),
            "state": obj.get("state")
        })
        return _obj


