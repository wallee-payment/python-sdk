# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class MerticUsageServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def calculate(self, space_id, start, end, **kwargs):
        """Calculate

        Calculates the consumed resources for the given space and time range.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate(space_id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param datetime start: The start date from which on the consumed units should be returned from. (required)
        :param datetime end: The end date to which the consumed units should be returned to. The end date is not included in the result. (required)
        :return: list[MetricUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.calculate_with_http_info(space_id, start, end, **kwargs)
        else:
            (data) = self.calculate_with_http_info(space_id, start, end, **kwargs)
            return data

    def calculate_with_http_info(self, space_id, start, end, **kwargs):
        """Calculate

        Calculates the consumed resources for the given space and time range.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_with_http_info(space_id, start, end, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param datetime start: The start date from which on the consumed units should be returned from. (required)
        :param datetime end: The end date to which the consumed units should be returned to. The end date is not included in the result. (required)
        :return: list[MetricUsage]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'start', 'end']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `calculate`")
        # verify the required parameter 'start' is set
        if ('start' not in params or
                params['start'] is None):
            raise ValueError("Missing the required parameter `start` when calling `calculate`")
        # verify the required parameter 'end' is set
        if ('end' not in params or
                params['end'] is None):
            raise ValueError("Missing the required parameter `end` when calling `calculate`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'start' in params:
            query_params.append(('start', params['start']))
        if 'end' in params:
            query_params.append(('end', params['end']))

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
            '/mertic-usage/calculate', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[MetricUsage]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
