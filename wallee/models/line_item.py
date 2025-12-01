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
from wallee.models.line_item_attribute import LineItemAttribute
from wallee.models.line_item_type import LineItemType
from wallee.models.tax import Tax
from typing import Optional, Set
from typing_extensions import Self

class LineItem(BaseModel):
    """
    LineItem
    """ # noqa: E501
    tax_amount_per_unit: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated tax amount per unit.", alias="taxAmountPerUnit")
    undiscounted_amount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The line item price with discounts not applied, excluding taxes.", alias="undiscountedAmountExcludingTax")
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of items that were purchased.")
    undiscounted_unit_price_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated price per unit with discounts not applied, including taxes.", alias="undiscountedUnitPriceIncludingTax")
    amount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The line item price with discounts applied, excluding taxes.", alias="amountExcludingTax")
    undiscounted_amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The line item price with discounts not applied, including taxes.", alias="undiscountedAmountIncludingTax")
    taxes: Optional[List[Tax]] = Field(default=None, description="A set of tax lines, each of which specifies a tax applied to the item.")
    type: Optional[LineItemType] = None
    unit_price_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated price per unit with discounts applied, including taxes.", alias="unitPriceIncludingTax")
    discount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The discount allocated to the item, excluding taxes.", alias="discountExcludingTax")
    shipping_required: Optional[StrictBool] = Field(default=None, description="Whether the item required shipping.", alias="shippingRequired")
    unit_price_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated price per unit with discounts applied, excluding taxes.", alias="unitPriceExcludingTax")
    name: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=150)]] = Field(default=None, description="The name of the product, ideally in the customer's language.")
    attributes: Optional[Dict[str, LineItemAttribute]] = Field(default=None, description="A map of custom information for the item.")
    undiscounted_unit_price_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The calculated price per unit with discounts not applied, excluding taxes.", alias="undiscountedUnitPriceExcludingTax")
    amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The line item price with discounts applied, including taxes.", alias="amountIncludingTax")
    discount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The discount allocated to the item, including taxes.", alias="discountIncludingTax")
    sku: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The SKU (stock-keeping unit) of the product.")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sum of all taxes applied to the item.", alias="taxAmount")
    aggregated_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total tax rate applied to the item, calculated from the rates of all tax lines.", alias="aggregatedTaxRate")
    unique_id: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The unique identifier of the line item within the set of line items.", alias="uniqueId")
    __properties: ClassVar[List[str]] = ["taxAmountPerUnit", "undiscountedAmountExcludingTax", "quantity", "undiscountedUnitPriceIncludingTax", "amountExcludingTax", "undiscountedAmountIncludingTax", "taxes", "type", "unitPriceIncludingTax", "discountExcludingTax", "shippingRequired", "unitPriceExcludingTax", "name", "attributes", "undiscountedUnitPriceExcludingTax", "amountIncludingTax", "discountIncludingTax", "sku", "taxAmount", "aggregatedTaxRate", "uniqueId"]

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
        """Create an instance of LineItem from a JSON string"""
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
            "tax_amount_per_unit",
            "undiscounted_amount_excluding_tax",
            "quantity",
            "undiscounted_unit_price_including_tax",
            "amount_excluding_tax",
            "undiscounted_amount_including_tax",
            "taxes",
            "unit_price_including_tax",
            "discount_excluding_tax",
            "shipping_required",
            "unit_price_excluding_tax",
            "name",
            "attributes",
            "undiscounted_unit_price_excluding_tax",
            "amount_including_tax",
            "discount_including_tax",
            "sku",
            "tax_amount",
            "aggregated_tax_rate",
            "unique_id",
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
        """Create an instance of LineItem from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxAmountPerUnit": obj.get("taxAmountPerUnit"),
            "undiscountedAmountExcludingTax": obj.get("undiscountedAmountExcludingTax"),
            "quantity": obj.get("quantity"),
            "undiscountedUnitPriceIncludingTax": obj.get("undiscountedUnitPriceIncludingTax"),
            "amountExcludingTax": obj.get("amountExcludingTax"),
            "undiscountedAmountIncludingTax": obj.get("undiscountedAmountIncludingTax"),
            "taxes": [Tax.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "type": obj.get("type"),
            "unitPriceIncludingTax": obj.get("unitPriceIncludingTax"),
            "discountExcludingTax": obj.get("discountExcludingTax"),
            "shippingRequired": obj.get("shippingRequired"),
            "unitPriceExcludingTax": obj.get("unitPriceExcludingTax"),
            "name": obj.get("name"),
            "attributes": dict(
                (_k, LineItemAttribute.from_dict(_v))
                for _k, _v in obj["attributes"].items()
            )
            if obj.get("attributes") is not None
            else None,
            "undiscountedUnitPriceExcludingTax": obj.get("undiscountedUnitPriceExcludingTax"),
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "discountIncludingTax": obj.get("discountIncludingTax"),
            "sku": obj.get("sku"),
            "taxAmount": obj.get("taxAmount"),
            "aggregatedTaxRate": obj.get("aggregatedTaxRate"),
            "uniqueId": obj.get("uniqueId")
        })
        return _obj


