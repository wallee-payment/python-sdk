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

from pydantic import Field, StrictBytes, StrictInt, StrictStr
from typing import List, Optional, Tuple, Union
from typing_extensions import Annotated
from wallee.models.human_user import HumanUser
from wallee.models.human_user_create import HumanUserCreate
from wallee.models.human_user_list_response import HumanUserListResponse
from wallee.models.human_user_search_response import HumanUserSearchResponse
from wallee.models.human_user_update import HumanUserUpdate
from wallee.models.sorting_order import SortingOrder

from wallee.api_client import ApiClient, RequestSerialized
from wallee.api_response import ApiResponse
from wallee.rest import RESTResponseType



class HumanUsersService:
    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)


    @validate_call
    def delete_human_users_id(
        self,
        id: StrictInt,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Delete a human user

        Permanently deletes a human user. It cannot be undone.
        

        :param id: (required)
        :type id: int
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

        _param = self._delete_human_users_id_serialize(
            id=id,
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
    def delete_human_users_id_with_http_info(
        self,
        id: StrictInt,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Delete a human user

        Permanently deletes a human user. It cannot be undone.
        

        :param id: (required)
        :type id: int
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

        _param = self._delete_human_users_id_serialize(
            id=id,
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
    def delete_human_users_id_without_preload_content(
        self,
        id: StrictInt,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Delete a human user

        Permanently deletes a human user. It cannot be undone.
        

        :param id: (required)
        :type id: int
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

        _param = self._delete_human_users_id_serialize(
            id=id,
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


    def _delete_human_users_id_serialize(
        self,
        id,
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        # process the header parameters
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
            resource_path='/human-users/{id}',
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
    def get_human_users(
        self,
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HumanUserListResponse:
        """List all human users



        :param after: Set to an object's ID to retrieve the page of objects coming immediately after the named object.
        :type after: int
        :param before: Set to an object's ID to retrieve the page of objects coming immediately before the named object.
        :type before: int
        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param order: Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.
        :type order: SortingOrder
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

        _param = self._get_human_users_serialize(
            after=after,
            before=before,
            expand=expand,
            limit=limit,
            order=order,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserListResponse",
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
    def get_human_users_with_http_info(
        self,
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HumanUserListResponse]:
        """List all human users



        :param after: Set to an object's ID to retrieve the page of objects coming immediately after the named object.
        :type after: int
        :param before: Set to an object's ID to retrieve the page of objects coming immediately before the named object.
        :type before: int
        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param order: Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.
        :type order: SortingOrder
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

        _param = self._get_human_users_serialize(
            after=after,
            before=before,
            expand=expand,
            limit=limit,
            order=order,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserListResponse",
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
    def get_human_users_without_preload_content(
        self,
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all human users



        :param after: Set to an object's ID to retrieve the page of objects coming immediately after the named object.
        :type after: int
        :param before: Set to an object's ID to retrieve the page of objects coming immediately before the named object.
        :type before: int
        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param order: Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.
        :type order: SortingOrder
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

        _param = self._get_human_users_serialize(
            after=after,
            before=before,
            expand=expand,
            limit=limit,
            order=order,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserListResponse",
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


    def _get_human_users_serialize(
        self,
        after,
        before,
        expand,
        limit,
        order,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
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
        # process the query parameters
        if after is not None:
            
            _query_params.append(('after', after))
            
        if before is not None:
            
            _query_params.append(('before', before))
            
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if order is not None:
            
            _query_params.append(('order', order.value))
            
        # process the header parameters
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
            resource_path='/human-users',
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
    def get_human_users_export(
        self,
        fields: Annotated[Optional[List[StrictStr]], Field(description="The fields to be included in the export.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned. Default is 2,000.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=100000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> bytearray:
        """Export human users

        Export human users into a CSV file.
        
        (The read time out for this request is 60 seconds.)

        :param fields: The fields to be included in the export.
        :type fields: List[str]
        :param limit: A limit on the number of objects to be returned. Default is 2,000.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_export_serialize(
            fields=fields,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
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
            _request_timeout = 60
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        ).data


    @validate_call
    def get_human_users_export_with_http_info(
        self,
        fields: Annotated[Optional[List[StrictStr]], Field(description="The fields to be included in the export.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned. Default is 2,000.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=100000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[bytearray]:
        """Export human users

        Export human users into a CSV file.
        
        (The read time out for this request is 60 seconds.)

        :param fields: The fields to be included in the export.
        :type fields: List[str]
        :param limit: A limit on the number of objects to be returned. Default is 2,000.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_export_serialize(
            fields=fields,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
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
            _request_timeout = 60
        )
        response_data.read()
        return self.api_client.response_deserialize(
            response_data=response_data,
            response_types_map=_response_types_map,
        )


    @validate_call
    def get_human_users_export_without_preload_content(
        self,
        fields: Annotated[Optional[List[StrictStr]], Field(description="The fields to be included in the export.")] = None,
        limit: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned. Default is 2,000.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=100000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Export human users

        Export human users into a CSV file.
        
        (The read time out for this request is 60 seconds.)

        :param fields: The fields to be included in the export.
        :type fields: List[str]
        :param limit: A limit on the number of objects to be returned. Default is 2,000.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_export_serialize(
            fields=fields,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "bytearray",
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
            _request_timeout = 60
        )
        return response_data.response


    def _get_human_users_export_serialize(
        self,
        fields,
        limit,
        offset,
        order,
        query,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'fields': 'multi',
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
        # process the query parameters
        if fields is not None:
            
            _query_params.append(('fields', fields))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if order is not None:
            
            _query_params.append(('order', order))
            
        if query is not None:
            
            _query_params.append(('query', query))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'text/csv', 
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='GET',
            resource_path='/human-users/export',
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
    def get_human_users_id(
        self,
        id: StrictInt,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HumanUser:
        """Retrieve a human user



        :param id: (required)
        :type id: int
        :param expand:
        :type expand: List[str]
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

        _param = self._get_human_users_id_serialize(
            id=id,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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
    def get_human_users_id_with_http_info(
        self,
        id: StrictInt,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HumanUser]:
        """Retrieve a human user



        :param id: (required)
        :type id: int
        :param expand:
        :type expand: List[str]
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

        _param = self._get_human_users_id_serialize(
            id=id,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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
    def get_human_users_id_without_preload_content(
        self,
        id: StrictInt,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve a human user



        :param id: (required)
        :type id: int
        :param expand:
        :type expand: List[str]
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

        _param = self._get_human_users_id_serialize(
            id=id,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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


    def _get_human_users_id_serialize(
        self,
        id,
        expand,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        # process the header parameters
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
            resource_path='/human-users/{id}',
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
    def get_human_users_search(
        self,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HumanUserSearchResponse:
        """Search human users



        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_search_serialize(
            expand=expand,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserSearchResponse",
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
    def get_human_users_search_with_http_info(
        self,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HumanUserSearchResponse]:
        """Search human users



        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_search_serialize(
            expand=expand,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserSearchResponse",
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
    def get_human_users_search_without_preload_content(
        self,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search human users



        :param expand:
        :type expand: List[str]
        :param limit: A limit on the number of objects to be returned, between 1 and 100. Default is 10.
        :type limit: int
        :param offset: A cursor for pagination, specifies the number of objects to skip.
        :type offset: int
        :param order: The fields and order to sort the objects by.
        :type order: str
        :param query: The search query to filter the objects by.
        :type query: str
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

        _param = self._get_human_users_search_serialize(
            expand=expand,
            limit=limit,
            offset=offset,
            order=order,
            query=query,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUserSearchResponse",
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


    def _get_human_users_search_serialize(
        self,
        expand,
        limit,
        offset,
        order,
        query,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
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
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        if limit is not None:
            
            _query_params.append(('limit', limit))
            
        if offset is not None:
            
            _query_params.append(('offset', offset))
            
        if order is not None:
            
            _query_params.append(('order', order))
            
        if query is not None:
            
            _query_params.append(('query', query))
            
        # process the header parameters
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
            resource_path='/human-users/search',
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
    def patch_human_users_id(
        self,
        id: StrictInt,
        human_user_update: HumanUserUpdate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HumanUser:
        """Update a human user



        :param id: (required)
        :type id: int
        :param human_user_update: (required)
        :type human_user_update: HumanUserUpdate
        :param expand:
        :type expand: List[str]
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

        _param = self._patch_human_users_id_serialize(
            id=id,
            human_user_update=human_user_update,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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
    def patch_human_users_id_with_http_info(
        self,
        id: StrictInt,
        human_user_update: HumanUserUpdate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HumanUser]:
        """Update a human user



        :param id: (required)
        :type id: int
        :param human_user_update: (required)
        :type human_user_update: HumanUserUpdate
        :param expand:
        :type expand: List[str]
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

        _param = self._patch_human_users_id_serialize(
            id=id,
            human_user_update=human_user_update,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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
    def patch_human_users_id_without_preload_content(
        self,
        id: StrictInt,
        human_user_update: HumanUserUpdate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update a human user



        :param id: (required)
        :type id: int
        :param human_user_update: (required)
        :type human_user_update: HumanUserUpdate
        :param expand:
        :type expand: List[str]
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

        _param = self._patch_human_users_id_serialize(
            id=id,
            human_user_update=human_user_update,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "HumanUser",
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


    def _patch_human_users_id_serialize(
        self,
        id,
        human_user_update,
        expand,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if human_user_update is not None:
            _body_params = human_user_update


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        return self.api_client.param_serialize(
            method='PATCH',
            resource_path='/human-users/{id}',
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
    def post_human_users(
        self,
        human_user_create: HumanUserCreate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> HumanUser:
        """Create a human user



        :param human_user_create: (required)
        :type human_user_create: HumanUserCreate
        :param expand:
        :type expand: List[str]
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

        _param = self._post_human_users_serialize(
            human_user_create=human_user_create,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "HumanUser",
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
    def post_human_users_with_http_info(
        self,
        human_user_create: HumanUserCreate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[HumanUser]:
        """Create a human user



        :param human_user_create: (required)
        :type human_user_create: HumanUserCreate
        :param expand:
        :type expand: List[str]
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

        _param = self._post_human_users_serialize(
            human_user_create=human_user_create,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "HumanUser",
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
    def post_human_users_without_preload_content(
        self,
        human_user_create: HumanUserCreate,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create a human user



        :param human_user_create: (required)
        :type human_user_create: HumanUserCreate
        :param expand:
        :type expand: List[str]
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

        _param = self._post_human_users_serialize(
            human_user_create=human_user_create,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "HumanUser",
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


    def _post_human_users_serialize(
        self,
        human_user_create,
        expand,
        _content_type,
        _headers,
        _host_index,
    ) -> RequestSerialized:

        _host = None

        _collection_formats: Dict[str, str] = {
            'expand': 'multi',
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
        # process the query parameters
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
        # process the header parameters
        # process the form parameters
        # process the body parameter
        if human_user_create is not None:
            _body_params = human_user_create


        # set the HTTP header `Accept`
        if 'Accept' not in _header_params:
            _header_params['Accept'] = self.api_client.select_header_accept(
                [
                    'application/json'
                ]
            )

        # set the HTTP header `Content-Type`
        if _content_type:
            _header_params['Content-Type'] = _content_type
        else:
            _default_content_type = (
                self.api_client.select_header_content_type(
                    [
                        'application/json'
                    ]
                )
            )
            if _default_content_type is not None:
                _header_params['Content-Type'] = _default_content_type

        return self.api_client.param_serialize(
            method='POST',
            resource_path='/human-users',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )



