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
from typing_extensions import Annotated
from wallee.models.persistable_currency_amount import PersistableCurrencyAmount
from wallee.models.product_fee_type import ProductFeeType
from wallee.models.subscription_product_component import SubscriptionProductComponent
from typing import Optional, Set
from typing_extensions import Self

class ProductSetupFee(BaseModel):
    """
    ProductSetupFee
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    component: Optional[SubscriptionProductComponent] = None
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the fee that is displayed to the customer.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the fee that is displayed to the customer.")
    setup_fee: Optional[Annotated[List[PersistableCurrencyAmount], Field(min_length=1)]] = Field(default=None, description="The amount charged to the customer once when they subscribe to a subscription.", alias="setupFee")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    on_downgrade_credited_amount: Optional[Annotated[List[PersistableCurrencyAmount], Field(min_length=1)]] = Field(default=None, description="The amount charged to the customer when a subscription is downgraded.", alias="onDowngradeCreditedAmount")
    type: Optional[ProductFeeType] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    on_upgrade_credited_amount: Optional[Annotated[List[PersistableCurrencyAmount], Field(min_length=1)]] = Field(default=None, description="The amount charged to the customer when a subscription is upgraded.", alias="onUpgradeCreditedAmount")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "component", "name", "description", "setupFee", "id", "onDowngradeCreditedAmount", "type", "version", "onUpgradeCreditedAmount"]

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
        """Create an instance of ProductSetupFee from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "name",
            "description",
            "setup_fee",
            "id",
            "on_downgrade_credited_amount",
            "version",
            "on_upgrade_credited_amount",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of component
        if self.component:
            _dict['component'] = self.component.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in setup_fee (list)
        _items = []
        if self.setup_fee:
            for _item_setup_fee in self.setup_fee:
                if _item_setup_fee:
                    _items.append(_item_setup_fee.to_dict())
            _dict['setupFee'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in on_downgrade_credited_amount (list)
        _items = []
        if self.on_downgrade_credited_amount:
            for _item_on_downgrade_credited_amount in self.on_downgrade_credited_amount:
                if _item_on_downgrade_credited_amount:
                    _items.append(_item_on_downgrade_credited_amount.to_dict())
            _dict['onDowngradeCreditedAmount'] = _items
        # override the default output from pydantic by calling `to_dict()` of each item in on_upgrade_credited_amount (list)
        _items = []
        if self.on_upgrade_credited_amount:
            for _item_on_upgrade_credited_amount in self.on_upgrade_credited_amount:
                if _item_on_upgrade_credited_amount:
                    _items.append(_item_on_upgrade_credited_amount.to_dict())
            _dict['onUpgradeCreditedAmount'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ProductSetupFee from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "component": SubscriptionProductComponent.from_dict(obj["component"]) if obj.get("component") is not None else None,
            "name": obj.get("name"),
            "description": obj.get("description"),
            "setupFee": [PersistableCurrencyAmount.from_dict(_item) for _item in obj["setupFee"]] if obj.get("setupFee") is not None else None,
            "id": obj.get("id"),
            "onDowngradeCreditedAmount": [PersistableCurrencyAmount.from_dict(_item) for _item in obj["onDowngradeCreditedAmount"]] if obj.get("onDowngradeCreditedAmount") is not None else None,
            "type": obj.get("type"),
            "version": obj.get("version"),
            "onUpgradeCreditedAmount": [PersistableCurrencyAmount.from_dict(_item) for _item in obj["onUpgradeCreditedAmount"]] if obj.get("onUpgradeCreditedAmount") is not None else None
        })
        return _obj


