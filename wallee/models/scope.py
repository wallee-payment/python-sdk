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

from datetime import datetime
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.feature import Feature
from typing import Optional, Set
from typing_extensions import Self

class Scope(BaseModel):
    """
    Scope
    """ # noqa: E501
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    ssl_active: Optional[StrictBool] = Field(default=None, description="Whether the scope supports SSL.", alias="sslActive")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    machine_name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name identifying the scope in e.g. URLs.", alias="machineName")
    url: Optional[StrictStr] = Field(default=None, description="The URL where the scope can be accessed.")
    features: Optional[List[Feature]] = Field(default=None, description="The list of features that are active in the scope.")
    themes: Optional[List[StrictStr]] = Field(default=None, description="The themes that determine the look and feel of the scope's user interface. A fall-through strategy is applied when building the actual theme.")
    port: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The port where the scope can be accessed.")
    preprod_domain_name: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The preprod domain name that belongs to the scope.", alias="preprodDomainName")
    domain_name: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The domain name that belongs to the scope.", alias="domainName")
    name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name used to identify the scope.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    sandbox_domain_name: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="The sandbox domain name that belongs to the scope.", alias="sandboxDomainName")
    __properties: ClassVar[List[str]] = ["plannedPurgeDate", "sslActive", "version", "machineName", "url", "features", "themes", "port", "preprodDomainName", "domainName", "name", "id", "state", "sandboxDomainName"]

    @field_validator('machine_name')
    def machine_name_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([A-Z][A-Za-z0-9]+)(_([A-Z][A-Za-z0-9]+))*", value):
            raise ValueError(r"must validate the regular expression /([A-Z][A-Za-z0-9]+)(_([A-Z][A-Za-z0-9]+))*/")
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
        """Create an instance of Scope from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "planned_purge_date",
            "ssl_active",
            "version",
            "machine_name",
            "url",
            "features",
            "themes",
            "port",
            "preprod_domain_name",
            "domain_name",
            "name",
            "id",
            "sandbox_domain_name",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in features (list)
        _items = []
        if self.features:
            for _item_features in self.features:
                if _item_features:
                    _items.append(_item_features.to_dict())
            _dict['features'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Scope from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "sslActive": obj.get("sslActive"),
            "version": obj.get("version"),
            "machineName": obj.get("machineName"),
            "url": obj.get("url"),
            "features": [Feature.from_dict(_item) for _item in obj["features"]] if obj.get("features") is not None else None,
            "themes": obj.get("themes"),
            "port": obj.get("port"),
            "preprodDomainName": obj.get("preprodDomainName"),
            "domainName": obj.get("domainName"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "sandboxDomainName": obj.get("sandboxDomainName")
        })
        return _obj


