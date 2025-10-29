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

from constants import API_CONFIG, SPACE_ID
from wallee import Configuration
from wallee.models import CreationEntityState, WebhookListenerCreate
from wallee.service import WebhookListenersService, WebhookURLsService


class TestWebhookListenersApi(unittest.TestCase):
    """wallee WebhookListeners Service tests"""

    WEBHOOK_LISTENER_ENTITY_ID = 1472041829003
    WEBHOOK_LISTENER_NAME = "Python Mock UnitTest Webhook Listener"

    def setUp(self):
        self.webhook_listeners_service = WebhookListenersService(API_CONFIG)
        self.webhook_urls_service = WebhookURLsService(API_CONFIG)

    def test_webhook_listener_create_and_delete(self):
        """test_webhook_listener_create_and_delete() should create and delete webhook listener"""

        webhook_url_search_response = self.webhook_urls_service.get_webhooks_urls_search(
            space=SPACE_ID,
            expand=["url", "group"],
            limit=1,
            order="id:DESC",
            query="name:\"Webhook Test URL Listener\"")
        self.assertEqual(first=len(webhook_url_search_response.data), second=1,
                         msg="The length of the searched webhook urls list should be 1.")

        webhook_url_id = webhook_url_search_response.data[0].id
        webhook_listener_create = self.webhook_listener_create(webhook_url_id)
        created_response = self.webhook_listeners_service.post_webhooks_listeners(
            SPACE_ID,
            webhook_listener_create,
            expand=["url", "group"])

        self.assertEqual(first=created_response.state, second=CreationEntityState.ACTIVE,
                         msg="State must be \"ACTIVE\".")
        self.assertEqual(first=created_response.linked_space_id, second=SPACE_ID, msg="Space id should match.")
        self.assertEqual(first=created_response.name, second=self.WEBHOOK_LISTENER_NAME, msg="Name should match.")
        self.assertEqual(first=created_response.entity, second=self.WEBHOOK_LISTENER_ENTITY_ID,
                         msg="Entity should match.")
        self.assertEqual(first=created_response.url.id, second=webhook_url_id, msg="URL id should match.")
        self.assertEqual(first=created_response.url.name, second="Webhook Test URL Listener",
                         msg="URL name should match.")

        self.webhook_listeners_service.delete_webhooks_listeners_id(created_response.id, SPACE_ID)

        get_deleted_response = self.webhook_listeners_service.get_webhooks_listeners_id(created_response.id, SPACE_ID)
        self.assertEqual(first=get_deleted_response.id, second=created_response.id, msg="Id should match.")
        self.assertEqual(first=get_deleted_response.state, second=CreationEntityState.DELETED,
                         msg="State must be \"DELETED\".")
        self.assertEqual(first=get_deleted_response.linked_space_id, second=SPACE_ID, msg="Space id should match.")
        self.assertEqual(first=get_deleted_response.name, second=self.WEBHOOK_LISTENER_NAME, msg="Name should match.")

    def webhook_listener_create(self, webhook_url_id):
        return WebhookListenerCreate(
            entity=self.WEBHOOK_LISTENER_ENTITY_ID,
            name=self.WEBHOOK_LISTENER_NAME,
            state=CreationEntityState.ACTIVE,
            url=webhook_url_id
        )

    def test_webhook_listeners_search_without_custom_timeout(self):
        """test_webhook_listeners_search_without_custom_timeout() should search webhook listener without custom timeout"""

        search_response = self.webhook_listeners_service.get_webhooks_listeners_search(
            space=SPACE_ID,
            expand=["url", "group"],
            limit=1,
            order="id:DESC",
            query="name:Test AND state:INACTIVE")

        self.assertEqual(first=len(search_response.data), second=1,
                         msg="The length of the searched webhook listeners list should be 1.")
        for webhook_listener in search_response.data:
            self.assertEqual(first="Test", second=webhook_listener.name,
                             msg=f"Expected name to be \"Test\", got {webhook_listener.name}.")
            self.assertEqual(first=SPACE_ID, second=webhook_listener.linked_space_id,
                             msg=f"Expected space ID: {SPACE_ID} does not match, got {webhook_listener.linked_space_id}.")

    def test_webhook_listeners_search_with_custom_timeout(self):
        """test_webhook_listeners_search_with_custom_timeout() should search webhook listener with custom timeout: 36 sec."""

        # Multiple independent Configuration instances
        # API_CONFIG and custom_configuration do not share state or configuration
        custom_configuration = Configuration(user_id=API_CONFIG.user_id,
                                             authentication_key=API_CONFIG.authentication_key,
                                             request_timeout=36)
        webhook_listeners_service_with_custom_timeout = WebhookListenersService(custom_configuration)

        search_response = webhook_listeners_service_with_custom_timeout.get_webhooks_listeners_search(
            space=SPACE_ID,
            expand=["url", "group"],
            limit=1,
            order="id:DESC",
            query="name:Test AND state:INACTIVE")

        self.assertEqual(first=len(search_response.data), second=1,
                         msg="The length of the searched webhook listeners list should be 1.")
        for webhook_listener in search_response.data:
            self.assertEqual(first="Test", second=webhook_listener.name,
                             msg=f"Expected name to be \"Test\", got {webhook_listener.name}.")
            self.assertEqual(first=SPACE_ID, second=webhook_listener.linked_space_id,
                             msg=f"Expected space ID: {SPACE_ID} does not match, got {webhook_listener.linked_space_id}.")
