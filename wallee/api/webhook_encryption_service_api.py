# coding: utf-8

from __future__ import absolute_import

import six
import re

from wallee.api_client import ApiClient
from wallee.encryption_util import EncryptionUtil

class WebhookEncryptionServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def read(self, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.
        
        >>> thread = api.read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the key version. (required)
        :return: WebhookEncryptionPublicKey
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        
        kwargs['request_timeout'] = self.api_client.configuration.request_timeout
        if kwargs.get('async_req'):
            return self.read_with_http_info(id, **kwargs)
        else:
            (data) = self.read_with_http_info(id, **kwargs)
            return data

    def read_with_http_info(self, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.
        
        >>> thread = api.read_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str id: The ID of the key version. (required)
        :return: WebhookEncryptionPublicKey
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `read`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/webhook-encryption/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebhookEncryptionPublicKey',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('request_timeout'),
            collection_formats=collection_formats)

    def is_content_valid(self, signature_header, content_to_verify):
        """Verify webhook content using signature header

        Verifies webhook content using signature header.

        :param str signature_header: Signature header 'X-Signature' value from the Http request
        :param str content_to_verify: Raw webhook content in String format
        :return: bool if webhook content body conforms with signature header
        """
        regex = r"^algorithm=([a-zA-Z0-9]+),\skeyId=([a-z0-9\-]+),\s{1}signature=([a-zA-Z0-9+\/=]+)$"
        pattern = re.compile(regex)
        matcher = pattern.match(signature_header)

        if matcher:
            signature_algorithm = matcher.group(1)
            public_key_id = matcher.group(2)
            content_signature = matcher.group(3)

            public_key_response = WebhookEncryptionServiceApi.read(self, public_key_id)

            if public_key_response is None or public_key_response.public_key is None:
                raise ValueError(f"Could not find public key with id {public_key_id}")

            return EncryptionUtil.is_content_valid(content_to_verify, content_signature, public_key_response.public_key,
                                                   signature_algorithm)
        else:
            raise ValueError(
                "Invalid webhook signature header. Expected format: 'algorithm=<algorithm>, keyId=<keyId>, "
                "signature=<signature>'")
