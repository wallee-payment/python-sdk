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
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.space_address_create import SpaceAddressCreate
from typing import Optional, Set
from typing_extensions import Self

class AbstractSpaceUpdate(BaseModel):
    """
    AbstractSpaceUpdate
    """ # noqa: E501
    request_limit: Optional[StrictInt] = Field(default=None, description="The maximum number of API requests that are accepted within two minutes. This limit can only be changed with special privileges.", alias="requestLimit")
    postal_address: Optional[SpaceAddressCreate] = Field(default=None, alias="postalAddress")
    name: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=200)]] = Field(default=None, description="The name used to identify the space.")
    technical_contact_addresses: Optional[List[StrictStr]] = Field(default=None, description="The email address that will receive messages about technical issues and errors that occur in the space.", alias="technicalContactAddresses")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that is used to schedule and run background processes. This does not affect the formatting of dates in the user interface.", alias="timeZone")
    state: Optional[CreationEntityState] = None
    primary_currency: Optional[StrictStr] = Field(default=None, description="The currency that is used to display aggregated amounts in the space.", alias="primaryCurrency")
    __properties: ClassVar[List[str]] = ["requestLimit", "postalAddress", "name", "technicalContactAddresses", "timeZone", "state", "primaryCurrency"]

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
        """Create an instance of AbstractSpaceUpdate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of postal_address
        if self.postal_address:
            _dict['postalAddress'] = self.postal_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AbstractSpaceUpdate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "requestLimit": obj.get("requestLimit"),
            "postalAddress": SpaceAddressCreate.from_dict(obj["postalAddress"]) if obj.get("postalAddress") is not None else None,
            "name": obj.get("name"),
            "technicalContactAddresses": obj.get("technicalContactAddresses"),
            "timeZone": obj.get("timeZone"),
            "state": obj.get("state"),
            "primaryCurrency": obj.get("primaryCurrency")
        })
        return _obj


