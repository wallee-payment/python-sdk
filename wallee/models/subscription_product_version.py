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
from typing_extensions import Annotated
from wallee.models.billing_cycle_model import BillingCycleModel
from wallee.models.subscription_product import SubscriptionProduct
from wallee.models.subscription_product_version_state import SubscriptionProductVersionState
from wallee.models.tax_calculation import TaxCalculation
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProductVersion(BaseModel):
    """
    SubscriptionProductVersion
    """ # noqa: E501
    retiring_finished_on: Optional[datetime] = Field(default=None, description="The date and time when the product version was retired.", alias="retiringFinishedOn")
    enabled_currencies: Optional[List[StrictStr]] = Field(default=None, description="The three-letter codes (ISO 4217 format) of the currencies that the product version supports.", alias="enabledCurrencies")
    product: Optional[SubscriptionProduct] = None
    retiring_started_on: Optional[datetime] = Field(default=None, description="The date and time when the product version's retirement was started.", alias="retiringStartedOn")
    tax_calculation: Optional[TaxCalculation] = Field(default=None, alias="taxCalculation")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the product version was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    reference: Optional[Annotated[str, Field(strict=True, max_length=125)]] = Field(default=None, description="The reference used to identify the product version.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the product version was activated.", alias="activatedOn")
    billing_cycle: Optional[StrictStr] = Field(default=None, description="The recurring period of time, typically monthly or annually, for which a subscriber is charged.", alias="billingCycle")
    default_currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the product version's default currency.", alias="defaultCurrency")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the product that is displayed to the customer.")
    minimal_number_of_periods: Optional[StrictInt] = Field(default=None, description="The minimum number of periods the subscription will run before it can be terminated.", alias="minimalNumberOfPeriods")
    obsoleted_on: Optional[datetime] = Field(default=None, description="The date and time when the product version was made obsolete.", alias="obsoletedOn")
    billing_cycle_model: Optional[BillingCycleModel] = Field(default=None, alias="billingCycleModel")
    comment: Optional[StrictStr] = Field(default=None, description="A comment that describes the product version and why it was created. It is not disclosed to the subscriber.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    increment_number: Optional[StrictInt] = Field(default=None, description="Whenever a new version of a product is created, the number is increased and assigned.", alias="incrementNumber")
    state: Optional[SubscriptionProductVersionState] = None
    number_of_notice_periods: Optional[StrictInt] = Field(default=None, description="The number of periods the subscription will keep running after its termination was requested.", alias="numberOfNoticePeriods")
    __properties: ClassVar[List[str]] = ["retiringFinishedOn", "enabledCurrencies", "product", "retiringStartedOn", "taxCalculation", "plannedPurgeDate", "createdOn", "version", "reference", "linkedSpaceId", "activatedOn", "billingCycle", "defaultCurrency", "name", "minimalNumberOfPeriods", "obsoletedOn", "billingCycleModel", "comment", "id", "incrementNumber", "state", "numberOfNoticePeriods"]

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
        """Create an instance of SubscriptionProductVersion from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "retiring_finished_on",
            "enabled_currencies",
            "retiring_started_on",
            "planned_purge_date",
            "created_on",
            "version",
            "reference",
            "linked_space_id",
            "activated_on",
            "billing_cycle",
            "default_currency",
            "name",
            "minimal_number_of_periods",
            "obsoleted_on",
            "comment",
            "id",
            "increment_number",
            "number_of_notice_periods",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of product
        if self.product:
            _dict['product'] = self.product.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_cycle_model
        if self.billing_cycle_model:
            _dict['billingCycleModel'] = self.billing_cycle_model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionProductVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "retiringFinishedOn": obj.get("retiringFinishedOn"),
            "enabledCurrencies": obj.get("enabledCurrencies"),
            "product": SubscriptionProduct.from_dict(obj["product"]) if obj.get("product") is not None else None,
            "retiringStartedOn": obj.get("retiringStartedOn"),
            "taxCalculation": obj.get("taxCalculation"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "reference": obj.get("reference"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "activatedOn": obj.get("activatedOn"),
            "billingCycle": obj.get("billingCycle"),
            "defaultCurrency": obj.get("defaultCurrency"),
            "name": obj.get("name"),
            "minimalNumberOfPeriods": obj.get("minimalNumberOfPeriods"),
            "obsoletedOn": obj.get("obsoletedOn"),
            "billingCycleModel": BillingCycleModel.from_dict(obj["billingCycleModel"]) if obj.get("billingCycleModel") is not None else None,
            "comment": obj.get("comment"),
            "id": obj.get("id"),
            "incrementNumber": obj.get("incrementNumber"),
            "state": obj.get("state"),
            "numberOfNoticePeriods": obj.get("numberOfNoticePeriods")
        })
        return _obj


