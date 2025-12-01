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
from wallee.models.charge_flow_level import ChargeFlowLevel
from typing import Optional, Set
from typing_extensions import Self

class ChargeFlowLevelPaymentLink(BaseModel):
    """
    ChargeFlowLevelPaymentLink
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    charge_flow_level: Optional[ChargeFlowLevel] = Field(default=None, alias="chargeFlowLevel")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    payment_link: Optional[StrictStr] = Field(default=None, description="The URL provided to the customer for entering their payment details and completing the transaction.", alias="paymentLink")
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "chargeFlowLevel", "id", "paymentLink"]

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
        """Create an instance of ChargeFlowLevelPaymentLink from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "id",
            "payment_link",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of charge_flow_level
        if self.charge_flow_level:
            _dict['chargeFlowLevel'] = self.charge_flow_level.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeFlowLevelPaymentLink from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "chargeFlowLevel": ChargeFlowLevel.from_dict(obj["chargeFlowLevel"]) if obj.get("chargeFlowLevel") is not None else None,
            "id": obj.get("id"),
            "paymentLink": obj.get("paymentLink")
        })
        return _obj


