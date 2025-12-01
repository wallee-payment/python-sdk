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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.bank_transaction import BankTransaction
from wallee.models.transaction import Transaction
from wallee.models.transaction_completion import TransactionCompletion
from typing import Optional, Set
from typing_extensions import Self

class ChargeBankTransaction(BaseModel):
    """
    ChargeBankTransaction
    """ # noqa: E501
    transaction_currency_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The posting amount represents the monetary value of the bank transaction, recorded in the payment transaction's currency, before applying any adjustments.", alias="transactionCurrencyAmount")
    completion: Optional[TransactionCompletion] = None
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    bank_transaction: Optional[BankTransaction] = Field(default=None, alias="bankTransaction")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    transaction: Optional[Transaction] = None
    transaction_currency_value_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value amount represents the net monetary value of the bank transaction, recorded in the payment transaction's currency, after applicable deductions.", alias="transactionCurrencyValueAmount")
    __properties: ClassVar[List[str]] = ["transactionCurrencyAmount", "completion", "linkedSpaceId", "language", "id", "spaceViewId", "linkedTransaction", "bankTransaction", "version", "transaction", "transactionCurrencyValueAmount"]

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
        """Create an instance of ChargeBankTransaction from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "transaction_currency_amount",
            "linked_space_id",
            "language",
            "id",
            "space_view_id",
            "linked_transaction",
            "version",
            "transaction_currency_value_amount",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of completion
        if self.completion:
            _dict['completion'] = self.completion.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bank_transaction
        if self.bank_transaction:
            _dict['bankTransaction'] = self.bank_transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeBankTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionCurrencyAmount": obj.get("transactionCurrencyAmount"),
            "completion": TransactionCompletion.from_dict(obj["completion"]) if obj.get("completion") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "language": obj.get("language"),
            "id": obj.get("id"),
            "spaceViewId": obj.get("spaceViewId"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "bankTransaction": BankTransaction.from_dict(obj["bankTransaction"]) if obj.get("bankTransaction") is not None else None,
            "version": obj.get("version"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None,
            "transactionCurrencyValueAmount": obj.get("transactionCurrencyValueAmount")
        })
        return _obj


