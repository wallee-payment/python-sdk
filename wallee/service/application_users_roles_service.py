# coding: utf-8

"""
Wallee AG Python SDK

This library allows to interact with the Wallee AG payment service.

Copyright owner: Wallee AG
Website: https://en.wallee.com
Developer email: ecosystem-team@wallee.com

Licensed under the Apache License, Version 2.0 (the "License");
you may not use this file except in compliance with the License.
You may obtain a copy of the License at

     http://www.apache.org/licenses/LICENSE-2.0

Unless required by applicable law or agreed to in writing, software
distributed under the License is distributed on an "AS IS" BASIS,
WITHOUT WARRANTIES OR CONDITIONS OF ANY KIND, either express or implied.
See the License for the specific language governing permissions and
limitations under the License.
"""


import warnings
from pydantic import validate_call, Field, StrictFloat, StrictStr, StrictInt
from typing import Any, Dict, List, Optional, Tuple, Union
from typing_extensions import Annotated

from pydantic import Field, StrictBool, StrictInt
from typing import Optional
from typing_extensions import Annotated
from wallee.models.user_account_role import UserAccountRole
from wallee.models.user_account_role_list_response import UserAccountRoleListResponse
from wallee.models.user_space_role import UserSpaceRole
from wallee.models.user_space_role_list_response import UserSpaceRoleListResponse

from wallee.api_client import ApiClient, RequestSerialized
from wallee.api_response import ApiResponse
from wallee.rest import RESTResponseType



