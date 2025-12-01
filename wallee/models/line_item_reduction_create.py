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

from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt
from typing import Any, ClassVar, Dict, List, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class LineItemReductionCreate(BaseModel):
    """
    LineItemReductionCreate
    """ # noqa: E501
    quantity_reduction: Union[StrictFloat, StrictInt] = Field(description="The quantity removed or reduced from the line item. This value reflects the decrease in the item count due to the reduction.", alias="quantityReduction")
    unit_price_reduction: Union[StrictFloat, StrictInt] = Field(description="The monetary amount by which the line item's unit price is discounted. This reduction adjusts the price without altering the quantity.", alias="unitPriceReduction")
    line_item_unique_id: Annotated[str, Field(strict=True, max_length=200)] = Field(description="The unique identifier of the line item to which the reduction is applied. This ID ensures the reduction is accurately associated with the correct item.", alias="lineItemUniqueId")
    __properties: ClassVar[List[str]] = ["quantityReduction", "unitPriceReduction", "lineItemUniqueId"]

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
        """Create an instance of LineItemReductionCreate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of LineItemReductionCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantityReduction": obj.get("quantityReduction"),
            "unitPriceReduction": obj.get("unitPriceReduction"),
            "lineItemUniqueId": obj.get("lineItemUniqueId")
        })
        return _obj


