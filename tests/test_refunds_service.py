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
import uuid

from constants import API_CONFIG, SPACE_ID, MOCK_CARD_DATA
from utils import Utils
from wallee.service import TransactionsService, RefundsService
from wallee.models import RefundCreate, RefundState, RefundType, TransactionCompletionState, TransactionState

class TestRefundsService(unittest.TestCase):
    """wallee refunds service tests"""

    def setUp(self):
        self.refunds_service = RefundsService(API_CONFIG)
        self.transactions_service = TransactionsService(API_CONFIG)

    def test_refund_of_completed_transaction_should_work(self):
        """
        Refund of fulfilled transaction should be created successfully.
        """

        transaction = self._create(Utils.get_transaction_create_payload())

        processed_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        transaction_completion = self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            transaction_completion.state,
            TransactionCompletionState.SUCCESSFUL,
            "Transaction completion state must be SUCCESSFUL"
        )

        read_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            read_transaction.state,
            TransactionState.FULFILL,
            "Transaction state must be FULFILL"
        )

        refund_create = self._get_refund_create(transaction)

        refund = self.refunds_service.post_payment_refunds(
            SPACE_ID, refund_create
        )

        self.assertEqual(
            refund.state,
            RefundState.SUCCESSFUL,
            "Refund state must be SUCCESSFUL"
        )

    def test_read_should_return_refund_data(self):
        """
        Refund read should return valid data.
        """

        transaction = self._create(Utils.get_transaction_create_payload())

        self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        refund_create = self._get_refund_create(transaction)

        refund = self.refunds_service.post_payment_refunds(
            SPACE_ID, refund_create
        )

        self.assertEqual(
            refund.state,
            RefundState.SUCCESSFUL,
            "Refund state must be SUCCESSFUL"
        )

        read_refund = self.refunds_service.get_payment_refunds_id(
            refund.id, SPACE_ID
        )

        self.assertEqual(
            refund.id, read_refund.id,
            "Refund ids should match"
        )

    def _get_refund_create(self, transaction):
        """
        Creates a RefundCreate payload for a given transaction.

        Args:
            transaction: The transaction to refund.

        Returns:
            RefundCreate: The refund payload.
        """
        return RefundCreate(
            transaction=transaction.id,
            type=RefundType.MERCHANT_INITIATED_ONLINE,
            external_id=str(uuid.uuid4()),
            amount=29.95
        )


    def _create(self, transaction_create):
        """
        Helper method to create a transaction.

        Args:
            transaction_create: The transaction payload.

        Returns:
            Transaction: The created transaction object.
        """
        return self.transactions_service.post_payment_transactions(
            SPACE_ID, transaction_create
        )
