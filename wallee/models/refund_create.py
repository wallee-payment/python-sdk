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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.line_item_reduction_create import LineItemReductionCreate
from wallee.models.refund_type import RefundType
from typing import Optional, Set
from typing_extensions import Self

class RefundCreate(BaseModel):
    """
    A refund is a credit issued to the customer, which can be initiated either by the merchant or by the customer as a reversal.
    """ # noqa: E501
    completion: Optional[StrictInt] = Field(default=None, description="The transaction completion that the refund belongs to.")
    amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total monetary amount of the refund, representing the exact credit issued to the customer.")
    reductions: Optional[List[LineItemReductionCreate]] = Field(default=None, description="The reductions applied on the original transaction items, detailing specific adjustments associated with the refund.")
    external_id: Annotated[str, Field(min_length=1, strict=True, max_length=100)] = Field(description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    type: RefundType
    merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the refund.", alias="merchantReference")
    transaction: Optional[StrictInt] = Field(default=None, description="The transaction that the refund belongs to.")
    __properties: ClassVar[List[str]] = ["completion", "amount", "reductions", "externalId", "type", "merchantReference", "transaction"]

    @field_validator('external_id')
    def external_id_validate_regular_expression(cls, value):
        """Validates the regular expression"""
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
        """Create an instance of RefundCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in reductions (list)
        _items = []
        if self.reductions:
            for _item_reductions in self.reductions:
                if _item_reductions:
                    _items.append(_item_reductions.to_dict())
            _dict['reductions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RefundCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion": obj.get("completion"),
            "amount": obj.get("amount"),
            "reductions": [LineItemReductionCreate.from_dict(_item) for _item in obj["reductions"]] if obj.get("reductions") is not None else None,
            "externalId": obj.get("externalId"),
            "type": obj.get("type"),
            "merchantReference": obj.get("merchantReference"),
            "transaction": obj.get("transaction")
        })
        return _obj


