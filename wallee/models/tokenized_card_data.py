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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.card_cryptogram import CardCryptogram
from wallee.models.recurring_indicator import RecurringIndicator
from typing import Optional, Set
from typing_extensions import Self

class TokenizedCardData(BaseModel):
    """
    TokenizedCardData
    """ # noqa: E501
    initial_recurring_transaction: Optional[StrictBool] = Field(default=None, description="Whether the transaction is an initial recurring transaction, based on the recurring indicator. This is used to identify the first transaction in a recurring payment setup.", alias="initialRecurringTransaction")
    recurring_indicator: Optional[RecurringIndicator] = Field(default=None, alias="recurringIndicator")
    token_requestor_id: Optional[StrictStr] = Field(default=None, description="The token requestor identifier (TRID) identifies the entity requesting tokenization for a card transaction.", alias="tokenRequestorId")
    cryptogram: Optional[CardCryptogram] = None
    __properties: ClassVar[List[str]] = ["initialRecurringTransaction", "recurringIndicator", "tokenRequestorId", "cryptogram"]

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
        """Create an instance of TokenizedCardData from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "initial_recurring_transaction",
            "token_requestor_id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of cryptogram
        if self.cryptogram:
            _dict['cryptogram'] = self.cryptogram.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TokenizedCardData from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "initialRecurringTransaction": obj.get("initialRecurringTransaction"),
            "recurringIndicator": obj.get("recurringIndicator"),
            "tokenRequestorId": obj.get("tokenRequestorId"),
            "cryptogram": CardCryptogram.from_dict(obj["cryptogram"]) if obj.get("cryptogram") is not None else None
        })
        return _obj


