from wallee import Configuration

from wallee.models import (
    LineItem,
    LineItemType,
    TransactionCreate,
    AuthenticatedCardDataCreate,
)

API_CONFIG = Configuration(
    user_id=512,
    api_secret="FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ=",
    request_timeout=30,
)

SPACE_ID = 405

def get_transaction_create():
    return TransactionCreate(
        line_items=[
            LineItem(
                name="Blue T-Shirt",
                unique_id="5412",
                sku="blue-t-shirt-123",
                quantity=1,
                amount_including_tax=3.50,
                type=LineItemType.PRODUCT,
            )
        ],
        auto_confirmation_enabled=True,
        currency="CHF",
    )


FAKE_CARD_DATA = AuthenticatedCardDataCreate(
    primary_account_number="4111111111111111", expiry_date="2026-12"
)

TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID = 1352
TEST_CUSTOMER_ID = 7311742
