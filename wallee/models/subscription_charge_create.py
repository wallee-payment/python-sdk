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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.subscription_charge_processing_type import SubscriptionChargeProcessingType
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionChargeCreate(BaseModel):
    """
    The subscription charge represents a single charge carried out for a particular subscription.
    """ # noqa: E501
    reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the charge.")
    planned_execution_date: Optional[datetime] = Field(default=None, description="The date and time when the execution of the charge is planned.", alias="plannedExecutionDate")
    processing_type: SubscriptionChargeProcessingType = Field(alias="processingType")
    external_id: StrictStr = Field(description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    success_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=500)]] = Field(default=None, description="The URL to redirect the customer back to after they successfully authenticated their payment.", alias="successUrl")
    subscription: StrictInt = Field(description="The subscription that the charge belongs to.")
    failed_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=500)]] = Field(default=None, description="The URL to redirect the customer back to after they canceled or failed to authenticated their payment.", alias="failedUrl")
    __properties: ClassVar[List[str]] = ["reference", "plannedExecutionDate", "processingType", "externalId", "successUrl", "subscription", "failedUrl"]

    @field_validator('reference')
    def reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
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
        """Create an instance of SubscriptionChargeCreate from a JSON string"""
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
        """Create an instance of SubscriptionChargeCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "reference": obj.get("reference"),
            "plannedExecutionDate": obj.get("plannedExecutionDate"),
            "processingType": obj.get("processingType"),
            "externalId": obj.get("externalId"),
            "successUrl": obj.get("successUrl"),
            "subscription": obj.get("subscription"),
            "failedUrl": obj.get("failedUrl")
        })
        return _obj


