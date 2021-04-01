# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class WebAppServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def check_installation(self, space_id, **kwargs):
        """Check Installation

        This operation returns true when the app is installed in given space. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_installation(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This parameter identifies the space which should be checked if the web app is installed. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.check_installation_with_http_info(space_id, **kwargs)
        else:
            (data) = self.check_installation_with_http_info(space_id, **kwargs)
            return data

    def check_installation_with_http_info(self, space_id, **kwargs):
        """Check Installation

        This operation returns true when the app is installed in given space. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.check_installation_with_http_info(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This parameter identifies the space which should be checked if the web app is installed. (required)
        :return: bool
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method check_installation" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `check_installation`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

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
            '/web-app/check-installation', 'GET',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='bool',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def confirm(self, request, **kwargs):
        """Confirm

        This operation confirms the app installation. This method has to be invoked after the user returns to the web app. The request of the user will contain the code as a request parameter. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebAppConfirmationRequest request:  (required)
        :return: WebAppConfirmationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.confirm_with_http_info(request, **kwargs)
        else:
            (data) = self.confirm_with_http_info(request, **kwargs)
            return data

    def confirm_with_http_info(self, request, **kwargs):
        """Confirm

        This operation confirms the app installation. This method has to be invoked after the user returns to the web app. The request of the user will contain the code as a request parameter. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.confirm_with_http_info(request, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param WebAppConfirmationRequest request:  (required)
        :return: WebAppConfirmationResponse
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['request']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method confirm" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'request' is set
        if ('request' not in params or
                params['request'] is None):
            raise ValueError("Missing the required parameter `request` when calling `confirm`")

        collection_formats = {}

        path_params = {}

        query_params = []

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        if 'request' in params:
            body_params = params['request']
        # HTTP header `Accept`
        header_params['Accept'] = self.api_client.select_header_accept(
            ['application/json;charset=utf-8'])

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/web-app/confirm', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='WebAppConfirmationResponse',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def uninstall(self, space_id, **kwargs):
        """Uninstall

        This operation uninstalls the web app from the provided space. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uninstall(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This parameter identifies the space within which the web app should be uninstalled. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.uninstall_with_http_info(space_id, **kwargs)
        else:
            (data) = self.uninstall_with_http_info(space_id, **kwargs)
            return data

    def uninstall_with_http_info(self, space_id, **kwargs):
        """Uninstall

        This operation uninstalls the web app from the provided space. The web app is implied by the client ID resp. user ID that is been used to invoke this operation.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.uninstall_with_http_info(space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int space_id: This parameter identifies the space within which the web app should be uninstalled. (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['space_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method uninstall" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `uninstall`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))

        header_params = {}

        form_params = []
        local_var_files = {}

        body_params = None
        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/web-app/uninstall', 'POST',
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
