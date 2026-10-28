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

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class PaymentTerminalCreationRequest(BaseModel):
    """
    PaymentTerminalCreationRequest
    """ # noqa: E501
    environment: Annotated[str, Field(strict=True)] = Field(description="The environment used to create the payment terminal (TEST/PRODUCTION).")
    configuration: StrictInt = Field(description="The configuration that is assigned to the terminal and determines how it works.")
    name: StrictStr = Field(description="The name used to identify the payment terminal.")
    external_id: StrictStr = Field(description="The ID assigned by the external system to this payment terminal", alias="externalId")
    location: StrictInt = Field(description="The physical location where the terminal is used.")
    __properties: ClassVar[List[str]] = ["environment", "configuration", "name", "externalId", "location"]

    @field_validator('environment')
    def environment_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"^(TEST|PRODUCTION)$", value):
            raise ValueError(r"must validate the regular expression /^(TEST|PRODUCTION)$/")
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
        """Create an instance of PaymentTerminalCreationRequest from a JSON string"""
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
        """Create an instance of PaymentTerminalCreationRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "environment": obj.get("environment"),
            "configuration": obj.get("configuration"),
            "name": obj.get("name"),
            "externalId": obj.get("externalId"),
            "location": obj.get("location")
        })
        return _obj


