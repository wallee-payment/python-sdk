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


class RefundPercentageRange(str, Enum):
    """
    RefundPercentageRange
    """

    """
    allowed enum values
    """
    ONE_TO_FIVE = 'ONE_TO_FIVE'
    FIVE_TO_TEN = 'FIVE_TO_TEN'
    TEN_TO_FIFTEEN = 'TEN_TO_FIFTEEN'
    FIFTEEN_TO_TWENTY = 'FIFTEEN_TO_TWENTY'
    TWENTY_TO_THIRTY = 'TWENTY_TO_THIRTY'
    THIRTY_TO_FORTY = 'THIRTY_TO_FORTY'
    FORTY_TO_FIFTY = 'FORTY_TO_FIFTY'
    OVER_FIFTY = 'OVER_FIFTY'

    @classmethod
    def from_json(cls, json_str: str) -> Self:
        """Create an instance of RefundPercentageRange from a JSON string"""
        return cls(json.loads(json_str))


