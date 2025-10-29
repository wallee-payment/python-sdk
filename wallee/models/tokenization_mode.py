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
import json
from enum import Enum
from typing_extensions import Self


class TokenizationMode(str, Enum):
    """
    The tokenization mode controls how the tokenization of payment information is applied on the transaction.
    """

    """
    allowed enum values
    """
    FORCE_UPDATE = 'FORCE_UPDATE'
    FORCE_CREATION = 'FORCE_CREATION'
    FORCE_CREATION_WITH_ONE_CLICK_PAYMENT = 'FORCE_CREATION_WITH_ONE_CLICK_PAYMENT'
    ALLOW_ONE_CLICK_PAYMENT = 'ALLOW_ONE_CLICK_PAYMENT'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of TokenizationMode from a JSON string"""
        return cls(json.loads(json_str))


