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
from wallee.models.dunning_case_state import DunningCaseState
from wallee.models.dunning_flow import DunningFlow
from wallee.models.transaction_invoice import TransactionInvoice
from typing import Optional, Set
from typing_extensions import Self

class DunningCase(BaseModel):
    """
    DunningCase
    """ # noqa: E501
    canceled_on: Optional[datetime] = Field(default=None, alias="canceledOn")
    derecognized_on: Optional[datetime] = Field(default=None, alias="derecognizedOn")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    initial_invoice: Optional[TransactionInvoice] = Field(default=None, alias="initialInvoice")
    succeeded_on: Optional[datetime] = Field(default=None, alias="succeededOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[DunningCaseState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    failed_on: Optional[datetime] = Field(default=None, alias="failedOn")
    flow: Optional[DunningFlow] = None
    __properties: ClassVar[List[str]] = ["canceledOn", "derecognizedOn", "plannedPurgeDate", "createdOn", "version", "linkedSpaceId", "initialInvoice", "succeededOn", "id", "state", "linkedTransaction", "failedOn", "flow"]

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
        """Create an instance of DunningCase from a JSON string"""
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
            "canceled_on",
            "derecognized_on",
            "planned_purge_date",
            "created_on",
            "version",
            "linked_space_id",
            "succeeded_on",
            "id",
            "linked_transaction",
            "failed_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of initial_invoice
        if self.initial_invoice:
            _dict['initialInvoice'] = self.initial_invoice.to_dict()
        # override the default output from pydantic by calling `to_dict()` of flow
        if self.flow:
            _dict['flow'] = self.flow.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DunningCase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "canceledOn": obj.get("canceledOn"),
            "derecognizedOn": obj.get("derecognizedOn"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "initialInvoice": TransactionInvoice.from_dict(obj["initialInvoice"]) if obj.get("initialInvoice") is not None else None,
            "succeededOn": obj.get("succeededOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "failedOn": obj.get("failedOn"),
            "flow": DunningFlow.from_dict(obj["flow"]) if obj.get("flow") is not None else None
        })
        return _obj


