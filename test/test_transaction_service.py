# coding: utf-8

from __future__ import absolute_import

import unittest

from wallee import Configuration, ApiClient
from wallee.api import TransactionServiceApi
from wallee.models import LineItem, LineItemType, TransactionCreate, TransactionState, EntityQuery, \
    EntityQueryFilter, EntityQueryFilterType, CriteriaOperator


class TestTransactionService(unittest.TestCase):
    """TransactionServiceApi unit test stubs"""

    def setUp(self):
        self.space_id = 405
        self.transaction_service = TransactionServiceApi(api_client=ApiClient(configuration=Configuration(
            user_id=512,  # change this to your application, user's user_id
            api_secret='FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ='  # change this to your application user's key
        )))

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

    def test_count(self):
        """Test case for count"""
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        entity_query_filter = EntityQueryFilter(
            field_name='id',
            value=transaction_create.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS
        )
        transaction_count = self.transaction_service.count(space_id=self.space_id, filter=entity_query_filter)
        self.assertEqual(transaction_count, 1)

    def test_create(self):
        """Test case for create"""
        # send transaction to our API
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        self.assertIsInstance(transaction_create.state, TransactionState)

    def test_read(self):
        """Test case for read"""
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        transaction_read = self.transaction_service.read(space_id=self.space_id, id=transaction_create.id)
        self.assertIsInstance(transaction_read.state, TransactionState)

    def test_search(self):
        """Test case for search"""
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        entity_query_filter = EntityQueryFilter(
            field_name='id',
            value=transaction_create.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS
        )
        entity_query = EntityQuery(filter=entity_query_filter)
        transaction_search = self.transaction_service.search(space_id=self.space_id, query=entity_query)
        self.assertEqual(len(transaction_search), 1)
        for transaction in transaction_search:
            self.assertIsInstance(transaction.state, TransactionState)

    def test_update(self):
        """Test case for update"""
        transaction_create = self.transaction_service.create(space_id=self.space_id, transaction=self.transaction)
        transaction_create.language = 'en-US'
        transaction_update = self.transaction_service.update(space_id=self.space_id, entity=transaction_create)
        self.assertEqual(transaction_update.language, 'en-US')


if __name__ == '__main__':
    unittest.main(failfast=True)
