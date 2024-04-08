import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    get_transaction_create,
    FAKE_CARD_DATA,
    TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
    TEST_CUSTOMER_ID,
)

from wallee.api import (
    TransactionServiceApi,
    CardProcessingServiceApi,
    TokenServiceApi,
    TransactionCompletionServiceApi,
)
from wallee.models import (
    TransactionState,
    EntityQuery,
    EntityQueryFilter,
    EntityQueryFilterType,
    CriteriaOperator,
    TokenizationMode,
    TransactionCompletionBehavior,
    CustomersPresence,
    TransactionCompletionState,
)
from wallee.rest import ApiException


class TransactionServiceTest(unittest.TestCase):
    """TransactionServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_completion_service = TransactionCompletionServiceApi(
            API_CONFIG)
        self.card_processing_service = CardProcessingServiceApi(API_CONFIG)
        self.token_service = TokenServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    def test_create(self):
        """create() should create transaction"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        self.assertEqual(
            TransactionState.PENDING, transaction.state, "State must be PENDING"
        )

    def test_confirm(self):
        """confirm() should mark transaction as confirmed"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_confirmed = self.transaction_service.confirm(
            space_id=SPACE_ID, transaction_model=transaction)

        self.assertEqual(
            TransactionState.CONFIRMED,
            transaction_confirmed.state,
            "State must be CONFIRMED",
        )

    def test_create_complete_deferred(self):
        """create() with COMPLETE_DEFERRED transaction behaviour should make transaction Authorized when we pay with card details"""

        transaction_create = get_transaction_create()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=transaction_create)
        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        self.assertEqual(
            TransactionState.AUTHORIZED,
            transaction_processed.state,
            "State must be AUTHORIZED",
        )

    def test_create_complete_immediately(self):
        """create() with COMPLETE_IMMEDIATELY transaction behaviour should make transaction Fulfilled when we pay with card details"""

        transaction_create = get_transaction_create()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_IMMEDIATELY

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=transaction_create)

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        self.assertEqual(TransactionState.FULFILL,
                         transaction_processed.state, "State must be FULFILL", )

    def test_count(self):
        """count() should count transactions matching given criteria"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        entity_query_filter = EntityQueryFilter(
            field_name="id",
            value=transaction.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS,
        )

        transaction_count = self.transaction_service.count(
            space_id=SPACE_ID, filter=entity_query_filter)

        self.assertEqual(1, transaction_count, "Transaction count should be 1")

    def test_create_transaction_credentials(self):
        """create_transaction_credentials() should create valid transaction credentials token"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        creds = self.transaction_service.create_transaction_credentials(
            space_id=SPACE_ID, id=transaction.id)

        self.assertTrue(creds.startswith(str(SPACE_ID)),
                        "Transaction credentials token should have valid format", )

    def test_fetch_payment_methods(self):
        """fetch_payment_methods() should fetch payment methods available for the transaction"""
        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        payment_methods = self.transaction_service.fetch_payment_methods(
            space_id=SPACE_ID,
            id=transaction.id,
            integration_mode="payment_page",
        )

        self.assertTrue(len(payment_methods) > 0,
                        "Payment methods should be configured for a given transaction in test space", )

    def test_read_not_found(self):
        """read_not_found() should read not found transaction as none"""

        NOT_FOUND_TRANSACTION_ID = 0

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=NOT_FOUND_TRANSACTION_ID)

        self.assertIsNone(transaction_read, "Return data must be None.")

    def test_read(self):
        """read() should read transaction details"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction.id)

        self.assertIsNotNone(transaction_read, "Return data must not be None.")

        self.assertEqual(transaction.id, transaction_read.id,
                         "Transaction ids should match")

        self.assertEqual(TransactionState.PENDING,
                         transaction_read.state, "State must be PENDING")

    def test_read_with_credentials_for_bad_creds(self):
        """read_with_credentials() should fail when credentials are bad"""

        try:
            self.transaction_service.read_with_credentials(
                credentials="invalid_token")
        except ApiException as ex:
            self.assertEqual(
                442,
                ex.status,
                "Bad token should produce 442 Unprocessable content HTTP status response",
            )

    def test_read_with_credentials(self):
        """read_with_credentials() should read transaction when valid credentials token is provided"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        creds = self.transaction_service.create_transaction_credentials(
            space_id=SPACE_ID, id=transaction.id)

        transaction_read = self.transaction_service.read_with_credentials(
            credentials=creds)

        self.assertIsNotNone(transaction_read, "Return data must not be None.")

        self.assertEqual(transaction.id, transaction_read.id,
                         "Transaction ids should match")

    def test_search(self):
        """search() should find transaction by id"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        entity_query_filter = EntityQueryFilter(
            field_name="id",
            value=transaction.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS,
        )
        entity_query = EntityQuery(filter=entity_query_filter)

        transactions = self.transaction_service.search(
            space_id=SPACE_ID, query=entity_query)

        self.assertEqual(1, len(transactions))
        for transaction_found in transactions:
            self.assertEqual(transaction.id, transaction_found.id)

    def test_update(self):
        """update() should successfully update existing transaction"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())
        transaction.language = "en-US"
        transaction_update = self.transaction_service.update(
            space_id=SPACE_ID, entity=transaction)
        self.assertEqual("en-US", transaction_update.language)

    def test_process_without_user_interaction(self):
        """process_without_user_interaction() should correctly process created transaction without need for user interaction"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_processed = self.transaction_service.process_without_user_interaction(
            space_id=SPACE_ID, id=transaction.id)

        self.assertEqual(
            transaction.id, transaction_processed.id, "Transaction ids must match"
        )

    def test_fetch_one_click_tokens_with_credentials_no_tokens(self):
        """fetch_one_click_tokens_with_credentials() should return one-click payment tokens (if any) for provided transaction"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        creds = self.transaction_service.create_transaction_credentials(
            space_id=SPACE_ID, id=transaction.id)

        tokens = self.transaction_service.fetch_one_click_tokens_with_credentials(
            creds)

        self.assertEqual(0, len(tokens), "Should be no tokens yet")

    def test_fetch_payment_methods_with_credentials(self):
        """fetch_payment_methods_with_credentials() should return payment methods (if any) for credentials"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        creds = self.transaction_service.create_transaction_credentials(
            space_id=SPACE_ID, id=transaction.id)

        methods = self.transaction_service.fetch_payment_methods_with_credentials(
            credentials=creds, integration_mode="payment_page")

        self.assertTrue(len(methods) > 0,
                        "Should have some payment methods set up")

    def test_process_one_click_token_and_redirect_with_credentials(self):
        """process_one_click_token_and_redirect_with_credentials() should create URL that can be used to authorize 2nd transaction after we have created token for 1st authorized transaction"""

        transaction1_create = get_transaction_create()
        transaction1_create.tokenization_mode = TokenizationMode.FORCE_CREATION_WITH_ONE_CLICK_PAYMENT

        transaction1_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction1_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        transaction1_create.customer_id = TEST_CUSTOMER_ID

        transaction1 = self.transaction_service.create(
            space_id=SPACE_ID, transaction=transaction1_create)

        transaction1_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction1.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        token = self.token_service.create_token(
            space_id=SPACE_ID, transaction_id=transaction1_processed.id)
        token.enabled_for_one_click_payment = True
        updated_token = self.token_service.update(
            space_id=SPACE_ID, entity=token
        )

        transaction2_create = get_transaction_create()
        transaction2_create.tokenization_mode = TokenizationMode.FORCE_CREATION_WITH_ONE_CLICK_PAYMENT
        transaction2_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction2_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED
        transaction2_create.customer_id = TEST_CUSTOMER_ID

        transaction2 = self.transaction_service.create(
            space_id=SPACE_ID, transaction=transaction2_create)
        creds2 = self.transaction_service.create_transaction_credentials(
            space_id=SPACE_ID, id=transaction2.id)
        payment_url2 = self.transaction_service.process_one_click_token_and_redirect_with_credentials(
            credentials=creds2, token_id=updated_token.id)

        self.assertTrue("securityToken" in payment_url2,
                        "URL must be of a proper format")

        transaction2_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction2.id)

        self.assertIsNotNone(transaction2_read, "Return data must not be None.")

        self.assertEqual(
            TransactionState.AUTHORIZED,
            transaction2_read.state,
            "State must be AUTHORIZED",
        )

        # cleanup - 2nd transaction
        transaction2_completed = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction2.id)

        self.assertEqual(TransactionCompletionState.SUCCESSFUL,
                         transaction2_completed.state, "State must be SUCCESSFUL", )

        # cleanup - 1st transaction
        transaction1_completed = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction1.id)

        self.assertEqual(TransactionCompletionState.SUCCESSFUL,
                         transaction1_completed.state, "State must be SUCCESSFUL", )

        self.token_service.delete(SPACE_ID, token.id)


if __name__ == "__main__":
    unittest.main(failfast=True)
