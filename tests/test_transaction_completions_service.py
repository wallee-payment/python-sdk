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
from wallee.service import TransactionsService, TransactionCompletionsService
from wallee.models import TransactionState

class TestTransactionCompletionsService(unittest.TestCase):
    """wallee transaction completions service tests"""

    def setUp(self):
        self.transaction_completions_service = TransactionCompletionsService(API_CONFIG)
        self.transactions_service = TransactionsService(API_CONFIG)

    def test_read_should_return_completed_transaction_data(self):
        """
        Transaction completion read should return valid data.
        IDs of transaction linked to transaction completion and initial transaction should match.
        """

        transaction = self._create(Utils.get_transaction_create_payload())

        processed_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.assertEqual(
            processed_transaction.state,
            TransactionState.FULFILL,
            "State must be FULFILL"
        )

        transaction_completion = self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        read_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            transaction_completion.linked_transaction,
            read_transaction.id,
            "Transaction IDs must match"
        )


    def _create(self, transaction_create):
        """
        Helper method to create a transaction.

        Args:
            transaction_create: The transaction creation payload.

        Returns:
            Transaction: The created transaction.
        """
        return self.transactions_service.post_payment_transactions(
            SPACE_ID, transaction_create
        )
