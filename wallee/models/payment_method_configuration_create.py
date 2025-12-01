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
from wallee.models.data_collection_type import DataCollectionType
from wallee.models.one_click_payment_mode import OneClickPaymentMode
from typing import Optional, Set
from typing_extensions import Self

class PaymentMethodConfigurationCreate(BaseModel):
    """
    PaymentMethodConfigurationCreate
    """ # noqa: E501
    image_resource_path: Optional[StrictStr] = Field(default=None, description="The resource path to a custom image for the payment method, displayed to the customer for visual identification.", alias="imageResourcePath")
    sort_order: Optional[StrictInt] = Field(default=None, description="When listing payment methods, they can be sorted by this number.", alias="sortOrder")
    name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name used to identify the payment method configuration.")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="A customer-facing custom description for the payment method.")
    one_click_payment_mode: Optional[OneClickPaymentMode] = Field(default=None, alias="oneClickPaymentMode")
    title: Optional[Dict[str, StrictStr]] = Field(default=None, description="A customer-facing custom title for the payment method.")
    data_collection_type: DataCollectionType = Field(alias="dataCollectionType")
    payment_method: StrictInt = Field(description="The payment method that the configuration is for.", alias="paymentMethod")
    state: CreationEntityState
    __properties: ClassVar[List[str]] = ["imageResourcePath", "sortOrder", "name", "description", "oneClickPaymentMode", "title", "dataCollectionType", "paymentMethod", "state"]

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
        """Create an instance of PaymentMethodConfigurationCreate from a JSON string"""
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
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentMethodConfigurationCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "imageResourcePath": obj.get("imageResourcePath"),
            "sortOrder": obj.get("sortOrder"),
            "name": obj.get("name"),
            "description": obj.get("description"),
            "oneClickPaymentMode": obj.get("oneClickPaymentMode"),
            "title": obj.get("title"),
            "dataCollectionType": obj.get("dataCollectionType"),
            "paymentMethod": obj.get("paymentMethod"),
            "state": obj.get("state")
        })
        return _obj


