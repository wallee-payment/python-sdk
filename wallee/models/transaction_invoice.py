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
from wallee.models.address import Address
from wallee.models.environment import Environment
from wallee.models.line_item import LineItem
from wallee.models.transaction_completion import TransactionCompletion
from wallee.models.transaction_invoice_state import TransactionInvoiceState
from typing import Optional, Set
from typing_extensions import Self

class TransactionInvoice(BaseModel):
    """
    TransactionInvoice
    """ # noqa: E501
    completion: Optional[TransactionCompletion] = None
    derecognized_on: Optional[datetime] = Field(default=None, description="The date and time when the invoice was derecognized, meaning it is no longer considered outstanding or valid in the system.", alias="derecognizedOn")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total sum of all line items on the invoice, including taxes.")
    due_on: Optional[datetime] = Field(default=None, description="The due date for payment of the invoice.", alias="dueOn")
    outstanding_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The remaining amount the buyer owes to the merchant. A negative value indicates the invoice has been overpaid.", alias="outstandingAmount")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that this object is associated with.", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    paid_on: Optional[datetime] = Field(default=None, description="The date and time when the invoice was recorded as paid. May differ from the actual payment date due to processing delays.", alias="paidOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The invoiced line items that will appear on the invoice document.", alias="lineItems")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    environment: Optional[Environment] = None
    derecognized_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the invoice was derecognized by.", alias="derecognizedBy")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[TransactionInvoiceState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The portion of the invoiced amount that corresponds to taxes.", alias="taxAmount")
    merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the invoice.", alias="merchantReference")
    __properties: ClassVar[List[str]] = ["completion", "derecognizedOn", "amount", "dueOn", "outstandingAmount", "plannedPurgeDate", "externalId", "timeZone", "language", "spaceViewId", "createdOn", "paidOn", "version", "lineItems", "linkedSpaceId", "environment", "derecognizedBy", "billingAddress", "id", "state", "linkedTransaction", "taxAmount", "merchantReference"]

    @field_validator('external_id')
    def external_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

    @field_validator('merchant_reference')
    def merchant_reference_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionInvoice from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "derecognized_on",
            "amount",
            "due_on",
            "outstanding_amount",
            "planned_purge_date",
            "external_id",
            "time_zone",
            "language",
            "space_view_id",
            "created_on",
            "paid_on",
            "version",
            "line_items",
            "linked_space_id",
            "derecognized_by",
            "id",
            "linked_transaction",
            "tax_amount",
            "merchant_reference",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of completion
        if self.completion:
            _dict['completion'] = self.completion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionInvoice from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion": TransactionCompletion.from_dict(obj["completion"]) if obj.get("completion") is not None else None,
            "derecognizedOn": obj.get("derecognizedOn"),
            "amount": obj.get("amount"),
            "dueOn": obj.get("dueOn"),
            "outstandingAmount": obj.get("outstandingAmount"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "spaceViewId": obj.get("spaceViewId"),
            "createdOn": obj.get("createdOn"),
            "paidOn": obj.get("paidOn"),
            "version": obj.get("version"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "environment": obj.get("environment"),
            "derecognizedBy": obj.get("derecognizedBy"),
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "taxAmount": obj.get("taxAmount"),
            "merchantReference": obj.get("merchantReference")
        })
        return _obj


