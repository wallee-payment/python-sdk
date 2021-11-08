# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class PaymentWebAppServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def activate_processor_for_production(self, space_id, external_id, **kwargs):
        """Activate Processor for Production

        This operation marks the processor to be usable within the production environment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_processor_for_production(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the processor is installed in. (required)
        :param str external_id: The external ID identifies the processor. The external ID corresponds to the ID provided during inserting of the processor. (required)
        :return: PaymentAppProcessor
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.activate_processor_for_production_with_http_info(space_id, external_id, **kwargs)
        else:
            (data) = self.activate_processor_for_production_with_http_info(space_id, external_id, **kwargs)
            return data

    def activate_processor_for_production_with_http_info(self, space_id, external_id, **kwargs):
        """Activate Processor for Production

        This operation marks the processor to be usable within the production environment.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.activate_processor_for_production_with_http_info(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the processor is installed in. (required)
        :param str external_id: The external ID identifies the processor. The external ID corresponds to the ID provided during inserting of the processor. (required)
        :return: PaymentAppProcessor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'external_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method activate_processor_for_production" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `activate_processor_for_production`")
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `activate_processor_for_production`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'external_id' in params:
            query_params.append(('externalId', params['external_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # HTTP header `Content-Type`
        header_params['Content-Type'] = self.api_client.select_header_content_type(
            ['*/*'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/activate-processor-for-production', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentAppProcessor',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def delete_connector(self, space_id, external_id, **kwargs):
        """Delete Connector

        This operation removes the web app payment connector from the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connector(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the connector is installed in. (required)
        :param str external_id: The external ID identifies the connector. The external ID corresponds to the ID provided during inserting of the connector. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.delete_connector_with_http_info(space_id, external_id, **kwargs)
        else:
            (data) = self.delete_connector_with_http_info(space_id, external_id, **kwargs)
            return data

    def delete_connector_with_http_info(self, space_id, external_id, **kwargs):
        """Delete Connector

        This operation removes the web app payment connector from the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_connector_with_http_info(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the connector is installed in. (required)
        :param str external_id: The external ID identifies the connector. The external ID corresponds to the ID provided during inserting of the connector. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'external_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `delete_connector`")
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `delete_connector`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'external_id' in params:
            query_params.append(('externalId', params['external_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/delete-connector', 'POST',
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

    def delete_processor(self, space_id, external_id, **kwargs):
        """Delete Processor

        This operation removes the web app payment processor and its connectors from the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_processor(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the processor is installed in. (required)
        :param str external_id: The external ID identifies the processor. The external ID corresponds to the ID provided during inserting of the processor. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.delete_processor_with_http_info(space_id, external_id, **kwargs)
        else:
            (data) = self.delete_processor_with_http_info(space_id, external_id, **kwargs)
            return data

    def delete_processor_with_http_info(self, space_id, external_id, **kwargs):
        """Delete Processor

        This operation removes the web app payment processor and its connectors from the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.delete_processor_with_http_info(space_id, external_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space in which the processor is installed in. (required)
        :param str external_id: The external ID identifies the processor. The external ID corresponds to the ID provided during inserting of the processor. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'external_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method delete_processor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `delete_processor`")
        # verify the required parameter 'external_id' is set
        if ('external_id' not in params or
                params['external_id'] is None):
            raise ValueError("Missing the required parameter `external_id` when calling `delete_processor`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'external_id' in params:
            query_params.append(('externalId', params['external_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/delete-processor', 'POST',
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

    def insert_or_update_connector(self, space_id, request, **kwargs):
        """Insert or Update Connector

        This operation inserts or updates a web app payment connector.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_or_update_connector(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space into which the connector should be inserted into. (required)
        :param PaymentAppConnectorCreationRequest request: The connector object contains all the details required to create or update a web app connector. (required)
        :return: PaymentAppConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.insert_or_update_connector_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.insert_or_update_connector_with_http_info(space_id, request, **kwargs)
            return data

    def insert_or_update_connector_with_http_info(self, space_id, request, **kwargs):
        """Insert or Update Connector

        This operation inserts or updates a web app payment connector.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_or_update_connector_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space into which the connector should be inserted into. (required)
        :param PaymentAppConnectorCreationRequest request: The connector object contains all the details required to create or update a web app connector. (required)
        :return: PaymentAppConnector
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_or_update_connector" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `insert_or_update_connector`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `insert_or_update_connector`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/insert-or-update-connector', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentAppConnector',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def insert_or_update_processor(self, space_id, request, **kwargs):
        """Insert or Update Processor

        This operation inserts or updates a web app payment processor.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_or_update_processor(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space into which the processor should be inserted into. (required)
        :param PaymentAppProcessorCreationRequest request: The processor object contains all the details required to create or update a web app processor. (required)
        :return: PaymentAppProcessor
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.insert_or_update_processor_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.insert_or_update_processor_with_http_info(space_id, request, **kwargs)
            return data

    def insert_or_update_processor_with_http_info(self, space_id, request, **kwargs):
        """Insert or Update Processor

        This operation inserts or updates a web app payment processor.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.insert_or_update_processor_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: The space ID identifies the space into which the processor should be inserted into. (required)
        :param PaymentAppProcessorCreationRequest request: The processor object contains all the details required to create or update a web app processor. (required)
        :return: PaymentAppProcessor
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method insert_or_update_processor" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `insert_or_update_processor`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `insert_or_update_processor`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/insert-or-update-processor', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='PaymentAppProcessor',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_charge_attempt(self, space_id, request, **kwargs):
        """Update Charge Attempt

        This operation updates the state of the charge attempt. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned charge attempt corresponds to the charge attempt indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_charge_attempt(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the charge attempt is located in. (required)
        :param PaymentAppChargeAttemptUpdateRequest request: The charge attempt update request allows to update the state of a charge attempt. (required)
        :return: ChargeAttempt
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_charge_attempt_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.update_charge_attempt_with_http_info(space_id, request, **kwargs)
            return data

    def update_charge_attempt_with_http_info(self, space_id, request, **kwargs):
        """Update Charge Attempt

        This operation updates the state of the charge attempt. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned charge attempt corresponds to the charge attempt indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_charge_attempt_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the charge attempt is located in. (required)
        :param PaymentAppChargeAttemptUpdateRequest request: The charge attempt update request allows to update the state of a charge attempt. (required)
        :return: ChargeAttempt
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_charge_attempt" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update_charge_attempt`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `update_charge_attempt`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/update-charge-attempt', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='ChargeAttempt',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_completion(self, space_id, request, **kwargs):
        """Update Completion

        This operation updates the state of the transaction completion. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned completion corresponds to the completion indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_completion(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the completion is located in. (required)
        :param PaymentAppCompletionUpdateRequest request: The completion update request allows to update the state of a completion. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_completion_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.update_completion_with_http_info(space_id, request, **kwargs)
            return data

    def update_completion_with_http_info(self, space_id, request, **kwargs):
        """Update Completion

        This operation updates the state of the transaction completion. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned completion corresponds to the completion indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_completion_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the completion is located in. (required)
        :param PaymentAppCompletionUpdateRequest request: The completion update request allows to update the state of a completion. (required)
        :return: TransactionCompletion
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_completion" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update_completion`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `update_completion`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/update-completion', 'POST',
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

    def update_refund(self, space_id, request, **kwargs):
        """Update Refund

        This operation updates the state of the refund. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned refund corresponds to the refund indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_refund(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the refund is located in. (required)
        :param PaymentAppRefundUpdateRequest request: The refund update request allows to update the state of a refund. (required)
        :return: Refund
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_refund_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.update_refund_with_http_info(space_id, request, **kwargs)
            return data

    def update_refund_with_http_info(self, space_id, request, **kwargs):
        """Update Refund

        This operation updates the state of the refund. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned refund corresponds to the refund indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_refund_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the refund is located in. (required)
        :param PaymentAppRefundUpdateRequest request: The refund update request allows to update the state of a refund. (required)
        :return: Refund
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_refund" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update_refund`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `update_refund`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/update-refund', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='Refund',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def update_void(self, space_id, request, **kwargs):
        """Update Void

        This operation updates the state of the transaction void. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned void corresponds to the void indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_void(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the void is located in. (required)
        :param PaymentAppVoidUpdateRequest request: The void update request allows to update the state of a void. (required)
        :return: TransactionVoid
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.update_void_with_http_info(space_id, request, **kwargs)
        else:
            (data) = self.update_void_with_http_info(space_id, request, **kwargs)
            return data

    def update_void_with_http_info(self, space_id, request, **kwargs):
        """Update Void

        This operation updates the state of the transaction void. This method can be invoked for transactions originally created with a processor associated with the web app that invokes this operation. The returned void corresponds to the void indicated in the request.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.update_void_with_http_info(space_id, request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This is the ID of the space in which the void is located in. (required)
        :param PaymentAppVoidUpdateRequest request: The void update request allows to update the state of a void. (required)
        :return: TransactionVoid
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id', 'request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method update_void" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `update_void`")
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `update_void`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/payment-web-app/update-void', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='TransactionVoid',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)
