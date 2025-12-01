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
from wallee.models.address import Address
from wallee.models.debt_collection_case_source import DebtCollectionCaseSource
from wallee.models.debt_collection_case_state import DebtCollectionCaseState
from wallee.models.debt_collection_environment import DebtCollectionEnvironment
from wallee.models.debt_collector_configuration import DebtCollectorConfiguration
from wallee.models.failure_reason import FailureReason
from wallee.models.label import Label
from wallee.models.line_item import LineItem
from typing import Optional, Set
from typing_extensions import Self

class DebtCollectionCase(BaseModel):
    """
    The debt collection case represents a try to collect the money from the debtor.
    """ # noqa: E501
    contract_date: Optional[datetime] = Field(default=None, description="The date and time when the contract with the debtor was signed.", alias="contractDate")
    due_date: Optional[datetime] = Field(default=None, description="The date and time when the claim was due.", alias="dueDate")
    closed_on: Optional[datetime] = Field(default=None, description="The date and time when the case was closed.", alias="closedOn")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    source: Optional[DebtCollectionCaseSource] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The line items that are subject of this debt collection case.", alias="lineItems")
    reference: Optional[StrictStr] = Field(default=None, description="A unique reference to identify the debt collection case in communication with the debtor.")
    currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the case's currency.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[DebtCollectionCaseState] = None
    processing_timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the processing of the case times out.", alias="processingTimeoutOn")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sum of all unpaid item prices in the case's currency. The amount can no longer be changed once the case has been reviewed.")
    creator: Optional[StrictInt] = Field(default=None, description="The ID of the user the case was created by.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    collector_configuration: Optional[DebtCollectorConfiguration] = Field(default=None, alias="collectorConfiguration")
    reviewer: Optional[StrictInt] = Field(default=None, description="The ID of the user the case was reviewed by.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    review_started_on: Optional[datetime] = Field(default=None, description="The date and time when the review of the case was started.", alias="reviewStartedOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    processing_started_on: Optional[datetime] = Field(default=None, description="The date and time when the processing of the case was started.", alias="processingStartedOn")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    environment: Optional[DebtCollectionEnvironment] = None
    reviewed_on: Optional[datetime] = Field(default=None, description="The date and time when the case was reviewed.", alias="reviewedOn")
    source_entity_id: Optional[StrictInt] = Field(default=None, description="The ID of the object that is the source of the case. Only defined if the case was created by an internal process.", alias="sourceEntityId")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the case failed.", alias="failedOn")
    next_attempt_on: Optional[datetime] = Field(default=None, description="The date and time when the next attempt at processing the case will be made.", alias="nextAttemptOn")
    __properties: ClassVar[List[str]] = ["contractDate", "dueDate", "closedOn", "language", "source", "createdOn", "lineItems", "reference", "currency", "id", "state", "processingTimeoutOn", "amount", "creator", "plannedPurgeDate", "externalId", "collectorConfiguration", "reviewer", "spaceViewId", "reviewStartedOn", "version", "labels", "processingStartedOn", "linkedSpaceId", "environment", "reviewedOn", "sourceEntityId", "failureReason", "billingAddress", "failedOn", "nextAttemptOn"]

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
        """Create an instance of DebtCollectionCase from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "contract_date",
            "due_date",
            "closed_on",
            "language",
            "created_on",
            "line_items",
            "reference",
            "currency",
            "id",
            "processing_timeout_on",
            "amount",
            "creator",
            "planned_purge_date",
            "external_id",
            "reviewer",
            "space_view_id",
            "review_started_on",
            "version",
            "labels",
            "processing_started_on",
            "linked_space_id",
            "reviewed_on",
            "source_entity_id",
            "failed_on",
            "next_attempt_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of source
        if self.source:
            _dict['source'] = self.source.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of collector_configuration
        if self.collector_configuration:
            _dict['collectorConfiguration'] = self.collector_configuration.to_dict()
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DebtCollectionCase from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "contractDate": obj.get("contractDate"),
            "dueDate": obj.get("dueDate"),
            "closedOn": obj.get("closedOn"),
            "language": obj.get("language"),
            "source": DebtCollectionCaseSource.from_dict(obj["source"]) if obj.get("source") is not None else None,
            "createdOn": obj.get("createdOn"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "reference": obj.get("reference"),
            "currency": obj.get("currency"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "processingTimeoutOn": obj.get("processingTimeoutOn"),
            "amount": obj.get("amount"),
            "creator": obj.get("creator"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "collectorConfiguration": DebtCollectorConfiguration.from_dict(obj["collectorConfiguration"]) if obj.get("collectorConfiguration") is not None else None,
            "reviewer": obj.get("reviewer"),
            "spaceViewId": obj.get("spaceViewId"),
            "reviewStartedOn": obj.get("reviewStartedOn"),
            "version": obj.get("version"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "processingStartedOn": obj.get("processingStartedOn"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "environment": obj.get("environment"),
            "reviewedOn": obj.get("reviewedOn"),
            "sourceEntityId": obj.get("sourceEntityId"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "failedOn": obj.get("failedOn"),
            "nextAttemptOn": obj.get("nextAttemptOn")
        })
        return _obj


