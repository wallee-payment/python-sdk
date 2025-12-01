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
from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.payment_app_completion_configuration import PaymentAppCompletionConfiguration
from wallee.models.payment_app_connector_state import PaymentAppConnectorState
from wallee.models.payment_app_processor import PaymentAppProcessor
from wallee.models.payment_app_refund_configuration import PaymentAppRefundConfiguration
from wallee.models.payment_connector_configuration import PaymentConnectorConfiguration
from typing import Optional, Set
from typing_extensions import Self

class PaymentAppConnector(BaseModel):
    """
    PaymentAppConnector
    """ # noqa: E501
    payment_page_endpoint: Optional[StrictStr] = Field(default=None, description="The URL where the user is redirected to process a payment. This endpoint is provided by the external service provider.", alias="paymentPageEndpoint")
    external_id: Optional[Annotated[str, Field(strict=True, max_length=40)]] = Field(default=None, description="A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.", alias="externalId")
    updated_on: Optional[datetime] = Field(default=None, description="The date and time when the connector was last updated.", alias="updatedOn")
    completion_configuration: Optional[PaymentAppCompletionConfiguration] = Field(default=None, alias="completionConfiguration")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the connector was created.", alias="createdOn")
    processor: Optional[PaymentAppProcessor] = None
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    connector_configuration: Optional[PaymentConnectorConfiguration] = Field(default=None, alias="connectorConfiguration")
    authorization_timeout: Optional[StrictStr] = Field(default=None, description="The duration within which the authorization process for a payment should complete.", alias="authorizationTimeout")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the connector.")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[PaymentAppConnectorState] = None
    refund_configuration: Optional[PaymentAppRefundConfiguration] = Field(default=None, alias="refundConfiguration")
    __properties: ClassVar[List[str]] = ["paymentPageEndpoint", "externalId", "updatedOn", "completionConfiguration", "createdOn", "processor", "version", "linkedSpaceId", "connectorConfiguration", "authorizationTimeout", "name", "id", "state", "refundConfiguration"]

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
        """Create an instance of PaymentAppConnector from a JSON string"""
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
            "payment_page_endpoint",
            "external_id",
            "updated_on",
            "created_on",
            "version",
            "linked_space_id",
            "authorization_timeout",
            "name",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of completion_configuration
        if self.completion_configuration:
            _dict['completionConfiguration'] = self.completion_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of processor
        if self.processor:
            _dict['processor'] = self.processor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connector_configuration
        if self.connector_configuration:
            _dict['connectorConfiguration'] = self.connector_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of refund_configuration
        if self.refund_configuration:
            _dict['refundConfiguration'] = self.refund_configuration.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentAppConnector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentPageEndpoint": obj.get("paymentPageEndpoint"),
            "externalId": obj.get("externalId"),
            "updatedOn": obj.get("updatedOn"),
            "completionConfiguration": PaymentAppCompletionConfiguration.from_dict(obj["completionConfiguration"]) if obj.get("completionConfiguration") is not None else None,
            "createdOn": obj.get("createdOn"),
            "processor": PaymentAppProcessor.from_dict(obj["processor"]) if obj.get("processor") is not None else None,
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "connectorConfiguration": PaymentConnectorConfiguration.from_dict(obj["connectorConfiguration"]) if obj.get("connectorConfiguration") is not None else None,
            "authorizationTimeout": obj.get("authorizationTimeout"),
            "name": obj.get("name"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "refundConfiguration": PaymentAppRefundConfiguration.from_dict(obj["refundConfiguration"]) if obj.get("refundConfiguration") is not None else None
        })
        return _obj


