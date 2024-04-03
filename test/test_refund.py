import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
    FAKE_CARD_DATA,
    get_transaction_create
)

from wallee.api import (
    TransactionServiceApi,
    CardProcessingServiceApi,
    TransactionCompletionServiceApi,
    RefundServiceApi
)

from wallee.models import (
    TransactionCompletionState,
    RefundCreate,
    RefundType,
    RefundState,
    EntityQuery,
    EntityQueryFilter,
    EntityQueryFilterType,
    CriteriaOperator
)


class RefundServiceTest(unittest.TestCase):
    """RefundServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_completion_service = TransactionCompletionServiceApi(
            API_CONFIG)
        self.card_processing_service = CardProcessingServiceApi(API_CONFIG)
        self.refund_service = RefundServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    def __get_refund_create(self, transaction):
        refund_create = RefundCreate(
            external_id=str(transaction.id),
            type=RefundType.MERCHANT_INITIATED_ONLINE,
            amount=transaction.authorization_amount,
            transaction=transaction.id,
            merchant_reference=transaction.merchant_reference
        )
        return refund_create

    def test_refund(self):
        """refund() should create a refund for transaction"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_offline(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction_processed.id)

        refund = self.refund_service.refund(
            space_id=SPACE_ID, refund=self.__get_refund_create(transaction_read))

        self.assertEqual(
            RefundState.SUCCESSFUL,
            refund.state,
            "State must be SUCCESSFUL",
        )

    def test_read_not_found(self):
        """read_not_found() should read not found refund as none"""

        NOT_FOUND_REFUND_ID = 0

        refund_read = self.refund_service.read(
            space_id=SPACE_ID, id=NOT_FOUND_REFUND_ID)

        self.assertIsNone(refund_read, "Return data must be None.")

    def test_read(self):
        """read() should fetch refund details"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_offline(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction_processed.id)

        refund = self.refund_service.refund(
            space_id=SPACE_ID, refund=self.__get_refund_create(transaction_read))

        self.assertEqual(
            RefundState.SUCCESSFUL,
            refund.state,
            "State must be SUCCESSFUL",
        )

        read_refund = self.refund_service.read(
            space_id=SPACE_ID, id=refund.id)

        self.assertIsNotNone(read_refund, "Return data must not be None.")

        self.assertEqual(
            refund.id,
            read_refund.id,
            "Refund ids must match",
        )

    def test_search(self):
        """search() should find a refund for a given criteria"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_offline(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction_processed.id)

        refund = self.refund_service.refund(
            space_id=SPACE_ID, refund=self.__get_refund_create(transaction_read))

        self.assertEqual(
            RefundState.SUCCESSFUL,
            refund.state,
            "State must be SUCCESSFUL",
        )

        criteria = EntityQuery(
            filter=EntityQueryFilter(
                field_name="id",
                value=refund.id,
                type=EntityQueryFilterType.LEAF,
                operator=CriteriaOperator.EQUALS
            )
        )

        refunds_found = self.refund_service.search(
            SPACE_ID, query=criteria)

        self.assertEqual(1, len(refunds_found))
        for ref in refunds_found:
            self.assertEqual(
                refund.id,
                ref.id,
                "Refund ids must match",
            )

    def test_count(self):
        """count() should count refunds for a given criteria"""

        transaction = self.transaction_service.create(
            space_id=SPACE_ID, transaction=get_transaction_create())

        transaction_processed = self.card_processing_service.process(
            space_id=SPACE_ID,
            transaction_id=transaction.id,
            payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
            card_data=FAKE_CARD_DATA,
        )

        transaction_completion = self.transaction_completion_service.complete_offline(
            space_id=SPACE_ID, id=transaction_processed.id)

        self.assertEqual(
            TransactionCompletionState.SUCCESSFUL,
            transaction_completion.state,
            "State must be SUCCESSFUL",
        )

        transaction_read = self.transaction_service.read(
            space_id=SPACE_ID, id=transaction_processed.id)

        refund = self.refund_service.refund(
            space_id=SPACE_ID, refund=self.__get_refund_create(transaction_read))

        self.assertEqual(
            RefundState.SUCCESSFUL,
            refund.state,
            "State must be SUCCESSFUL",
        )

        criteria = EntityQueryFilter(
            field_name="id",
            value=refund.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS
        )

        count = self.refund_service.count(
            SPACE_ID, filter=criteria)

        self.assertEqual(1, count, "Should find 1 refund", )


if __name__ == "__main__":
    unittest.main(failfast=True)
