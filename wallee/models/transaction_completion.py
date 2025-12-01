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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.failure_reason import FailureReason
from wallee.models.label import Label
from wallee.models.line_item import LineItem
from wallee.models.transaction_completion_mode import TransactionCompletionMode
from wallee.models.transaction_completion_state import TransactionCompletionState
from wallee.models.transaction_line_item_version import TransactionLineItemVersion
from typing import Optional, Set
from typing_extensions import Self

class TransactionCompletion(BaseModel):
    """
    TransactionCompletion
    """ # noqa: E501
    line_item_version: Optional[TransactionLineItemVersion] = Field(default=None, alias="lineItemVersion")
    statement_descriptor: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="The statement descriptor that appears on a customer's bank statement, providing an explanation for charges or payments, helping customers identify the transaction.", alias="statementDescriptor")
    base_line_items: Optional[List[LineItem]] = Field(default=None, description="The original line items from the transaction that serve as the baseline for this completion.", alias="baseLineItems")
    processing_on: Optional[datetime] = Field(default=None, description="The date and time when the processing of the transaction completion was started.", alias="processingOn")
    invoice_merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the invoice.", alias="invoiceMerchantReference")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    remaining_line_items: Optional[List[LineItem]] = Field(default=None, description="The line items yet to be captured in the transaction.", alias="remainingLineItems")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The line items captured in this transaction completion.", alias="lineItems")
    mode: Optional[TransactionCompletionMode] = None
    succeeded_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction completion succeeded.", alias="succeededOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[TransactionCompletionState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    payment_information: Optional[StrictStr] = Field(default=None, description="Payment-specific details related to this transaction completion such as payment instructions or references needed for processing.", alias="paymentInformation")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount to be captured in this completion, including taxes.")
    last_completion: Optional[StrictBool] = Field(default=None, description="Whether this is the final completion for the transaction. After the last completion is successfully created, the transaction enters its final state, and no further completions can occur.", alias="lastCompletion")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that this object is associated with.", alias="timeZone")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the object will expire.", alias="timeoutOn")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the transaction completion was created by.", alias="createdBy")
    next_update_on: Optional[datetime] = Field(default=None, description="The date and time when the next update of the object's state is planned.", alias="nextUpdateOn")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The portion of the captured amount that corresponds to taxes.", alias="taxAmount")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction completion failed.", alias="failedOn")
    processor_reference: Optional[StrictStr] = Field(default=None, description="The reference ID provided by the payment processor, used to trace the completion through the external payment system.", alias="processorReference")
    __properties: ClassVar[List[str]] = ["lineItemVersion", "statementDescriptor", "baseLineItems", "processingOn", "invoiceMerchantReference", "language", "remainingLineItems", "createdOn", "lineItems", "mode", "succeededOn", "id", "state", "linkedTransaction", "paymentInformation", "amount", "lastCompletion", "plannedPurgeDate", "externalId", "timeZone", "spaceViewId", "version", "labels", "linkedSpaceId", "timeoutOn", "createdBy", "nextUpdateOn", "failureReason", "taxAmount", "failedOn", "processorReference"]

    @field_validator('statement_descriptor')
    def statement_descriptor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9\s.,_?+\/-]*", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9\s.,_?+\/-]*/")
        return value

    @field_validator('invoice_merchant_reference')
    def invoice_merchant_reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

    @field_validator('external_id')
    def external_id_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionCompletion from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "statement_descriptor",
            "base_line_items",
            "processing_on",
            "invoice_merchant_reference",
            "language",
            "remaining_line_items",
            "created_on",
            "line_items",
            "succeeded_on",
            "id",
            "linked_transaction",
            "payment_information",
            "amount",
            "last_completion",
            "planned_purge_date",
            "external_id",
            "time_zone",
            "space_view_id",
            "version",
            "labels",
            "linked_space_id",
            "timeout_on",
            "created_by",
            "next_update_on",
            "tax_amount",
            "failed_on",
            "processor_reference",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of line_item_version
        if self.line_item_version:
            _dict['lineItemVersion'] = self.line_item_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in base_line_items (list)
        _items = []
        if self.base_line_items:
            for _item_base_line_items in self.base_line_items:
                if _item_base_line_items:
                    _items.append(_item_base_line_items.to_dict())
            _dict['baseLineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in remaining_line_items (list)
        _items = []
        if self.remaining_line_items:
            for _item_remaining_line_items in self.remaining_line_items:
                if _item_remaining_line_items:
                    _items.append(_item_remaining_line_items.to_dict())
            _dict['remainingLineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionCompletion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineItemVersion": TransactionLineItemVersion.from_dict(obj["lineItemVersion"]) if obj.get("lineItemVersion") is not None else None,
            "statementDescriptor": obj.get("statementDescriptor"),
            "baseLineItems": [LineItem.from_dict(_item) for _item in obj["baseLineItems"]] if obj.get("baseLineItems") is not None else None,
            "processingOn": obj.get("processingOn"),
            "invoiceMerchantReference": obj.get("invoiceMerchantReference"),
            "language": obj.get("language"),
            "remainingLineItems": [LineItem.from_dict(_item) for _item in obj["remainingLineItems"]] if obj.get("remainingLineItems") is not None else None,
            "createdOn": obj.get("createdOn"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "mode": obj.get("mode"),
            "succeededOn": obj.get("succeededOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "paymentInformation": obj.get("paymentInformation"),
            "amount": obj.get("amount"),
            "lastCompletion": obj.get("lastCompletion"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "timeZone": obj.get("timeZone"),
            "spaceViewId": obj.get("spaceViewId"),
            "version": obj.get("version"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "createdBy": obj.get("createdBy"),
            "nextUpdateOn": obj.get("nextUpdateOn"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "taxAmount": obj.get("taxAmount"),
            "failedOn": obj.get("failedOn"),
            "processorReference": obj.get("processorReference")
        })
        return _obj


