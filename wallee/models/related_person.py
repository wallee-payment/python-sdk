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

from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.basic_address import BasicAddress
from wallee.models.identity_info import IdentityInfo
from wallee.models.representative_info import RepresentativeInfo
from typing import Optional, Set
from typing_extensions import Self

class RelatedPerson(BaseModel):
    """
    RelatedPerson
    """ # noqa: E501
    email_address: Optional[StrictStr] = Field(default=None, alias="emailAddress")
    is_selected_shareholder_or_director: Optional[StrictBool] = Field(default=None, alias="isSelectedShareholderOrDirector")
    place_of_birth: Optional[StrictStr] = Field(default=None, alias="placeOfBirth")
    identity_info: Optional[IdentityInfo] = Field(default=None, alias="identityInfo")
    nationality: Optional[StrictStr] = None
    contact_language: Optional[StrictStr] = Field(default=None, alias="contactLanguage")
    is_director: Optional[StrictBool] = Field(default=None, alias="isDirector")
    representative_info: Optional[RepresentativeInfo] = Field(default=None, alias="representativeInfo")
    job_role: Optional[StrictStr] = Field(default=None, alias="jobRole")
    id: Optional[StrictStr] = None
    company_share: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, alias="companyShare")
    residence_address: Optional[BasicAddress] = Field(default=None, alias="residenceAddress")
    __properties: ClassVar[List[str]] = ["emailAddress", "isSelectedShareholderOrDirector", "placeOfBirth", "identityInfo", "nationality", "contactLanguage", "isDirector", "representativeInfo", "jobRole", "id", "companyShare", "residenceAddress"]

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
        """Create an instance of RelatedPerson from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of identity_info
        if self.identity_info:
            _dict['identityInfo'] = self.identity_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of representative_info
        if self.representative_info:
            _dict['representativeInfo'] = self.representative_info.to_dict()
        # override the default output from pydantic by calling `to_dict()` of residence_address
        if self.residence_address:
            _dict['residenceAddress'] = self.residence_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of RelatedPerson from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "emailAddress": obj.get("emailAddress"),
            "isSelectedShareholderOrDirector": obj.get("isSelectedShareholderOrDirector"),
            "placeOfBirth": obj.get("placeOfBirth"),
            "identityInfo": IdentityInfo.from_dict(obj["identityInfo"]) if obj.get("identityInfo") is not None else None,
            "nationality": obj.get("nationality"),
            "contactLanguage": obj.get("contactLanguage"),
            "isDirector": obj.get("isDirector"),
            "representativeInfo": RepresentativeInfo.from_dict(obj["representativeInfo"]) if obj.get("representativeInfo") is not None else None,
            "jobRole": obj.get("jobRole"),
            "id": obj.get("id"),
            "companyShare": obj.get("companyShare"),
            "residenceAddress": BasicAddress.from_dict(obj["residenceAddress"]) if obj.get("residenceAddress") is not None else None
        })
        return _obj


