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

class PaymentTerminalDccTransactionSum(BaseModel):
    """
    Represents the aggregated summary of Dynamic Currency Conversion (DCC) transactions grouped by brand and currency combinations in a transaction summary receipt.
    """ # noqa: E501
    transaction_currency: Optional[StrictStr] = Field(default=None, description="The original currency of the transactions before DCC conversion (typically the merchant's local currency).", alias="transactionCurrency")
    transaction_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total sum of all transactions in the original transaction currency (the amount in merchant's local currency before DCC conversion).", alias="transactionAmount")
    dcc_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total sum of all transactions in the converted DCC currency (the amount paid by customers in their chosen currency).", alias="dccAmount")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    transaction_count: Optional[StrictInt] = Field(default=None, description="The total count of DCC transactions processed for this specific brand and currency combination.", alias="transactionCount")
    dcc_currency: Optional[StrictStr] = Field(default=None, description="The converted currency used in DCC transactions (the currency chosen by the customer for payment).", alias="dccCurrency")
    brand: Optional[StrictStr] = Field(default=None, description="The payment brand for which these DCC transactions are summarized.")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["transactionCurrency", "transactionAmount", "dccAmount", "id", "transactionCount", "dccCurrency", "brand", "version"]

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
        """Create an instance of PaymentTerminalDccTransactionSum from a JSON string"""
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
            "transaction_currency",
            "transaction_amount",
            "dcc_amount",
            "id",
            "transaction_count",
            "dcc_currency",
            "brand",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentTerminalDccTransactionSum from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "transactionCurrency": obj.get("transactionCurrency"),
            "transactionAmount": obj.get("transactionAmount"),
            "dccAmount": obj.get("dccAmount"),
            "id": obj.get("id"),
            "transactionCount": obj.get("transactionCount"),
            "dccCurrency": obj.get("dccCurrency"),
            "brand": obj.get("brand"),
            "version": obj.get("version")
        })
        return _obj


