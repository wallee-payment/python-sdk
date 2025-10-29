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


from enum import Enum

class ErrorCode(Enum):
    """
    The error code represents a potential error which may be thrown by the SDK.

    Error Code Ranges:
      - 1000 - 1999: Client-side errors - typically due to invalid input (e.g., malformed headers, bad keys).
      - 2000 - 2999: Server-side errors - typically due to incorrect data provided by the server.
      - 404: Not Found - used when the endpoint returns an empty response.
    """
    # 403
    UNKNOWN_WEBHOOK_ENCRYPTION_PUBLIC_KEY = (404, "Unknown webhook signature public key")

    # 1000 - 1999
    WEBHOOK_ENCRYPTION_GENERAL_ERROR = (1000, "General webhook encryption error")
    INVALID_WEBHOOK_ENCRYPTION_PUBLIC_KEY = (1001, "Invalid webhook signature public key")
    INVALID_WEBHOOK_ENCRYPTION_HEADER_FORMAT = (1002, "Invalid webhook signature header")
    UNSUPPORTED_WEBHOOK_ENCRYPTION_ALGORYTHM = (1003, "Unsupported webhook signature algorithm")
    UNKNOWN_WEBHOOK_ENCRYPTION_PROVIDER = (1004, "Unknown webhook encryption provider")
    WEBHOOK_ENCRYPTION_VERIFIER_INIT_ERROR = (1005, "Encryption verifier initialization error")
    WEBHOOK_ENCRYPTION_VERIFIER_CONTENT_UPDATE_ERROR = (1006, "Error during content update in encryption verifier")
    WEBHOOK_ENCRYPTION_SIGNATURE_VERIFICATION_FAILED = (1007, "Encryption signature verification failed")
    INVALID_WEBHOOK_ENCRYPTION_CONTENT_SIGNATURE = (1008, "Invalid webhook content signature")

    # 2000 - 2999
    MISSING_WEBHOOK_ENCRYPTION_ALGORYTHM = (2000, "Missing webhook signature algorithm value")

    def __init__(self, code, description):
        self._code = code
        self._description = description

    @property
    def code(self):
        return self._code

    @property
    def description(self):
        return self._description

    def __str__(self):
        return f"{self.code}: {self.description}"