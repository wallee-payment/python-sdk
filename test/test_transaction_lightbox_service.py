import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    get_transaction_create,
)

from wallee.api import (
    TransactionServiceApi,
    TransactionLightboxServiceApi
)


class TransactionLigthboxServiceTest(unittest.TestCase):
    """TransactionLigthboxServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_lightbox_service = TransactionLightboxServiceApi(
            API_CONFIG)

    def tearDown(self):
        pass

    def test_javascript_url(self):
        """javascript_url() should create URL for use in Lightbox checkout flow javascript"""

        transaction_create = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        url = self.transaction_lightbox_service.javascript_url(
            space_id=SPACE_ID, id=transaction_create.id)

        self.assertTrue("securityToken" in url,
                        "URL must have proper format")


if __name__ == '__main__':
    unittest.main(failfast=True)
