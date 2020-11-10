# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class TransactionCompletionServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def complete_offline(self, space_id, id, **kwargs):
        """completeOffline

        This operation completes the transaction offline. The completion is not forwarded to the processor. This implies the processor does not do anything. This method is only here to fix manually the transaction state.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_offline(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction which should be completed. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.complete_offline_with_http_info(space_id, id, **kwargs)
        else:
            (data) = self.complete_offline_with_http_info(space_id, id, **kwargs)
            return data

    def complete_offline_with_http_info(self, space_id, id, **kwargs):
        """completeOffline

        This operation completes the transaction offline. The completion is not forwarded to the processor. This implies the processor does not do anything. This method is only here to fix manually the transaction state.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_offline_with_http_info(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction which should be completed. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complete_offline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `complete_offline`")
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `complete_offline`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'id' in params:
            query_params.append(('id', params['id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-completion/completeOffline', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionCompletion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def complete_online(self, space_id, id, **kwargs):
        """completeOnline

        This operation completes the transaction online. The completion is forwarded to the processor. This implies that the processor may take some actions based on the completion.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_online(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction which should be completed. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.complete_online_with_http_info(space_id, id, **kwargs)
        else:
            (data) = self.complete_online_with_http_info(space_id, id, **kwargs)
            return data

    def complete_online_with_http_info(self, space_id, id, **kwargs):
        """completeOnline

        This operation completes the transaction online. The completion is forwarded to the processor. This implies that the processor may take some actions based on the completion.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_online_with_http_info(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction which should be completed. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complete_online" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `complete_online`")
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `complete_online`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'id' in params:
            query_params.append(('id', params['id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-completion/completeOnline', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionCompletion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def complete_partially_offline(self, space_id, completion, **kwargs):
        """completePartiallyOffline

        This operation can be used to partially complete the transaction offline. The completion is not forwarded to the processor. This implies the processor does not do anything. This method is only here to fix manually the transaction state.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_partially_offline(space_id, completion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TransactionCompletionRequest completion:  (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.complete_partially_offline_with_http_info(space_id, completion, **kwargs)
        else:
            (data) = self.complete_partially_offline_with_http_info(space_id, completion, **kwargs)
            return data

    def complete_partially_offline_with_http_info(self, space_id, completion, **kwargs):
        """completePartiallyOffline

        This operation can be used to partially complete the transaction offline. The completion is not forwarded to the processor. This implies the processor does not do anything. This method is only here to fix manually the transaction state.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_partially_offline_with_http_info(space_id, completion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TransactionCompletionRequest completion:  (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'completion']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complete_partially_offline" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `complete_partially_offline`")
        # verify the required parameter 'completion' is set
        if ('completion' not in params or
                params['completion'] is None):
            raise ValueError("Missing the required parameter `completion` when calling `complete_partially_offline`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'completion' in params:
            body_params = params['completion']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-completion/completePartiallyOffline', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionCompletion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def complete_partially_online(self, space_id, completion, **kwargs):
        """completePartiallyOnline

        This operation can be used to partially complete the transaction online. The completion is forwarded to the processor. This implies that the processor may take some actions based on the completion.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_partially_online(space_id, completion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TransactionCompletionRequest completion:  (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.complete_partially_online_with_http_info(space_id, completion, **kwargs)
        else:
            (data) = self.complete_partially_online_with_http_info(space_id, completion, **kwargs)
            return data

    def complete_partially_online_with_http_info(self, space_id, completion, **kwargs):
        """completePartiallyOnline

        This operation can be used to partially complete the transaction online. The completion is forwarded to the processor. This implies that the processor may take some actions based on the completion.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.complete_partially_online_with_http_info(space_id, completion, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param TransactionCompletionRequest completion:  (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'completion']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method complete_partially_online" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `complete_partially_online`")
        # verify the required parameter 'completion' is set
        if ('completion' not in params or
                params['completion'] is None):
            raise ValueError("Missing the required parameter `completion` when calling `complete_partially_online`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'completion' in params:
            body_params = params['completion']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-completion/completePartiallyOnline', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionCompletion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def count(self, space_id, **kwargs):
        """Count

        Counts the number of items in the database as restricted by the given filter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQueryFilter filter: The filter which restricts the entities which are used to calculate the count.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.count_with_http_info(space_id, **kwargs)
        else:
            (data) = self.count_with_http_info(space_id, **kwargs)
            return data

    def count_with_http_info(self, space_id, **kwargs):
        """Count

        Counts the number of items in the database as restricted by the given filter.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.count_with_http_info(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQueryFilter filter: The filter which restricts the entities which are used to calculate the count.
        :return: int
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'filter']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method count" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `count`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'filter' in params:
            body_params = params['filter']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/transaction-completion/count', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='int',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def read(self, space_id, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction completions which should be returned. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.read_with_http_info(space_id, id, **kwargs)
        else:
            (data) = self.read_with_http_info(space_id, id, **kwargs)
            return data

    def read_with_http_info(self, space_id, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read_with_http_info(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the transaction completions which should be returned. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method read" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `read`")
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `read`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
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
            '/transaction-completion/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionCompletion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def search(self, space_id, query, **kwargs):
        """Search

        Searches for the entities as specified by the given query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search(space_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQuery query: The query restricts the transaction completions which are returned by the search. (required)
        :return: list[TransactionCompletion]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.search_with_http_info(space_id, query, **kwargs)
        else:
            (data) = self.search_with_http_info(space_id, query, **kwargs)
            return data

    def search_with_http_info(self, space_id, query, **kwargs):
        """Search

        Searches for the entities as specified by the given query.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.search_with_http_info(space_id, query, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param EntityQuery query: The query restricts the transaction completions which are returned by the search. (required)
        :return: list[TransactionCompletion]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'query']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method search" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `search`")
        # verify the required parameter 'query' is set
        if ('query' not in params or
                params['query'] is None):
            raise ValueError("Missing the required parameter `query` when calling `search`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

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
            '/transaction-completion/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[TransactionCompletion]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
