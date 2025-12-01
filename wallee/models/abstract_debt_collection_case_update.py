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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.address_create import AddressCreate
from wallee.models.debt_collection_environment import DebtCollectionEnvironment
from wallee.models.line_item_create import LineItemCreate
from typing import Optional, Set
from typing_extensions import Self

class AbstractDebtCollectionCaseUpdate(BaseModel):
    """
    AbstractDebtCollectionCaseUpdate
    """ # noqa: E501
    line_items: Optional[List[LineItemCreate]] = Field(default=None, description="The line items that are subject of this debt collection case.", alias="lineItems")
    contract_date: Optional[datetime] = Field(default=None, description="The date and time when the contract with the debtor was signed.", alias="contractDate")
    environment: Optional[DebtCollectionEnvironment] = None
    due_date: Optional[datetime] = Field(default=None, description="The date and time when the claim was due.", alias="dueDate")
    currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the case's currency.")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    billing_address: Optional[AddressCreate] = Field(default=None, alias="billingAddress")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    __properties: ClassVar[List[str]] = ["lineItems", "contractDate", "environment", "dueDate", "currency", "language", "billingAddress", "spaceViewId"]

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
        """Create an instance of AbstractDebtCollectionCaseUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AbstractDebtCollectionCaseUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "lineItems": [LineItemCreate.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "contractDate": obj.get("contractDate"),
            "environment": obj.get("environment"),
            "dueDate": obj.get("dueDate"),
            "currency": obj.get("currency"),
            "language": obj.get("language"),
            "billingAddress": AddressCreate.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "spaceViewId": obj.get("spaceViewId")
        })
        return _obj


