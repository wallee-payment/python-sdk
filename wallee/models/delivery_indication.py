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
from wallee.models.delivery_indication_decision_reason import DeliveryIndicationDecisionReason
from wallee.models.delivery_indication_state import DeliveryIndicationState
from wallee.models.transaction import Transaction
from wallee.models.transaction_completion import TransactionCompletion
from typing import Optional, Set
from typing_extensions import Self

class DeliveryIndication(BaseModel):
    """
    DeliveryIndication
    """ # noqa: E501
    completion: Optional[TransactionCompletion] = None
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    automatic_decision_reason: Optional[DeliveryIndicationDecisionReason] = Field(default=None, alias="automaticDecisionReason")
    automatically_decided_on: Optional[datetime] = Field(default=None, description="The date and time when an automatic decision was made.", alias="automaticallyDecidedOn")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    manually_decided_by: Optional[StrictInt] = Field(default=None, description="The ID of the user who manually decided the delivery indication's state.", alias="manuallyDecidedBy")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the delivery indication will expire.", alias="timeoutOn")
    manual_decision_timeout_on: Optional[datetime] = Field(default=None, description="The date and time by which a decision must be made before the system automatically proceeds according to the connector's predefined settings.", alias="manualDecisionTimeoutOn")
    manually_decided_on: Optional[datetime] = Field(default=None, description="The date and time when a manual decision was made.", alias="manuallyDecidedOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[DeliveryIndicationState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    transaction: Optional[Transaction] = None
    __properties: ClassVar[List[str]] = ["completion", "plannedPurgeDate", "automaticDecisionReason", "automaticallyDecidedOn", "createdOn", "linkedSpaceId", "manuallyDecidedBy", "timeoutOn", "manualDecisionTimeoutOn", "manuallyDecidedOn", "id", "state", "linkedTransaction", "transaction"]

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
        """Create an instance of DeliveryIndication from a JSON string"""
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
            "planned_purge_date",
            "automatically_decided_on",
            "created_on",
            "linked_space_id",
            "manually_decided_by",
            "timeout_on",
            "manual_decision_timeout_on",
            "manually_decided_on",
            "id",
            "linked_transaction",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of completion
        if self.completion:
            _dict['completion'] = self.completion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of automatic_decision_reason
        if self.automatic_decision_reason:
            _dict['automaticDecisionReason'] = self.automatic_decision_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DeliveryIndication from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion": TransactionCompletion.from_dict(obj["completion"]) if obj.get("completion") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "automaticDecisionReason": DeliveryIndicationDecisionReason.from_dict(obj["automaticDecisionReason"]) if obj.get("automaticDecisionReason") is not None else None,
            "automaticallyDecidedOn": obj.get("automaticallyDecidedOn"),
            "createdOn": obj.get("createdOn"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "manuallyDecidedBy": obj.get("manuallyDecidedBy"),
            "timeoutOn": obj.get("timeoutOn"),
            "manualDecisionTimeoutOn": obj.get("manualDecisionTimeoutOn"),
            "manuallyDecidedOn": obj.get("manuallyDecidedOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


