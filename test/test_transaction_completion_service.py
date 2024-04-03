import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    get_transaction_create,
    TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
    FAKE_CARD_DATA
)

from wallee.api import (
    TransactionServiceApi,
    CardProcessingServiceApi,
    TransactionCompletionServiceApi,
)

from wallee.models import (
    TokenizationMode,
    TransactionCompletionBehavior,
    CustomersPresence,
    EntityQueryFilter,
    EntityQueryFilterType,
    CriteriaOperator,
    EntityQuery,
    TransactionState,
    TransactionCompletionState
)


class TransactionCompletionServiceTest(unittest.TestCase):
    """TransactionCompletionServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_completion_service = TransactionCompletionServiceApi(
            API_CONFIG)
        self.card_processing_service = CardProcessingServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    def __get_deferred_transaction_create(self):
        transaction_create = get_transaction_create()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED
        return transaction_create

    def test_complete_offline(self):
        """complete_offline() should complete transaction offline (completion is NOT forwarded to processor)"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=self.__get_deferred_transaction_create())

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

        transaction_completion = self.transaction_completion_service.complete_offline(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

    def test_complete_online(self):
        """complete_online() should complete transaction online (completion is forwarded to processor)"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=self.__get_deferred_transaction_create())

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

        transaction_completion = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

    def test_read(self):
        """read() should read details of transaction completion by id"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=self.__get_deferred_transaction_create())

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

        transaction_completion = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction_processed.id)

        transaction_read = self.transaction_completion_service.read(
            space_id=SPACE_ID, id=transaction_completion.id)

        self.assertIsNotNone(transaction_read, "Return data must not be None.")

        self.assertEqual(transaction_completion.id,
                         transaction_read.id, "Transaction ids must match", )

    def test_count(self):
        """count() should count transaction completions based on provided criteria"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=self.__get_deferred_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction_processed.id)

        criteria = EntityQueryFilter(
            field_name="id",
            value=transaction_completion.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS
        )

        count = self.transaction_completion_service.count(
            space_id=SPACE_ID, filter=criteria)

        self.assertEqual(1, count, "Count of completions should be 1", )

    def test_search(self):
        """search() should find transaction completions based on provided criteria"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=self.__get_deferred_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_online(
            space_id=SPACE_ID, id=transaction_processed.id)

        criteria = EntityQuery(
            filter=EntityQueryFilter(
                field_name="id",
                value=transaction_completion.id,
                type=EntityQueryFilterType.LEAF,
                operator=CriteriaOperator.EQUALS
            )
        )

        found_completions = self.transaction_completion_service.search(
            space_id=SPACE_ID, query=criteria)

        for compl in found_completions:
            self.assertEqual(transaction_completion.id,
                             compl.id, "Completion id should match")


if __name__ == "__main__":
    unittest.main(failfast=True)
