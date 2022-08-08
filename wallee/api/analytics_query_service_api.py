# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class AnalyticsQueryServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def cancel_execution(self, id, **kwargs):
        """Cancel Execution

        Cancels the specified query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_execution(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution to cancel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.cancel_execution_with_http_info(id, **kwargs)
        else:
            (data) = self.cancel_execution_with_http_info(id, **kwargs)
            return data

    def cancel_execution_with_http_info(self, id, **kwargs):
        """Cancel Execution

        Cancels the specified query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.cancel_execution_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution to cancel. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method cancel_execution" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `cancel_execution`")

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
            '/analytics-query/cancel-execution', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type=None,
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def fetch_result(self, id, **kwargs):
        """Fetch Result

        Fetches one batch of the result of a query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_result(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to fetch the result. (required)
        :param int timeout: The maximal time in seconds to wait for the result if it is not yet available. Use 0 (the default) to return immediately without waiting.
        :param int max_rows: The maximum number of rows to return per batch. (Between 1 and 999. The default is 999.)
        :param str next_token: The next-token of the preceding batch to get the next result batch or null to get the first result batch.
        :return: AnalyticsQueryResultBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.fetch_result_with_http_info(id, **kwargs)
        else:
            (data) = self.fetch_result_with_http_info(id, **kwargs)
            return data

    def fetch_result_with_http_info(self, id, **kwargs):
        """Fetch Result

        Fetches one batch of the result of a query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.fetch_result_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to fetch the result. (required)
        :param int timeout: The maximal time in seconds to wait for the result if it is not yet available. Use 0 (the default) to return immediately without waiting.
        :param int max_rows: The maximum number of rows to return per batch. (Between 1 and 999. The default is 999.)
        :param str next_token: The next-token of the preceding batch to get the next result batch or null to get the first result batch.
        :return: AnalyticsQueryResultBatch
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'timeout', 'max_rows', 'next_token']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method fetch_result" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `fetch_result`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))
        if 'max_rows' in params:
            query_params.append(('maxRows', params['max_rows']))
        if 'next_token' in params:
            query_params.append(('nextToken', params['next_token']))

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
            '/analytics-query/fetch-result', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsQueryResultBatch',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def generate_download_url(self, id, **kwargs):
        """Generate Download URL

        Generate a URL from which the results of a query execution can be downloaded in CSV format.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_download_url(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to generate the download URL. (required)
        :param int timeout: The maximal time in seconds to wait for the result if it is not yet available. Use 0 (the default) to return immediately without waiting.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.generate_download_url_with_http_info(id, **kwargs)
        else:
            (data) = self.generate_download_url_with_http_info(id, **kwargs)
            return data

    def generate_download_url_with_http_info(self, id, **kwargs):
        """Generate Download URL

        Generate a URL from which the results of a query execution can be downloaded in CSV format.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.generate_download_url_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to generate the download URL. (required)
        :param int timeout: The maximal time in seconds to wait for the result if it is not yet available. Use 0 (the default) to return immediately without waiting.
        :return: str
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id', 'timeout']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method generate_download_url" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `generate_download_url`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'id' in params:
            query_params.append(('id', params['id']))
        if 'timeout' in params:
            query_params.append(('timeout', params['timeout']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['text/plain'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/analytics-query/generate-download-url', 'GET',
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

    def schema(self, **kwargs):
        """Get Schemas

        Get the schemas describing the available tables and their columns.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schema(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AnalyticsSchemaTable]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.schema_with_http_info(**kwargs)
        else:
            (data) = self.schema_with_http_info(**kwargs)
            return data

    def schema_with_http_info(self, **kwargs):
        """Get Schemas

        Get the schemas describing the available tables and their columns.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.schema_with_http_info(async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :return: list[AnalyticsSchemaTable]
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
                    " to method schema" % key
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
            '/analytics-query/schema', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[AnalyticsSchemaTable]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def status(self, id, **kwargs):
        """Execution Status

        Returns the current status of a query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.status(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to get the status. (required)
        :return: AnalyticsQueryExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.status_with_http_info(id, **kwargs)
        else:
            (data) = self.status_with_http_info(id, **kwargs)
            return data

    def status_with_http_info(self, id, **kwargs):
        """Execution Status

        Returns the current status of a query execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.status_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The ID of the query execution for which to get the status. (required)
        :return: AnalyticsQueryExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method status" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `status`")

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
            '/analytics-query/status', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsQueryExecution',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def submit_query(self, query, **kwargs):
        """Submit Query

        Submits a query for execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_query(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyticsQuery query: The query to submit. (required)
        :return: AnalyticsQueryExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.submit_query_with_http_info(query, **kwargs)
        else:
            (data) = self.submit_query_with_http_info(query, **kwargs)
            return data

    def submit_query_with_http_info(self, query, **kwargs):
        """Submit Query

        Submits a query for execution.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.submit_query_with_http_info(query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param AnalyticsQuery query: The query to submit. (required)
        :return: AnalyticsQueryExecution
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['query']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method submit_query" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `submit_query`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'query' in params:
            body_params = params['query']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/analytics-query/submit-query', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='AnalyticsQueryExecution',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