class ApplicationUsersRolesService:
    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)


    @validate_call
    def delete_application_users_user_id_account_roles(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Unassign a role from an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_application_users_user_id_account_roles_with_http_info(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Unassign a role from an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_application_users_user_id_account_roles_without_preload_content(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Unassign a role from an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _delete_application_users_user_id_account_roles_serialize(
        self,
        user_id,
        role_id,
        account,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if role_id is not None:
            
            _query_params.append(('roleId', role_id))
            
        # process the header parameters
        if account is not None:
            _header_params['Account'] = account
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/application-users/{userId}/account-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )





    @validate_call
    def delete_application_users_user_id_space_roles(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Unassign a role from an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def delete_application_users_user_id_space_roles_with_http_info(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Unassign a role from an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def delete_application_users_user_id_space_roles_without_preload_content(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Unassign a role from an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._delete_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '204': None,
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _delete_application_users_user_id_space_roles_serialize(
        self,
        user_id,
        role_id,
        space,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if role_id is not None:
            
            _query_params.append(('roleId', role_id))
            
        # process the header parameters
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='DELETE',
            resource_path='/application-users/{userId}/space-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )





    @validate_call
    def get_application_users_user_id_account_roles(
        self,
        user_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserAccountRoleListResponse:
        """List all roles of an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_application_users_user_id_account_roles_with_http_info(
        self,
        user_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserAccountRoleListResponse]:
        """List all roles of an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_application_users_user_id_account_roles_without_preload_content(
        self,
        user_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all roles of an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            account=account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _get_application_users_user_id_account_roles_serialize(
        self,
        user_id,
        account,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        # process the header parameters
        if account is not None:
            _header_params['Account'] = account
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='GET',
            resource_path='/application-users/{userId}/account-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )





    @validate_call
    def get_application_users_user_id_space_roles(
        self,
        user_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserSpaceRoleListResponse:
        """List all roles of an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_application_users_user_id_space_roles_with_http_info(
        self,
        user_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserSpaceRoleListResponse]:
        """List all roles of an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_application_users_user_id_space_roles_without_preload_content(
        self,
        user_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all roles of an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._get_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRoleListResponse",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _get_application_users_user_id_space_roles_serialize(
        self,
        user_id,
        space,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        # process the header parameters
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='GET',
            resource_path='/application-users/{userId}/space-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )





    @validate_call
    def post_application_users_user_id_account_roles(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        applies_on_sub_account: Annotated[Optional[StrictBool], Field(description="Whether the role should be assigned to the user in subaccounts only.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserAccountRole:
        """Assign a role to an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param applies_on_sub_account: Whether the role should be assigned to the user in subaccounts only.
        :type applies_on_sub_account: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            applies_on_sub_account=applies_on_sub_account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def post_application_users_user_id_account_roles_with_http_info(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        applies_on_sub_account: Annotated[Optional[StrictBool], Field(description="Whether the role should be assigned to the user in subaccounts only.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserAccountRole]:
        """Assign a role to an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param applies_on_sub_account: Whether the role should be assigned to the user in subaccounts only.
        :type applies_on_sub_account: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            applies_on_sub_account=applies_on_sub_account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def post_application_users_user_id_account_roles_without_preload_content(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        account: Annotated[StrictInt, Field(description="Specifies the ID of the account the operation should be executed in.")],
        applies_on_sub_account: Annotated[Optional[StrictBool], Field(description="Whether the role should be assigned to the user in subaccounts only.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Assign a role to an application user for an account



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param account: Specifies the ID of the account the operation should be executed in. (required)
        :type account: int
        :param applies_on_sub_account: Whether the role should be assigned to the user in subaccounts only.
        :type applies_on_sub_account: bool
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_account_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            account=account,
            applies_on_sub_account=applies_on_sub_account,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserAccountRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _post_application_users_user_id_account_roles_serialize(
        self,
        user_id,
        role_id,
        account,
        applies_on_sub_account,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if role_id is not None:
            
            _query_params.append(('roleId', role_id))
            
        if applies_on_sub_account is not None:
            
            _query_params.append(('appliesOnSubAccount', applies_on_sub_account))
            
        # process the header parameters
        if account is not None:
            _header_params['Account'] = account
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='POST',
            resource_path='/application-users/{userId}/account-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )





    @validate_call
    def post_application_users_user_id_space_roles(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> UserSpaceRole:
        """Assign a role to an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def post_application_users_user_id_space_roles_with_http_info(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[UserSpaceRole]:
        """Assign a role to an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }

        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def post_application_users_user_id_space_roles_without_preload_content(
        self,
        user_id: StrictInt,
        role_id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Assign a role to an application user for a space



        :param user_id: (required)
        :type user_id: int
        :param role_id: (required)
        :type role_id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param _request_timeout: timeout setting for this request. If one
                                 number provided, it will be total request
                                 timeout. It can also be a pair (tuple) of
                                 (connection, read) timeouts.
        :type _request_timeout: int, tuple(int, int), optional
        :param _content_type: force content-type for the request.
        :type _content_type: str, Optional
        :param _headers: set to override the headers for a single
                         request; this effectively ignores the headers
                         in the spec for a single request.
        :type _headers: dict, optional
        :param _host_index: set to override the host_index for a single
                            request; this effectively ignores the host_index
                            in the spec for a single request.
        :type _host_index: int, optional
        :return: Returns the result object.
        """ # noqa: E501

        _param = self._post_application_users_user_id_space_roles_serialize(
            user_id=user_id,
            role_id=role_id,
            space=space,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "UserSpaceRole",
            '400': "RestApiErrorResponse",
            '401': "RestApiErrorResponse",
            '403': "RestApiErrorResponse",
            '404': "RestApiErrorResponse",
            '406': "RestApiErrorResponse",
            '409': "RestApiErrorResponse",
            '415': "RestApiErrorResponse",
            '422': "RestApiErrorResponse",
            '429': "RestApiErrorResponse",
            '5XX': "RestApiErrorResponse",
        }
        response_data = self.api_client.call_api(
            *_param,
            _request_timeout = self.api_client.configuration.request_timeout
        )
        return response_data.response


    def _post_application_users_user_id_space_roles_serialize(
        self,
        user_id,
        role_id,
        space,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
        }

        _path_params: Dict[str, str] = {}
        _query_params: List[Tuple[str, str]] = []
        _header_params: Dict[str, Optional[str]] = _headers or {}
        _form_params: List[Tuple[str, str]] = []
        _files: Dict[
            str, Union[str, bytes, List[str], List[bytes], List[Tuple[str, bytes]]]
        ] = {}
        _body_params: Optional[bytes] = None

        # process the path parameters
        if user_id is not None:
            _path_params['userId'] = user_id
        # process the query parameters
        if role_id is not None:
            
            _query_params.append(('roleId', role_id))
            
        # process the header parameters
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='POST',
            resource_path='/application-users/{userId}/space-roles',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )



