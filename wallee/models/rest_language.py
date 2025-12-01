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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing import Optional, Set
from typing_extensions import Self

class RestLanguage(BaseModel):
    """
    RestLanguage
    """ # noqa: E501
    primary_of_group: Optional[StrictBool] = Field(default=None, description="Whether this is the primary language in a group of languages.", alias="primaryOfGroup")
    country_code: Optional[StrictStr] = Field(default=None, description="The two-letter code of the language's region (ISO 3166-1 alpha-2 format).", alias="countryCode")
    iso2_code: Optional[StrictStr] = Field(default=None, description="The language's two-letter code (ISO 639-1 format).", alias="iso2Code")
    name: Optional[StrictStr] = Field(default=None, description="The name of the language.")
    ietf_code: Optional[StrictStr] = Field(default=None, description="The language's IETF tag consisting of the two-letter ISO code and region e.g. en-US, de-CH.", alias="ietfCode")
    iso3_code: Optional[StrictStr] = Field(default=None, description="The language's three-letter code (ISO 639-2/T format).", alias="iso3Code")
    plural_expression: Optional[StrictStr] = Field(default=None, description="The expression to determine the plural index for a given number of items used to find the proper plural form for translations.", alias="pluralExpression")
    __properties: ClassVar[List[str]] = ["primaryOfGroup", "countryCode", "iso2Code", "name", "ietfCode", "iso3Code", "pluralExpression"]

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
        """Create an instance of RestLanguage from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "primary_of_group",
            "country_code",
            "iso2_code",
            "name",
            "ietf_code",
            "iso3_code",
            "plural_expression",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RestLanguage from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "primaryOfGroup": obj.get("primaryOfGroup"),
            "countryCode": obj.get("countryCode"),
            "iso2Code": obj.get("iso2Code"),
            "name": obj.get("name"),
            "ietfCode": obj.get("ietfCode"),
            "iso3Code": obj.get("iso3Code"),
            "pluralExpression": obj.get("pluralExpression")
        })
        return _obj


