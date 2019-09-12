# coding: utf-8

from __future__ import absolute_import

import unittest

from wallee import Configuration
from wallee.api import TransactionServiceApi, TransactionPaymentPageServiceApi
from wallee.models import LineItem, LineItemType, TransactionCreate


class TransactionPaymentPageServiceTest(unittest.TestCase):
    """TransactionPaymentPageService unit test stubs"""

    def setUp(self):
        self.space_id = 405
        config = Configuration(
            user_id=512,
            api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ='
        )
        self.transaction_service = TransactionServiceApi(configuration=config)
        self.transaction_payment_page_service = TransactionPaymentPageServiceApi(configuration=config)

        # create line item
        self.line_item = LineItem(
            name='Red T-Shirt',
            unique_id=5412,
            sku='red-t-shirt-123',
            quantity=1,
            amount_including_tax=3.50,
            type=LineItemType.PRODUCT
        )

        # create transaction model
        self.transaction = TransactionCreate(
            line_items=[self.line_item],
            auto_confirmation_enabled=True,
            currency='EUR',
        )

    def tearDown(self):
        pass

    def test_payment_page_url(self):
        """Test case for count"""
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        payment_page_url = self.transaction_payment_page_service.payment_page_url(space_id=self.space_id, id=transaction_create.id)
        self.assertRegex(payment_page_url, "http")

if __name__ == '__main__':
    unittest.main(failfast=True)
