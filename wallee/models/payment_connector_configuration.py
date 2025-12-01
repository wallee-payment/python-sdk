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
from wallee.models.condition import Condition
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.payment_connector import PaymentConnector
from wallee.models.payment_method_configuration import PaymentMethodConfiguration
from wallee.models.payment_processor_configuration import PaymentProcessorConfiguration
from wallee.models.sales_channel import SalesChannel
from typing import Optional, Set
from typing_extensions import Self

class PaymentConnectorConfiguration(BaseModel):
    """
    PaymentConnectorConfiguration
    """ # noqa: E501
    payment_method_configuration: Optional[PaymentMethodConfiguration] = Field(default=None, alias="paymentMethodConfiguration")
    image_path: Optional[StrictStr] = Field(default=None, description="The URL to the connector's image.", alias="imagePath")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    priority: Optional[StrictInt] = Field(default=None, description="The priority that determines the order in which connector configurations are taken into account when processing a payment. Low values are considered first.")
    enabled_sales_channels: Optional[List[SalesChannel]] = Field(default=None, description="The sales channels for which the connector configuration is enabled. If empty, it is enabled for all sales channels.", alias="enabledSalesChannels")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    processor_configuration: Optional[PaymentProcessorConfiguration] = Field(default=None, alias="processorConfiguration")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    connector: Optional[PaymentConnector] = None
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the connector configuration.")
    enabled_space_views: Optional[List[StrictInt]] = Field(default=None, description="The space views for which the connector configuration is enabled. If empty, it is enabled for all space views.", alias="enabledSpaceViews")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    applicable_for_transaction_processing: Optional[StrictBool] = Field(default=None, description="Whether this connector configuration is enabled for processing payments, taking into account the state of the processor and payment method configurations.", alias="applicableForTransactionProcessing")
    conditions: Optional[List[Condition]] = Field(default=None, description="Conditions allow to define criteria that a transaction must fulfill in order for the connector configuration to be considered for processing the payment.")
    __properties: ClassVar[List[str]] = ["paymentMethodConfiguration", "imagePath", "plannedPurgeDate", "priority", "enabledSalesChannels", "version", "processorConfiguration", "linkedSpaceId", "connector", "name", "enabledSpaceViews", "id", "state", "applicableForTransactionProcessing", "conditions"]

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
        """Create an instance of PaymentConnectorConfiguration from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "image_path",
            "planned_purge_date",
            "priority",
            "enabled_sales_channels",
            "version",
            "linked_space_id",
            "name",
            "enabled_space_views",
            "id",
            "applicable_for_transaction_processing",
            "conditions",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payment_method_configuration
        if self.payment_method_configuration:
            _dict['paymentMethodConfiguration'] = self.payment_method_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in enabled_sales_channels (list)
        _items = []
        if self.enabled_sales_channels:
            for _item_enabled_sales_channels in self.enabled_sales_channels:
                if _item_enabled_sales_channels:
                    _items.append(_item_enabled_sales_channels.to_dict())
            _dict['enabledSalesChannels'] = _items
        # override the default output from pydantic by calling `to_dict()` of processor_configuration
        if self.processor_configuration:
            _dict['processorConfiguration'] = self.processor_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connector
        if self.connector:
            _dict['connector'] = self.connector.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in conditions (list)
        _items = []
        if self.conditions:
            for _item_conditions in self.conditions:
                if _item_conditions:
                    _items.append(_item_conditions.to_dict())
            _dict['conditions'] = _items
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentConnectorConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "paymentMethodConfiguration": PaymentMethodConfiguration.from_dict(obj["paymentMethodConfiguration"]) if obj.get("paymentMethodConfiguration") is not None else None,
            "imagePath": obj.get("imagePath"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "priority": obj.get("priority"),
            "enabledSalesChannels": [SalesChannel.from_dict(_item) for _item in obj["enabledSalesChannels"]] if obj.get("enabledSalesChannels") is not None else None,
            "version": obj.get("version"),
            "processorConfiguration": PaymentProcessorConfiguration.from_dict(obj["processorConfiguration"]) if obj.get("processorConfiguration") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "connector": PaymentConnector.from_dict(obj["connector"]) if obj.get("connector") is not None else None,
            "name": obj.get("name"),
            "enabledSpaceViews": obj.get("enabledSpaceViews"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "applicableForTransactionProcessing": obj.get("applicableForTransactionProcessing"),
            "conditions": [Condition.from_dict(_item) for _item in obj["conditions"]] if obj.get("conditions") is not None else None
        })
        return _obj


