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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.webhook_identity import WebhookIdentity
from wallee.models.webhook_url import WebhookUrl
from typing import Optional, Set
from typing_extensions import Self

class WebhookListener(BaseModel):
    """
    WebhookListener
    """ # noqa: E501
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    entity_states: Optional[List[StrictStr]] = Field(default=None, description="The entity's target states that are to be monitored.", alias="entityStates")
    identity: Optional[WebhookIdentity] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=50)]] = Field(default=None, description="The name used to identify the webhook listener.")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    notify_every_change: Optional[StrictBool] = Field(default=None, description="Whether every update of the entity or only state changes are to be monitored.", alias="notifyEveryChange")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    enable_payload_signature_and_state: Optional[StrictBool] = Field(default=None, description="Whether signature header and 'state' property are enabled in webhook payload.", alias="enablePayloadSignatureAndState")
    entity: Optional[StrictInt] = Field(default=None, description="The entity that is to be monitored.")
    url: Optional[WebhookUrl] = None
    __properties: ClassVar[List[str]] = ["linkedSpaceId", "entityStates", "identity", "name", "plannedPurgeDate", "id", "state", "notifyEveryChange", "version", "enablePayloadSignatureAndState", "entity", "url"]

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
        """Create an instance of WebhookListener from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "linked_space_id",
            "entity_states",
            "name",
            "planned_purge_date",
            "id",
            "notify_every_change",
            "version",
            "enable_payload_signature_and_state",
            "entity",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of identity
        if self.identity:
            _dict['identity'] = self.identity.to_dict()
        # override the default output from pydantic by calling `to_dict()` of url
        if self.url:
            _dict['url'] = self.url.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of WebhookListener from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "entityStates": obj.get("entityStates"),
            "identity": WebhookIdentity.from_dict(obj["identity"]) if obj.get("identity") is not None else None,
            "name": obj.get("name"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "notifyEveryChange": obj.get("notifyEveryChange"),
            "version": obj.get("version"),
            "enablePayloadSignatureAndState": obj.get("enablePayloadSignatureAndState"),
            "entity": obj.get("entity"),
            "url": WebhookUrl.from_dict(obj["url"]) if obj.get("url") is not None else None
        })
        return _obj


