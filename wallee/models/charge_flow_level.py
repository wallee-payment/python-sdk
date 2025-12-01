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
from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.charge import Charge
from wallee.models.charge_flow_level_configuration import ChargeFlowLevelConfiguration
from wallee.models.charge_flow_level_state import ChargeFlowLevelState
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class ChargeFlowLevel(BaseModel):
    """
    ChargeFlowLevel
    """ # noqa: E501
    synchronous_charge: Optional[Charge] = Field(default=None, alias="synchronousCharge")
    configuration: Optional[ChargeFlowLevelConfiguration] = None
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the charge flow level will expire.", alias="timeoutOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[ChargeFlowLevelState] = None
    asynchronous_charge: Optional[Charge] = Field(default=None, alias="asynchronousCharge")
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    token_charge: Optional[Charge] = Field(default=None, alias="tokenCharge")
    transaction: Optional[Transaction] = None
    __properties: ClassVar[List[str]] = ["synchronousCharge", "configuration", "plannedPurgeDate", "createdOn", "version", "linkedSpaceId", "timeoutOn", "id", "state", "asynchronousCharge", "linkedTransaction", "tokenCharge", "transaction"]

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
        """Create an instance of ChargeFlowLevel from a JSON string"""
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
            "planned_purge_date",
            "created_on",
            "version",
            "linked_space_id",
            "timeout_on",
            "id",
            "linked_transaction",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of synchronous_charge
        if self.synchronous_charge:
            _dict['synchronousCharge'] = self.synchronous_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of configuration
        if self.configuration:
            _dict['configuration'] = self.configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of asynchronous_charge
        if self.asynchronous_charge:
            _dict['asynchronousCharge'] = self.asynchronous_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token_charge
        if self.token_charge:
            _dict['tokenCharge'] = self.token_charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeFlowLevel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "synchronousCharge": Charge.from_dict(obj["synchronousCharge"]) if obj.get("synchronousCharge") is not None else None,
            "configuration": ChargeFlowLevelConfiguration.from_dict(obj["configuration"]) if obj.get("configuration") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "asynchronousCharge": Charge.from_dict(obj["asynchronousCharge"]) if obj.get("asynchronousCharge") is not None else None,
            "linkedTransaction": obj.get("linkedTransaction"),
            "tokenCharge": Charge.from_dict(obj["tokenCharge"]) if obj.get("tokenCharge") is not None else None,
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


