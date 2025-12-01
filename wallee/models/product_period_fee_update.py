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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.persistable_currency_amount_update import PersistableCurrencyAmountUpdate
from typing import Optional, Set
from typing_extensions import Self

class ProductPeriodFeeUpdate(BaseModel):
    """
    ProductPeriodFeeUpdate
    """ # noqa: E501
    period_fee: Optional[List[PersistableCurrencyAmountUpdate]] = Field(default=None, description="The amount charged to the customer for each billing cycle during the term of a subscription.", alias="periodFee")
    component: Optional[StrictInt] = Field(default=None, description="The product component that the fee belongs to.")
    number_of_free_trial_periods: Optional[StrictInt] = Field(default=None, description="The number of subscription billing cycles that count as a trial phase and during which no fees are charged.", alias="numberOfFreeTrialPeriods")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the fee that is displayed to the customer.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the fee that is displayed to the customer.")
    version: StrictInt = Field(description="The version number indicates the version of the entity. The version is incremented whenever the entity is changed.")
    ledger_entry_title: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized title that be used on ledger entries and invoices.", alias="ledgerEntryTitle")
    __properties: ClassVar[List[str]] = ["periodFee", "component", "numberOfFreeTrialPeriods", "name", "description", "version", "ledgerEntryTitle"]

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
        """Create an instance of ProductPeriodFeeUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in period_fee (list)
        _items = []
        if self.period_fee:
            for _item_period_fee in self.period_fee:
                if _item_period_fee:
                    _items.append(_item_period_fee.to_dict())
            _dict['periodFee'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductPeriodFeeUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "periodFee": [PersistableCurrencyAmountUpdate.from_dict(_item) for _item in obj["periodFee"]] if obj.get("periodFee") is not None else None,
            "component": obj.get("component"),
            "numberOfFreeTrialPeriods": obj.get("numberOfFreeTrialPeriods"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "version": obj.get("version"),
            "ledgerEntryTitle": obj.get("ledgerEntryTitle")
        })
        return _obj


