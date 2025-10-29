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


from wallee import Configuration
from wallee import AuthenticatedCardRequest, AuthenticatedCardDataCreate

# The new Configuration method creates (Non-singleton, instance-per-use model) independent
# instances, unique and created on demand. Allowing for configuration flexibility
# and avoiding shared state across the application.

# Create a Configuration instance independent and does not share state with others.
API_CONFIG = Configuration(
    user_id=512,
    authentication_key="FKrO76r5VwJtBrqZawBspljbBNOxp5veKQQkOnZxucQ=",
    default_headers={'x-meta-custom-header': 'value-1', 'x-meta-custom-header-2': 'value-2'}
)

SPACE_ID = 405

TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID = 1352
TEST_CUSTOMER_ID = "7311742"

MOCK_CARD_DATA = AuthenticatedCardRequest(
    cardData = AuthenticatedCardDataCreate(
        primaryAccountNumber = "4111111111111111",
        expiryDate = "2026-12"
        ),
    paymentMethodConfiguration = TEST_CARD_PAYMENT_METHOD_CONFIGURATION_ID
)