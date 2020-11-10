# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class TransactionMobileSdkServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def payment_form_url(self, credentials, **kwargs):
        """Build Mobile SDK URL

        This operation builds the URL which is used to load the payment form within a WebView on a mobile device. This operation is typically called through the mobile SDK.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payment_form_url(credentials, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credentials: The credentials identifies the transaction and contains the security details which grants the access this operation. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.payment_form_url_with_http_info(credentials, **kwargs)
        else:
            (data) = self.payment_form_url_with_http_info(credentials, **kwargs)
            return data

    def payment_form_url_with_http_info(self, credentials, **kwargs):
        """Build Mobile SDK URL

        This operation builds the URL which is used to load the payment form within a WebView on a mobile device. This operation is typically called through the mobile SDK.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.payment_form_url_with_http_info(credentials, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str credentials: The credentials identifies the transaction and contains the security details which grants the access this operation. (required)
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['credentials']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method payment_form_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'credentials' is set
        if ('credentials' not in params or
                params['credentials'] is None):
            raise ValueError("Missing the required parameter `credentials` when calling `payment_form_url`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'credentials' in params:
            query_params.append(('credentials', params['credentials']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json', 'text/plain;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-mobile-sdk/payment-form-url', 'GET',
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
