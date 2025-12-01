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
from wallee.models.customers_presence import CustomersPresence
from wallee.models.data_collection_type import DataCollectionType
from wallee.models.payment_connector_feature import PaymentConnectorFeature
from wallee.models.payment_method import PaymentMethod
from wallee.models.payment_method_brand import PaymentMethodBrand
from wallee.models.payment_primary_risk_taker import PaymentPrimaryRiskTaker
from wallee.models.payment_processor import PaymentProcessor
from typing import Optional, Set
from typing_extensions import Self

class PaymentConnector(BaseModel):
    """
    PaymentConnector
    """ # noqa: E501
    supported_features: Optional[List[PaymentConnectorFeature]] = Field(default=None, description="The features that are supported by the connector.", alias="supportedFeatures")
    supported_customers_presences: Optional[List[CustomersPresence]] = Field(default=None, description="The types of customer's presence that are supported by the connector.", alias="supportedCustomersPresences")
    data_collection_type: Optional[DataCollectionType] = Field(default=None, alias="dataCollectionType")
    deprecated: Optional[StrictBool] = Field(default=None, description="Whether the object was deprecated.")
    primary_risk_taker: Optional[PaymentPrimaryRiskTaker] = Field(default=None, alias="primaryRiskTaker")
    description: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized description of the object.")
    payment_method_brand: Optional[PaymentMethodBrand] = Field(default=None, alias="paymentMethodBrand")
    processor: Optional[PaymentProcessor] = None
    deprecation_reason: Optional[Dict[str, StrictStr]] = Field(default=None, description="The deprecation reason describes why the object was deprecated.", alias="deprecationReason")
    supported_currencies: Optional[List[StrictStr]] = Field(default=None, description="The currencies that are supported by the connector.", alias="supportedCurrencies")
    name: Optional[Dict[str, StrictStr]] = Field(default=None, description="The localized name of the object.")
    payment_method: Optional[PaymentMethod] = Field(default=None, alias="paymentMethod")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    __properties: ClassVar[List[str]] = ["supportedFeatures", "supportedCustomersPresences", "dataCollectionType", "deprecated", "primaryRiskTaker", "description", "paymentMethodBrand", "processor", "deprecationReason", "supportedCurrencies", "name", "paymentMethod", "id"]

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
        """Create an instance of PaymentConnector from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "supported_features",
            "supported_customers_presences",
            "deprecated",
            "description",
            "deprecation_reason",
            "supported_currencies",
            "name",
            "id",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of each item in supported_features (list)
        _items = []
        if self.supported_features:
            for _item_supported_features in self.supported_features:
                if _item_supported_features:
                    _items.append(_item_supported_features.to_dict())
            _dict['supportedFeatures'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_method_brand
        if self.payment_method_brand:
            _dict['paymentMethodBrand'] = self.payment_method_brand.to_dict()
        # override the default output from pydantic by calling `to_dict()` of processor
        if self.processor:
            _dict['processor'] = self.processor.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_method
        if self.payment_method:
            _dict['paymentMethod'] = self.payment_method.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of PaymentConnector from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "supportedFeatures": [PaymentConnectorFeature.from_dict(_item) for _item in obj["supportedFeatures"]] if obj.get("supportedFeatures") is not None else None,
            "supportedCustomersPresences": obj.get("supportedCustomersPresences"),
            "dataCollectionType": obj.get("dataCollectionType"),
            "deprecated": obj.get("deprecated"),
            "primaryRiskTaker": obj.get("primaryRiskTaker"),
            "description": obj.get("description"),
            "paymentMethodBrand": PaymentMethodBrand.from_dict(obj["paymentMethodBrand"]) if obj.get("paymentMethodBrand") is not None else None,
            "processor": PaymentProcessor.from_dict(obj["processor"]) if obj.get("processor") is not None else None,
            "deprecationReason": obj.get("deprecationReason"),
            "supportedCurrencies": obj.get("supportedCurrencies"),
            "name": obj.get("name"),
            "paymentMethod": PaymentMethod.from_dict(obj["paymentMethod"]) if obj.get("paymentMethod") is not None else None,
            "id": obj.get("id")
        })
        return _obj


