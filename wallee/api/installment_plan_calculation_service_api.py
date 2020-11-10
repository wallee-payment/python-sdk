# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class InstallmentPlanCalculationServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def calculate_plans(self, space_id, transaction_id, **kwargs):
        """Calculate Plans

        This operation allows to calculate all plans for the given transaction. The transaction will not be changed in any way.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_plans(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The transaction for which the plans should be calculated for. (required)
        :return: list[InstallmentCalculatedPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.calculate_plans_with_http_info(space_id, transaction_id, **kwargs)
        else:
            (data) = self.calculate_plans_with_http_info(space_id, transaction_id, **kwargs)
            return data

    def calculate_plans_with_http_info(self, space_id, transaction_id, **kwargs):
        """Calculate Plans

        This operation allows to calculate all plans for the given transaction. The transaction will not be changed in any way.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.calculate_plans_with_http_info(space_id, transaction_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id:  (required)
        :param int transaction_id: The transaction for which the plans should be calculated for. (required)
        :return: list[InstallmentCalculatedPlan]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'transaction_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method calculate_plans" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `calculate_plans`")
        # verify the required parameter 'transaction_id' is set
        if ('transaction_id' not in params or
                params['transaction_id'] is None):
            raise ValueError("Missing the required parameter `transaction_id` when calling `calculate_plans`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'transaction_id' in params:
            query_params.append(('transactionId', params['transaction_id']))

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
            '/installment-plan-calculation/calculatePlans', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[InstallmentCalculatedPlan]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
