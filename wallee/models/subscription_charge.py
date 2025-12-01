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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.subscription import Subscription
from wallee.models.subscription_charge_processing_type import SubscriptionChargeProcessingType
from wallee.models.subscription_charge_state import SubscriptionChargeState
from wallee.models.subscription_charge_type import SubscriptionChargeType
from wallee.models.subscription_ledger_entry import SubscriptionLedgerEntry
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionCharge(BaseModel):
    """
    The subscription charge represents a single charge carried out for a particular subscription.
    """ # noqa: E501
    discarded_on: Optional[datetime] = Field(default=None, description="The date and time when the charge was discarded.", alias="discardedOn")
    planned_execution_date: Optional[datetime] = Field(default=None, description="The date and time when the execution of the charge is planned.", alias="plannedExecutionDate")
    processing_type: Optional[SubscriptionChargeProcessingType] = Field(default=None, alias="processingType")
    ledger_entries: Optional[List[SubscriptionLedgerEntry]] = Field(default=None, description="The ledger entries that belong to the charge.", alias="ledgerEntries")
    discarded_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the charge was discarded by.", alias="discardedBy")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    success_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=500)]] = Field(default=None, description="The URL to redirect the customer back to after they successfully authenticated their payment.", alias="successUrl")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    subscription: Optional[Subscription] = None
    type: Optional[SubscriptionChargeType] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the charge was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the charge.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionChargeState] = None
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the charge failed.", alias="failedOn")
    transaction: Optional[Transaction] = None
    failed_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=500)]] = Field(default=None, description="The URL to redirect the customer back to after they canceled or failed to authenticated their payment.", alias="failedUrl")
    succeed_on: Optional[datetime] = Field(default=None, description="The date and time when the charge succeeded.", alias="succeedOn")
    __properties: ClassVar[List[str]] = ["discardedOn", "plannedExecutionDate", "processingType", "ledgerEntries", "discardedBy", "plannedPurgeDate", "externalId", "successUrl", "language", "subscription", "type", "createdOn", "version", "reference", "linkedSpaceId", "id", "state", "failedOn", "transaction", "failedUrl", "succeedOn"]

    @field_validator('reference')
    def reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
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
        """Create an instance of SubscriptionCharge from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "discarded_on",
            "planned_execution_date",
            "ledger_entries",
            "discarded_by",
            "planned_purge_date",
            "external_id",
            "success_url",
            "language",
            "created_on",
            "version",
            "reference",
            "linked_space_id",
            "id",
            "failed_on",
            "failed_url",
            "succeed_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in ledger_entries (list)
        _items = []
        if self.ledger_entries:
            for _item_ledger_entries in self.ledger_entries:
                if _item_ledger_entries:
                    _items.append(_item_ledger_entries.to_dict())
            _dict['ledgerEntries'] = _items
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionCharge from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discardedOn": obj.get("discardedOn"),
            "plannedExecutionDate": obj.get("plannedExecutionDate"),
            "processingType": obj.get("processingType"),
            "ledgerEntries": [SubscriptionLedgerEntry.from_dict(_item) for _item in obj["ledgerEntries"]] if obj.get("ledgerEntries") is not None else None,
            "discardedBy": obj.get("discardedBy"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "successUrl": obj.get("successUrl"),
            "language": obj.get("language"),
            "subscription": Subscription.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "type": obj.get("type"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "reference": obj.get("reference"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "failedOn": obj.get("failedOn"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "failedUrl": obj.get("failedUrl"),
            "succeedOn": obj.get("succeedOn")
        })
        return _obj


