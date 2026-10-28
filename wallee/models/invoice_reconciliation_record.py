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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.bank_payment_type import BankPaymentType
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.failure_reason import FailureReason
from wallee.models.invoice_reconciliation_record_rejection_status import InvoiceReconciliationRecordRejectionStatus
from wallee.models.invoice_reconciliation_record_state import InvoiceReconciliationRecordState
from wallee.models.invoice_reconciliation_record_type import InvoiceReconciliationRecordType
from typing import Optional, Set
from typing_extensions import Self

class InvoiceReconciliationRecord(BaseModel):
    """
    InvoiceReconciliationRecord
    """ # noqa: E501
    discarded_on: Optional[datetime] = Field(default=None, description="The discarded on date indicates when the bank transaction has been discarded.", alias="discardedOn")
    last_resolution_failure: Optional[FailureReason] = Field(default=None, alias="lastResolutionFailure")
    country: Optional[StrictStr] = None
    rejection_status: Optional[InvoiceReconciliationRecordRejectionStatus] = Field(default=None, alias="rejectionStatus")
    city: Optional[StrictStr] = None
    resolved_by: Optional[StrictInt] = Field(default=None, alias="resolvedBy")
    discarded_by: Optional[StrictInt] = Field(default=None, alias="discardedBy")
    type: Optional[InvoiceReconciliationRecordType] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    payment_fee_currency: Optional[StrictStr] = Field(default=None, alias="paymentFeeCurrency")
    payment_reason: Optional[StrictStr] = Field(default=None, alias="paymentReason")
    reference_number: Optional[Annotated[str, Field(strict=True, max_length=255)]] = Field(default=None, alias="referenceNumber")
    street: Optional[StrictStr] = None
    family_name: Optional[StrictStr] = Field(default=None, alias="familyName")
    currency: Optional[StrictStr] = None
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[InvoiceReconciliationRecordState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    resolved_on: Optional[datetime] = Field(default=None, description="The resolved on date indicates when the bank transaction has been resolved.", alias="resolvedOn")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    address: Optional[StrictStr] = None
    given_name: Optional[StrictStr] = Field(default=None, alias="givenName")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    bank_payment_type: Optional[BankPaymentType] = Field(default=None, alias="bankPaymentType")
    value_date: Optional[datetime] = Field(default=None, alias="valueDate")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    payment_fee_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="paymentFeeAmount")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    environment: Optional[ChargeAttemptEnvironment] = None
    sender_bank_account: Optional[StrictStr] = Field(default=None, alias="senderBankAccount")
    participant_number: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="participantNumber")
    iban: Optional[Annotated[str, Field(strict=True, max_length=100)]] = None
    post_code: Optional[StrictStr] = Field(default=None, alias="postCode")
    unique_id: Optional[Annotated[str, Field(strict=True, max_length=500)]] = Field(default=None, alias="uniqueId")
    __properties: ClassVar[List[str]] = ["discardedOn", "lastResolutionFailure", "country", "rejectionStatus", "city", "resolvedBy", "discardedBy", "type", "createdOn", "paymentFeeCurrency", "paymentReason", "referenceNumber", "street", "familyName", "currency", "id", "state", "linkedTransaction", "resolvedOn", "amount", "address", "givenName", "plannedPurgeDate", "bankPaymentType", "valueDate", "version", "paymentFeeAmount", "linkedSpaceId", "environment", "senderBankAccount", "participantNumber", "iban", "postCode", "uniqueId"]

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
        """Create an instance of InvoiceReconciliationRecord from a JSON string"""
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
            "country",
            "city",
            "resolved_by",
            "discarded_by",
            "created_on",
            "payment_fee_currency",
            "payment_reason",
            "reference_number",
            "street",
            "family_name",
            "currency",
            "id",
            "linked_transaction",
            "resolved_on",
            "amount",
            "address",
            "given_name",
            "planned_purge_date",
            "value_date",
            "version",
            "payment_fee_amount",
            "linked_space_id",
            "sender_bank_account",
            "participant_number",
            "iban",
            "post_code",
            "unique_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of last_resolution_failure
        if self.last_resolution_failure:
            _dict['lastResolutionFailure'] = self.last_resolution_failure.to_dict()
        # override the default output from pydantic by calling `to_dict()` of type
        if self.type:
            _dict['type'] = self.type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceReconciliationRecord from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discardedOn": obj.get("discardedOn"),
            "lastResolutionFailure": FailureReason.from_dict(obj["lastResolutionFailure"]) if obj.get("lastResolutionFailure") is not None else None,
            "country": obj.get("country"),
            "rejectionStatus": obj.get("rejectionStatus"),
            "city": obj.get("city"),
            "resolvedBy": obj.get("resolvedBy"),
            "discardedBy": obj.get("discardedBy"),
            "type": InvoiceReconciliationRecordType.from_dict(obj["type"]) if obj.get("type") is not None else None,
            "createdOn": obj.get("createdOn"),
            "paymentFeeCurrency": obj.get("paymentFeeCurrency"),
            "paymentReason": obj.get("paymentReason"),
            "referenceNumber": obj.get("referenceNumber"),
            "street": obj.get("street"),
            "familyName": obj.get("familyName"),
            "currency": obj.get("currency"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "resolvedOn": obj.get("resolvedOn"),
            "amount": obj.get("amount"),
            "address": obj.get("address"),
            "givenName": obj.get("givenName"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "bankPaymentType": obj.get("bankPaymentType"),
            "valueDate": obj.get("valueDate"),
            "version": obj.get("version"),
            "paymentFeeAmount": obj.get("paymentFeeAmount"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "environment": obj.get("environment"),
            "senderBankAccount": obj.get("senderBankAccount"),
            "participantNumber": obj.get("participantNumber"),
            "iban": obj.get("iban"),
            "postCode": obj.get("postCode"),
            "uniqueId": obj.get("uniqueId")
        })
        return _obj


