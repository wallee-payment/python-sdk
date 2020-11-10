# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class CountryStateServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def all(self, **kwargs):
        """All

        This operation returns all states of all countries.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[RestCountryState]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.all_with_http_info(**kwargs)
        else:
            (data) = self.all_with_http_info(**kwargs)
            return data

    def all_with_http_info(self, **kwargs):
        """All

        This operation returns all states of all countries.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[RestCountryState]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method all" % key
                )
            params[key] = val
        del params['kwargs']

        collection_formats = {}

        path_params = {}

        query_params = []

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
            '/country-state/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RestCountryState]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def country(self, code, **kwargs):
        """Find by Country

        This operation returns all states for a given country.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.country(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: The country code in ISO code two letter format for which all states should be returned. (required)
        :return: list[RestCountryState]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.country_with_http_info(code, **kwargs)
        else:
            (data) = self.country_with_http_info(code, **kwargs)
            return data

    def country_with_http_info(self, code, **kwargs):
        """Find by Country

        This operation returns all states for a given country.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.country_with_http_info(code, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param str code: The country code in ISO code two letter format for which all states should be returned. (required)
        :return: list[RestCountryState]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['code']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method country" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'code' is set
        if ('code' not in params or
                params['code'] is None):
            raise ValueError("Missing the required parameter `code` when calling `country`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'code' in params:
            query_params.append(('code', params['code']))

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
            '/country-state/country', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[RestCountryState]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
