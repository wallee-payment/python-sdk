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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.completion_line_item_create import CompletionLineItemCreate
from typing import Optional, Set
from typing_extensions import Self

class TransactionCompletionDetails(BaseModel):
    """
    TransactionCompletionDetails
    """ # noqa: E501
    line_items: Optional[List[CompletionLineItemCreate]] = Field(default=None, description="The line items to be captured in the transaction completion.", alias="lineItems")
    last_completion: Optional[StrictBool] = Field(default=None, description="Whether this is the final completion for the transaction, meaning no further completions can occur, and the transaction will move to its completed state upon success.", alias="lastCompletion")
    statement_descriptor: Optional[Annotated[str, Field(strict=True, max_length=80)]] = Field(default=None, description="The statement descriptor that appears on a customer's bank statement, providing an explanation for charges or payments, helping customers identify the transaction.", alias="statementDescriptor")
    external_id: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=100)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    invoice_merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the invoice.", alias="invoiceMerchantReference")
    __properties: ClassVar[List[str]] = ["lineItems", "lastCompletion", "statementDescriptor", "externalId", "invoiceMerchantReference"]

    @field_validator('statement_descriptor')
    def statement_descriptor_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[a-zA-Z0-9\s.,_?+\/-]*", value):
            raise ValueError(r"must validate the regular expression /[a-zA-Z0-9\s.,_?+\/-]*/")
        return value

    @field_validator('external_id')
    def external_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

    @field_validator('invoice_merchant_reference')
    def invoice_merchant_reference_validate_regular_expression(cls, value):
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
        """Create an instance of TransactionCompletionDetails from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionCompletionDetails from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineItems": [CompletionLineItemCreate.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "lastCompletion": obj.get("lastCompletion"),
            "statementDescriptor": obj.get("statementDescriptor"),
            "externalId": obj.get("externalId"),
            "invoiceMerchantReference": obj.get("invoiceMerchantReference")
        })
        return _obj


