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
from wallee.models.label import Label
from wallee.models.transaction import Transaction
from wallee.models.transaction_void_mode import TransactionVoidMode
from wallee.models.transaction_void_state import TransactionVoidState
from typing import Optional, Set
from typing_extensions import Self

class TransactionVoid(BaseModel):
    """
    TransactionVoid
    """ # noqa: E501
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    mode: Optional[TransactionVoidMode] = None
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the object will expire.", alias="timeoutOn")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the transaction void was created by.", alias="createdBy")
    next_update_on: Optional[datetime] = Field(default=None, description="The date and time when the next update of the object's state is planned.", alias="nextUpdateOn")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    succeeded_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction void succeeded.", alias="succeededOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[TransactionVoidState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction void failed.", alias="failedOn")
    transaction: Optional[Transaction] = None
    processor_reference: Optional[StrictStr] = Field(default=None, description="The reference ID provided by the payment processor, used to trace the void through the external payment system.", alias="processorReference")
    __properties: ClassVar[List[str]] = ["plannedPurgeDate", "language", "spaceViewId", "createdOn", "version", "labels", "mode", "linkedSpaceId", "timeoutOn", "createdBy", "nextUpdateOn", "failureReason", "succeededOn", "id", "state", "linkedTransaction", "failedOn", "transaction", "processorReference"]

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
        """Create an instance of TransactionVoid from a JSON string"""
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
            "planned_purge_date",
            "language",
            "space_view_id",
            "created_on",
            "version",
            "labels",
            "linked_space_id",
            "timeout_on",
            "created_by",
            "next_update_on",
            "succeeded_on",
            "id",
            "linked_transaction",
            "failed_on",
            "processor_reference",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionVoid from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "language": obj.get("language"),
            "spaceViewId": obj.get("spaceViewId"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "mode": obj.get("mode"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "createdBy": obj.get("createdBy"),
            "nextUpdateOn": obj.get("nextUpdateOn"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "succeededOn": obj.get("succeededOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "failedOn": obj.get("failedOn"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "processorReference": obj.get("processorReference")
        })
        return _obj


