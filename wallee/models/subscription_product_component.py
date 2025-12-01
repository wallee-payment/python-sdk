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
from wallee.models.subscription_product_component_group import SubscriptionProductComponentGroup
from wallee.models.subscription_product_component_reference import SubscriptionProductComponentReference
from wallee.models.tax_class import TaxClass
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionProductComponent(BaseModel):
    """
    SubscriptionProductComponent
    """ # noqa: E501
    tax_class: Optional[TaxClass] = Field(default=None, alias="taxClass")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the component that is displayed to the customer.")
    component_change_weight: Optional[StrictInt] = Field(default=None, description="If switching from a component with a lower tier to a component with a higher one, this is considered an upgrade and a fee may be applied.", alias="componentChangeWeight")
    maximal_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A maximum of the defined quantity can be selected for this component.", alias="maximalQuantity")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    minimal_quantity: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="A minimum of the defined quantity must be selected for this component.", alias="minimalQuantity")
    reference: Optional[SubscriptionProductComponentReference] = None
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    quantity_step: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The quantity step determines the interval in which the quantity can be increased.", alias="quantityStep")
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing components, they can be sorted by this number.", alias="sortOrder")
    component_group: Optional[SubscriptionProductComponentGroup] = Field(default=None, alias="componentGroup")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the component that is displayed to the customer.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    default_component: Optional[StrictBool] = Field(default=None, description="Whether this is the default component in its group and preselected.", alias="defaultComponent")
    __properties: ClassVar[List[str]] = ["taxClass", "description", "componentChangeWeight", "maximalQuantity", "version", "minimalQuantity", "reference", "linkedSpaceId", "quantityStep", "sortOrder", "componentGroup", "name", "id", "defaultComponent"]

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
        """Create an instance of SubscriptionProductComponent from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "description",
            "component_change_weight",
            "maximal_quantity",
            "version",
            "minimal_quantity",
            "linked_space_id",
            "quantity_step",
            "sort_order",
            "name",
            "id",
            "default_component",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of tax_class
        if self.tax_class:
            _dict['taxClass'] = self.tax_class.to_dict()
        # override the default output from pydantic by calling `to_dict()` of reference
        if self.reference:
            _dict['reference'] = self.reference.to_dict()
        # override the default output from pydantic by calling `to_dict()` of component_group
        if self.component_group:
            _dict['componentGroup'] = self.component_group.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionProductComponent from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "taxClass": TaxClass.from_dict(obj["taxClass"]) if obj.get("taxClass") is not None else None,
            "description": obj.get("description"),
            "componentChangeWeight": obj.get("componentChangeWeight"),
            "maximalQuantity": obj.get("maximalQuantity"),
            "version": obj.get("version"),
            "minimalQuantity": obj.get("minimalQuantity"),
            "reference": SubscriptionProductComponentReference.from_dict(obj["reference"]) if obj.get("reference") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "quantityStep": obj.get("quantityStep"),
            "sortOrder": obj.get("sortOrder"),
            "componentGroup": SubscriptionProductComponentGroup.from_dict(obj["componentGroup"]) if obj.get("componentGroup") is not None else None,
            "name": obj.get("name"),
            "id": obj.get("id"),
            "defaultComponent": obj.get("defaultComponent")
        })
        return _obj


