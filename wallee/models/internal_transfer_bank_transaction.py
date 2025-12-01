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

from pydantic import BaseModel, ConfigDict, Field, StrictInt
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.bank_transaction import BankTransaction
from typing import Optional, Set
from typing_extensions import Self

class InternalTransferBankTransaction(BaseModel):
    """
    InternalTransferBankTransaction
    """ # noqa: E501
    source_bank_transaction: Optional[BankTransaction] = Field(default=None, alias="sourceBankTransaction")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    target_bank_transaction: Optional[BankTransaction] = Field(default=None, alias="targetBankTransaction")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    __properties: ClassVar[List[str]] = ["sourceBankTransaction", "linkedSpaceId", "targetBankTransaction", "id", "version"]

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
        """Create an instance of InternalTransferBankTransaction from a JSON string"""
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
            "version",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of source_bank_transaction
        if self.source_bank_transaction:
            _dict['sourceBankTransaction'] = self.source_bank_transaction.to_dict()
        # override the default output from pydantic by calling `to_dict()` of target_bank_transaction
        if self.target_bank_transaction:
            _dict['targetBankTransaction'] = self.target_bank_transaction.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InternalTransferBankTransaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sourceBankTransaction": BankTransaction.from_dict(obj["sourceBankTransaction"]) if obj.get("sourceBankTransaction") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "targetBankTransaction": BankTransaction.from_dict(obj["targetBankTransaction"]) if obj.get("targetBankTransaction") is not None else None,
            "id": obj.get("id"),
            "version": obj.get("version")
        })
        return _obj


