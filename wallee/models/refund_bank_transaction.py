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
from wallee.models.refund import Refund
from typing import Optional, Set
from typing_extensions import Self

class RefundBankTransaction(BaseModel):
    """
    RefundBankTransaction
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    refund_currency_value_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The value amount represents the net monetary value of the bank transaction, recorded in the refund's currency, after applicable deductions.", alias="refundCurrencyValueAmount")
    refund_currency_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The posting amount represents the monetary value of the bank transaction, recorded in the refund's currency, before applying any adjustments.", alias="refundCurrencyAmount")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    bank_transaction: Optional[BankTransaction] = Field(default=None, alias="bankTransaction")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    refund: Optional[Refund] = None
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "refundCurrencyValueAmount", "refundCurrencyAmount", "language", "id", "spaceViewId", "linkedTransaction", "bankTransaction", "version", "refund"]

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
        """Create an instance of RefundBankTransaction from a JSON string"""
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
            "linked_space_id",
            "refund_currency_value_amount",
            "refund_currency_amount",
            "language",
            "id",
            "space_view_id",
            "linked_transaction",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of bank_transaction
        if self.bank_transaction:
            _dict['bankTransaction'] = self.bank_transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refund
        if self.refund:
            _dict['refund'] = self.refund.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RefundBankTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "refundCurrencyValueAmount": obj.get("refundCurrencyValueAmount"),
            "refundCurrencyAmount": obj.get("refundCurrencyAmount"),
            "language": obj.get("language"),
            "id": obj.get("id"),
            "spaceViewId": obj.get("spaceViewId"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "bankTransaction": BankTransaction.from_dict(obj["bankTransaction"]) if obj.get("bankTransaction") is not None else None,
            "version": obj.get("version"),
            "refund": Refund.from_dict(obj["refund"]) if obj.get("refund") is not None else None
        })
        return _obj


