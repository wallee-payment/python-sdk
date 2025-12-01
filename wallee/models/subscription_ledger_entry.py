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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.product_fee_type import ProductFeeType
from wallee.models.subscription_ledger_entry_state import SubscriptionLedgerEntryState
from wallee.models.tax import Tax
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionLedgerEntry(BaseModel):
    """
    The subscription ledger entry represents a single change on the subscription balance.
    """ # noqa: E501
    quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of items that were consumed.")
    amount_excluding_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The leger entry's amount with discounts applied, excluding taxes.", alias="amountExcludingTax")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    subscription_version: Optional[StrictInt] = Field(default=None, description="The subscription version that the ledger entry belongs to.", alias="subscriptionVersion")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    taxes: Optional[List[Tax]] = Field(default=None, description="A set of tax lines, each of which specifies a tax applied to the ledger entry.")
    fee_type: Optional[ProductFeeType] = Field(default=None, alias="feeType")
    title: Optional[Annotated[str, Field(min_length=1, strict=True, max_length=150)]] = Field(default=None, description="The title that indicates what the ledger entry is about.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    component_reference_name: Optional[StrictStr] = Field(default=None, alias="componentReferenceName")
    subscription_metric_id: Optional[StrictInt] = Field(default=None, alias="subscriptionMetricId")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    pro_rata_calculated: Optional[StrictBool] = Field(default=None, alias="proRataCalculated")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the ledger entry was created by.", alias="createdBy")
    component_reference_sku: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, alias="componentReferenceSku")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionLedgerEntryState] = None
    amount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The leger entry's amount with discounts applied, including taxes.", alias="amountIncludingTax")
    discount_including_tax: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The discount allocated to the ledger entry, including taxes.", alias="discountIncludingTax")
    tax_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sum of all taxes applied to the ledger entry.", alias="taxAmount")
    aggregated_tax_rate: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total tax rate applied to the ledger entry, calculated from the rates of all tax lines.", alias="aggregatedTaxRate")
    __properties: ClassVar[List[str]] = ["quantity", "amountExcludingTax", "plannedPurgeDate", "subscriptionVersion", "externalId", "taxes", "feeType", "title", "createdOn", "version", "componentReferenceName", "subscriptionMetricId", "linkedSpaceId", "proRataCalculated", "createdBy", "componentReferenceSku", "id", "state", "amountIncludingTax", "discountIncludingTax", "taxAmount", "aggregatedTaxRate"]

    @field_validator('component_reference_sku')
    def component_reference_sku_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([0-9a-zA-Z\-_]+)", value):
            raise ValueError(r"must validate the regular expression /([0-9a-zA-Z\-_]+)/")
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
        """Create an instance of SubscriptionLedgerEntry from a JSON string"""
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
            "quantity",
            "amount_excluding_tax",
            "planned_purge_date",
            "subscription_version",
            "external_id",
            "taxes",
            "title",
            "created_on",
            "version",
            "component_reference_name",
            "subscription_metric_id",
            "linked_space_id",
            "pro_rata_calculated",
            "created_by",
            "component_reference_sku",
            "id",
            "amount_including_tax",
            "discount_including_tax",
            "tax_amount",
            "aggregated_tax_rate",
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
        """Create an instance of SubscriptionLedgerEntry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "quantity": obj.get("quantity"),
            "amountExcludingTax": obj.get("amountExcludingTax"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "subscriptionVersion": obj.get("subscriptionVersion"),
            "externalId": obj.get("externalId"),
            "taxes": [Tax.from_dict(_item) for _item in obj["taxes"]] if obj.get("taxes") is not None else None,
            "feeType": obj.get("feeType"),
            "title": obj.get("title"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "componentReferenceName": obj.get("componentReferenceName"),
            "subscriptionMetricId": obj.get("subscriptionMetricId"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "proRataCalculated": obj.get("proRataCalculated"),
            "createdBy": obj.get("createdBy"),
            "componentReferenceSku": obj.get("componentReferenceSku"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "amountIncludingTax": obj.get("amountIncludingTax"),
            "discountIncludingTax": obj.get("discountIncludingTax"),
            "taxAmount": obj.get("taxAmount"),
            "aggregatedTaxRate": obj.get("aggregatedTaxRate")
        })
        return _obj


