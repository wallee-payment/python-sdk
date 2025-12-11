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
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalTransactionSum(BaseModel):
    """
    Represents the aggregated transaction data for a specific brand and currency, including regular and DCC (Dynamic Currency Conversion) transactions.
    """ # noqa: E501
    transaction_tip_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of tips from regular (non-DCC) transactions in the transaction currency.", alias="transactionTipAmount")
    product: Optional[StrictStr] = Field(default=None, description="The product within the brand for which transactions are summarized.")
    transaction_currency: Optional[StrictStr] = Field(default=None, description="The base currency in which the transactions were processed and settled, excluding any DCC conversions.", alias="transactionCurrency")
    transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total monetary value of all transactions in the transaction currency, excluding DCC transactions.", alias="transactionAmount")
    dcc_tip_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount of tips from DCC transactions, converted and presented in the transaction currency.", alias="dccTipAmount")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    transaction_count: Optional[StrictInt] = Field(default=None, description="The total count of regular (non-DCC) transactions processed within this summary period.", alias="transactionCount")
    brand: Optional[StrictStr] = Field(default=None, description="The payment brand for which the transactions are summarized.")
    dcc_transaction_count: Optional[StrictInt] = Field(default=None, description="The number of transactions where Dynamic Currency Conversion (DCC) was applied, allowing customers to pay in their home currency.", alias="dccTransactionCount")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    dcc_transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total monetary value of DCC transactions, converted and presented in the transaction currency.", alias="dccTransactionAmount")
    __properties: ClassVar[List[str]] = ["transactionTipAmount", "product", "transactionCurrency", "transactionAmount", "dccTipAmount", "id", "transactionCount", "brand", "dccTransactionCount", "version", "dccTransactionAmount"]

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
        """Create an instance of PaymentTerminalTransactionSum from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "transaction_tip_amount",
            "product",
            "transaction_currency",
            "transaction_amount",
            "dcc_tip_amount",
            "id",
            "transaction_count",
            "brand",
            "dcc_transaction_count",
            "version",
            "dcc_transaction_amount",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalTransactionSum from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionTipAmount": obj.get("transactionTipAmount"),
            "product": obj.get("product"),
            "transactionCurrency": obj.get("transactionCurrency"),
            "transactionAmount": obj.get("transactionAmount"),
            "dccTipAmount": obj.get("dccTipAmount"),
            "id": obj.get("id"),
            "transactionCount": obj.get("transactionCount"),
            "brand": obj.get("brand"),
            "dccTransactionCount": obj.get("dccTransactionCount"),
            "version": obj.get("version"),
            "dccTransactionAmount": obj.get("dccTransactionAmount")
        })
        return _obj


