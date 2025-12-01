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
from typing import Optional, Set
from typing_extensions import Self

class PaymentAppCompletionConfiguration(BaseModel):
    """
    PaymentAppCompletionConfiguration
    """ # noqa: E501
    multiple_completions_supported: Optional[StrictBool] = Field(default=None, description="Whether the payment connector can process multiple completions for a single transaction.", alias="multipleCompletionsSupported")
    maximal_completion_delay_in_days: Optional[StrictInt] = Field(default=None, description="The maximum number of days after a transaction's authorization during which a completion or void action can be triggered. Once this period has passed, neither action can be executed.", alias="maximalCompletionDelayInDays")
    completion_endpoint: Optional[StrictStr] = Field(default=None, description="The URL that the payment service provider will invoke to process a completion request. This endpoint handles communication with the provider for initiating and managing completions.", alias="completionEndpoint")
    completion_timeout_in_minutes: Optional[StrictInt] = Field(default=None, description="The maximum time (in minutes) to wait for a response from the payment service provider after a completion request is triggered. If no feedback or final status is received within this period, the completion is considered failed.", alias="completionTimeoutInMinutes")
    void_endpoint: Optional[StrictStr] = Field(default=None, description="The URL that the payment service provider will invoke to process a void request. This endpoint handles communication with the provider for initiating and managing voids.", alias="voidEndpoint")
    __properties: ClassVar[List[str]] = ["multipleCompletionsSupported", "maximalCompletionDelayInDays", "completionEndpoint", "completionTimeoutInMinutes", "voidEndpoint"]

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
        """Create an instance of PaymentAppCompletionConfiguration from a JSON string"""
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
            "multiple_completions_supported",
            "maximal_completion_delay_in_days",
            "completion_endpoint",
            "completion_timeout_in_minutes",
            "void_endpoint",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentAppCompletionConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "multipleCompletionsSupported": obj.get("multipleCompletionsSupported"),
            "maximalCompletionDelayInDays": obj.get("maximalCompletionDelayInDays"),
            "completionEndpoint": obj.get("completionEndpoint"),
            "completionTimeoutInMinutes": obj.get("completionTimeoutInMinutes"),
            "voidEndpoint": obj.get("voidEndpoint")
        })
        return _obj


