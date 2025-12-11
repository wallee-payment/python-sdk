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
from wallee.models.payment_terminal_dcc_transaction_sum import PaymentTerminalDccTransactionSum
from wallee.models.payment_terminal_transaction_sum import PaymentTerminalTransactionSum
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalTransactionSummary(BaseModel):
    """
    PaymentTerminalTransactionSummary
    """ # noqa: E501
    reference: Optional[StrictInt] = Field(default=None, description="The unique reference assigned to this transaction summary.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    transaction_sums: Optional[List[PaymentTerminalTransactionSum]] = Field(default=None, description="The total monetary amounts of all transactions, organized and grouped by brand and currency.", alias="transactionSums")
    dcc_transaction_sums: Optional[List[PaymentTerminalDccTransactionSum]] = Field(default=None, description="Detailed breakdown of Dynamic Currency Conversion (DCC) transactions, showing transaction amounts in both original and converted currencies, grouped by payment brand.", alias="dccTransactionSums")
    ended_on: Optional[datetime] = Field(default=None, description="The end of the time period covered by this summary report.", alias="endedOn")
    balance_amount_per_currency: Optional[Dict[str, Union[StrictFloat, StrictInt]]] = Field(default=None, description="The overall transaction volume in each processed currency.", alias="balanceAmountPerCurrency")
    payment_terminal: Optional[StrictInt] = Field(default=None, description="The payment terminal that processed the transactions included in this summary report.", alias="paymentTerminal")
    receipt: Optional[StrictStr] = Field(default=None, description="The HTML content of the transaction summary receipt.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    number_of_transactions: Optional[StrictInt] = Field(default=None, description="The total count of all transactions processed by the terminal during the summary period.", alias="numberOfTransactions")
    started_on: Optional[datetime] = Field(default=None, description="The beginning of the time period covered by this summary report.", alias="startedOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["reference", "linkedSpaceId", "transactionSums", "dccTransactionSums", "endedOn", "balanceAmountPerCurrency", "paymentTerminal", "receipt", "id", "numberOfTransactions", "startedOn", "version"]

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
        """Create an instance of PaymentTerminalTransactionSummary from a JSON string"""
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
            "reference",
            "linked_space_id",
            "transaction_sums",
            "dcc_transaction_sums",
            "ended_on",
            "balance_amount_per_currency",
            "payment_terminal",
            "receipt",
            "id",
            "number_of_transactions",
            "started_on",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in transaction_sums (list)
        _items = []
        if self.transaction_sums:
            for _item_transaction_sums in self.transaction_sums:
                if _item_transaction_sums:
                    _items.append(_item_transaction_sums.to_dict())
            _dict['transactionSums'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in dcc_transaction_sums (list)
        _items = []
        if self.dcc_transaction_sums:
            for _item_dcc_transaction_sums in self.dcc_transaction_sums:
                if _item_dcc_transaction_sums:
                    _items.append(_item_dcc_transaction_sums.to_dict())
            _dict['dccTransactionSums'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalTransactionSummary from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "transactionSums": [PaymentTerminalTransactionSum.from_dict(_item) for _item in obj["transactionSums"]] if obj.get("transactionSums") is not None else None,
            "dccTransactionSums": [PaymentTerminalDccTransactionSum.from_dict(_item) for _item in obj["dccTransactionSums"]] if obj.get("dccTransactionSums") is not None else None,
            "endedOn": obj.get("endedOn"),
            "balanceAmountPerCurrency": obj.get("balanceAmountPerCurrency"),
            "paymentTerminal": obj.get("paymentTerminal"),
            "receipt": obj.get("receipt"),
            "id": obj.get("id"),
            "numberOfTransactions": obj.get("numberOfTransactions"),
            "startedOn": obj.get("startedOn"),
            "version": obj.get("version")
        })
        return _obj


