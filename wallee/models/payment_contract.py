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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.failure_reason import FailureReason
from wallee.models.payment_contract_state import PaymentContractState
from wallee.models.payment_contract_type import PaymentContractType
from typing import Optional, Set
from typing_extensions import Self

class PaymentContract(BaseModel):
    """
    PaymentContract
    """ # noqa: E501
    contract_type: Optional[PaymentContractType] = Field(default=None, alias="contractType")
    terminated_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the contract was terminated by.", alias="terminatedBy")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    terminated_on: Optional[datetime] = Field(default=None, description="The date and time when the contract was terminated.", alias="terminatedOn")
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the contract was activated.", alias="activatedOn")
    start_terminating_on: Optional[datetime] = Field(default=None, description="The date and time when the termination process of the contract was started.", alias="startTerminatingOn")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the contract was created by.", alias="createdBy")
    contract_identifier: Optional[StrictStr] = Field(default=None, description="The identifier of the contract.", alias="contractIdentifier")
    rejected_on: Optional[datetime] = Field(default=None, description="The date and time when the contract was rejected.", alias="rejectedOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentContractState] = None
    rejection_reason: Optional[FailureReason] = Field(default=None, alias="rejectionReason")
    account: Optional[StrictInt] = Field(default=None, description="This account that the contract belongs to.")
    __properties: ClassVar[List[str]] = ["contractType", "terminatedBy", "externalId", "createdOn", "version", "terminatedOn", "activatedOn", "startTerminatingOn", "createdBy", "contractIdentifier", "rejectedOn", "id", "state", "rejectionReason", "account"]

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
        """Create an instance of PaymentContract from a JSON string"""
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
            "terminated_by",
            "external_id",
            "created_on",
            "version",
            "terminated_on",
            "activated_on",
            "start_terminating_on",
            "created_by",
            "contract_identifier",
            "rejected_on",
            "id",
            "account",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of contract_type
        if self.contract_type:
            _dict['contractType'] = self.contract_type.to_dict()
        # override the default output from pydantic by calling `to_dict()` of rejection_reason
        if self.rejection_reason:
            _dict['rejectionReason'] = self.rejection_reason.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentContract from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contractType": PaymentContractType.from_dict(obj["contractType"]) if obj.get("contractType") is not None else None,
            "terminatedBy": obj.get("terminatedBy"),
            "externalId": obj.get("externalId"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "terminatedOn": obj.get("terminatedOn"),
            "activatedOn": obj.get("activatedOn"),
            "startTerminatingOn": obj.get("startTerminatingOn"),
            "createdBy": obj.get("createdBy"),
            "contractIdentifier": obj.get("contractIdentifier"),
            "rejectedOn": obj.get("rejectedOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "rejectionReason": FailureReason.from_dict(obj["rejectionReason"]) if obj.get("rejectionReason") is not None else None,
            "account": obj.get("account")
        })
        return _obj


