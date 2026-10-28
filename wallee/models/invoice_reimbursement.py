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
from pydantic import BaseModel, ConfigDict, Field, StrictFloat, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional, Union
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.invoice_processor import InvoiceProcessor
from wallee.models.invoice_reimbursement_state import InvoiceReimbursementState
from wallee.models.payment_connector_configuration import PaymentConnectorConfiguration
from wallee.models.payment_initiation_advice_file import PaymentInitiationAdviceFile
from typing import Optional, Set
from typing_extensions import Self

class InvoiceReimbursement(BaseModel):
    """
    InvoiceReimbursement
    """ # noqa: E501
    discarded_on: Optional[datetime] = Field(default=None, alias="discardedOn")
    amount: Optional[Union[StrictFloat, StrictInt]] = None
    recipient_given_name: Optional[StrictStr] = Field(default=None, alias="recipientGivenName")
    recipient_iban: Optional[StrictStr] = Field(default=None, alias="recipientIban")
    recipient_organization_name: Optional[StrictStr] = Field(default=None, alias="recipientOrganizationName")
    recipient_street: Optional[StrictStr] = Field(default=None, alias="recipientStreet")
    discarded_by: Optional[StrictInt] = Field(default=None, alias="discardedBy")
    sender_iban: Optional[StrictStr] = Field(default=None, alias="senderIban")
    source: Optional[InvoiceProcessor] = None
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    environment: Optional[ChargeAttemptEnvironment] = None
    recipient_family_name: Optional[StrictStr] = Field(default=None, alias="recipientFamilyName")
    processed_on: Optional[datetime] = Field(default=None, alias="processedOn")
    payment_connector_configuration: Optional[PaymentConnectorConfiguration] = Field(default=None, alias="paymentConnectorConfiguration")
    recipient_postcode: Optional[StrictStr] = Field(default=None, alias="recipientPostcode")
    currency: Optional[StrictStr] = None
    recipient_country: Optional[StrictStr] = Field(default=None, alias="recipientCountry")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[InvoiceReimbursementState] = None
    processed_by: Optional[StrictInt] = Field(default=None, alias="processedBy")
    recipient_city: Optional[StrictStr] = Field(default=None, alias="recipientCity")
    payment_initiation_advice_file: Optional[PaymentInitiationAdviceFile] = Field(default=None, alias="paymentInitiationAdviceFile")
    __properties: ClassVar[List[str]] = ["discardedOn", "amount", "recipientGivenName", "recipientIban", "recipientOrganizationName", "recipientStreet", "discardedBy", "senderIban", "source", "createdOn", "version", "linkedSpaceId", "environment", "recipientFamilyName", "processedOn", "paymentConnectorConfiguration", "recipientPostcode", "currency", "recipientCountry", "id", "state", "processedBy", "recipientCity", "paymentInitiationAdviceFile"]

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
        """Create an instance of InvoiceReimbursement from a JSON string"""
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
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        * OpenAPI `readOnly` fields are excluded.
        """
        excluded_fields: Set[str] = set([
            "discarded_on",
            "amount",
            "recipient_given_name",
            "recipient_iban",
            "recipient_organization_name",
            "recipient_street",
            "discarded_by",
            "sender_iban",
            "created_on",
            "version",
            "linked_space_id",
            "recipient_family_name",
            "processed_on",
            "recipient_postcode",
            "currency",
            "recipient_country",
            "id",
            "processed_by",
            "recipient_city",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of payment_connector_configuration
        if self.payment_connector_configuration:
            _dict['paymentConnectorConfiguration'] = self.payment_connector_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_initiation_advice_file
        if self.payment_initiation_advice_file:
            _dict['paymentInitiationAdviceFile'] = self.payment_initiation_advice_file.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of InvoiceReimbursement from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "discardedOn": obj.get("discardedOn"),
            "amount": obj.get("amount"),
            "recipientGivenName": obj.get("recipientGivenName"),
            "recipientIban": obj.get("recipientIban"),
            "recipientOrganizationName": obj.get("recipientOrganizationName"),
            "recipientStreet": obj.get("recipientStreet"),
            "discardedBy": obj.get("discardedBy"),
            "senderIban": obj.get("senderIban"),
            "source": obj.get("source"),
            "createdOn": obj.get("createdOn"),
            "version": obj.get("version"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "environment": obj.get("environment"),
            "recipientFamilyName": obj.get("recipientFamilyName"),
            "processedOn": obj.get("processedOn"),
            "paymentConnectorConfiguration": PaymentConnectorConfiguration.from_dict(obj["paymentConnectorConfiguration"]) if obj.get("paymentConnectorConfiguration") is not None else None,
            "recipientPostcode": obj.get("recipientPostcode"),
            "currency": obj.get("currency"),
            "recipientCountry": obj.get("recipientCountry"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "processedBy": obj.get("processedBy"),
            "recipientCity": obj.get("recipientCity"),
            "paymentInitiationAdviceFile": PaymentInitiationAdviceFile.from_dict(obj["paymentInitiationAdviceFile"]) if obj.get("paymentInitiationAdviceFile") is not None else None
        })
        return _obj


