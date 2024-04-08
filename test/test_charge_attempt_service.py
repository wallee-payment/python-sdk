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
    ChargeAttemptServiceApi
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
)

class ChargeAttemptServiceTest(unittest.TestCase):
    """ChargeAttemptServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.card_processing_service = CardProcessingServiceApi(API_CONFIG)
        self.charge_attempt_service = ChargeAttemptServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    def test_search(self):
        """search() should find charge attempts by given criteria"""

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

        entity_query_filter = EntityQueryFilter(
            field_name="charge.transaction.id",
            value=transaction.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS,
        )
        entity_query = EntityQuery(filter=entity_query_filter)

        attempts_found = self.charge_attempt_service.search(
            space_id=SPACE_ID, query=entity_query)

        self.assertTrue(len(attempts_found) > 0)
        for attempt in attempts_found:
            self.assertEqual(transaction.id, attempt.linked_transaction)

    # TODO write more API tests


if __name__ == "__main__":
    unittest.main(failfast=True)
