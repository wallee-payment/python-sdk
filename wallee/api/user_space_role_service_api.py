# coding: utf-8

from __future__ import absolute_import

import six

from wallee.api_client import ApiClient

class UserSpaceRoleServiceApi:

    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)

    def add_role(self, user_id, space_id, role_id, **kwargs):
        """Add Role

        This operation grants the given role to the user in the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_role(user_id, space_id, role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: The id of the user to whom the role is assigned. (required)
        :param int space_id: The space to which the role is mapped. (required)
        :param int role_id: The role which is mapped to the user and space. (required)
        :return: UserSpaceRole
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.add_role_with_http_info(user_id, space_id, role_id, **kwargs)
        else:
            (data) = self.add_role_with_http_info(user_id, space_id, role_id, **kwargs)
            return data

    def add_role_with_http_info(self, user_id, space_id, role_id, **kwargs):
        """Add Role

        This operation grants the given role to the user in the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.add_role_with_http_info(user_id, space_id, role_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: The id of the user to whom the role is assigned. (required)
        :param int space_id: The space to which the role is mapped. (required)
        :param int role_id: The role which is mapped to the user and space. (required)
        :return: UserSpaceRole
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'space_id', 'role_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method add_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `add_role`")
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `add_role`")
        # verify the required parameter 'role_id' is set
        if ('role_id' not in params or
                params['role_id'] is None):
            raise ValueError("Missing the required parameter `role_id` when calling `add_role`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))
        if 'space_id' in params:
            query_params.append(('spaceId', params['space_id']))
        if 'role_id' in params:
            query_params.append(('roleId', params['role_id']))

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
            '/user-space-role/addRole', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='UserSpaceRole',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def list(self, user_id, space_id, **kwargs):
        """List Roles

        List all the roles that are assigned to the given user in the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list(user_id, space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: The id of the user to whom the role is assigned. (required)
        :param int space_id: The space to which the role is mapped. (required)
        :return: list[UserSpaceRole]
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.list_with_http_info(user_id, space_id, **kwargs)
        else:
            (data) = self.list_with_http_info(user_id, space_id, **kwargs)
            return data

    def list_with_http_info(self, user_id, space_id, **kwargs):
        """List Roles

        List all the roles that are assigned to the given user in the given space.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.list_with_http_info(user_id, space_id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int user_id: The id of the user to whom the role is assigned. (required)
        :param int space_id: The space to which the role is mapped. (required)
        :return: list[UserSpaceRole]
                 If the method is called asynchronously,
                 returns the request thread.
        """

        all_params = ['user_id', 'space_id']
        all_params.append('async_req')
        all_params.append('_return_http_data_only')
        all_params.append('_preload_content')
        all_params.append('_request_timeout')

        params = locals()
        for key, val in six.iteritems(params['kwargs']):
            if key not in all_params:
                raise TypeError(
                    "Got an unexpected keyword argument '%s'"
                    " to method list" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'user_id' is set
        if ('user_id' not in params or
                params['user_id'] is None):
            raise ValueError("Missing the required parameter `user_id` when calling `list`")
        # verify the required parameter 'space_id' is set
        if ('space_id' not in params or
                params['space_id'] is None):
            raise ValueError("Missing the required parameter `space_id` when calling `list`")

        collection_formats = {}

        path_params = {}

        query_params = []
        if 'user_id' in params:
            query_params.append(('userId', params['user_id']))
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
            '/user-space-role/list', 'POST',
            path_params,
            query_params,
            header_params,
            body=body_params,
            post_params=form_params,
            files=local_var_files,
            response_type='list[UserSpaceRole]',
            auth_settings=auth_settings,
            async_req=params.get('async_req'),
            _return_http_data_only=params.get('_return_http_data_only'),
            _preload_content=params.get('_preload_content', True),
            _request_timeout=params.get('_request_timeout'),
            collection_formats=collection_formats)

    def remove_role(self, id, **kwargs):
        """Remove Role

        This operation removes the specified user space role.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_role(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of user space role which should be removed (required)
        :return: None
                 If the method is called asynchronously,
                 returns the request thread.
        """
        kwargs['_return_http_data_only'] = True


        if kwargs.get('async_req'):
            return self.remove_role_with_http_info(id, **kwargs)
        else:
            (data) = self.remove_role_with_http_info(id, **kwargs)
            return data

    def remove_role_with_http_info(self, id, **kwargs):
        """Remove Role

        This operation removes the specified user space role.
        This method makes a synchronous HTTP request by default. To make an
        asynchronous HTTP request, please pass async_req=True
        >>> thread = api.remove_role_with_http_info(id, async_req=True)
        >>> result = thread.get()

        :param async_req bool
        :param int id: The id of user space role which should be removed (required)
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
                    " to method remove_role" % key
                )
            params[key] = val
        del params['kwargs']
        # verify the required parameter 'id' is set
        if ('id' not in params or
                params['id'] is None):
            raise ValueError("Missing the required parameter `id` when calling `remove_role`")

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

        # Authentication setting
        auth_settings = []

        return self.api_client.call_api(
            '/user-space-role/removeRole', 'POST',
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
