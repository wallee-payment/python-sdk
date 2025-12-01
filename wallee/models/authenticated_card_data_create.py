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

from pydantic import BaseModel, ConfigDict, Field, StrictStr, field_validator
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from wallee.models.card_cryptogram_create import CardCryptogramCreate
from wallee.models.cardholder_authentication_create import CardholderAuthenticationCreate
from wallee.models.pan_type import PanType
from wallee.models.recurring_indicator import RecurringIndicator
from typing import Optional, Set
from typing_extensions import Self

class AuthenticatedCardDataCreate(BaseModel):
    """
    AuthenticatedCardDataCreate
    """ # noqa: E501
    expiry_date: Optional[Annotated[str, Field(strict=True)]] = Field(default=None, description="The expiry date of the card, indicating its validity period in yyyy-mm format (e.g., 2023-09).", alias="expiryDate")
    pan_type: Optional[PanType] = Field(default=None, alias="panType")
    card_holder_name: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="The name of the cardholder, as printed on the card, identifying the card owner.", alias="cardHolderName")
    card_verification_code: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=4)]] = Field(default=None, description="The security code used to validate the card during transactions.", alias="cardVerificationCode")
    primary_account_number: Annotated[str, Field(min_length=10, strict=True, max_length=30)] = Field(description="The card's primary account number (PAN), the unique identifier of the card.", alias="primaryAccountNumber")
    recurring_indicator: Optional[RecurringIndicator] = Field(default=None, alias="recurringIndicator")
    scheme_transaction_reference: Optional[Annotated[str, Field(strict=True, max_length=100)]] = Field(default=None, description="A reference specific to the card's transaction within its payment scheme.", alias="schemeTransactionReference")
    cardholder_authentication: Optional[CardholderAuthenticationCreate] = Field(default=None, alias="cardholderAuthentication")
    token_requestor_id: Optional[StrictStr] = Field(default=None, description="The token requestor identifier (TRID) identifies the entity requesting tokenization for a card transaction.", alias="tokenRequestorId")
    cryptogram: Optional[CardCryptogramCreate] = None
    __properties: ClassVar[List[str]] = ["expiryDate", "panType", "cardHolderName", "cardVerificationCode", "primaryAccountNumber", "recurringIndicator", "schemeTransactionReference", "cardholderAuthentication", "tokenRequestorId", "cryptogram"]

    @field_validator('expiry_date')
    def expiry_date_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"(\d{4})-(11|12|10|0[1-9])", value):
            raise ValueError(r"must validate the regular expression /(\d{4})-(11|12|10|0[1-9])/")
        return value

    @field_validator('card_verification_code')
    def card_verification_code_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if value is None:
            return value

        if not re.match(r"([0-9 ]+)", value):
            raise ValueError(r"must validate the regular expression /([0-9 ]+)/")
        return value

    @field_validator('primary_account_number')
    def primary_account_number_validate_regular_expression(cls, value):
        """Validates the regular expression"""
        if not re.match(r"([0-9 ]+)", value):
            raise ValueError(r"must validate the regular expression /([0-9 ]+)/")
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
        """Create an instance of AuthenticatedCardDataCreate from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of cardholder_authentication
        if self.cardholder_authentication:
            _dict['cardholderAuthentication'] = self.cardholder_authentication.to_dict()
        # override the default output from pydantic by calling `to_dict()` of cryptogram
        if self.cryptogram:
            _dict['cryptogram'] = self.cryptogram.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AuthenticatedCardDataCreate from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "expiryDate": obj.get("expiryDate"),
            "panType": obj.get("panType"),
            "cardHolderName": obj.get("cardHolderName"),
            "cardVerificationCode": obj.get("cardVerificationCode"),
            "primaryAccountNumber": obj.get("primaryAccountNumber"),
            "recurringIndicator": obj.get("recurringIndicator"),
            "schemeTransactionReference": obj.get("schemeTransactionReference"),
            "cardholderAuthentication": CardholderAuthenticationCreate.from_dict(obj["cardholderAuthentication"]) if obj.get("cardholderAuthentication") is not None else None,
            "tokenRequestorId": obj.get("tokenRequestorId"),
            "cryptogram": CardCryptogramCreate.from_dict(obj["cryptogram"]) if obj.get("cryptogram") is not None else None
        })
        return _obj


