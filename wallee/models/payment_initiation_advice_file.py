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
from wallee.models.payment_initiation_advice_file_state import PaymentInitiationAdviceFileState
from wallee.models.payment_processor import PaymentProcessor
from typing import Optional, Set
from typing_extensions import Self

class PaymentInitiationAdviceFile(BaseModel):
    """
    PaymentInitiationAdviceFile
    """ # noqa: E501
    forwarded_on: Optional[datetime] = Field(default=None, description="The shipping date indicates the date on which the pain file was transferred to an external processing system.", alias="forwardedOn")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    processed_on: Optional[datetime] = Field(default=None, alias="processedOn")
    file_generated_on: Optional[datetime] = Field(default=None, alias="fileGeneratedOn")
    name: Optional[StrictStr] = None
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentInitiationAdviceFileState] = None
    created_on: Optional[datetime] = Field(default=None, description="The created on date indicates the date on which the entity was stored into the database.", alias="createdOn")
    failure_message: Optional[StrictStr] = Field(default=None, alias="failureMessage")
    processor: Optional[PaymentProcessor] = None
    __properties: ClassVar[List[str]] = ["forwardedOn", "linkedSpaceId", "processedOn", "fileGeneratedOn", "name", "id", "state", "createdOn", "failureMessage", "processor"]

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
        """Create an instance of PaymentInitiationAdviceFile from a JSON string"""
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
            "forwarded_on",
            "linked_space_id",
            "processed_on",
            "file_generated_on",
            "name",
            "id",
            "created_on",
            "failure_message",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of processor
        if self.processor:
            _dict['processor'] = self.processor.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentInitiationAdviceFile from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "forwardedOn": obj.get("forwardedOn"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "processedOn": obj.get("processedOn"),
            "fileGeneratedOn": obj.get("fileGeneratedOn"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "createdOn": obj.get("createdOn"),
            "failureMessage": obj.get("failureMessage"),
            "processor": PaymentProcessor.from_dict(obj["processor"]) if obj.get("processor") is not None else None
        })
        return _obj


