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

from constants import API_CONFIG, SPACE_ID, MOCK_CARD_DATA
from utils import Utils
from wallee.service import TransactionsService
from wallee.models import SortingOrder, TransactionState

class TestQuerying(unittest.TestCase):
    """wallee querying features test using transactions service"""

    def setUp(self):
        self.transactions_service = TransactionsService(API_CONFIG)

        transaction_base = self.transactions_service.post_payment_transactions(
            SPACE_ID, Utils.get_transaction_create_payload()
        )
        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction_base.id, SPACE_ID, MOCK_CARD_DATA
        )
        self.transactions_service.post_payment_transactions_id_complete_online(
            authorized_transaction.id, SPACE_ID
        )
        self.transaction1 = self.transactions_service.get_payment_transactions_id(
            authorized_transaction.id, SPACE_ID
        )

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.currency = "USD"
        transaction_create.merchant_reference = "Transaction for querying test"

        self.transaction2 = self.transactions_service.post_payment_transactions(
            SPACE_ID, transaction_create
        )

    def test_search_with_limit_should_return_correct_amount_of_items(self):
        """
        Transaction search with limit parameter set to 2 items.
        """

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=2, offset=0, order="", query=""
        )
        self.assertEqual(len(response.data), 2, "Response should contain 2 items (as limited)")

    def test_search_with_offset_should_return_correct_response(self):
        """
        Transaction search with offset parameter.
        Search selects 2 items, offset is set to 1.
        Response should contain 1 item with the higher transaction ID.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = f"id:{self.transaction1.id} OR id:{self.transaction2.id}"
        higher_id = max(self.transaction1.id, self.transaction2.id)

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=2, offset=1, order="id:ASC", query=query
        )

        self.assertEqual(response.data[0].id, higher_id, "Response offset should be correct")

    def test_search_with_before_parameter_should_return_correct_responses(self):
        """
        Transaction search using the 'before' parameter.
        Ensures transactions with IDs less than the upper bound are returned.
        """

        self.assertIsNotNone(self.transaction1, "First transaction must be initialized for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction must be initialized for this test")

        upper_id = max(self.transaction1.id, self.transaction2.id)
        lower_id = min(self.transaction1.id, self.transaction2.id)

        response = self.transactions_service.get_payment_transactions(
            SPACE_ID, before=upper_id, expand=list(), limit=10, order=SortingOrder.ASC
        )

        self.assertIsNotNone(response.data, "Response data should not be null")
        self.assertTrue(
            any(t.id == lower_id for t in response.data),
            f"Response should contain transaction with ID: {lower_id}"
        )

    def test_fetch_with_search_query_should_return_list_with_valid_items(self):
        """
        Transaction search made with query. Response should contain 2 items.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = f"id:{self.transaction1.id} OR id:{self.transaction2.id}"

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=4, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(len(response.data), 2, "Response should contain only 2 items")

    def test_fetch_with_search_query_with_quotes_should_return_list_with_valid_items(self):
        """
        Transaction search with a query containing quotes. Response should contain 1 item.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = f'merchantReference:"Transaction for querying test" AND id:{self.transaction2.id}'

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=4, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertNotEqual(len(response.data), 0, "Response should contain more than 0 items")
        self.assertEqual(len(response.data), 1, "Response should contain 1 item")

    def test_fetch_with_query_with_contains_clause_should_return_list_with_valid_items(self):
        """
        Transaction search using 'contains' clause in query. Response should contain valid items.
        """

        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = "merchantReference:~querying"

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=2, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertNotEqual(len(response.data), 0, "Response should contain more than 0 items")

    def test_fetch_with_query_with_grouping_should_return_list_with_valid_items(self):
        """
        Transaction search using a grouped query clause. Response should contain 1 item.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = f"id:{self.transaction1.id} AND (currency:EUR OR currency:CHF)"

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=4, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertEqual(len(response.data), 1, "Response should contain only 1 item")

    def test_fetch_with_query_with_range_should_return_list_with_valid_items(self):
        """
        Transaction search using range clause. Response should contain transaction with expected ID.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")

        query = f"id:>{self.transaction1.id - 2} id:<={self.transaction1.id + 2}"

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=8, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertTrue(
            any(t.id == self.transaction1.id for t in response.data),
            "Transaction with expected ID should be found"
        )

    def test_fetch_with_query_with_negation_should_return_list_with_valid_items(self):
        """
        Transaction search using negation in query.
        Response should not contain the transaction with the excluded ID.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")

        query = (
            f"id:>{self.transaction1.id - 2} id:<={self.transaction1.id + 2} "
            f"AND -id:{self.transaction1.id}"
        )

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, expand=list(), limit=8, offset=0, order="id:ASC", query=query
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertFalse(
            any(t.id == self.transaction1.id for t in response.data),
            "Transaction with excluded ID should not be present"
        )

    def test_query_with_is_null_constraint_should_return_valid_item(self):
        """
        Transaction search made with query which has isNull constraint.
        Response should contain 1 item.
        """

        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        query = f"id:{self.transaction2.id} AND paymentConnectorConfiguration:*"

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, set(), 4, 0, "id:ASC", query
        )

        self.assertIsNotNone(response, "Response should be present")
        self.assertIsNotNone(response.data)
        self.assertEqual(1, len(response.data), "Response should contain only 1 item")

    def test_search_with_desc_sorting_should_return_sorted_response(self):
        """
        Transaction search made with order clause.
        Items in response should be in descending order.
        """

        self.assertIsNotNone(self.transaction1, "First transaction should be present for this test")
        self.assertIsNotNone(self.transaction2, "Second transaction should be present for this test")

        response = self.transactions_service.get_payment_transactions_search(
            SPACE_ID, set(), 4, 0, "id:DESC", ""
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data)
        self.assertGreaterEqual(len(response.data), 2, "Response should contain at least two transactions")

        first_id = response.data[0].id
        last_id = response.data[-1].id

        self.assertIsNotNone(first_id, "First transaction ID should not be None")
        self.assertIsNotNone(last_id, "Last transaction ID should not be None")

        difference = first_id - last_id

        self.assertGreater(difference, 0, "Response should be sorted descending. First ID should be greater than last ID.")

    def test_fetch_with_no_expanding_should_return_collapsed_response(self):
        """
        Gets transaction with no expand parameters.
        Checks if response does not contain any data which should be present only when expand is used.
        Example: group id should be present, but group state should be null.
        """

        self.assertIsNotNone(self.transaction1, "Transaction should be present for this test")

        response = self.transactions_service.get_payment_transactions_id(
            self.transaction1.id, SPACE_ID, set()
        )

        self.assertIsNotNone(response.group, "Group always should be present")
        self.assertIsNotNone(response.group.id, "Id always should be present")

        self.assertIsNone(response.group.state, "Group state should be null when response collapsed")
        self.assertIsNone(response.group.version, "Group version should be null when response collapsed")

    def test_fetch_with_expanding_should_return_expanded_response(self):
        """
        Gets transaction with expand parameters.
        Checks if response contains data which should be present when expand parameter is enabled.
        Example: group id and group state, version
        """

        self.assertIsNotNone(self.transaction1, "Transaction should be present for this test")
        self.assertEqual(TransactionState.FULFILL, self.transaction1.state,
                        "Transaction state should be FULFILLED for this test")

        expand_set = {"group", "paymentConnectorConfiguration"}

        response = self.transactions_service.get_payment_transactions_id(
            self.transaction1.id, SPACE_ID, expand_set
        )

        self.assertIsNotNone(response.group, "Group always should be present")
        self.assertIsNotNone(response.group.id, "Group id always should be present")

        self.assertIsNotNone(response.group.state, "Group state should be present when response expanded")
        self.assertIsNotNone(response.group.version, "Group version should be present when response expanded")

        self.assertIsNotNone(response.payment_connector_configuration)
        self.assertIsNotNone(response.payment_connector_configuration.processor_configuration,
                            "Both items in expand set should be expanded")

    def test_fetch_with_nested_expanding_should_return_expanded_response(self):
        """
        Gets transaction with nested expand parameter.
        Checks if response contains data related to parent item and to child item.
        Example: paymentConnectorConfiguration - parent item and processorConfiguration - child item.
        """

        self.assertIsNotNone(self.transaction1, "Transaction should be present for this test")
        self.assertEqual(TransactionState.FULFILL, self.transaction1.state,
                        "Transaction state should be FULFILLED for this test")

        expand_set = {"paymentConnectorConfiguration.processorConfiguration"}

        response = self.transactions_service.get_payment_transactions_id(
            self.transaction1.id, SPACE_ID, expand_set
        )

        self.assertIsNotNone(response.payment_connector_configuration)
        self.assertIsNotNone(response.payment_connector_configuration.processor_configuration)
        self.assertIsNotNone(
            response.payment_connector_configuration.processor_configuration.linked_space_id,
            "Items in nested response should be present"
        )
