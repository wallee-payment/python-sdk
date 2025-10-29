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


import base64
import binascii

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes

from wallee.wallee_sdk_exception import WalleeSdkException
from wallee.error_code import ErrorCode


class EncryptionUtil:
    @staticmethod
    def is_content_valid(content, signature, public_key, encryption_algorithm):

        if not encryption_algorithm:
            raise WalleeSdkException(
                ErrorCode.MISSING_WEBHOOK_ENCRYPTION_ALGORYTHM,
                "Webhook signature algorithm was not provided"
            )

        algorithm_class = EncryptionUtil._get_algorithm_class(encryption_algorithm)
        if algorithm_class is None:
            raise WalleeSdkException(
                ErrorCode.UNSUPPORTED_WEBHOOK_ENCRYPTION_ALGORYTHM,
                f"Unsupported encryption algorithm: {encryption_algorithm}"
            )

        try:
            signature = base64.b64decode(signature)
        except binascii.Error:
            raise WalleeSdkException(
                ErrorCode.INVALID_WEBHOOK_ENCRYPTION_CONTENT_SIGNATURE,
                "Invalid signature value format"
            )

        try:
            public_key_bytes = base64.b64decode(public_key)
        except binascii.Error:
            raise WalleeSdkException(
                ErrorCode.INVALID_WEBHOOK_ENCRYPTION_PUBLIC_KEY,
                "Invalid public key value base64 format"
            )

        try:
            public_key = serialization.load_der_public_key(public_key_bytes, backend=default_backend())
        except (ValueError, binascii.Error) as e:
            raise WalleeSdkException(
                ErrorCode.INVALID_WEBHOOK_ENCRYPTION_PUBLIC_KEY,
                f"Invalid public key format: {str(e)}"
            )

        try:
            public_key.verify(
                signature,
                content.encode('utf-8'),
                algorithm_class(hashes.SHA256())
            )
            return True
        except InvalidSignature:
            return False

    @staticmethod
    def _get_algorithm_class(algorithm):
        switch = {
            'SHA256withECDSA': ec.ECDSA,
        }
        return switch.get(algorithm, None)
