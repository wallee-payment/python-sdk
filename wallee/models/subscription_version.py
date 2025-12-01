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
from wallee.models.billing_cycle_model import BillingCycleModel
from wallee.models.subscription import Subscription
from wallee.models.subscription_component_configuration import SubscriptionComponentConfiguration
from wallee.models.subscription_product_version import SubscriptionProductVersion
from wallee.models.subscription_version_state import SubscriptionVersionState
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionVersion(BaseModel):
    """
    SubscriptionVersion
    """ # noqa: E501
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    subscription: Optional[Subscription] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription version was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    terminated_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription version was terminated.", alias="terminatedOn")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    termination_issued_on: Optional[datetime] = Field(default=None, description="The date and time when the termination of the subscription version was issued.", alias="terminationIssuedOn")
    component_configurations: Optional[List[SubscriptionComponentConfiguration]] = Field(default=None, description="The configurations of the subscription's components.", alias="componentConfigurations")
    product_version: Optional[SubscriptionProductVersion] = Field(default=None, alias="productVersion")
    activated_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription version was activated.", alias="activatedOn")
    terminating_on: Optional[datetime] = Field(default=None, description="The date and time when the termination of the subscription version started.", alias="terminatingOn")
    billing_currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the currency used to invoice the customer. Must be one of the currencies supported by the product.", alias="billingCurrency")
    expected_last_period_end: Optional[datetime] = Field(default=None, description="The date and time when the last period is expected to end.", alias="expectedLastPeriodEnd")
    billing_cycle_model: Optional[BillingCycleModel] = Field(default=None, alias="billingCycleModel")
    planned_termination_date: Optional[datetime] = Field(default=None, description="The date and time when the termination of the subscription version is planned.", alias="plannedTerminationDate")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[SubscriptionVersionState] = None
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the subscription version failed.", alias="failedOn")
    __properties: ClassVar[List[str]] = ["plannedPurgeDate", "language", "subscription", "createdOn", "version", "terminatedOn", "linkedSpaceId", "terminationIssuedOn", "componentConfigurations", "productVersion", "activatedOn", "terminatingOn", "billingCurrency", "expectedLastPeriodEnd", "billingCycleModel", "plannedTerminationDate", "id", "state", "failedOn"]

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
        """Create an instance of SubscriptionVersion from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "planned_purge_date",
            "language",
            "created_on",
            "version",
            "terminated_on",
            "linked_space_id",
            "termination_issued_on",
            "component_configurations",
            "activated_on",
            "terminating_on",
            "billing_currency",
            "expected_last_period_end",
            "planned_termination_date",
            "id",
            "failed_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of subscription
        if self.subscription:
            _dict['subscription'] = self.subscription.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in component_configurations (list)
        _items = []
        if self.component_configurations:
            for _item_component_configurations in self.component_configurations:
                if _item_component_configurations:
                    _items.append(_item_component_configurations.to_dict())
            _dict['componentConfigurations'] = _items
        # override the default output from pydantic by calling `to_dict()` of product_version
        if self.product_version:
            _dict['productVersion'] = self.product_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_cycle_model
        if self.billing_cycle_model:
            _dict['billingCycleModel'] = self.billing_cycle_model.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionVersion from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "language": obj.get("language"),
            "subscription": Subscription.from_dict(obj["subscription"]) if obj.get("subscription") is not None else None,
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "terminatedOn": obj.get("terminatedOn"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "terminationIssuedOn": obj.get("terminationIssuedOn"),
            "componentConfigurations": [SubscriptionComponentConfiguration.from_dict(_item) for _item in obj["componentConfigurations"]] if obj.get("componentConfigurations") is not None else None,
            "productVersion": SubscriptionProductVersion.from_dict(obj["productVersion"]) if obj.get("productVersion") is not None else None,
            "activatedOn": obj.get("activatedOn"),
            "terminatingOn": obj.get("terminatingOn"),
            "billingCurrency": obj.get("billingCurrency"),
            "expectedLastPeriodEnd": obj.get("expectedLastPeriodEnd"),
            "billingCycleModel": BillingCycleModel.from_dict(obj["billingCycleModel"]) if obj.get("billingCycleModel") is not None else None,
            "plannedTerminationDate": obj.get("plannedTerminationDate"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "failedOn": obj.get("failedOn")
        })
        return _obj


