# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class LabelDescriptionServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def all(self, **kwargs):
        """All

        This operation returns all entities which are available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.
        
        >>> thread = api.all(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[LabelDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True
        
        kwargs['request_timeout'] = self.api_client.configuration.request_timeout
        if kwargs.get('async_req'):
            return self.all_with_http_info(**kwargs)
        else:
            (data) = self.all_with_http_info(**kwargs)
            return data

    def all_with_http_info(self, **kwargs):
        """All

        This operation returns all entities which are available.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.
        
        >>> thread = api.all_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[LabelDescriptor]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = []
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('request_timeout')

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
            '/label-description-service/all', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[LabelDescriptor]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('request_timeout'),
            collection_formats=collection_formats)

    def read(self, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True.
        
        >>> thread = api.read(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of the label descriptor which should be returned. (required)
        :return: LabelDescriptor
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
        :param int id: The id of the label descriptor which should be returned. (required)
        :return: LabelDescriptor
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
            '/label-description-service/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='LabelDescriptor',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('request_timeout'),
            collection_formats=collection_formats)
