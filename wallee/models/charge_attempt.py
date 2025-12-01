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
from wallee.models.charge import Charge
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.charge_attempt_state import ChargeAttemptState
from wallee.models.connector_invocation import ConnectorInvocation
from wallee.models.customers_presence import CustomersPresence
from wallee.models.failure_reason import FailureReason
from wallee.models.label import Label
from wallee.models.payment_connector_configuration import PaymentConnectorConfiguration
from wallee.models.payment_terminal import PaymentTerminal
from wallee.models.token_version import TokenVersion
from wallee.models.transaction_completion_behavior import TransactionCompletionBehavior
from wallee.models.wallet_type import WalletType
from typing import Optional, Set
from typing_extensions import Self

class ChargeAttempt(BaseModel):
    """
    ChargeAttempt
    """ # noqa: E501
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    sales_channel: Optional[StrictInt] = Field(default=None, description="The sales channel through which the charge attempt was made.", alias="salesChannel")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    initializing_token_version: Optional[StrictBool] = Field(default=None, description="Whether a new token version is being initialized.", alias="initializingTokenVersion")
    token_version: Optional[TokenVersion] = Field(default=None, alias="tokenVersion")
    succeeded_on: Optional[datetime] = Field(default=None, description="The date and time when the charge attempt succeeded.", alias="succeededOn")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[ChargeAttemptState] = None
    linked_transaction: Optional[StrictInt] = Field(default=None, description="The payment transaction this object is linked to.", alias="linkedTransaction")
    redirection_url: Optional[StrictStr] = Field(default=None, description="The URL to redirect the customer to after payment processing.", alias="redirectionUrl")
    charge: Optional[Charge] = None
    wallet: Optional[WalletType] = None
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    time_zone: Optional[StrictStr] = Field(default=None, description="The time zone that this object is associated with.", alias="timeZone")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    terminal: Optional[PaymentTerminal] = None
    user_failure_message: Optional[Annotated[str, Field(strict=True, max_length=2000)]] = Field(default=None, description="The message that can be displayed to the customer explaining why the charge attempt failed, in the customer's language.", alias="userFailureMessage")
    completion_behavior: Optional[TransactionCompletionBehavior] = Field(default=None, alias="completionBehavior")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    labels: Optional[List[Label]] = Field(default=None, description="The labels providing additional information about the object.")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the object will expire.", alias="timeoutOn")
    environment: Optional[ChargeAttemptEnvironment] = None
    invocation: Optional[ConnectorInvocation] = None
    connector_configuration: Optional[PaymentConnectorConfiguration] = Field(default=None, alias="connectorConfiguration")
    next_update_on: Optional[datetime] = Field(default=None, description="The date and time when the next update of the object's state is planned.", alias="nextUpdateOn")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    customers_presence: Optional[CustomersPresence] = Field(default=None, alias="customersPresence")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the charge attempt failed.", alias="failedOn")
    __properties: ClassVar[List[str]] = ["language", "salesChannel", "createdOn", "initializingTokenVersion", "tokenVersion", "succeededOn", "id", "state", "linkedTransaction", "redirectionUrl", "charge", "wallet", "plannedPurgeDate", "timeZone", "spaceViewId", "terminal", "userFailureMessage", "completionBehavior", "version", "labels", "linkedSpaceId", "timeoutOn", "environment", "invocation", "connectorConfiguration", "nextUpdateOn", "failureReason", "customersPresence", "failedOn"]

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
        """Create an instance of ChargeAttempt from a JSON string"""
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
        """
        excluded_fields: Set[str] = set([
            "language",
            "sales_channel",
            "created_on",
            "initializing_token_version",
            "succeeded_on",
            "id",
            "linked_transaction",
            "redirection_url",
            "planned_purge_date",
            "time_zone",
            "space_view_id",
            "user_failure_message",
            "version",
            "labels",
            "linked_space_id",
            "timeout_on",
            "next_update_on",
            "failed_on",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of token_version
        if self.token_version:
            _dict['tokenVersion'] = self.token_version.to_dict()
        # override the default output from pydantic by calling `to_dict()` of charge
        if self.charge:
            _dict['charge'] = self.charge.to_dict()
        # override the default output from pydantic by calling `to_dict()` of wallet
        if self.wallet:
            _dict['wallet'] = self.wallet.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terminal
        if self.terminal:
            _dict['terminal'] = self.terminal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in labels (list)
        _items = []
        if self.labels:
            for _item_labels in self.labels:
                if _item_labels:
                    _items.append(_item_labels.to_dict())
            _dict['labels'] = _items
        # override the default output from pydantic by calling `to_dict()` of invocation
        if self.invocation:
            _dict['invocation'] = self.invocation.to_dict()
        # override the default output from pydantic by calling `to_dict()` of connector_configuration
        if self.connector_configuration:
            _dict['connectorConfiguration'] = self.connector_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of ChargeAttempt from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "language": obj.get("language"),
            "salesChannel": obj.get("salesChannel"),
            "createdOn": obj.get("createdOn"),
            "initializingTokenVersion": obj.get("initializingTokenVersion"),
            "tokenVersion": TokenVersion.from_dict(obj["tokenVersion"]) if obj.get("tokenVersion") is not None else None,
            "succeededOn": obj.get("succeededOn"),
            "id": obj.get("id"),
            "state": obj.get("state"),
            "linkedTransaction": obj.get("linkedTransaction"),
            "redirectionUrl": obj.get("redirectionUrl"),
            "charge": Charge.from_dict(obj["charge"]) if obj.get("charge") is not None else None,
            "wallet": WalletType.from_dict(obj["wallet"]) if obj.get("wallet") is not None else None,
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "timeZone": obj.get("timeZone"),
            "spaceViewId": obj.get("spaceViewId"),
            "terminal": PaymentTerminal.from_dict(obj["terminal"]) if obj.get("terminal") is not None else None,
            "userFailureMessage": obj.get("userFailureMessage"),
            "completionBehavior": obj.get("completionBehavior"),
            "version": obj.get("version"),
            "labels": [Label.from_dict(_item) for _item in obj["labels"]] if obj.get("labels") is not None else None,
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "timeoutOn": obj.get("timeoutOn"),
            "environment": obj.get("environment"),
            "invocation": ConnectorInvocation.from_dict(obj["invocation"]) if obj.get("invocation") is not None else None,
            "connectorConfiguration": PaymentConnectorConfiguration.from_dict(obj["connectorConfiguration"]) if obj.get("connectorConfiguration") is not None else None,
            "nextUpdateOn": obj.get("nextUpdateOn"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "customersPresence": obj.get("customersPresence"),
            "failedOn": obj.get("failedOn")
        })
        return _obj


