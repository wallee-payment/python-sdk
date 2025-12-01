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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictBytes, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.payment_terminal_receipt_type import PaymentTerminalReceiptType
from typing import Optional, Set
from typing_extensions import Self

class RenderedTerminalReceipt(BaseModel):
    """
    RenderedTerminalReceipt
    """ # noqa: E501
    printed: Optional[StrictBool] = Field(default=None, description="Whether the terminal's configuration mandates printing and the device has receipt printing capabilities.")
    data: Optional[Union[StrictBytes, StrictStr]] = Field(default=None, description="The receipt document data in binary format, presented as a Base64-encoded string.")
    receipt_type: Optional[PaymentTerminalReceiptType] = Field(default=None, alias="receiptType")
    mime_type: Optional[StrictStr] = Field(default=None, description="The MIME type specifies the format of the receipt document and is determined by the requested format.", alias="mimeType")
    __properties: ClassVar[List[str]] = ["printed", "data", "receiptType", "mimeType"]

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
        """Create an instance of RenderedTerminalReceipt from a JSON string"""
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
            "printed",
            "data",
            "mime_type",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of receipt_type
        if self.receipt_type:
            _dict['receiptType'] = self.receipt_type.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RenderedTerminalReceipt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "printed": obj.get("printed"),
            "data": obj.get("data"),
            "receiptType": PaymentTerminalReceiptType.from_dict(obj["receiptType"]) if obj.get("receiptType") is not None else None,
            "mimeType": obj.get("mimeType")
        })
        return _obj


