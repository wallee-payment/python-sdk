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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class SubscriptionMetricUsageReport(BaseModel):
    """
    The metric usage is the actual usage of a metric for a particular subscription as collected by an external application.
    """ # noqa: E501
    consumed_units: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The number of resources consumed, will be charged in the next billing cycle.", alias="consumedUnits")
    created_by_user_id: Optional[StrictInt] = Field(default=None, description="The ID of the user the usage report was created by.", alias="createdByUserId")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    metric: Optional[StrictInt] = Field(default=None, description="The metric that the usage report is recorded for.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    description: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="A description used to identify the usage report.")
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    subscription: Optional[StrictInt] = Field(default=None, description="The subscription that the usage report is recorded for.")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the usage report was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["consumedUnits", "createdByUserId", "linkedSpaceId", "metric", "plannedPurgeDate", "description", "externalId", "id", "subscription", "createdOn", "version"]

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
        """Create an instance of SubscriptionMetricUsageReport from a JSON string"""
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
            "consumed_units",
            "created_by_user_id",
            "linked_space_id",
            "metric",
            "planned_purge_date",
            "description",
            "external_id",
            "id",
            "subscription",
            "created_on",
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of SubscriptionMetricUsageReport from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "consumedUnits": obj.get("consumedUnits"),
            "createdByUserId": obj.get("createdByUserId"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "metric": obj.get("metric"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "description": obj.get("description"),
            "externalId": obj.get("externalId"),
            "id": obj.get("id"),
            "subscription": obj.get("subscription"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version")
        })
        return _obj


