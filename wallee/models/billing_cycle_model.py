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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.billing_cycle_type import BillingCycleType
from wallee.models.billing_day_customization import BillingDayCustomization
from wallee.models.displayable_day_of_week import DisplayableDayOfWeek
from wallee.models.displayable_month import DisplayableMonth
from typing import Optional, Set
from typing_extensions import Self

class BillingCycleModel(BaseModel):
    """
    BillingCycleModel
    """ # noqa: E501
    month: Optional[DisplayableMonth] = None
    customization: Optional[BillingDayCustomization] = None
    day_of_month: Optional[StrictInt] = Field(default=None, alias="dayOfMonth")
    weekly_day: Optional[DisplayableDayOfWeek] = Field(default=None, alias="weeklyDay")
    number_of_periods: Annotated[int, Field(strict=True, ge=1)] = Field(description="Billing Cycle type multiplied by Number of Periods defines billing cycle duration, e.g. 3 months. Monthly types require 1-12; weekly and yearly types require 1-9 periods; and daily types require 1-30.", alias="numberOfPeriods")
    billing_cycle_type: BillingCycleType = Field(alias="billingCycleType")
    __properties: ClassVar[List[str]] = ["month", "customization", "dayOfMonth", "weeklyDay", "numberOfPeriods", "billingCycleType"]

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
        """Create an instance of BillingCycleModel from a JSON string"""
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
        """Create an instance of BillingCycleModel from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "month": obj.get("month"),
            "customization": obj.get("customization"),
            "dayOfMonth": obj.get("dayOfMonth"),
            "weeklyDay": obj.get("weeklyDay"),
            "numberOfPeriods": obj.get("numberOfPeriods"),
            "billingCycleType": obj.get("billingCycleType")
        })
        return _obj


