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


import unittest
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.primitives import hashes

from wallee.utils.encryption_util import EncryptionUtil
from wallee.wallee_sdk_exception import WalleeSdkException

class EncryptionUtilTest(unittest.TestCase):
    """wallee Encryption Util tests"""

    SIGNATURE_ALGORITHM = 'SHA256withECDSA'

    VALID_CONTENT_TO_VERIFY = (
    '{"entityId":11,"eventId":35,"listenerEntityId":1472041829003,"listenerEntityTechnicalName":"Transaction",'
    '"spaceId":1,"state":"PROCESSING","timestamp":"2023-12-19T13:43:35+0000","webhookListenerId":2}'
    )

    VALID_CONTENT_SIGNATURE = (
    "MEYCIQCTzbMrMsOAC6T57T9kQTb1iGZVg2R7n6pY9A4ML4P31gIhAIOoav8cG8x0jpRWQztqSJIC8gXWKq+4DuENEySvmMYf"
    )

    VALID_PUBLIC_KEY = (
    "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdWq7ZBGsjUzhBO3e6mzUBLpjpV3TQw1bL1rk3ocjn5C5qne7TY0OBBhiWgaPtWlvUcqASz903vtfeSTQma+SBA=="
    )

    def test_validation_should_pass_for_valid_content_signature_and_key(self):
        result = EncryptionUtil.is_content_valid(
            self.VALID_CONTENT_TO_VERIFY,
            self.VALID_CONTENT_SIGNATURE,
            self.VALID_PUBLIC_KEY,
            self.SIGNATURE_ALGORITHM
        )
        self.assertTrue(result)

    def test_validation_should_fail_for_bad_content(self):
        result = EncryptionUtil.is_content_valid(
            "ModifiedContent",
            self.VALID_CONTENT_SIGNATURE,
            self.VALID_PUBLIC_KEY,
            self.SIGNATURE_ALGORITHM
        )
        self.assertFalse(result)

    def test_validation_should_fail_for_bad_signature_format(self):
        result = EncryptionUtil.is_content_valid(
            self.VALID_CONTENT_TO_VERIFY,
            "InvalidModifiedSignature",
            self.VALID_PUBLIC_KEY,
            self.SIGNATURE_ALGORITHM
        )
        self.assertFalse(result)

    def test_validation_should_fail_for_bad_signature_base64_format(self):
        with self.assertRaises(WalleeSdkException ):
            EncryptionUtil.is_content_valid(
                self.VALID_CONTENT_TO_VERIFY,
                "MEYCIQCTzbMrMsOAC6T57T9kQTb1iGZVg2R7n6pY9A4ML4P31gIhAIOoav8cG8x0jpRWQztqSJIC8gXWKq",
                self.VALID_PUBLIC_KEY,
                self.SIGNATURE_ALGORITHM
            )

    def test_validation_should_fail_for_bad_public_key_format(self):
        with self.assertRaises(WalleeSdkException ):
            EncryptionUtil.is_content_valid(
                self.VALID_CONTENT_TO_VERIFY,
                self.VALID_CONTENT_SIGNATURE,
                "InvalidModifiedPublicKey",
                self.SIGNATURE_ALGORITHM
            )

    def test_validation_should_fail_for_bad_public_key_base64_format(self):
        with self.assertRaises(WalleeSdkException ):
            EncryptionUtil.is_content_valid(
                self.VALID_CONTENT_TO_VERIFY,
                self.VALID_CONTENT_SIGNATURE,
                "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdWq7ZBGsjUzhBO3e6mzUBLpjpV3TQw1bL1rk3ocjn5C5qne7TY0OBBhiWgaPtWlvUcqASz903vtfeSTQm",
                self.SIGNATURE_ALGORITHM
            )


    if __name__ == '__main__':
        unittest.main()
