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
from wallee.models.bank_transaction_flow_direction import BankTransactionFlowDirection
from wallee.models.bank_transaction_state import BankTransactionState
from wallee.models.currency_bank_account import CurrencyBankAccount
from wallee.models.payment_adjustment import PaymentAdjustment
from typing import Optional, Set
from typing_extensions import Self

class BankTransaction(BaseModel):
    """
    BankTransaction
    """ # noqa: E501
    adjustments: Optional[List[PaymentAdjustment]] = Field(default=None, description="Adjustments are changes made to the initial transaction amount, such as fees or corrections.")
    currency_bank_account: Optional[CurrencyBankAccount] = Field(default=None, alias="currencyBankAccount")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    external_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.", alias="externalId")
    posting_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The posting amount refers to the monetary value recorded for the bank transaction prior to any adjustments.", alias="postingAmount")
    source: Optional[StrictInt] = Field(default=None, description="The source indicates how the bank transaction was created.")
    value_date: Optional[datetime] = Field(default=None, description="The value date indicates the date on which the transaction amount becomes effective.", alias="valueDate")
    type: Optional[StrictInt] = Field(default=None, description="The bank transaction's type.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    reference: Optional[StrictStr] = Field(default=None, description="A unique reference to identify the bank transaction.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    value_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value amount represents the net monetary value of the transaction after applicable deductions.", alias="valueAmount")
    flow_direction: Optional[BankTransactionFlowDirection] = Field(default=None, alias="flowDirection")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the bank transaction was created by.", alias="createdBy")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[BankTransactionState] = None
    payment_date: Optional[datetime] = Field(default=None, description="The payment date specifies the date on which the payment was processed.", alias="paymentDate")
    total_adjustment_amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Represents the total value of all adjustments to the bank transaction, including tax.", alias="totalAdjustmentAmountIncludingTax")
    __properties: ClassVar[List[str]] = ["adjustments", "currencyBankAccount", "plannedPurgeDate", "externalId", "postingAmount", "source", "valueDate", "type", "createdOn", "version", "reference", "linkedSpaceId", "valueAmount", "flowDirection", "createdBy", "id", "state", "paymentDate", "totalAdjustmentAmountIncludingTax"]

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
        """Create an instance of BankTransaction from a JSON string"""
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
            "adjustments",
            "planned_purge_date",
            "external_id",
            "posting_amount",
            "source",
            "value_date",
            "type",
            "created_on",
            "version",
            "reference",
            "linked_space_id",
            "value_amount",
            "created_by",
            "id",
            "payment_date",
            "total_adjustment_amount_including_tax",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in adjustments (list)
        _items = []
        if self.adjustments:
            for _item_adjustments in self.adjustments:
                if _item_adjustments:
                    _items.append(_item_adjustments.to_dict())
            _dict['adjustments'] = _items
        # override the default output from pydantic by calling `to_dict()` of currency_bank_account
        if self.currency_bank_account:
            _dict['currencyBankAccount'] = self.currency_bank_account.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of BankTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "adjustments": [PaymentAdjustment.from_dict(_item) for _item in obj["adjustments"]] if obj.get("adjustments") is not None else None,
            "currencyBankAccount": CurrencyBankAccount.from_dict(obj["currencyBankAccount"]) if obj.get("currencyBankAccount") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "externalId": obj.get("externalId"),
            "postingAmount": obj.get("postingAmount"),
            "source": obj.get("source"),
            "valueDate": obj.get("valueDate"),
            "type": obj.get("type"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "reference": obj.get("reference"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "valueAmount": obj.get("valueAmount"),
            "flowDirection": obj.get("flowDirection"),
            "createdBy": obj.get("createdBy"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "paymentDate": obj.get("paymentDate"),
            "totalAdjustmentAmountIncludingTax": obj.get("totalAdjustmentAmountIncludingTax")
        })
        return _obj


