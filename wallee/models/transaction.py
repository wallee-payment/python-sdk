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
from pydantic import BaseModel, ConfigDict, Field, StrictBool, StrictFloat, StrictInt, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional, Union
from typing_extensions import Annotated
from wallee.models.address import Address
from wallee.models.charge_attempt_environment import ChargeAttemptEnvironment
from wallee.models.customers_presence import CustomersPresence
from wallee.models.environment import Environment
from wallee.models.failure_reason import FailureReason
from wallee.models.line_item import LineItem
from wallee.models.payment_connector_configuration import PaymentConnectorConfiguration
from wallee.models.payment_terminal import PaymentTerminal
from wallee.models.token import Token
from wallee.models.tokenization_mode import TokenizationMode
from wallee.models.transaction_completion_behavior import TransactionCompletionBehavior
from wallee.models.transaction_environment_selection_strategy import TransactionEnvironmentSelectionStrategy
from wallee.models.transaction_group import TransactionGroup
from wallee.models.transaction_state import TransactionState
from wallee.models.transaction_user_interface_type import TransactionUserInterfaceType
from typing import Optional, Set
from typing_extensions import Self

class Transaction(BaseModel):
    """
    Transaction
    """ # noqa: E501
    parent: Optional[Transaction] = None
    total_settled_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount that was settled, in the transaction's currency.", alias="totalSettledAmount")
    device_session_identifier: Optional[Annotated[str, Field(min_length=10, strict=True, max_length=40)]] = Field(default=None, description="Allows to link the transaction to the data collected from the customer's device.", alias="deviceSessionIdentifier")
    processing_on: Optional[datetime] = Field(default=None, description="The date and time when the processing of the transaction was started.", alias="processingOn")
    invoice_merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the invoice.", alias="invoiceMerchantReference")
    language: Optional[StrictStr] = Field(default=None, description="The language that is linked to the object.")
    confirmed_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction was created.", alias="confirmedOn")
    line_items: Optional[List[LineItem]] = Field(default=None, description="The line items purchased by the customer.", alias="lineItems")
    accept_language_header: Optional[StrictStr] = Field(default=None, description="The 'Accept Language' header of the customer's web browser.", alias="acceptLanguageHeader")
    java_enabled: Optional[StrictBool] = Field(default=None, description="Whether Java is enabled on the customer's web browser.", alias="javaEnabled")
    confirmed_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the transaction was confirmed by.", alias="confirmedBy")
    payment_connector_configuration: Optional[PaymentConnectorConfiguration] = Field(default=None, alias="paymentConnectorConfiguration")
    id: Optional[StrictInt] = Field(default=None, description="A unique identifier for the object.")
    state: Optional[TransactionState] = None
    window_width: Optional[StrictStr] = Field(default=None, description="The window width of the customer's web browser.", alias="windowWidth")
    allowed_payment_method_configurations: Optional[List[StrictInt]] = Field(default=None, description="The payment method configurations that can be used to authorize the transaction.", alias="allowedPaymentMethodConfigurations")
    group: Optional[TransactionGroup] = None
    charge_retry_enabled: Optional[StrictBool] = Field(default=None, description="Whether the customer can make further payment attempts if the first one has failed. Default is true.", alias="chargeRetryEnabled")
    accept_header: Optional[StrictStr] = Field(default=None, description="The 'Accept' header of the customer's web browser.", alias="acceptHeader")
    user_agent_header: Optional[StrictStr] = Field(default=None, description="The 'User Agent' header of the customer's web browser.", alias="userAgentHeader")
    shipping_method: Optional[Annotated[str, Field(strict=True, max_length=200)]] = Field(default=None, description="The name of the shipping method used to ship the products.", alias="shippingMethod")
    planned_purge_date: Optional[datetime] = Field(default=None, description="The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.", alias="plannedPurgeDate")
    success_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=2000)]] = Field(default=None, description="The URL to redirect the customer back to after they successfully authenticated their payment.", alias="successUrl")
    time_zone: Optional[StrictStr] = Field(default=None, description="The customer's time zone, which affects how dates and times are formatted when communicating with the customer.", alias="timeZone")
    space_view_id: Optional[StrictInt] = Field(default=None, description="The ID of the space view this object is linked to.", alias="spaceViewId")
    user_failure_message: Optional[StrictStr] = Field(default=None, description="The message that can be displayed to the customer explaining why the transaction failed, in the customer's language.", alias="userFailureMessage")
    completion_behavior: Optional[TransactionCompletionBehavior] = Field(default=None, alias="completionBehavior")
    version: Optional[StrictInt] = Field(default=None, description="The version is used for optimistic locking and incremented whenever the object is updated.")
    internet_protocol_address_country: Optional[StrictStr] = Field(default=None, description="The country determined from the IP address of the customer's device.", alias="internetProtocolAddressCountry")
    linked_space_id: Optional[StrictInt] = Field(default=None, description="The ID of the space this object belongs to.", alias="linkedSpaceId")
    delivery_decision_made_on: Optional[datetime] = Field(default=None, description="This date and time when the decision was made as to whether the order should be shipped.", alias="deliveryDecisionMadeOn")
    authorization_environment: Optional[ChargeAttemptEnvironment] = Field(default=None, alias="authorizationEnvironment")
    auto_confirmation_enabled: Optional[StrictBool] = Field(default=None, description="Whether the transaction can be confirmed automatically or whether this must be done explicitly via the API. Default is true.", alias="autoConfirmationEnabled")
    failure_reason: Optional[FailureReason] = Field(default=None, alias="failureReason")
    total_applied_fees: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total of all fees charged, in the transaction's currency.", alias="totalAppliedFees")
    customers_presence: Optional[CustomersPresence] = Field(default=None, alias="customersPresence")
    failed_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction failed.", alias="failedOn")
    refunded_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount that was refunded, in the transaction's currency.", alias="refundedAmount")
    authorization_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The sum of all line item prices including taxes in the transaction's currency.", alias="authorizationAmount")
    screen_width: Optional[StrictStr] = Field(default=None, description="The screen width of the customer's web browser.", alias="screenWidth")
    environment_selection_strategy: Optional[TransactionEnvironmentSelectionStrategy] = Field(default=None, alias="environmentSelectionStrategy")
    customer_email_address: Optional[Annotated[str, Field(strict=True, max_length=254)]] = Field(default=None, description="The customer's email address.", alias="customerEmailAddress")
    window_height: Optional[StrictStr] = Field(default=None, description="The window height of the customer's web browser.", alias="windowHeight")
    tokenization_mode: Optional[TokenizationMode] = Field(default=None, alias="tokenizationMode")
    authorization_timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction must be authorized, otherwise it will canceled.", alias="authorizationTimeoutOn")
    allowed_payment_method_brands: Optional[List[StrictInt]] = Field(default=None, description="The payment method brands that can be used to authorize the transaction.", alias="allowedPaymentMethodBrands")
    created_on: Optional[datetime] = Field(default=None, description="The date and time when the object was created.", alias="createdOn")
    meta_data: Optional[Dict[str, StrictStr]] = Field(default=None, description="Allow to store additional information about the object.", alias="metaData")
    emails_disabled: Optional[StrictBool] = Field(default=None, description="Whether email sending is deactivated for the transaction. Default is false.", alias="emailsDisabled")
    user_interface_type: Optional[TransactionUserInterfaceType] = Field(default=None, alias="userInterfaceType")
    customer_id: Optional[StrictStr] = Field(default=None, description="The unique identifier of the customer in the external system.", alias="customerId")
    currency: Optional[StrictStr] = Field(default=None, description="The three-letter code (ISO 4217 format) of the transaction's currency.")
    merchant_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The merchant's reference used to identify the transaction.", alias="merchantReference")
    authorization_sales_channel: Optional[StrictInt] = Field(default=None, description="The sales channel through which the transaction was placed.", alias="authorizationSalesChannel")
    years_to_keep: Optional[StrictInt] = Field(default=None, description="The number of years the transaction is kept after its authorization.", alias="yearsToKeep")
    completed_amount: Optional[Union[StrictFloat, StrictInt]] = Field(default=None, description="The total amount that was completed, in the transaction's currency.", alias="completedAmount")
    screen_height: Optional[StrictStr] = Field(default=None, description="The screen height of the customer's web browser.", alias="screenHeight")
    internet_protocol_address: Optional[StrictStr] = Field(default=None, description="The IP address of the customer's device.", alias="internetProtocolAddress")
    terminal: Optional[PaymentTerminal] = None
    end_of_life: Optional[datetime] = Field(default=None, description="The date and time when the transaction reaches its end of live. No further actions can be carried out at this time.", alias="endOfLife")
    token: Optional[Token] = None
    environment: Optional[Environment] = None
    screen_color_depth: Optional[StrictStr] = Field(default=None, description="The screen color depth of the customer's web browser.", alias="screenColorDepth")
    created_by: Optional[StrictInt] = Field(default=None, description="The ID of the user the transaction was created by.", alias="createdBy")
    completed_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction was completed.", alias="completedOn")
    completion_timeout_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction is completed automatically.", alias="completionTimeoutOn")
    shipping_address: Optional[Address] = Field(default=None, alias="shippingAddress")
    billing_address: Optional[Address] = Field(default=None, alias="billingAddress")
    authorized_on: Optional[datetime] = Field(default=None, description="The date and time when the transaction was authorized.", alias="authorizedOn")
    failed_url: Optional[Annotated[str, Field(min_length=9, strict=True, max_length=2000)]] = Field(default=None, description="The URL to redirect the customer back to after they canceled or failed to authenticated their payment.", alias="failedUrl")
    __properties: ClassVar[List[str]] = ["parent", "totalSettledAmount", "deviceSessionIdentifier", "processingOn", "invoiceMerchantReference", "language", "confirmedOn", "lineItems", "acceptLanguageHeader", "javaEnabled", "confirmedBy", "paymentConnectorConfiguration", "id", "state", "windowWidth", "allowedPaymentMethodConfigurations", "group", "chargeRetryEnabled", "acceptHeader", "userAgentHeader", "shippingMethod", "plannedPurgeDate", "successUrl", "timeZone", "spaceViewId", "userFailureMessage", "completionBehavior", "version", "internetProtocolAddressCountry", "linkedSpaceId", "deliveryDecisionMadeOn", "authorizationEnvironment", "autoConfirmationEnabled", "failureReason", "totalAppliedFees", "customersPresence", "failedOn", "refundedAmount", "authorizationAmount", "screenWidth", "environmentSelectionStrategy", "customerEmailAddress", "windowHeight", "tokenizationMode", "authorizationTimeoutOn", "allowedPaymentMethodBrands", "createdOn", "metaData", "emailsDisabled", "userInterfaceType", "customerId", "currency", "merchantReference", "authorizationSalesChannel", "yearsToKeep", "completedAmount", "screenHeight", "internetProtocolAddress", "terminal", "endOfLife", "token", "environment", "screenColorDepth", "createdBy", "completedOn", "completionTimeoutOn", "shippingAddress", "billingAddress", "authorizedOn", "failedUrl"]

    @field_validator('device_session_identifier')
    def device_session_identifier_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([a-zA-Z0-9_-])*", value):
            raise ValueError(r"must validate the regular expression /([a-zA-Z0-9_-])*/")
        return value

    @field_validator('invoice_merchant_reference')
    def invoice_merchant_reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
        return value

    @field_validator('merchant_reference')
    def merchant_reference_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"[	\x20-\x7e]*", value):
            raise ValueError(r"must validate the regular expression /[	\x20-\x7e]*/")
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
        """Create an instance of Transaction from a JSON string"""
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
            "total_settled_amount",
            "device_session_identifier",
            "processing_on",
            "invoice_merchant_reference",
            "language",
            "confirmed_on",
            "line_items",
            "accept_language_header",
            "java_enabled",
            "confirmed_by",
            "id",
            "window_width",
            "allowed_payment_method_configurations",
            "charge_retry_enabled",
            "accept_header",
            "user_agent_header",
            "shipping_method",
            "planned_purge_date",
            "success_url",
            "time_zone",
            "space_view_id",
            "user_failure_message",
            "version",
            "internet_protocol_address_country",
            "linked_space_id",
            "delivery_decision_made_on",
            "auto_confirmation_enabled",
            "total_applied_fees",
            "failed_on",
            "refunded_amount",
            "authorization_amount",
            "screen_width",
            "customer_email_address",
            "window_height",
            "authorization_timeout_on",
            "allowed_payment_method_brands",
            "created_on",
            "meta_data",
            "emails_disabled",
            "customer_id",
            "currency",
            "merchant_reference",
            "authorization_sales_channel",
            "years_to_keep",
            "completed_amount",
            "screen_height",
            "internet_protocol_address",
            "end_of_life",
            "screen_color_depth",
            "created_by",
            "completed_on",
            "completion_timeout_on",
            "authorized_on",
            "failed_url",
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        # override the default output from pydantic by calling `to_dict()` of parent
        if self.parent:
            _dict['parent'] = self.parent.to_dict()
        # override the default output from pydantic by calling `to_dict()` of each item in line_items (list)
        _items = []
        if self.line_items:
            for _item_line_items in self.line_items:
                if _item_line_items:
                    _items.append(_item_line_items.to_dict())
            _dict['lineItems'] = _items
        # override the default output from pydantic by calling `to_dict()` of payment_connector_configuration
        if self.payment_connector_configuration:
            _dict['paymentConnectorConfiguration'] = self.payment_connector_configuration.to_dict()
        # override the default output from pydantic by calling `to_dict()` of group
        if self.group:
            _dict['group'] = self.group.to_dict()
        # override the default output from pydantic by calling `to_dict()` of failure_reason
        if self.failure_reason:
            _dict['failureReason'] = self.failure_reason.to_dict()
        # override the default output from pydantic by calling `to_dict()` of terminal
        if self.terminal:
            _dict['terminal'] = self.terminal.to_dict()
        # override the default output from pydantic by calling `to_dict()` of token
        if self.token:
            _dict['token'] = self.token.to_dict()
        # override the default output from pydantic by calling `to_dict()` of shipping_address
        if self.shipping_address:
            _dict['shippingAddress'] = self.shipping_address.to_dict()
        # override the default output from pydantic by calling `to_dict()` of billing_address
        if self.billing_address:
            _dict['billingAddress'] = self.billing_address.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of Transaction from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "parent": Transaction.from_dict(obj["parent"]) if obj.get("parent") is not None else None,
            "totalSettledAmount": obj.get("totalSettledAmount"),
            "deviceSessionIdentifier": obj.get("deviceSessionIdentifier"),
            "processingOn": obj.get("processingOn"),
            "invoiceMerchantReference": obj.get("invoiceMerchantReference"),
            "language": obj.get("language"),
            "confirmedOn": obj.get("confirmedOn"),
            "lineItems": [LineItem.from_dict(_item) for _item in obj["lineItems"]] if obj.get("lineItems") is not None else None,
            "acceptLanguageHeader": obj.get("acceptLanguageHeader"),
            "javaEnabled": obj.get("javaEnabled"),
            "confirmedBy": obj.get("confirmedBy"),
            "paymentConnectorConfiguration": PaymentConnectorConfiguration.from_dict(obj["paymentConnectorConfiguration"]) if obj.get("paymentConnectorConfiguration") is not None else None,
            "id": obj.get("id"),
            "state": obj.get("state"),
            "windowWidth": obj.get("windowWidth"),
            "allowedPaymentMethodConfigurations": obj.get("allowedPaymentMethodConfigurations"),
            "group": TransactionGroup.from_dict(obj["group"]) if obj.get("group") is not None else None,
            "chargeRetryEnabled": obj.get("chargeRetryEnabled"),
            "acceptHeader": obj.get("acceptHeader"),
            "userAgentHeader": obj.get("userAgentHeader"),
            "shippingMethod": obj.get("shippingMethod"),
            "plannedPurgeDate": obj.get("plannedPurgeDate"),
            "successUrl": obj.get("successUrl"),
            "timeZone": obj.get("timeZone"),
            "spaceViewId": obj.get("spaceViewId"),
            "userFailureMessage": obj.get("userFailureMessage"),
            "completionBehavior": obj.get("completionBehavior"),
            "version": obj.get("version"),
            "internetProtocolAddressCountry": obj.get("internetProtocolAddressCountry"),
            "linkedSpaceId": obj.get("linkedSpaceId"),
            "deliveryDecisionMadeOn": obj.get("deliveryDecisionMadeOn"),
            "authorizationEnvironment": obj.get("authorizationEnvironment"),
            "autoConfirmationEnabled": obj.get("autoConfirmationEnabled"),
            "failureReason": FailureReason.from_dict(obj["failureReason"]) if obj.get("failureReason") is not None else None,
            "totalAppliedFees": obj.get("totalAppliedFees"),
            "customersPresence": obj.get("customersPresence"),
            "failedOn": obj.get("failedOn"),
            "refundedAmount": obj.get("refundedAmount"),
            "authorizationAmount": obj.get("authorizationAmount"),
            "screenWidth": obj.get("screenWidth"),
            "environmentSelectionStrategy": obj.get("environmentSelectionStrategy"),
            "customerEmailAddress": obj.get("customerEmailAddress"),
            "windowHeight": obj.get("windowHeight"),
            "tokenizationMode": obj.get("tokenizationMode"),
            "authorizationTimeoutOn": obj.get("authorizationTimeoutOn"),
            "allowedPaymentMethodBrands": obj.get("allowedPaymentMethodBrands"),
            "createdOn": obj.get("createdOn"),
            "metaData": obj.get("metaData"),
            "emailsDisabled": obj.get("emailsDisabled"),
            "userInterfaceType": obj.get("userInterfaceType"),
            "customerId": obj.get("customerId"),
            "currency": obj.get("currency"),
            "merchantReference": obj.get("merchantReference"),
            "authorizationSalesChannel": obj.get("authorizationSalesChannel"),
            "yearsToKeep": obj.get("yearsToKeep"),
            "completedAmount": obj.get("completedAmount"),
            "screenHeight": obj.get("screenHeight"),
            "internetProtocolAddress": obj.get("internetProtocolAddress"),
            "terminal": PaymentTerminal.from_dict(obj["terminal"]) if obj.get("terminal") is not None else None,
            "endOfLife": obj.get("endOfLife"),
            "token": Token.from_dict(obj["token"]) if obj.get("token") is not None else None,
            "environment": obj.get("environment"),
            "screenColorDepth": obj.get("screenColorDepth"),
            "createdBy": obj.get("createdBy"),
            "completedOn": obj.get("completedOn"),
            "completionTimeoutOn": obj.get("completionTimeoutOn"),
            "shippingAddress": Address.from_dict(obj["shippingAddress"]) if obj.get("shippingAddress") is not None else None,
            "billingAddress": Address.from_dict(obj["billingAddress"]) if obj.get("billingAddress") is not None else None,
            "authorizedOn": obj.get("authorizedOn"),
            "failedUrl": obj.get("failedUrl")
        })
        return _obj

# TODO: Rewrite to not use raise_errors
Transaction.model_rebuild(raise_errors=False)

