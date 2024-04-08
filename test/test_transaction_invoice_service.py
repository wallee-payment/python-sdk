import unittest

from constants import (
    API_CONFIG,
    SPACE_ID,
    get_transaction_create,
    FAKE_CARD_DATA,
    TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
    TEST_ISR_INVOICE_PAYMENT_METHOD_CONFIGURATION_ID,
)

from wallee.api import (
    TransactionServiceApi,
    CardProcessingServiceApi,
    TransactionInvoiceServiceApi,
    TransactionCompletionServiceApi,
)
from wallee.models import (
    TransactionState,
    TransactionInvoiceState,
    EntityQuery,
    EntityQueryFilter,
    EntityQueryFilterType,
    CriteriaOperator,
    TokenizationMode,
    TransactionCompletionBehavior,
    CustomersPresence,
)


class TransactionInvoiceServiceTest(unittest.TestCase):
    """TransactionInvoiceServiceApi tests"""

    def setUp(self):
        self.transaction_service = TransactionServiceApi(API_CONFIG)
        self.transaction_invoice_service = TransactionInvoiceServiceApi(API_CONFIG)
        self.transaction_completion_service = TransactionCompletionServiceApi(
            API_CONFIG)
        self.card_processing_service = CardProcessingServiceApi(API_CONFIG)

    def tearDown(self):
        pass

    def test_search(self):
        """search() should find transaction invoice by a given criteria"""

        transaction_create = get_transaction_create()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_IMMEDIATELY
        transaction = self.transaction_service.create(space_id=SPACE_ID, transaction=transaction_create)

        transaction_processed = self.card_processing_service.process(
                    space_id=SPACE_ID,
                    transaction_id=transaction.id,
                    payment_method_configuration_id=TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID,
                    card_data=FAKE_CARD_DATA,
                )

        self.assertEqual(
                TransactionState.FULFILL,
                transaction_processed.state,
                "State must be FULFILL",
            )

        entity_query_filter = EntityQueryFilter(
            # linkedTransaction does not work here as criteria
            field_name="completion.lineItemVersion.transaction.id",
            value=transaction_processed.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS,
        )
        entity_query = EntityQuery(filter=entity_query_filter)

        invoices_found = self.transaction_invoice_service.search(
            space_id=SPACE_ID, query=entity_query)
        
        self.assertTrue(len(invoices_found) > 0,
                        "Should find invoice", )
        
        for invoice in invoices_found:
            self.assertEqual(TransactionInvoiceState.NOT_APPLICABLE, invoice.state,
                             "Invoice paid by card is expected to be of NOT_APPLICABLE state")



    def test_derecognize_transaction_invoice(self):
        """mark_as_derecognized() should derecognize open invoice"""

        transaction_create = get_transaction_create()
        transaction_create.tokenization_mode = TokenizationMode.FORCE_CREATION
        transaction_create.customers_presence = CustomersPresence.NOT_PRESENT
        transaction_create.completion_behavior = TransactionCompletionBehavior.COMPLETE_DEFERRED

        # we want invoice in OPEN state (OPEN invoices can be derecognized), so we force payment by invoice
        transaction_create.allowed_payment_method_configurations = [TEST_ISR_INVOICE_PAYMENT_METHOD_CONFIGURATION_ID]
        transaction = self.transaction_service.create(space_id=SPACE_ID, transaction=transaction_create)

        transaction_processed = self.transaction_service.process_without_user_interaction(
            space_id=SPACE_ID, id=transaction.id)
        
        transaction_completion = self.transaction_completion_service.complete_online(
                    space_id=SPACE_ID, id=transaction_processed.id)
        
        entity_query_filter = EntityQueryFilter(
            field_name="completion.lineItemVersion.transaction.id",
            value=transaction_processed.id,
            type=EntityQueryFilterType.LEAF,
            operator=CriteriaOperator.EQUALS,
        )
        entity_query = EntityQuery(filter=entity_query_filter)

        invoices_found = self.transaction_invoice_service.search(
            space_id=SPACE_ID, query=entity_query)
        
        self.assertTrue(len(invoices_found) > 0,
                        "Should find invoice", )
        
        found_invoice = invoices_found[0]

        self.assertEqual(TransactionInvoiceState.OPEN, found_invoice.state,
                         "Transaction paid by invoice should create invoice in OPEN state" )
        
        derecognized_invoice = self.transaction_invoice_service.mark_as_derecognized(
            space_id=SPACE_ID, id=found_invoice.id);
        
        self.assertEqual(TransactionInvoiceState.DERECOGNIZED, derecognized_invoice.state,
                         "Expected DERECOGNIZED invoice state")


if __name__ == "__main__":
    unittest.main(failfast=True)
