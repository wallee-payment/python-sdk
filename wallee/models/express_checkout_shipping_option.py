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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.tax import Tax
from typing import Optional, Set
from typing_extensions import Self

class ExpressCheckoutShippingOption(BaseModel):
    """
    ExpressCheckoutShippingOption
    """ # noqa: E501
    description: Optional[StrictStr] = Field(default=None, description="Description of the option")
    taxes: Optional[List[Tax]] = Field(default=None, description="A set of tax lines, each of which specifies a tax applied to this shipping option.")
    currency: Optional[StrictStr] = Field(default=None, description="Currency code (ISO-4217) of this shipping option.")
    id: Optional[StrictStr] = Field(default=None, description="Identifier of the option.")
    label: Optional[StrictStr] = Field(default=None, description="Label of the option.")
    amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="Total cost of this shipping option, including taxes.", alias="amountIncludingTax")
    selected: Optional[StrictBool] = Field(default=None, description="Whether it was the option selected by the customer.")
    __properties: ClassVar[List[str]] = ["description", "taxes", "currency", "id", "label", "amountIncludingTax", "selected"]

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
        """Create an instance of ExpressCheckoutShippingOption from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "description",
            "taxes",
            "currency",
            "id",
            "label",
            "amount_including_tax",
            "selected",
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ExpressCheckoutShippingOption from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "description": obj.get("description"),
            "taxes": [Tax.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "currency": obj.get("currency"),
            "id": obj.get("id"),
            "label": obj.get("label"),
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "selected": obj.get("selected")
        })
        return _obj


