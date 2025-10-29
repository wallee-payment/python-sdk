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
import re
import json

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.transaction import Transaction
from typing import Optional, Set
from typing_extensions import Self

class TransactionComment(BaseModel):
    """
    TransactionComment
    """
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    pinned: Optional[StrictBool] = Field(default=None, description="Whether the comment is pinned to the top.")
    edited_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the comment was last updated by.", alias="editedBy")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the comment was created by.", alias="createdBy")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    edited_on: Optional[datetime] = Field(default=None, description="The date and time when the comment was last updated.", alias="editedOn")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    content: Optional[Annotated[str, Field(strict=True, max_length=262144)]] = Field(default=None, description="The comment's actual content.")
    transaction: Optional[Transaction] = None
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "pinned", "editedBy", "createdBy", "id", "editedOn", "createdOn", "version", "content", "transaction"]

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
        """Create an instance of TransactionComment from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "pinned",
            "edited_by",
            "created_by",
            "id",
            "edited_on",
            "created_on",
            "version",
            "content",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of transaction
        if self.transaction:
            _dict['transaction'] = self.transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionComment from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "pinned": obj.get("pinned"),
            "editedBy": obj.get("editedBy"),
            "createdBy": obj.get("createdBy"),
            "id": obj.get("id"),
            "editedOn": obj.get("editedOn"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "content": obj.get("content"),
            "transaction": Transaction.from_dict(obj["transaction"]) if obj.get("transaction") is not None else None
        })
        return _obj


