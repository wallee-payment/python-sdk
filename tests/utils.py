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


from wallee.models import LineItemCreate, AddressCreate, TransactionCreate

class Utils:
    @staticmethod
    def get_transaction_create_payload():
        line_item = LineItemCreate(
            name="Red T-Shirt",
            unique_id="5412",
            type="PRODUCT",
            quantity=1,
            amount_including_tax=29.95,
            sku="red-t-shirt-789"
        )

        email = "test@domain.com"

        address = AddressCreate(
            city="Winterthur",
            country="CH",
            email_address=email,
            family_name="Customer",
            given_name="Good",
            postcode="8400",
            postal_state="ZH",
            organization_name="Test GmbH",
            mobile_phone_number="+41791234567",
            salutation="Ms"
        )

        return TransactionCreate(
            auto_confirmation_enabled=True,
            currency="CHF",
            language="en-US",
            line_items=[line_item],
            customer_id="1234",
            customer_email_address=email,
            billing_address=address,
            shipping_address=address
        )