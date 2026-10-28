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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.fulfillment_state import FulfillmentState
from wallee.models.transaction_completion import TransactionCompletion
from typing import Optional, Set
from typing_extensions import Self

class Fulfillment(BaseModel):
    """
    Fulfillment
    """ # noqa: E501
    completion: Optional[TransactionCompletion] = None
    overridden_by: Optional[StrictInt] = Field(default=None, alias="overriddenBy")
    override_reason: Optional[StrictStr] = Field(default=None, alias="overrideReason")
    description: Optional[StrictStr] = None
    external_id: Optional[StrictStr] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    gross_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="grossAmount")
    created_on: Optional[datetime] = Field(default=None, alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    created_by: Optional[StrictInt] = Field(default=None, alias="createdBy")
    failure_reason: Optional[StrictStr] = Field(default=None, alias="failureReason")
    fulfilled_by: Optional[StrictInt] = Field(default=None, alias="fulfilledBy")
    in_store_pickup: Optional[StrictBool] = Field(default=None, alias="inStorePickup")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[FulfillmentState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    tracking_number: Optional[StrictStr] = Field(default=None, alias="trackingNumber")
    failed_on: Optional[datetime] = Field(default=None, alias="failedOn")
    overridden_on: Optional[datetime] = Field(default=None, alias="overriddenOn")
    fulfilled_on: Optional[datetime] = Field(default=None, alias="fulfilledOn")
    __properties: ClassVar[List[str]] = ["completion", "overriddenBy", "overrideReason", "description", "externalId", "grossAmount", "createdOn", "version", "linkedSpaceId", "createdBy", "failureReason", "fulfilledBy", "inStorePickup", "id", "state", "linkedTransaction", "trackingNumber", "failedOn", "overriddenOn", "fulfilledOn"]

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
        """Create an instance of Fulfillment from a JSON string"""
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
            "overridden_by",
            "override_reason",
            "description",
            "external_id",
            "gross_amount",
            "created_on",
            "version",
            "linked_space_id",
            "created_by",
            "failure_reason",
            "fulfilled_by",
            "in_store_pickup",
            "id",
            "linked_transaction",
            "tracking_number",
            "failed_on",
            "overridden_on",
            "fulfilled_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of completion
        if self.completion:
            _dict['completion'] = self.completion.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Fulfillment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "completion": TransactionCompletion.from_dict(obj["completion"]) if obj.get("completion") is not None else None,
            "overriddenBy": obj.get("overriddenBy"),
            "overrideReason": obj.get("overrideReason"),
            "description": obj.get("description"),
            "externalId": obj.get("externalId"),
            "grossAmount": obj.get("grossAmount"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "createdBy": obj.get("createdBy"),
            "failureReason": obj.get("failureReason"),
            "fulfilledBy": obj.get("fulfilledBy"),
            "inStorePickup": obj.get("inStorePickup"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "trackingNumber": obj.get("trackingNumber"),
            "failedOn": obj.get("failedOn"),
            "overriddenOn": obj.get("overriddenOn"),
            "fulfilledOn": obj.get("fulfilledOn")
        })
        return _obj


