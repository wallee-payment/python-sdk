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

from pydantic import BaseModel, ConfigDict, Field, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.rest_address_format import RestAddressFormat
from typing import Optional, Set
from typing_extensions import Self

class RestCountry(BaseModel):
    """
    RestCountry
    """ # noqa: E501
    iso_code2: Optional[StrictStr] = Field(default=None, description="The country's two-letter code (ISO 3166-1 alpha-2 format).", alias="isoCode2")
    address_format: Optional[RestAddressFormat] = Field(default=None, alias="addressFormat")
    iso_code3: Optional[StrictStr] = Field(default=None, description="The country's three-letter code (ISO 3166-1 alpha-3 format).", alias="isoCode3")
    state_codes: Optional[List[StrictStr]] = Field(default=None, description="The codes of all regions (e.g. states, provinces) of the country (ISO 3166-2 format).", alias="stateCodes")
    name: Optional[StrictStr] = Field(default=None, description="The name of the country.")
    numeric_code: Optional[StrictStr] = Field(default=None, description="The country's three-digit code (ISO 3166-1 numeric format).", alias="numericCode")
    __properties: ClassVar[List[str]] = ["isoCode2", "addressFormat", "isoCode3", "stateCodes", "name", "numericCode"]

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
        """Create an instance of RestCountry from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "iso_code2",
            "iso_code3",
            "state_codes",
            "name",
            "numeric_code",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of address_format
        if self.address_format:
            _dict['addressFormat'] = self.address_format.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestCountry from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "isoCode2": obj.get("isoCode2"),
            "addressFormat": RestAddressFormat.from_dict(obj["addressFormat"]) if obj.get("addressFormat") is not None else None,
            "isoCode3": obj.get("isoCode3"),
            "stateCodes": obj.get("stateCodes"),
            "name": obj.get("name"),
            "numericCode": obj.get("numericCode")
        })
        return _obj


