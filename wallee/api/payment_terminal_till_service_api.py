# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class PaymentTerminalTillServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def perform_transaction(self, space_id, transaction_id, terminal_id, **kwargs):
        """Perform Payment Terminal Transaction

        Starts a payment terminal transaction and waits for its completion. If the call returns with a long polling timeout status, you may try again. The processing of the transaction will be picked up where it was left off.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_transaction(space_id, transaction_id, terminal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which is used to process with the terminal. (required)
        :param int terminal_id: The ID of the terminal which should be used to process the transaction. (required)
        :param str language: The language in which the messages should be rendered in.
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        kwargs['_request_timeout'] = 90

        if kwargs.get('async_req'):
            return self.perform_transaction_with_http_info(space_id, transaction_id, terminal_id, **kwargs)
        else:
            (data) = self.perform_transaction_with_http_info(space_id, transaction_id, terminal_id, **kwargs)
            return data

    def perform_transaction_with_http_info(self, space_id, transaction_id, terminal_id, **kwargs):
        """Perform Payment Terminal Transaction

        Starts a payment terminal transaction and waits for its completion. If the call returns with a long polling timeout status, you may try again. The processing of the transaction will be picked up where it was left off.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_transaction_with_http_info(space_id, transaction_id, terminal_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which is used to process with the terminal. (required)
        :param int terminal_id: The ID of the terminal which should be used to process the transaction. (required)
        :param str language: The language in which the messages should be rendered in.
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id', 'terminal_id', 'language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_transaction" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `perform_transaction`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `perform_transaction`")
        # verify the required parameter 'terminal_id' is set
        if ('terminal_id' not in params or
                params['terminal_id'] is None):
            raise ValueError("Missing the required parameter `terminal_id` when calling `perform_transaction`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))
        if 'terminal_id' in params:
            query_params.append(('terminalId', params['terminal_id']))
        if 'language' in params:
            query_params.append(('language', params['language']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-terminal-till/perform-transaction', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transaction',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def perform_transaction_by_identifier(self, space_id, transaction_id, terminal_identifier, **kwargs):
        """Perform Payment Terminal Transaction (using TID)

        Starts a payment terminal transaction and waits for its completion. If the call returns with a long polling timeout status, you may try again. The processing of the transaction will be picked up where it was left off.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_transaction_by_identifier(space_id, transaction_id, terminal_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which is used to process with the terminal. (required)
        :param str terminal_identifier: The identifier (aka TID) of the terminal which should be used to process the transaction. (required)
        :param str language: The language in which the messages should be rendered in.
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True

        kwargs['_request_timeout'] = 90

        if kwargs.get('async_req'):
            return self.perform_transaction_by_identifier_with_http_info(space_id, transaction_id, terminal_identifier, **kwargs)
        else:
            (data) = self.perform_transaction_by_identifier_with_http_info(space_id, transaction_id, terminal_identifier, **kwargs)
            return data

    def perform_transaction_by_identifier_with_http_info(self, space_id, transaction_id, terminal_identifier, **kwargs):
        """Perform Payment Terminal Transaction (using TID)

        Starts a payment terminal transaction and waits for its completion. If the call returns with a long polling timeout status, you may try again. The processing of the transaction will be picked up where it was left off.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.perform_transaction_by_identifier_with_http_info(space_id, transaction_id, terminal_identifier, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which is used to process with the terminal. (required)
        :param str terminal_identifier: The identifier (aka TID) of the terminal which should be used to process the transaction. (required)
        :param str language: The language in which the messages should be rendered in.
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id', 'terminal_identifier', 'language']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method perform_transaction_by_identifier" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `perform_transaction_by_identifier`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `perform_transaction_by_identifier`")
        # verify the required parameter 'terminal_identifier' is set
        if ('terminal_identifier' not in params or
                params['terminal_identifier'] is None):
            raise ValueError("Missing the required parameter `terminal_identifier` when calling `perform_transaction_by_identifier`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))
        if 'terminal_identifier' in params:
            query_params.append(('terminalIdentifier', params['terminal_identifier']))
        if 'language' in params:
            query_params.append(('language', params['language']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-terminal-till/perform-transaction-by-identifier', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Transaction',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
