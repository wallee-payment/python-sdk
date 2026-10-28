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

from pydantic import BaseModel, ConfigDict, Field
from typing import Any, ClassVar, Dict, List, Optional
from wallee.models.merchant_bank_details_dto import MerchantBankDetailsDto
from wallee.models.merchant_company_details_dto import MerchantCompanyDetailsDto
from wallee.models.merchant_contract_revenue_dto import MerchantContractRevenueDto
from wallee.models.merchant_ecommerce_details_dto import MerchantEcommerceDetailsDto
from wallee.models.merchant_payment_channels_dto import MerchantPaymentChannelsDto
from wallee.models.merchant_related_persons_dto import MerchantRelatedPersonsDto
from typing import Optional, Set
from typing_extensions import Self

class MerchantApplicationDataDto(BaseModel):
    """
    MerchantApplicationDataDto
    """ # noqa: E501
    related_persons: Optional[MerchantRelatedPersonsDto] = Field(default=None, alias="relatedPersons")
    bank_details: Optional[MerchantBankDetailsDto] = Field(default=None, alias="bankDetails")
    company_details: Optional[MerchantCompanyDetailsDto] = Field(default=None, alias="companyDetails")
    payment_channels: Optional[MerchantPaymentChannelsDto] = Field(default=None, alias="paymentChannels")
    contract_revenue: Optional[MerchantContractRevenueDto] = Field(default=None, alias="contractRevenue")
    ecommerce_details: Optional[MerchantEcommerceDetailsDto] = Field(default=None, alias="ecommerceDetails")
    __properties: ClassVar[List[str]] = ["relatedPersons", "bankDetails", "companyDetails", "paymentChannels", "contractRevenue", "ecommerceDetails"]

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
        """Create an instance of MerchantApplicationDataDto from a JSON string"""
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
        # override the default output from pydantic by calling `to_dict()` of related_persons
        if self.related_persons:
            _dict['relatedPersons'] = self.related_persons.to_dict()
        # override the default output from pydantic by calling `to_dict()` of bank_details
        if self.bank_details:
            _dict['bankDetails'] = self.bank_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of company_details
        if self.company_details:
            _dict['companyDetails'] = self.company_details.to_dict()
        # override the default output from pydantic by calling `to_dict()` of payment_channels
        if self.payment_channels:
            _dict['paymentChannels'] = self.payment_channels.to_dict()
        # override the default output from pydantic by calling `to_dict()` of contract_revenue
        if self.contract_revenue:
            _dict['contractRevenue'] = self.contract_revenue.to_dict()
        # override the default output from pydantic by calling `to_dict()` of ecommerce_details
        if self.ecommerce_details:
            _dict['ecommerceDetails'] = self.ecommerce_details.to_dict()
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of MerchantApplicationDataDto from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "relatedPersons": MerchantRelatedPersonsDto.from_dict(obj["relatedPersons"]) if obj.get("relatedPersons") is not None else None,
            "bankDetails": MerchantBankDetailsDto.from_dict(obj["bankDetails"]) if obj.get("bankDetails") is not None else None,
            "companyDetails": MerchantCompanyDetailsDto.from_dict(obj["companyDetails"]) if obj.get("companyDetails") is not None else None,
            "paymentChannels": MerchantPaymentChannelsDto.from_dict(obj["paymentChannels"]) if obj.get("paymentChannels") is not None else None,
            "contractRevenue": MerchantContractRevenueDto.from_dict(obj["contractRevenue"]) if obj.get("contractRevenue") is not None else None,
            "ecommerceDetails": MerchantEcommerceDetailsDto.from_dict(obj["ecommerceDetails"]) if obj.get("ecommerceDetails") is not None else None
        })
        return _obj


