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

from constants import API_CONFIG, SPACE_ID, MOCK_CARD_DATA, TEST_CUSTOMER_ID, TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID
from utils import Utils
from wallee.service import TransactionsService, TokensService
from wallee.models import ( TransactionState,
                            TransactionCompletionState,
                            TokenizationMode,
                            CustomersPresence,
                            TransactionVoidState,
                            TransactionCompletionBehavior,
                            TransactionCompletionDetails,
                            TransactionPending,
                            TokenCreate,
                            CreationEntityState,
                            TokenUpdate,
                            TokenizedCardDataCreate,
                            TokenizedCardRequest,
                            TerminalReceiptFormat,
                            LineItemCreate)
from wallee import ApiException

class TestTransactionsService(unittest.TestCase):
    """wallee transactions service tests"""

    def setUp(self):
        self.tokens_service = TokensService(API_CONFIG)
        self.transactions_service = TransactionsService(API_CONFIG)
        self.INTEGRATION_MODE = "payment_page"


    def test_create_and_find_pending_transaction(self):
        """
        Creates a new transaction.

        Verifies that:
        - Transaction state is PENDING
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        found = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.PENDING,
            transaction.state,
            "Transaction state must be PENDING"
        )
        self.assertEqual(
            transaction.merchant_reference,
            found.merchant_reference,
            "Merchant reference should match."
        )

    def test_confirm_should_make_transaction_confirmed(self):
        """
        Confirms a pending transaction.

        Verifies that:
        - Transaction state is CONFIRMED
        - Transaction entity version is correctly incremented
        - Merchant reference is correctly updated
        """

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.merchant_reference = "Test Initial Confirm"
        created = self.create(transaction_create)

        transaction_pending = TransactionPending(version= 2)
        transaction_pending.merchant_reference = "Test Confirm"

        confirmed = self.transactions_service.post_payment_transactions_id_confirm(
            created.id, SPACE_ID, transaction_pending
        )

        self.assertEqual(
            TransactionState.CONFIRMED,
            confirmed.state,
            "Transaction state must be CONFIRMED"
        )
        self.assertEqual(3, confirmed.version, "Version should match.")
        self.assertEqual(
            transaction_pending.merchant_reference,
            confirmed.merchant_reference,
            "Merchant reference should match."
        )
    def test_process_deferred_transaction_should_make_transaction_authorized(self):
        """
        Processes a deferred transaction.

        Verifies that:
        - Transaction state is AUTHORIZED
        """

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction = self.create(transaction_create)

        processed = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.assertEqual(
            TransactionState.AUTHORIZED,
            processed.state,
            "Transaction state must be AUTHORIZED"
        )

    def test_process_via_charge_flow_should_make_transaction_processing(self):
        """
        Processes a transaction via charge flow.

        Verifies that:
        - Transaction state is PROCESSING
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        processing_transaction = self.transactions_service.post_payment_transactions_id_charge_flow_apply(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.PROCESSING,
            processing_transaction.state,
            "Transaction state must be PROCESSING"
        )

    def test_cancel_charge_flow_should_make_transaction_failed(self):
        """
        Processes and cancels a transaction via charge flow.

        Verifies that:
        - Initially, transaction state is PROCESSING
        - After cancellation, transaction state is FAILED
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        processing_transaction = self.transactions_service.post_payment_transactions_id_charge_flow_apply(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.PROCESSING,
            processing_transaction.state,
            "Transaction state must be PROCESSING"
        )

        failed_transaction = self.transactions_service.post_payment_transactions_id_charge_flow_cancel(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.FAILED,
            failed_transaction.state,
            "Transaction state must be FAILED"
        )

    def test_fetch_payment_page_url_should_return_valid_url(self):
        """
        Processes a transaction and retrieves payment page URL.

        Verifies that:
        - Retrieved URL contains space ID
        - Retrieved URL contains transaction ID
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        processing_transaction = self.transactions_service.post_payment_transactions_id_charge_flow_apply(
            transaction.id, SPACE_ID
        )

        url = self.transactions_service.get_payment_transactions_id_payment_page_url(
            transaction.id, SPACE_ID
        )

        self.assertIn(f"/s/{SPACE_ID}", url, "Space id should be present in url")
        self.assertIn("securityToken=", url, "Security token should be present in url")
        self.assertIn(str(processing_transaction.id), url, "Transaction id should be present in url")

    def test_fetch_charge_flow_url_should_return_valid_url(self):
        """
        Processes a transaction via charge flow and retrieves payment page URL.

        Verifies that:
        - Transaction state is PROCESSING
        - Retrieved URL contains space ID
        - Retrieved URL contains transaction ID
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        processing_transaction = self.transactions_service.post_payment_transactions_id_charge_flow_apply(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.PROCESSING,
            processing_transaction.state,
            "Transaction state must be PROCESSING"
        )

        url = self.transactions_service.get_payment_transactions_id_charge_flow_payment_page_url(
            processing_transaction.id, SPACE_ID
        )

        self.assertIn(str(SPACE_ID), url, "Url must contain space id")
        self.assertIn(str(processing_transaction.id), url, "Url must contain transaction id")
        self.assertIn("securityToken=", url, "Url must contain security token")

    def test_complete_online_should_make_transaction_completion_state_successful(self):
        """
        Authorizes and completes a transaction online using card details.

        Verifies that:
        - Transaction completion state is SUCCESSFUL
        - Transaction state is FULFILL
        """

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_IMMEDIATELY

        transaction = self.create(transaction_create)

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        processed_transaction = self.transactions_service.post_payment_transactions_id_complete_online(
            authorized_transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            processed_transaction.state,
            "Transaction completion state must be SUCCESSFUL"
        )

        completed_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.FULFILL,
            completed_transaction.state,
            "Transaction state must be FULFILLED"
        )

    def test_complete_online_partially_should_make_transaction_completion_state_successful(self):
        """
        Authorizes and completes a transaction online partially using card details.

        Verifies that:
        - Transaction completion state is SUCCESSFUL
        - Transaction state is FULFILL
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        tcd = TransactionCompletionDetails()
        tcd.external_id = str(uuid.uuid4())

        processed_transaction = self.transactions_service.post_payment_transactions_id_complete_partially_online(
            authorized_transaction.id, SPACE_ID, tcd
        )

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            processed_transaction.state,
            "Transaction completion state must be SUCCESSFUL"
        )

        completed_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.FULFILL,
            completed_transaction.state,
            "Transaction state must be FULFILLED"
        )



    def test_void_transaction_online_should_return_voided_transaction(self):
        """
        Authorizes and voids a transaction online.

        Verifies that:
        - Transaction void state is SUCCESSFUL
        - Transaction state is VOIDED
        """

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction = self.create(transaction_create)

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.assertEqual(
            TransactionState.AUTHORIZED,
            authorized_transaction.state,
            "Transaction state should be AUTHORIZED"
        )

        expand = {"transaction"}

        transaction_void = self.transactions_service.post_payment_transactions_id_void_online(
            authorized_transaction.id, SPACE_ID, expand
        )

        self.assertEqual(
            TransactionVoidState.SUCCESSFUL,
            transaction_void.state,
            "Transaction void state should be SUCCESSFUL"
        )

        self.assertIsNotNone(transaction_void.transaction)

        self.assertEqual(
            TransactionState.VOIDED,
            transaction_void.transaction.state,
            "Transaction state should be VOIDED"
        )


    def test_check_if_possible_to_create_token_for_fulfilled_transaction(self):
        """
        Creates, authorizes and completes a transaction.

        Verifies that:
        - It's possible to create a transaction token for the fulfilled transaction
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        fulfilled_transaction_completion = self.transactions_service.post_payment_transactions_id_complete_online(
            authorized_transaction.id, SPACE_ID
        )

        fulfilled_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionState.FULFILL,
            fulfilled_transaction.state,
            "Transaction state must be FULFILL"
        )

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            fulfilled_transaction_completion.state,
            "Transaction completion state must be SUCCESSFUL"
        )

        self.assertTrue(
            self.transactions_service.get_payment_transactions_id_check_token_creation_possible(
                fulfilled_transaction.id, SPACE_ID
            ),
            "Should be possible to create token for successful transaction"
        )

    def test_check_if_possible_to_create_token_for_voided_transaction(self):
        """
        Creates, authorizes and voids a transaction.

        Verifies that:
        - It's NOT possible to create a transaction token for the voided transaction
        """

        transaction_create = Utils.get_transaction_create_payload()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction = self.create(transaction_create)

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.assertEqual(
            TransactionState.AUTHORIZED,
            authorized_transaction.state,
            "Transaction state should be AUTHORIZED"
        )

        transaction_void = self.transactions_service.post_payment_transactions_id_void_online(
            authorized_transaction.id, SPACE_ID
        )

        voided_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        self.assertEqual(
            TransactionVoidState.SUCCESSFUL,
            transaction_void.state,
            "Transaction void state should be SUCCESSFUL"
        )

        self.assertEqual(
            TransactionState.VOIDED,
            voided_transaction.state,
            "Transaction state should be VOIDED"
        )

        self.assertTrue(
            self.transactions_service.get_payment_transactions_id_check_token_creation_possible(
                voided_transaction.id, SPACE_ID
            ),
            "Should be not possible to create token for voided transaction"
        )

    def test_create_transaction_credentials_should_create_transaction_token(self):
        """
        Creates transaction token for a transaction.

        Verifies that:
        - Token contains space ID
        - Token contains transaction ID
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        credentials = self.get_credentials(transaction.id)

        self.assertTrue(
            credentials.startswith(str(SPACE_ID)),
            "Transaction credentials token should have valid format"
        )
        self.assertIsNotNone(transaction.id)
        self.assertTrue(
            str(transaction.id) in credentials,
            "Transaction credentials token should contain transaction id"
        )

    def test_fetch_iframe_url_should_return_valid_url(self):
        """
        Gets IFrame payment URL for transaction.

        Verifies that:
        - URL contains space ID
        - URL contains transaction ID
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        iframe_url = self.transactions_service.get_payment_transactions_id_iframe_javascript_url(
            transaction.id, SPACE_ID
        )

        self.assertTrue(
            str(SPACE_ID) in iframe_url,
            "IFrame JavaScript URL should contain space id"
        )

        self.assertTrue(
            str(transaction.id) in iframe_url,
            "IFrame JavaScript URL should contain transaction id"
        )

    def test_fetch_lightbox_url_should_return_valid_url(self):
        """
        Gets Lightbox payment URL for transaction.

        Verifies that:
        - URL contains space ID
        - URL contains transaction ID
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        lightbox_javascript_url = self.transactions_service.get_payment_transactions_id_lightbox_javascript_url(
            transaction.id, SPACE_ID
        )

        self.assertTrue(
            str(SPACE_ID) in lightbox_javascript_url,
            "Lightbox URL should contain space id"
        )

        self.assertTrue(
            str(transaction.id) in lightbox_javascript_url,
            "Lightbox URL should contain transaction id"
        )

    def test_fetch_invoice_should_return_pdf_file(self):
        """
        Creates, authorizes, completes transaction and gets invoice file.

        - Creates, authorizes and completes transaction
        - Gets transaction invoice file
        Verifies that:
            - File title contains "invoice"
            - File mime type is PDF
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        fulfilled_transaction_completion = self.transactions_service.post_payment_transactions_id_complete_online(
            authorized_transaction.id, SPACE_ID
        )

        fulfilled_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        invoice = self.transactions_service.get_payment_transactions_id_invoice_document(
            fulfilled_transaction.id, SPACE_ID
        )

        self.assertIsNotNone(invoice.title)
        self.assertTrue(
            "invoice" in invoice.title.lower(), "Invoice title should be present"
        )

        self.assertIsNotNone(invoice.mime_type)
        self.assertTrue(
            "pdf" in invoice.mime_type.lower(), "Invoice mimetype should be pdf"
        )

    def test_fetch_package_slip_should_return_pdf_file(self):
        """
        Creates, authorizes, completes transaction and gets packing slip.

        - Creates, authorizes and completes transaction
        - Gets transaction packing slip
        Verifies that:
            - File title contains "packing slip"
            - File mime type is PDF
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        authorized_transaction = self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        fulfilled_transaction_completion = self.transactions_service.post_payment_transactions_id_complete_online(
            authorized_transaction.id, SPACE_ID
        )

        fulfilled_transaction = self.transactions_service.get_payment_transactions_id(
            transaction.id, SPACE_ID
        )

        packing_slip = self.transactions_service.get_payment_transactions_id_packing_slip_document(
            fulfilled_transaction.id, SPACE_ID
        )

        self.assertIsNotNone(packing_slip.title)
        self.assertTrue(
            "packing slip" in packing_slip.title.lower(),
            "Packing slip title should be present"
        )

        self.assertIsNotNone(packing_slip.mime_type)
        self.assertTrue(
            "pdf" in packing_slip.mime_type.lower(),
            "Packing slip mimetype should be pdf"
        )

    def test_fetch_payment_methods_by_id_should_return_available_payment_methods(self):
        """
        Creates transaction and gets payment methods configuration.

        - Creates transaction
        - Gets payment methods configuration
        Verifies that:
            - Payment methods are present
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        method_configuration_list_response = self.transactions_service.get_payment_transactions_id_payment_method_configurations(
            transaction.id, self.INTEGRATION_MODE, SPACE_ID
        )

        self.assertIsNotNone(
            method_configuration_list_response.data, "The payment method list should be present"
        )
        self.assertFalse(
            len(method_configuration_list_response.data) == 0,
            "Payment methods should be configured for a given transaction in test space"
        )

    def test_fetch_transaction_with_credentials_should_return_transaction(self):
        """
        Creates transaction and finds it by credentials.

        - Creates transaction and gets its credentials
        - Finds transaction by credentials
        Verifies that:
            - Transaction is present
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        credentials = self.transactions_service.get_payment_transactions_id_credentials(
            transaction.id, SPACE_ID
        )

        retrieved_transaction = self.transactions_service.get_payment_transactions_by_credentials_credentials(
            credentials, SPACE_ID
        )

        self.assertIsNotNone(retrieved_transaction, "Transaction must be present")

    def test_fetch_payment_methods_with_credentials_should_return_available_payment_methods(self):
        """
        Creates transaction and gets payment methods configuration by credentials.

        - Creates transaction and gets its credentials
        - Gets payment methods configuration by credentials
        Verifies that:
            - Payment methods are present
        """

        transaction = self.create(Utils.get_transaction_create_payload())
        credentials = self.get_credentials(transaction.id)

        method_config_response = self.transactions_service.get_payment_transactions_by_credentials_credentials_payment_method_configurations(
            credentials, self.INTEGRATION_MODE, SPACE_ID
        )

        self.assertIsNotNone(
            method_config_response.data, "The payment method list should be present."
        )
        self.assertTrue(
            method_config_response.data,
            "Payment methods should be configured for a given transaction in test space"
        )

    def test_export_transactions_should_return_file(self):
        """
        Creates and exports a transaction.

        Verifies that:
            - Export file exists
        """

        transaction = self.create(Utils.get_transaction_create_payload())
        self.assertIsNotNone(transaction.id)

        fields = ["id"]
        export_data = self.transactions_service.get_payment_transactions_export(
            SPACE_ID, fields, 1, 0, order="id:ASC", query=f"id:{transaction.id}"
        )

        self.assertIsInstance(export_data, bytes)
        self.assertGreater(len(export_data), 0, "Exported data should be empty")

    def test_fetch_with_credentials_with_given_bad_credentials_should_fail(self):
        """
        Gets transaction by invalid credentials.

        - Attempts to retrieve a transaction using invalid credentials
        Verifies that:
        - Operation fails as expected
        """

        with self.assertRaises(ApiException, msg="Bad token should error response"):
            self.transactions_service.get_payment_transactions_by_credentials_credentials(
                "bad_credentials", SPACE_ID
            )

    def test_update_should_change_transaction_data(self):
        """
        Creates and updates a transaction.

        - Creates a new transaction
        - Updates it with new data
        Verifies that:
            - Update was successful
            - Version was incremented correctly
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        update = TransactionPending(version=2, language="en-GB")
        updated_transaction = self.transactions_service.patch_payment_transactions_id(
            transaction.id, SPACE_ID, update
        )

        self.assertEqual("en-GB", updated_transaction.language)
        self.assertEqual(
            transaction.merchant_reference,
            updated_transaction.merchant_reference,
            "Merchant reference should match."
        )
        self.assertEqual(2, updated_transaction.version, "Version should match")

    def test_process_one_click_token_and_redirect_with_credentials_should_return_payment_url(self):
        """
        Tests one-click token flow: creation, update, usage.

        - Creates token
        - Updates token settings (enabling one click payment)
        - Creates transaction with linked token
        - Processes and completes transaction
        - Creates new transaction and completes it using token
        """

        token_create = TokenCreate(externalId=str(uuid.uuid4()))
        token_create.state = CreationEntityState.ACTIVE
        token_create.token_reference = "testtoken"
        token_create.customer_id = TEST_CUSTOMER_ID
        token_create.customer_email_address = "test@domain.com"

        token = self.tokens_service.post_payment_tokens(SPACE_ID, token_create)

        self.assertIsNotNone(token.version)

        token_update = TokenUpdate(enabledForOneClickPayment=True, version=token.version)

        updated_token = self.tokens_service.patch_payment_tokens_id(token.id, SPACE_ID, token_update)

        transaction1 = self.tokens_service.post_payment_tokens_id_create_transaction_for_token_update(
            token.id, SPACE_ID
        )

        line_item = LineItemCreate(
            name="Red T-Shirt",
            unique_id="5412",
            type="PRODUCT",
            quantity=1,
            amount_including_tax=29.95,
            sku="red-t-shirt-789"
        )

        transaction1_pending = TransactionPending(
            lineItems=[line_item],
            version=2,
            currency="CHF"
        )

        self.transactions_service.patch_payment_transactions_id(
            transaction1.id, SPACE_ID, transaction1_pending
        )

        self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction1.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.transactions_service.post_payment_transactions_id_complete_online(
            transaction1.id, SPACE_ID
        )

        transaction2_create = Utils.get_transaction_create_payload()
        transaction2_create.customer_id = TEST_CUSTOMER_ID
        transaction2_create.tokenization_mode = TokenizationMode.FORCE_CREATION_WITH_ONE_CLICK_PAYMENT
        transaction2_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction2_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction2 = self.create(transaction2_create)

        credentials1 = self.get_credentials(transaction1.id)
        credentials2 = self.get_credentials(transaction2.id)

        url = self.transactions_service.post_payment_transactions_by_credentials_credentials_one_click_tokens_id_process(
            credentials2, updated_token.id, SPACE_ID
        )

        self.assertIsNotNone(url, "Url should not be none")
        self.assertNotEqual(url, "", "Url should not be empty")

        read_transaction2 = self.transactions_service.get_payment_transactions_id(transaction2.id, SPACE_ID)

        self.assertNotEqual(read_transaction2.state, TransactionState.FAILED, "Transaction state should not be FAILED")
        self.assertNotEqual(read_transaction2.state, TransactionState.PENDING, "Transaction state should not be PENDING")

        completed_transaction1 = self.transactions_service.post_payment_transactions_id_complete_online(
            transaction1.id, SPACE_ID
        )

        self.assertEqual(completed_transaction1.state, TransactionCompletionState.SUCCESSFUL, "State must be SUCCESSFUL")

    def test_process_transaction_via_token_should_process_transaction(self):
        """
        Processes transaction via token

        - Creates token
        - Creates transaction with linked token
        - Processes and completes transaction
        - Creates new transaction and completes it using token
        """

        line_item = LineItemCreate(
            name="Red T-Shirt",
            unique_id="5412",
            type="PRODUCT",
            quantity=1,
            amount_including_tax=29.95,
            sku="red-t-shirt-789"
        )

        token_create = TokenCreate(externalId=str(uuid.uuid4()))
        token_create.state = CreationEntityState.ACTIVE
        token_create.token_reference = "testtoken"
        token_create.customer_email_address = TEST_CUSTOMER_ID
        token_create.customer_email_address = "test@domain.com"

        token = self.tokens_service.post_payment_tokens(SPACE_ID, token_create)

        transaction = self.tokens_service.post_payment_tokens_id_create_transaction_for_token_update(
            token.id, SPACE_ID
        )

        transaction1_pending = TransactionPending(
            lineItems = [line_item],
            version=2,
            currency="CHF"
        )

        self.transactions_service.patch_payment_transactions_id(
            transaction.id, SPACE_ID, transaction1_pending
        )

        self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        transaction2 = self.create(Utils.get_transaction_create_payload())

        transaction_pending = TransactionPending(
            token=token.id,
            version=transaction2.version,
            currency="CHF",
            lineItems=[line_item]
        )

        updated_transaction = self.transactions_service.patch_payment_transactions_id(
            transaction2.id, SPACE_ID, transaction_pending
        )

        charge = self.transactions_service.post_payment_transactions_id_process_with_token(
            updated_transaction.id, SPACE_ID
        )

        self.assertEqual(charge.state, TransactionCompletionState.SUCCESSFUL, "Charge state must be SUCCESSFUL")

        read_transaction = self.transactions_service.get_payment_transactions_id(transaction2.id, SPACE_ID)
        self.assertEqual(read_transaction.token.id, token.id, "Tokens id should match")
        self.assertEqual(read_transaction.state, TransactionState.FULFILL, "Transaction state must be FULFILLED")

    def test_process_without_user_interaction_should_process_transaction_properly(self):
        """
        Verifies non-interactive transaction processing.

        - Processes a transaction without user interaction
        Verifies that:
            - Transaction reaches the AUTHORIZED state
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        processed = self.transactions_service.post_payment_transactions_id_process_without_interaction(
            transaction.id, SPACE_ID
        )

        self.assertEqual(processed.id, transaction.id, "Transaction ids must match")
        self.assertEqual(processed.state, TransactionState.PROCESSING, "Transaction state should be PROCESSING")

    def test_fetch_one_click_token_should_return_response_without_exception(self):
        """
        Retrieves tokens by transaction credentials.

        - Creates a new transaction
        - Attempts to retrieve one-click tokens
        Verifies that:
            - Response data is present
        """

        transaction = self.create(Utils.get_transaction_create_payload())
        credentials = self.get_credentials(transaction.id)

        response = self.transactions_service.get_payment_transactions_by_credentials_credentials_one_click_tokens(
            credentials, SPACE_ID
        )

        self.assertIsNotNone(response)
        self.assertIsNotNone(response.data, "Token data should not be null")

    def test_process_transaction_with_three_d_secure_should_fulfill_transaction(self):
        """
        Processes transaction with 3-D security

        - Creates a new transaction
        - Processes transaction with 3-D security
        Verifies that:
            - Returned url contains space id
            - Returned url contains securityToken
            - Transaction state is fulfilled
        """

        transaction = self.create(Utils.get_transaction_create_payload())
        tokenized_card_data_create = TokenizedCardDataCreate(primaryAccountNumber=MOCK_CARD_DATA.card_data.primary_account_number)
        tokenized_card_data_create.expiry_date = MOCK_CARD_DATA.card_data.expiry_date

        tcr = TokenizedCardRequest(cardData=tokenized_card_data_create)
        tcr.payment_method_configuration = TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID

        url = self.transactions_service.post_payment_transactions_id_process_card_details_threed(
            transaction.id, SPACE_ID, tcr
        )

        processed = self.transactions_service.get_payment_transactions_id(transaction.id, SPACE_ID)

        self.assertIsNotNone(url, "Url should not be null")
        self.assertNotEqual(url, "", "Url should not be empty")
        self.assertNotEqual(processed.state, TransactionState.FAILED, "Transaction state should not be FAILED")
        self.assertNotEqual(processed.state, TransactionState.PENDING, "Transaction state should not be PENDING")

    def test_fetch_mobile_sdk_url_by_credentials_should_return_valid_url(self):
        """
        Gets mobile sdk url by credentials

        - Creates a new transaction
        - Gets mobile sdk url
        Verifies that:
            - Returned url contains space id
            - Returned url contains securityToken
        """

        transaction = self.create(Utils.get_transaction_create_payload())
        credentials = self.get_credentials(transaction.id)

        url = self.transactions_service.get_payment_transactions_by_credentials_credentials_mobile_sdk_url(
            credentials, SPACE_ID
        )

        self.assertIn(f"/s/{SPACE_ID}", url, "Space id should be present in url")
        self.assertIn("securityToken=", url, "Security token should be present in url")

    def test_fetch_terminal_receipts_should_return_valid_terminal_receipts_list(self):
        """
        Gets all terminal receipts for transaction.

        Verifies that:
            - List of terminal receipts is empty (as they were not created)
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        receipt_response = self.transactions_service.get_payment_transactions_id_terminal_receipts(
            transaction.id, TerminalReceiptFormat.TXT, 200, SPACE_ID
        )

        self.assertIsNotNone(receipt_response, "Response should be present")
        self.assertEqual(len(receipt_response.data), 0, "Response size should be 0 as no terminal receipts created for this transaction")

    def test_update_charge_flow_recipient_should_not_throw_exception(self):
        """
        Updates charge flow recipient for processing transaction

        Verifies that:
            - Operation was made without exceptions
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        self.transactions_service.post_payment_transactions_id_charge_flow_apply(
            transaction.id, SPACE_ID
        )

        try:
            self.transactions_service.post_payment_transactions_id_charge_flow_update_recipient(
                transaction.id, 1453447675844, "test2@domain.com", SPACE_ID
            )
        except Exception:
            self.fail("ApiException should not be thrown when updating recipient")

    def test_fetch_line_items_version_should_return_latest_line_items_version(self):
        """
        Gets last version of line items list

        - Creates a new transaction
        - Gets line items
        Verifies that:
            - Amount is correct
            - Version is correct
            - Transaction id is same in transaction and charge
        """

        transaction = self.create(Utils.get_transaction_create_payload())

        self.transactions_service.post_payment_transactions_id_process_card_details(
            transaction.id, SPACE_ID, MOCK_CARD_DATA
        )

        self.transactions_service.post_payment_transactions_id_complete_online(
            transaction.id, SPACE_ID
        )

        line_items = self.transactions_service.get_payment_transactions_id_latest_line_item_version(
            transaction.id, SPACE_ID
        )

        self.assertEqual(line_items.version, 1, "Line items version should be 1")
        self.assertEqual(line_items.amount, 29.95, "Line items amount should be 29.95")
        self.assertEqual(line_items.linked_transaction, transaction.id, "Transaction ids should match")

    def create(self, transaction_create):
        return self.transactions_service.post_payment_transactions(SPACE_ID, transaction_create)

    def get_credentials(self, transaction_id):
        return self.transactions_service.get_payment_transactions_id_credentials(transaction_id, SPACE_ID)
