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
from wallee.models.creation_entity_state import CreationEntityState
from wallee.models.data_collection_type import DataCollectionType
from wallee.models.one_click_payment_mode import OneClickPaymentMode
from wallee.models.payment_method import PaymentMethod
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodConfiguration(BaseModel):
    """
    PaymentMethodConfiguration
    """ # noqa: E501
    data_collection_type: Optional[DataCollectionType] = Field(default=None, alias="dataCollectionType")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="A customer-facing custom description for the payment method.")
    resolved_image_url: Optional[StrictStr] = Field(default=None, description="The URL to the image of the payment method displayed to the customer. If a custom image is defined, it will be used; otherwise, the default image of the payment method will be shown.", alias="resolvedImageUrl")
    one_click_payment_mode: Optional[OneClickPaymentMode] = Field(default=None, alias="oneClickPaymentMode")
    title: Optional[Dict[str, StrictStr]] = Field(default=None, description="A customer-facing custom title for the payment method.")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    space_id: Optional[Annotated[int, Field(strict=True, ge=1)]] = Field(default=None, description="The ID of the space this object belongs to.", alias="spaceId")
    image_resource_path: Optional[StrictStr] = Field(default=None, description="The resource path to a custom image for the payment method, displayed to the customer for visual identification.", alias="imageResourcePath")
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing payment methods, they can be sorted by this number.", alias="sortOrder")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the payment method configuration.")
    resolved_description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The description of the payment method displayed to the customer. If a custom description is defined, it will be used; otherwise, the default description of the payment method will be shown.", alias="resolvedDescription")
    resolved_title: Optional[Dict[str, StrictStr]] = Field(default=None, description="The title of the payment method displayed to the customer. If a custom title is defined, it will be used; otherwise, the default title of the payment method will be shown.", alias="resolvedTitle")
    payment_method: Optional[PaymentMethod] = Field(default=None, alias="paymentMethod")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[CreationEntityState] = None
    __properties: ClassVar[List[str]] = ["dataCollectionType", "plannedPurgeDate", "description", "resolvedImageUrl", "oneClickPaymentMode", "title", "version", "linkedSpaceId", "spaceId", "imageResourcePath", "sortOrder", "name", "resolvedDescription", "resolvedTitle", "paymentMethod", "id", "state"]

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
        """Create an instance of PaymentMethodConfiguration from a JSON string"""
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
            "description",
            "resolved_image_url",
            "title",
            "version",
            "linked_space_id",
            "space_id",
            "image_resource_path",
            "sort_order",
            "name",
            "resolved_description",
            "resolved_title",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodConfiguration from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "dataCollectionType": obj.get("dataCollectionType"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "description": obj.get("description"),
            "resolvedImageUrl": obj.get("resolvedImageUrl"),
            "oneClickPaymentMode": obj.get("oneClickPaymentMode"),
            "title": obj.get("title"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "spaceId": obj.get("spaceId"),
            "imageResourcePath": obj.get("imageResourcePath"),
            "sortOrder": obj.get("sortOrder"),
            "name": obj.get("name"),
            "resolvedDescription": obj.get("resolvedDescription"),
            "resolvedTitle": obj.get("resolvedTitle"),
            "paymentMethod": PaymentMethod.from_dict(obj["paymentMethod"]) if obj.get("paymentMethod") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state")
        })
        return _obj


