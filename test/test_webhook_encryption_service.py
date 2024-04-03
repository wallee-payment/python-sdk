import unittest
from unittest.mock import patch

from constants import (
    API_CONFIG
)
from wallee.api import (
    WebhookEncryptionServiceApi
)
from wallee.models import (
    WebhookEncryptionPublicKey
)

CONTENT_TO_VERIFY = ('{"entityId":11,"eventId":35,"listenerEntityId":1472041829003,'
                     '"listenerEntityTechnicalName":"Transaction","spaceId":1,"state":"PROCESSING",'
                     '"timestamp":"2023-12-19T13:43:35+0000","webhookListenerId":2}')

SIGNATURE_HEADER = ("algorithm=SHA256withECDSA, keyId=ab3b774e-770e-4644-9b51-885d71f973e5, "
                    "signature=MEYCIQCTzbMrMsOAC6T57T9kQTb1iGZVg2R7n6pY9A4ML4P31gIhAIOoav8cG8x0jpRWQztqSJIC8gXWKq+4DuENEySvmMYf")

PUBLIC_KEY_ID = "ab3b774e-770e-4644-9b51-885d71f973e5"

VALID_ENCODED_PUBLIC_KEY = "MFkwEwYHKoZIzj0CAQYIKoZIzj0DAQcDQgAEdWq7ZBGsjUzhBO3e6mzUBLpjpV3TQw1bL1rk3ocjn5C5qne7TY0OBBhiWgaPtWlvUcqASz903vtfeSTQma+SBA=="


class WebhookEncryptionServiceTest(unittest.TestCase):
    """WebhookEncryptionServiceApi tests"""

    def setUp(self):
        self.webhook_encryption_service = WebhookEncryptionServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    @patch('wallee.api.WebhookEncryptionServiceApi.read')
    def test_validate_valid_content_and_signature(self, mock_webhook_encryption_service_read):
        """validate_valid_content_and_signature() should validate correct content and signature"""

        mock_webhook_encryption_service_read.return_value = (
            WebhookEncryptionPublicKey(id=1, public_key=VALID_ENCODED_PUBLIC_KEY))

        is_content_valid = self.webhook_encryption_service.is_content_valid(SIGNATURE_HEADER, CONTENT_TO_VERIFY)

        mock_webhook_encryption_service_read.assert_called_once()
        self.assertIsNotNone(is_content_valid, "Return webhook encryption validation marker must not be None.")
        self.assertTrue(is_content_valid, "The webhook encryption content and signature must be valid.")

    @patch('wallee.api.WebhookEncryptionServiceApi.read')
    def test_read_webhook_encryption_not_found(self, mock_webhook_encryption_service_read):
        """read_webhook_encryption_not_found() should fail when webhook encryption public key is none """

        mock_webhook_encryption_service_read.return_value = None

        with self.assertRaises(ValueError) as context:
            self.webhook_encryption_service.is_content_valid(SIGNATURE_HEADER, CONTENT_TO_VERIFY)

        self.assertEqual(str(context.exception), f"Could not find public key with id {PUBLIC_KEY_ID}")

        mock_webhook_encryption_service_read.assert_called_once()

    @patch('wallee.api.WebhookEncryptionServiceApi.read')
    def test_validate_invalid_signature_header(self, mock_webhook_encryption_service_read):
        """validate_invalid_signature_header() should fail when signature header is invalid """

        mock_webhook_encryption_service_read.return_value = (
            WebhookEncryptionPublicKey(id=1, public_key=VALID_ENCODED_PUBLIC_KEY))

        invalid_signature_header = "algorithm=SHA256withECDSA, keyId=ab3b774e-770e-4644-9b51-885d71f973e5"

        with self.assertRaises(ValueError) as context:
            self.webhook_encryption_service.is_content_valid(invalid_signature_header, CONTENT_TO_VERIFY)

        self.assertEqual(str(context.exception), "Invalid webhook signature header. Expected format: "
                                                 "'algorithm=<algorithm>, keyId=<keyId>, signature=<signature>'")


if __name__ == "__main__":
    unittest.main(failfast=True)
