# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class ShopifySubscriptionSuspensionServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

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
            '/shopify-subscription-suspension/count', 'POST',
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

    def reactivate(self, space_id, subscription_id, **kwargs):
        """Reactivate

        This operation allows to reactivate a suspended Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reactivate(space_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int subscription_id: The ID identifies the suspended Shopify subscription which should be reactivated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.reactivate_with_http_info(space_id, subscription_id, **kwargs)
        else:
            (data) = self.reactivate_with_http_info(space_id, subscription_id, **kwargs)
            return data

    def reactivate_with_http_info(self, space_id, subscription_id, **kwargs):
        """Reactivate

        This operation allows to reactivate a suspended Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.reactivate_with_http_info(space_id, subscription_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int subscription_id: The ID identifies the suspended Shopify subscription which should be reactivated. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'subscription_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method reactivate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `reactivate`")
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `reactivate`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))

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
            '/shopify-subscription-suspension/reactivate', 'POST',
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

    def read(self, space_id, id, **kwargs):
        """Read

        Reads the entity with the given 'id' and returns it.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.read(space_id, id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int id: The id of the Shopify subscription suspension which should be returned. (required)
        :return: ShopifySubscriptionSuspension
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
        :param int id: The id of the Shopify subscription suspension which should be returned. (required)
        :return: ShopifySubscriptionSuspension
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
            '/shopify-subscription-suspension/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscriptionSuspension',
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
        :param EntityQuery query: The query restricts the Shopify subscription suspensions which are returned by the search. (required)
        :return: list[ShopifySubscriptionSuspension]
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
        :param EntityQuery query: The query restricts the Shopify subscription suspensions which are returned by the search. (required)
        :return: list[ShopifySubscriptionSuspension]
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
            '/shopify-subscription-suspension/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ShopifySubscriptionSuspension]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def suspend(self, space_id, suspension, **kwargs):
        """Suspend

        This operation allows to suspend a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.suspend(space_id, suspension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionSuspensionCreate suspension:  (required)
        :return: ShopifySubscriptionSuspension
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.suspend_with_http_info(space_id, suspension, **kwargs)
        else:
            (data) = self.suspend_with_http_info(space_id, suspension, **kwargs)
            return data

    def suspend_with_http_info(self, space_id, suspension, **kwargs):
        """Suspend

        This operation allows to suspend a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.suspend_with_http_info(space_id, suspension, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionSuspensionCreate suspension:  (required)
        :return: ShopifySubscriptionSuspension
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'suspension']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method suspend" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `suspend`")
        # verify the required parameter 'suspension' is set
        if ('suspension' not in params or
                params['suspension'] is None):
            raise ValueError("Missing the required parameter `suspension` when calling `suspend`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'suspension' in params:
            body_params = params['suspension']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/shopify-subscription-suspension/suspend', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscriptionSuspension',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
