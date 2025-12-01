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
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.tax import Tax
from typing import Optional, Set
from typing_extensions import Self

class PaymentAdjustment(BaseModel):
    """
    PaymentAdjustment
    """ # noqa: E501
    amount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The adjustment's amount, excluding taxes.", alias="amountExcludingTax")
    rate_in_percentage: Optional[Union[Annotated[float, Field(le=100, strict=True)], Annotated[int, Field(le=100, strict=True)]]] = Field(default=None, description="The percentage rate used to calculate the adjustment amount.", alias="rateInPercentage")
    tax: Optional[Tax] = None
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The adjustment's amount, including taxes.", alias="amountIncludingTax")
    type: Optional[StrictInt] = Field(default=None, description="The type of the adjustment.")
    __properties: ClassVar[List[str]] = ["amountExcludingTax", "rateInPercentage", "tax", "id", "amountIncludingTax", "type"]

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
        """Create an instance of PaymentAdjustment from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "amount_excluding_tax",
            "rate_in_percentage",
            "id",
            "amount_including_tax",
            "type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tax
        if self.tax:
            _dict['tax'] = self.tax.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentAdjustment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "amountExcludingTax": obj.get("amountExcludingTax"),
            "rateInPercentage": obj.get("rateInPercentage"),
            "tax": Tax.from_dict(obj["tax"]) if obj.get("tax") is not None else None,
            "id": obj.get("id"),
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "type": obj.get("type")
        })
        return _obj


