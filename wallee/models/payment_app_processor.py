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
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.payment_app_processor_state import PaymentAppProcessorState
from wallee.models.payment_processor_configuration import PaymentProcessorConfiguration
from typing import Optional, Set
from typing_extensions import Self

class PaymentAppProcessor(BaseModel):
    """
    PaymentAppProcessor
    """ # noqa: E501
    documentation_url: Optional[StrictStr] = Field(default=None, description="A URL pointing to the documentation that explains how to configure and use the processor.", alias="documentationUrl")
    configured_environment: Optional[ChargeAttemptEnvironment] = Field(default=None, alias="configuredEnvironment")
    external_id: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    svg_icon: Optional[Annotated[str, Field(strict=True, max_length=10000)]] = Field(default=None, description="An SVG icon representing the processor, displayed to the user in the interface.", alias="svgIcon")
    updated_on: Optional[datetime] = Field(default=None, description="The date and time when the processor was last updated.", alias="updatedOn")
    usable_in_production: Optional[StrictBool] = Field(default=None, description="Whether the processor is fully prepared and available for handling transactions in a production environment.", alias="usableInProduction")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the processor was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    processor_configuration: Optional[PaymentProcessorConfiguration] = Field(default=None, alias="processorConfiguration")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    usable_in_production_since: Optional[datetime] = Field(default=None, description="the date and time when the processor became fully usable and available for handling transactions in a production environment.", alias="usableInProductionSince")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the processor.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    installation_id: Optional[StrictInt] = Field(default=None, description="The installation ID identifies the Web App installation.", alias="installationId")
    production_mode_url: Optional[StrictStr] = Field(default=None, description="A URL pointing to the site where merchants can set up production mode for the processor.", alias="productionModeUrl")
    state: Optional[PaymentAppProcessorState] = None
    __properties: ClassVar[List[str]] = ["documentationUrl", "configuredEnvironment", "externalId", "svgIcon", "updatedOn", "usableInProduction", "createdOn", "version", "processorConfiguration", "linkedSpaceId", "usableInProductionSince", "name", "id", "installationId", "productionModeUrl", "state"]

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
        """Create an instance of PaymentAppProcessor from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "documentation_url",
            "external_id",
            "svg_icon",
            "updated_on",
            "usable_in_production",
            "created_on",
            "version",
            "linked_space_id",
            "usable_in_production_since",
            "name",
            "id",
            "installation_id",
            "production_mode_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of processor_configuration
        if self.processor_configuration:
            _dict['processorConfiguration'] = self.processor_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentAppProcessor from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "documentationUrl": obj.get("documentationUrl"),
            "configuredEnvironment": obj.get("configuredEnvironment"),
            "externalId": obj.get("externalId"),
            "svgIcon": obj.get("svgIcon"),
            "updatedOn": obj.get("updatedOn"),
            "usableInProduction": obj.get("usableInProduction"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "processorConfiguration": PaymentProcessorConfiguration.from_dict(obj["processorConfiguration"]) if obj.get("processorConfiguration") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "usableInProductionSince": obj.get("usableInProductionSince"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "installationId": obj.get("installationId"),
            "productionModeUrl": obj.get("productionModeUrl"),
            "state": obj.get("state")
        })
        return _obj


