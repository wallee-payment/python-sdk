from wallee import Configuration

from wallee.models import (
    AddressCreate,
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
    address = AddressCreate(
        city = "Winterthur",
        country = "CH",
        email_address = "test@example.com",
        family_name = "Customer",
        given_name = "Good",
        postcode = "8400",
        postal_state = "ZH",
        organization_name = "Test GmbH",
        mobile_phone_number = "+41791234567",
        salutation = "Ms"
    )

    return TransactionCreate(
        currency="CHF",
        auto_confirmation_enabled=True,
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
        billing_address=address,
        shipping_address=address,
        language="en-GB",
    )


FAKE_CARD_DATA = AuthenticatedCardDataCreate(
    primary_account_number="4111111111111111", expiry_date="2026-12"
)

TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID = 1352
TEST_ISR_INVOICE_PAYMENT_METHOD_CONFIGURATION_ID = 8656
TEST_CUSTOMER_ID = 7311742
