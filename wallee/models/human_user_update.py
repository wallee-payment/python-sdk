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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from typing import Optional, Set
from typing_extensions import Self

class HumanUserUpdate(BaseModel):
    """
    HumanUserUpdate
    """ # noqa: E501
    mobile_phone_number: Optional[Annotated[str, Field(strict=True, max_length=30)]] = Field(default=None, description="The user's mobile phone number.", alias="mobilePhoneNumber")
    two_factor_enabled: Optional[StrictBool] = Field(default=None, description="Whether two-factor authentication is enabled for this user.", alias="twoFactorEnabled")
    email_address: Optional[Annotated[str, Field(strict=True, max_length=128)]] = Field(default=None, description="The user's email address.", alias="emailAddress")
    firstname: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The user's first name.")
    time_zone: Optional[StrictStr] = Field(default=None, description="The user's time zone. If none is specified, the one provided by the browser will be used.", alias="timeZone")
    language: Optional[StrictStr] = Field(default=None, description="The user's preferred language.")
    state: Optional[CreationEntityState] = None
    lastname: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The user's last name.")
    version: StrictInt = Field(description="The version number indicates the version of the entity. The version is incremented whenever the entity is changed.")
    __properties: ClassVar[List[str]] = ["mobilePhoneNumber", "twoFactorEnabled", "emailAddress", "firstname", "timeZone", "language", "state", "lastname", "version"]

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
        """Create an instance of HumanUserUpdate from a JSON string"""
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
        """Create an instance of HumanUserUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "mobilePhoneNumber": obj.get("mobilePhoneNumber"),
            "twoFactorEnabled": obj.get("twoFactorEnabled"),
            "emailAddress": obj.get("emailAddress"),
            "firstname": obj.get("firstname"),
            "timeZone": obj.get("timeZone"),
            "language": obj.get("language"),
            "state": obj.get("state"),
            "lastname": obj.get("lastname"),
            "version": obj.get("version")
        })
        return _obj


