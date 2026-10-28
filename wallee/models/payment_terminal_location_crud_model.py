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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.payment_terminal_address import PaymentTerminalAddress
from wallee.models.payment_terminal_location_state import PaymentTerminalLocationState
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalLocationCrudModel(BaseModel):
    """
    PaymentTerminalLocationCrudModel
    """ # noqa: E501
    production_merchant_id: Optional[Annotated[str, Field(min_length=15, strict=True, max_length=15)]] = Field(default=None, description="The production merchant identifier assigned to the location.", alias="productionMerchantId")
    address: Optional[PaymentTerminalAddress] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the payment terminal location.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    contact_address: Optional[PaymentTerminalAddress] = Field(default=None, alias="contactAddress")
    version_applied_immediately: Optional[StrictBool] = Field(default=None, description="Whether changes to the location are applied to terminals immediately.", alias="versionAppliedImmediately")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentTerminalLocationState] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["productionMerchantId", "address", "name", "plannedPurgeDate", "externalId", "contactAddress", "versionAppliedImmediately", "id", "state", "version"]

    @field_validator('production_merchant_id')
    def production_merchant_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([0-9a-zA-Z])+", value):
            raise ValueError(r"must validate the regular expression /([0-9a-zA-Z])+/")
        return value

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
        """Create an instance of PaymentTerminalLocationCrudModel from a JSON string"""
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
            "production_merchant_id",
            "name",
            "planned_purge_date",
            "external_id",
            "version_applied_immediately",
            "id",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalLocationCrudModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "productionMerchantId": obj.get("productionMerchantId"),
            "address": PaymentTerminalAddress.from_dict(obj["address"]) if obj.get("address") is not None else None,
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "contactAddress": PaymentTerminalAddress.from_dict(obj["contactAddress"]) if obj.get("contactAddress") is not None else None,
            "versionAppliedImmediately": obj.get("versionAppliedImmediately"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "version": obj.get("version")
        })
        return _obj


