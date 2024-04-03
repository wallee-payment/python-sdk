import base64
import binascii

from cryptography.exceptions import InvalidSignature
from cryptography.hazmat.primitives import serialization
from cryptography.hazmat.primitives.asymmetric import ec
from cryptography.hazmat.backends import default_backend
from cryptography.hazmat.primitives import hashes


class EncryptionUtil:
    @staticmethod
    def is_content_valid(content, signature, public_key, encryption_algorithm):
        algorithm_class = EncryptionUtil._get_algorithm_class(encryption_algorithm)
        if algorithm_class is None:
            raise ValueError(f"Unsupported algorithm: {encryption_algorithm}")

        try:
            signature = base64.b64decode(signature)
        except binascii.Error:
            raise ValueError("Invalid signature value format")

        try:
            public_key_bytes = base64.b64decode(public_key)
        except binascii.Error:
            raise ValueError("Invalid public key value format")

        public_key = serialization.load_der_public_key(public_key_bytes, backend=default_backend())

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
