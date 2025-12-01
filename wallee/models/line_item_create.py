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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.line_item_attribute_create import LineItemAttributeCreate
from wallee.models.line_item_type import LineItemType
from wallee.models.tax_create import TaxCreate
from typing import Optional, Set
from typing_extensions import Self

class LineItemCreate(BaseModel):
    """
    LineItemCreate
    """ # noqa: E501
    shipping_required: Optional[StrictBool] = Field(default=None, description="Whether the item required shipping.", alias="shippingRequired")
    quantity: Union[StrictFloat, StrictInt] = Field(description="The number of items that were purchased.")
    name: Annotated[str, Field(min_length=1, strict=True, max_length=150)] = Field(description="The name of the product, ideally in the customer's language.")
    taxes: Optional[List[TaxCreate]] = Field(default=None, description="A set of tax lines, each of which specifies a tax applied to the item.")
    attributes: Optional[Dict[str, LineItemAttributeCreate]] = Field(default=None, description="A map of custom information for the item.")
    amount_including_tax: Union[StrictFloat, StrictInt] = Field(description="The line item price with discounts applied, including taxes.", alias="amountIncludingTax")
    discount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The discount allocated to the item, including taxes.", alias="discountIncludingTax")
    sku: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The SKU (stock-keeping unit) of the product.")
    type: LineItemType
    unique_id: Annotated[str, Field(strict=True, max_length=200)] = Field(description="The unique identifier of the line item within the set of line items.", alias="uniqueId")
    __properties: ClassVar[List[str]] = ["shippingRequired", "quantity", "name", "taxes", "attributes", "amountIncludingTax", "discountIncludingTax", "sku", "type", "uniqueId"]

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
        """Create an instance of LineItemCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in taxes (list)
        _items = []
        if self.taxes:
            for _item_taxes in self.taxes:
                if _item_taxes:
                    _items.append(_item_taxes.to_dict())
            _dict['taxes'] = _items
        # override the default output from pydantic by calling `to_dict()` of each value in attributes (dict)
        _field_dict = {}
        if self.attributes:
            for _key_attributes in self.attributes:
                if self.attributes[_key_attributes]:
                    _field_dict[_key_attributes] = self.attributes[_key_attributes].to_dict()
            _dict['attributes'] = _field_dict
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LineItemCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "shippingRequired": obj.get("shippingRequired"),
            "quantity": obj.get("quantity"),
            "name": obj.get("name"),
            "taxes": [TaxCreate.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "attributes": dict(
                (_k, LineItemAttributeCreate.from_dict(_v))
                for _k, _v in obj["attributes"].items()
            )
            if obj.get("attributes") is not None
            else None,
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "discountIncludingTax": obj.get("discountIncludingTax"),
            "sku": obj.get("sku"),
            "type": obj.get("type"),
            "uniqueId": obj.get("uniqueId")
        })
        return _obj


