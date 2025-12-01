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
from typing import Optional, Set
from typing_extensions import Self

class TransactionClientPlatformInformation(BaseModel):
    """
    TransactionClientPlatformInformation
    """ # noqa: E501
    space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="spaceId")
    integration_type: Optional[StrictStr] = Field(default=None, description="The type of integration that was used to collect the payment information.", alias="integrationType")
    os_version: Optional[StrictStr] = Field(default=None, description="The version of the operating system that was used to collect the payment information.", alias="osVersion")
    platform_type: Optional[StrictStr] = Field(default=None, description="The type of platform that was used to collect the payment information, e.g. Android or iOS.", alias="platformType")
    sdk_version: Optional[StrictStr] = Field(default=None, description="The type of the SDK that was used to collect the payment information.", alias="sdkVersion")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    transaction: Optional[StrictInt] = Field(default=None, description="The transaction that is associated with the client platform information.")
    __properties: ClassVar[List[str]] = ["spaceId", "integrationType", "osVersion", "platformType", "sdkVersion", "id", "version", "transaction"]

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
        """Create an instance of TransactionClientPlatformInformation from a JSON string"""
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
            "space_id",
            "integration_type",
            "os_version",
            "platform_type",
            "sdk_version",
            "id",
            "version",
            "transaction",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of TransactionClientPlatformInformation from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "spaceId": obj.get("spaceId"),
            "integrationType": obj.get("integrationType"),
            "osVersion": obj.get("osVersion"),
            "platformType": obj.get("platformType"),
            "sdkVersion": obj.get("sdkVersion"),
            "id": obj.get("id"),
            "version": obj.get("version"),
            "transaction": obj.get("transaction")
        })
        return _obj


