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

class SdkExceptionErrorCodes(Enum):
    """
    SDK Local Error Codes
    """
    # Unknown webhook signature public key
    UNKNOWN_WEBHOOK_ENCRYPTION_PUBLIC_KEY = "unknown_public_key"
    # General webhook encryption error
    WEBHOOK_ENCRYPTION_GENERAL_ERROR = "encryption_error"
    # Invalid webhook signature public key
    INVALID_WEBHOOK_ENCRYPTION_PUBLIC_KEY = "invalid_public_key"
    # Invalid webhook signature header
    INVALID_WEBHOOK_ENCRYPTION_HEADER_FORMAT = "invalid_webhook_header"
    # Unsupported webhook signature algorithm
    UNSUPPORTED_WEBHOOK_ENCRYPTION_ALGORYTHM = "unsupported_encryption_algorythm"
    # Unknown webhook encryption provider
    UNKNOWN_WEBHOOK_ENCRYPTION_PROVIDER = "unknown_encryption_provider"
    # Encryption verifier initialization error
    WEBHOOK_ENCRYPTION_VERIFIER_INIT_ERROR = "verifier_init_failure"
    # Error during content update in encryption verifier
    WEBHOOK_ENCRYPTION_VERIFIER_CONTENT_UPDATE_ERROR = "content_update_failure"
    # Encryption signature verification failed
    WEBHOOK_ENCRYPTION_SIGNATURE_VERIFICATION_FAILED = "signature_verification_failure"
    # Invalid webhook content signature
    INVALID_WEBHOOK_ENCRYPTION_CONTENT_SIGNATURE = "invalid_content_signature"
    # Missing webhook signature algorithm value
    MISSING_WEBHOOK_ENCRYPTION_ALGORYTHM = "missing_encryption_algorythm"

    def __init__(self, code):
        self._code = code

    @property
    def code(self):
        return self._code

    def matches(self, sdk_exception):
        """
        Checks if the given exception matches this error code.
        """
        return sdk_exception.code == self.code