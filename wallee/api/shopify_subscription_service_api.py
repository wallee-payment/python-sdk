# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class ShopifySubscriptionServiceApi:

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
            '/shopify-subscription/count', 'POST',
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

    def create(self, space_id, creation_request, **kwargs):
        """Create

        This operation allows to create a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create(space_id, creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionCreationRequest creation_request:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.create_with_http_info(space_id, creation_request, **kwargs)
        else:
            (data) = self.create_with_http_info(space_id, creation_request, **kwargs)
            return data

    def create_with_http_info(self, space_id, creation_request, **kwargs):
        """Create

        This operation allows to create a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.create_with_http_info(space_id, creation_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionCreationRequest creation_request:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'creation_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method create" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `create`")
        # verify the required parameter 'creation_request' is set
        if ('creation_request' not in params or
                params['creation_request'] is None):
            raise ValueError("Missing the required parameter `creation_request` when calling `create`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'creation_request' in params:
            body_params = params['creation_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/shopify-subscription/create', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscriptionVersion',
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
        :param int id: The id of the Shopify subscription which should be returned. (required)
        :return: ShopifySubscription
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
        :param int id: The id of the Shopify subscription which should be returned. (required)
        :return: ShopifySubscription
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
            '/shopify-subscription/read', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscription',
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
        :param EntityQuery query: The query restricts the Shopify subscriptions which are returned by the search. (required)
        :return: list[ShopifySubscription]
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
        :param EntityQuery query: The query restricts the Shopify subscriptions which are returned by the search. (required)
        :return: list[ShopifySubscription]
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
            '/shopify-subscription/search', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[ShopifySubscription]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def terminate(self, space_id, subscription_id, respect_termination_period, **kwargs):
        """Terminate

        This operation allows to terminate a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.terminate(space_id, subscription_id, respect_termination_period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int subscription_id: The ID identifies the Shopify subscription which should be terminated. (required)
        :param bool respect_termination_period: The respect termination period controls whether the termination period configured on the product version should be respected or if the operation should take effect immediately. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.terminate_with_http_info(space_id, subscription_id, respect_termination_period, **kwargs)
        else:
            (data) = self.terminate_with_http_info(space_id, subscription_id, respect_termination_period, **kwargs)
            return data

    def terminate_with_http_info(self, space_id, subscription_id, respect_termination_period, **kwargs):
        """Terminate

        This operation allows to terminate a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.terminate_with_http_info(space_id, subscription_id, respect_termination_period, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int subscription_id: The ID identifies the Shopify subscription which should be terminated. (required)
        :param bool respect_termination_period: The respect termination period controls whether the termination period configured on the product version should be respected or if the operation should take effect immediately. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'subscription_id', 'respect_termination_period']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method terminate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `terminate`")
        # verify the required parameter 'subscription_id' is set
        if ('subscription_id' not in params or
                params['subscription_id'] is None):
            raise ValueError("Missing the required parameter `subscription_id` when calling `terminate`")
        # verify the required parameter 'respect_termination_period' is set
        if ('respect_termination_period' not in params or
                params['respect_termination_period'] is None):
            raise ValueError("Missing the required parameter `respect_termination_period` when calling `terminate`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'subscription_id' in params:
            query_params.append(('subscriptionId', params['subscription_id']))
        if 'respect_termination_period' in params:
            query_params.append(('respectTerminationPeriod', params['respect_termination_period']))

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
            '/shopify-subscription/terminate', 'POST',
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

    def update(self, space_id, subscription, **kwargs):
        """Update

        This operation allows to update a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update(space_id, subscription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionUpdateRequest subscription:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_with_http_info(space_id, subscription, **kwargs)
        else:
            (data) = self.update_with_http_info(space_id, subscription, **kwargs)
            return data

    def update_with_http_info(self, space_id, subscription, **kwargs):
        """Update

        This operation allows to update a Shopify subscription.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_with_http_info(space_id, subscription, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionUpdateRequest subscription:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'subscription']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update`")
        # verify the required parameter 'subscription' is set
        if ('subscription' not in params or
                params['subscription'] is None):
            raise ValueError("Missing the required parameter `subscription` when calling `update`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'subscription' in params:
            body_params = params['subscription']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/shopify-subscription/update', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscriptionVersion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_addresses(self, space_id, update_request, **kwargs):
        """Update Addresses

        This operation allows to update a Shopify subscription addresses.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addresses(space_id, update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionUpdateAddressesRequest update_request:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_addresses_with_http_info(space_id, update_request, **kwargs)
        else:
            (data) = self.update_addresses_with_http_info(space_id, update_request, **kwargs)
            return data

    def update_addresses_with_http_info(self, space_id, update_request, **kwargs):
        """Update Addresses

        This operation allows to update a Shopify subscription addresses.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_addresses_with_http_info(space_id, update_request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param ShopifySubscriptionUpdateAddressesRequest update_request:  (required)
        :return: ShopifySubscriptionVersion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'update_request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_addresses" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update_addresses`")
        # verify the required parameter 'update_request' is set
        if ('update_request' not in params or
                params['update_request'] is None):
            raise ValueError("Missing the required parameter `update_request` when calling `update_addresses`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'update_request' in params:
            body_params = params['update_request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/shopify-subscription/update-addresses', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ShopifySubscriptionVersion',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
