import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    get_transaction_create,
)

from wallee.api import (
    TransactionServiceApi,
    TransactionPaymentPageServiceApi
)


class TransactionPaymentPageServiceTest(unittest.TestCase):
    """TransactionPaymentPageServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_payment_page_service = TransactionPaymentPageServiceApi(
            API_CONFIG)

    def tearDown(self):
        pass

    def test_payment_page_url(self):
        """payment_page_url() should create payment page URL"""

        transaction_create = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        url = self.transaction_payment_page_service.payment_page_url(
            space_id=SPACE_ID, id=transaction_create.id)

        self.assertTrue("securityToken" in url,
                        "URL must have proper format")


if __name__ == '__main__':
    unittest.main(failfast=True)
