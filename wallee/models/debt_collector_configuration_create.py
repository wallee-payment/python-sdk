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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.debt_collector_condition import DebtCollectorCondition
from typing import Optional, Set
from typing_extensions import Self

class DebtCollectorConfigurationCreate(BaseModel):
    """
    The debt collector configuration defines the behavior of the collection process for a particular collector.
    """ # noqa: E501
    skip_review_enabled: Optional[StrictBool] = Field(default=None, description="Whether the review of debt collection cases is skipped.", alias="skipReviewEnabled")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the debt collector configuration.")
    enabled_space_views: Optional[List[StrictInt]] = Field(default=None, description="The space views for which the debt collector configuration is enabled. If empty, it is enabled for all space views.", alias="enabledSpaceViews")
    state: Optional[CreationEntityState] = None
    conditions: Optional[List[DebtCollectorCondition]] = Field(default=None, description="Conditions allow to define criteria that a debt collection case must fulfill in order for the debt collector configuration to be considered for processing the case.")
    priority: Optional[StrictInt] = Field(default=None, description="The priority that determines the order in which debt collector configurations are taken into account when processing a case. Low values are considered first.")
    collector: StrictInt = Field(description="The debt collector that the configuration is for.")
    __properties: ClassVar[List[str]] = ["skipReviewEnabled", "name", "enabledSpaceViews", "state", "conditions", "priority", "collector"]

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
        """Create an instance of DebtCollectorConfigurationCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of DebtCollectorConfigurationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "skipReviewEnabled": obj.get("skipReviewEnabled"),
            "name": obj.get("name"),
            "enabledSpaceViews": obj.get("enabledSpaceViews"),
            "state": obj.get("state"),
            "conditions": [DebtCollectorCondition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None,
            "priority": obj.get("priority"),
            "collector": obj.get("collector")
        })
        return _obj


