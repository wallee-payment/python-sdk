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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.environment import Environment
from wallee.models.failure_reason import FailureReason
from wallee.models.label import Label
from wallee.models.line_item import LineItem
from wallee.models.line_item_reduction import LineItemReduction
from wallee.models.refund_state import RefundState
from wallee.models.refund_type import RefundType
from wallee.models.tax import Tax
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class Refund(BaseModel):
    """
    A refund is a credit issued to the customer, which can be initiated either by the merchant or by the customer as a reversal.
    """ # noqa: E501
    total_settled_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount settled for the refund, factoring in reductions, taxes, and any additional applied fees.", alias="totalSettledAmount")
    reductions: Optional[List[LineItemReduction]] = Field(default=None, description="The reductions applied on the original transaction items, detailing specific adjustments associated with the refund.")
    base_line_items: Optional[List[LineItem]] = Field(default=None, description="The original base line items from the transaction prior to the refund, serving as a reference for the refunded amounts.", alias="baseLineItems")
    processing_on: Optional[datetime] = Field(default=None, description="The date and time when the processing of the refund was started.", alias="processingOn")
    taxes: Optional[List[Tax]] = Field(default=None, description="The tax breakdown applied to the refund amount, helping with tax calculations or reporting.")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    type: Optional[RefundType] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The line items included in the refund, representing the reductions.", alias="lineItems")
    succeeded_on: Optional[datetime] = Field(default=None, description="The date and time when the refund succeeded.", alias="succeededOn")
    reduced_line_items: Optional[List[LineItem]] = Field(default=None, description="The line items from the original transaction, adjusted to reflect any reductions applied during the refund process.", alias="reducedLineItems")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[RefundState] = None
    merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the refund.", alias="merchantReference")
    completion: Optional[StrictInt] = Field(default=None, description="The transaction completion that the refund belongs to.")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total monetary amount of the refund, representing the exact credit issued to the customer.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that this object is associated with.", alias="timeZone")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the object will expire.", alias="timeoutOn")
    environment: Optional[Environment] = None
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the refund was created by.", alias="createdBy")
    next_update_on: Optional[datetime] = Field(default=None, description="The date and time when the next update of the object's state is planned.", alias="nextUpdateOn")
    updated_invoice: Optional[StrictInt] = Field(default=None, description="An updated invoice reflecting adjustments made by the refund.", alias="updatedInvoice")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    total_applied_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sum of fees applied to the refund transaction, such as processing or service charges.", alias="totalAppliedFees")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the refund failed.", alias="failedOn")
    transaction: Optional[Transaction] = None
    processor_reference: Optional[Annotated[str, Field(strict=True, max_length=150)]] = Field(default=None, description="The reference ID provided by the payment processor, used to trace the refund through the external payment system.", alias="processorReference")
    __properties: ClassVar[List[str]] = ["totalSettledAmount", "reductions", "baseLineItems", "processingOn", "taxes", "language", "type", "createdOn", "lineItems", "succeededOn", "reducedLineItems", "id", "state", "merchantReference", "completion", "amount", "plannedPurgeDate", "externalId", "timeZone", "version", "labels", "linkedSpaceId", "timeoutOn", "environment", "createdBy", "nextUpdateOn", "updatedInvoice", "failureReason", "totalAppliedFees", "failedOn", "transaction", "processorReference"]

    @field_validator('merchant_reference')
    def merchant_reference_validate_regular_expression(cls, value):
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
        """Create an instance of Refund from a JSON string"""
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
            "total_settled_amount",
            "reductions",
            "base_line_items",
            "processing_on",
            "taxes",
            "language",
            "created_on",
            "line_items",
            "succeeded_on",
            "reduced_line_items",
            "id",
            "merchant_reference",
            "completion",
            "amount",
            "planned_purge_date",
            "external_id",
            "time_zone",
            "version",
            "labels",
            "linked_space_id",
            "timeout_on",
            "created_by",
            "next_update_on",
            "updated_invoice",
            "total_applied_fees",
            "failed_on",
            "processor_reference",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in reductions (list)
        _items = []
        if self.reductions:
            for _item_reductions in self.reductions:
                if _item_reductions:
                    _items.append(_item_reductions.to_dict())
            _dict['reductions'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in base_line_items (list)
        _items = []
        if self.base_line_items:
            for _item_base_line_items in self.base_line_items:
                if _item_base_line_items:
                    _items.append(_item_base_line_items.to_dict())
            _dict['baseLineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in taxes (list)
        _items = []
        if self.taxes:
            for _item_taxes in self.taxes:
                if _item_taxes:
                    _items.append(_item_taxes.to_dict())
            _dict['taxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in reduced_line_items (list)
        _items = []
        if self.reduced_line_items:
            for _item_reduced_line_items in self.reduced_line_items:
                if _item_reduced_line_items:
                    _items.append(_item_reduced_line_items.to_dict())
            _dict['reducedLineItems'] = _items
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
        """Create an instance of Refund from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "totalSettledAmount": obj.get("totalSettledAmount"),
            "reductions": [LineItemReduction.from_dict(_item) for _item in obj["reductions"]] if obj.get("reductions") is not None else None,
            "baseLineItems": [LineItem.from_dict(_item) for _item in obj["baseLineItems"]] if obj.get("baseLineItems") is not None else None,
            "processingOn": obj.get("processingOn"),
            "taxes": [Tax.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "language": obj.get("language"),
            "type": obj.get("type"),
            "createdOn": obj.get("createdOn"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "succeededOn": obj.get("succeededOn"),
            "reducedLineItems": [LineItem.from_dict(_item) for _item in obj["reducedLineItems"]] if obj.get("reducedLineItems") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "merchantReference": obj.get("merchantReference"),
            "completion": obj.get("completion"),
            "amount": obj.get("amount"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "timeZone": obj.get("timeZone"),
            "version": obj.get("version"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "environment": obj.get("environment"),
            "createdBy": obj.get("createdBy"),
            "nextUpdateOn": obj.get("nextUpdateOn"),
            "updatedInvoice": obj.get("updatedInvoice"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "totalAppliedFees": obj.get("totalAppliedFees"),
            "failedOn": obj.get("failedOn"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "processorReference": obj.get("processorReference")
        })
        return _obj


