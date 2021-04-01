# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class CardProcessingServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def process(self, space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs):
        """Process

        The process method will process the transaction with the given card details without using 3-D secure.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process(space_id, transaction_id, payment_method_configuration_id, card_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which should be processed. (required)
        :param int payment_method_configuration_id: The payment method configuration ID which is applied to the transaction. (required)
        :param AuthenticatedCardDataCreate card_data: The card details as JSON in plain which should be used to authorize the payment. (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.process_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs)
        else:
            (data) = self.process_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs)
            return data

    def process_with_http_info(self, space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs):
        """Process

        The process method will process the transaction with the given card details without using 3-D secure.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which should be processed. (required)
        :param int payment_method_configuration_id: The payment method configuration ID which is applied to the transaction. (required)
        :param AuthenticatedCardDataCreate card_data: The card details as JSON in plain which should be used to authorize the payment. (required)
        :return: Transaction
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id', 'payment_method_configuration_id', 'card_data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `process`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `process`")
        # verify the required parameter 'payment_method_configuration_id' is set
        if ('payment_method_configuration_id' not in params or
                params['payment_method_configuration_id'] is None):
            raise ValueError("Missing the required parameter `payment_method_configuration_id` when calling `process`")
        # verify the required parameter 'card_data' is set
        if ('card_data' not in params or
                params['card_data'] is None):
            raise ValueError("Missing the required parameter `card_data` when calling `process`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))
        if 'payment_method_configuration_id' in params:
            query_params.append(('paymentMethodConfigurationId', params['payment_method_configuration_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'card_data' in params:
            body_params = params['card_data']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/card-processing/process', 'POST',
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

    def process_with3_d_secure(self, space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs):
        """Process With 3-D Secure

        The process method will process the transaction with the given card details by eventually using 3-D secure. The buyer has to be redirect to the URL returned by this method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_with3_d_secure(space_id, transaction_id, payment_method_configuration_id, card_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which should be processed. (required)
        :param int payment_method_configuration_id: The payment method configuration ID which is applied to the transaction. (required)
        :param TokenizedCardDataCreate card_data: The card details as JSON in plain which should be used to authorize the payment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.process_with3_d_secure_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs)
        else:
            (data) = self.process_with3_d_secure_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs)
            return data

    def process_with3_d_secure_with_http_info(self, space_id, transaction_id, payment_method_configuration_id, card_data, **kwargs):
        """Process With 3-D Secure

        The process method will process the transaction with the given card details by eventually using 3-D secure. The buyer has to be redirect to the URL returned by this method.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.process_with3_d_secure_with_http_info(space_id, transaction_id, payment_method_configuration_id, card_data, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The ID of the transaction which should be processed. (required)
        :param int payment_method_configuration_id: The payment method configuration ID which is applied to the transaction. (required)
        :param TokenizedCardDataCreate card_data: The card details as JSON in plain which should be used to authorize the payment. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id', 'payment_method_configuration_id', 'card_data']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method process_with3_d_secure" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `process_with3_d_secure`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `process_with3_d_secure`")
        # verify the required parameter 'payment_method_configuration_id' is set
        if ('payment_method_configuration_id' not in params or
                params['payment_method_configuration_id'] is None):
            raise ValueError("Missing the required parameter `payment_method_configuration_id` when calling `process_with3_d_secure`")
        # verify the required parameter 'card_data' is set
        if ('card_data' not in params or
                params['card_data'] is None):
            raise ValueError("Missing the required parameter `card_data` when calling `process_with3_d_secure`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))
        if 'payment_method_configuration_id' in params:
            query_params.append(('paymentMethodConfigurationId', params['payment_method_configuration_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'card_data' in params:
            body_params = params['card_data']
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/card-processing/processWith3DSecure', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='str',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
