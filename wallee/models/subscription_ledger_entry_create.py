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
from typing_extensions import Annotated
from wallee.models.tax_create import TaxCreate
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionLedgerEntryCreate(BaseModel):
    """
    The subscription ledger entry represents a single change on the subscription balance.
    """ # noqa: E501
    quantity: Union[StrictFloat, StrictInt] = Field(description="The number of items that were consumed.")
    subscription_version: StrictInt = Field(description="The subscription version that the ledger entry belongs to.", alias="subscriptionVersion")
    external_id: StrictStr = Field(description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    taxes: Optional[List[TaxCreate]] = Field(default=None, description="A set of tax lines, each of which specifies a tax applied to the ledger entry.")
    amount_including_tax: Union[StrictFloat, StrictInt] = Field(description="The leger entry's amount with discounts applied, including taxes.", alias="amountIncludingTax")
    title: Annotated[str, Field(min_length=1, strict=True, max_length=150)] = Field(description="The title that indicates what the ledger entry is about.")
    component_reference_name: Optional[StrictStr] = Field(default=None, alias="componentReferenceName")
    subscription_metric_id: Optional[StrictInt] = Field(default=None, alias="subscriptionMetricId")
    __properties: ClassVar[List[str]] = ["quantity", "subscriptionVersion", "externalId", "taxes", "amountIncludingTax", "title", "componentReferenceName", "subscriptionMetricId"]

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
        """Create an instance of SubscriptionLedgerEntryCreate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionLedgerEntryCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "subscriptionVersion": obj.get("subscriptionVersion"),
            "externalId": obj.get("externalId"),
            "taxes": [TaxCreate.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "title": obj.get("title"),
            "componentReferenceName": obj.get("componentReferenceName"),
            "subscriptionMetricId": obj.get("subscriptionMetricId")
        })
        return _obj


