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

from pydantic import Field, StrictBool, StrictInt, StrictStr
from typing import List, Optional
from typing_extensions import Annotated
from wallee.models.invoice_search_response import InvoiceSearchResponse
from wallee.models.sorting_order import SortingOrder
from wallee.models.subscription import Subscription
from wallee.models.subscription_charge import SubscriptionCharge
from wallee.models.subscription_create_request import SubscriptionCreateRequest
from wallee.models.subscription_initialize_subscriber_present_request import SubscriptionInitializeSubscriberPresentRequest
from wallee.models.subscription_list_response import SubscriptionListResponse
from wallee.models.subscription_search_response import SubscriptionSearchResponse
from wallee.models.subscription_suspension import SubscriptionSuspension
from wallee.models.subscription_update_request import SubscriptionUpdateRequest
from wallee.models.subscription_version import SubscriptionVersion
from wallee.models.suspension_creation_request import SuspensionCreationRequest

from wallee.api_client import ApiClient, RequestSerialized
from wallee.api_response import ApiResponse
from wallee.rest import RESTResponseType



class SubscriptionsService:
    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)


    @validate_call
    def get_subscriptions(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionListResponse:
        """List all subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_serialize(
            space=space,
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
            '200': "SubscriptionListResponse",
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
    def get_subscriptions_with_http_info(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionListResponse]:
        """List all subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_serialize(
            space=space,
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
            '200': "SubscriptionListResponse",
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
    def get_subscriptions_without_preload_content(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        after: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately after the named object.")] = None,
        before: Annotated[Optional[Annotated[int, Field(strict=True, ge=1)]], Field(description="Set to an object's ID to retrieve the page of objects coming immediately before the named object.")] = None,
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        order: Annotated[Optional[SortingOrder], Field(description="Specify to retrieve objects in chronological (ASC) or reverse chronological (DESC) order.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """List all subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_serialize(
            space=space,
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
            '200': "SubscriptionListResponse",
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


    def _get_subscriptions_serialize(
        self,
        space,
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
            resource_path='/subscriptions',
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
    def get_subscriptions_id(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Subscription:
        """Retrieve a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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
    def get_subscriptions_id_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Subscription]:
        """Retrieve a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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
    def get_subscriptions_id_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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


    def _get_subscriptions_id_serialize(
        self,
        id,
        space,
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
            resource_path='/subscriptions/{id}',
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
    def get_subscriptions_id_invoices(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> InvoiceSearchResponse:
        """Search subscription invoices



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_invoices_serialize(
            id=id,
            space=space,
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
            '200': "InvoiceSearchResponse",
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
    def get_subscriptions_id_invoices_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[InvoiceSearchResponse]:
        """Search subscription invoices



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_invoices_serialize(
            id=id,
            space=space,
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
            '200': "InvoiceSearchResponse",
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
    def get_subscriptions_id_invoices_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search subscription invoices



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_id_invoices_serialize(
            id=id,
            space=space,
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
            '200': "InvoiceSearchResponse",
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


    def _get_subscriptions_id_invoices_serialize(
        self,
        id,
        space,
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
        if id is not None:
            _path_params['id'] = id
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
            resource_path='/subscriptions/{id}/invoices',
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
    def get_subscriptions_search(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionSearchResponse:
        """Search subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_search_serialize(
            space=space,
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
            '200': "SubscriptionSearchResponse",
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
    def get_subscriptions_search_with_http_info(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionSearchResponse]:
        """Search subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_search_serialize(
            space=space,
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
            '200': "SubscriptionSearchResponse",
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
    def get_subscriptions_search_without_preload_content(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        limit: Annotated[Optional[Annotated[int, Field(le=100, strict=True, ge=1)]], Field(description="A limit on the number of objects to be returned, between 1 and 100. Default is 10.")] = None,
        offset: Annotated[Optional[Annotated[int, Field(le=10000, strict=True)]], Field(description="A cursor for pagination, specifies the number of objects to skip.")] = None,
        order: Annotated[Optional[StrictStr], Field(description="The fields and order to sort the objects by.")] = None,
        query: Annotated[Optional[StrictStr], Field(description="The search query to filter the objects by.")] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Search subscriptions



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._get_subscriptions_search_serialize(
            space=space,
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
            '200': "SubscriptionSearchResponse",
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


    def _get_subscriptions_search_serialize(
        self,
        space,
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
            resource_path='/subscriptions/search',
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
    def patch_subscriptions_id(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> Subscription:
        """Update a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._patch_subscriptions_id_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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
    def patch_subscriptions_id_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[Subscription]:
        """Update a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._patch_subscriptions_id_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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
    def patch_subscriptions_id_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Update a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._patch_subscriptions_id_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "Subscription",
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


    def _patch_subscriptions_id_serialize(
        self,
        id,
        space,
        subscription_update_request,
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
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter
        if subscription_update_request is not None:
            _body_params = subscription_update_request


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
            resource_path='/subscriptions/{id}',
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
    def post_subscriptions(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_create_request: SubscriptionCreateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionVersion:
        """Create a subscription



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_create_request: (required)
        :type subscription_create_request: SubscriptionCreateRequest
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

        _param = self._post_subscriptions_serialize(
            space=space,
            subscription_create_request=subscription_create_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "SubscriptionVersion",
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
    def post_subscriptions_with_http_info(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_create_request: SubscriptionCreateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionVersion]:
        """Create a subscription



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_create_request: (required)
        :type subscription_create_request: SubscriptionCreateRequest
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

        _param = self._post_subscriptions_serialize(
            space=space,
            subscription_create_request=subscription_create_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "SubscriptionVersion",
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
    def post_subscriptions_without_preload_content(
        self,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_create_request: SubscriptionCreateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Create a subscription



        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_create_request: (required)
        :type subscription_create_request: SubscriptionCreateRequest
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

        _param = self._post_subscriptions_serialize(
            space=space,
            subscription_create_request=subscription_create_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '201': "SubscriptionVersion",
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


    def _post_subscriptions_serialize(
        self,
        space,
        subscription_create_request,
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
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter
        if subscription_create_request is not None:
            _body_params = subscription_create_request


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
            resource_path='/subscriptions',
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
    def post_subscriptions_id_apply_changes(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionVersion:
        """Apply changes to a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._post_subscriptions_id_apply_changes_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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
    def post_subscriptions_id_apply_changes_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionVersion]:
        """Apply changes to a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._post_subscriptions_id_apply_changes_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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
    def post_subscriptions_id_apply_changes_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_update_request: SubscriptionUpdateRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Apply changes to a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_update_request: (required)
        :type subscription_update_request: SubscriptionUpdateRequest
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

        _param = self._post_subscriptions_id_apply_changes_serialize(
            id=id,
            space=space,
            subscription_update_request=subscription_update_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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


    def _post_subscriptions_id_apply_changes_serialize(
        self,
        id,
        space,
        subscription_update_request,
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
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter
        if subscription_update_request is not None:
            _body_params = subscription_update_request


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
            resource_path='/subscriptions/{id}/apply-changes',
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
    def post_subscriptions_id_initialize(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionCharge:
        """Initialize a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_initialize_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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
    def post_subscriptions_id_initialize_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionCharge]:
        """Initialize a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_initialize_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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
    def post_subscriptions_id_initialize_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Initialize a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_initialize_serialize(
            id=id,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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


    def _post_subscriptions_id_initialize_serialize(
        self,
        id,
        space,
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
            resource_path='/subscriptions/{id}/initialize',
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
    def post_subscriptions_id_initialize_subscriber_present(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionCharge:
        """Initialize a subscription with the subscriber present



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_initialize_subscriber_present_request: (required)
        :type subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest
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

        _param = self._post_subscriptions_id_initialize_subscriber_present_serialize(
            id=id,
            space=space,
            subscription_initialize_subscriber_present_request=subscription_initialize_subscriber_present_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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
    def post_subscriptions_id_initialize_subscriber_present_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionCharge]:
        """Initialize a subscription with the subscriber present



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_initialize_subscriber_present_request: (required)
        :type subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest
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

        _param = self._post_subscriptions_id_initialize_subscriber_present_serialize(
            id=id,
            space=space,
            subscription_initialize_subscriber_present_request=subscription_initialize_subscriber_present_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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
    def post_subscriptions_id_initialize_subscriber_present_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Initialize a subscription with the subscriber present



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param subscription_initialize_subscriber_present_request: (required)
        :type subscription_initialize_subscriber_present_request: SubscriptionInitializeSubscriberPresentRequest
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

        _param = self._post_subscriptions_id_initialize_subscriber_present_serialize(
            id=id,
            space=space,
            subscription_initialize_subscriber_present_request=subscription_initialize_subscriber_present_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionCharge",
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


    def _post_subscriptions_id_initialize_subscriber_present_serialize(
        self,
        id,
        space,
        subscription_initialize_subscriber_present_request,
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
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter
        if subscription_initialize_subscriber_present_request is not None:
            _body_params = subscription_initialize_subscriber_present_request


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
            resource_path='/subscriptions/{id}/initialize-subscriber-present',
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
    def post_subscriptions_id_reactivate(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Reactivate a suspended subscription



        :param id: (required)
        :type id: int
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

        _param = self._post_subscriptions_id_reactivate_serialize(
            id=id,
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
    def post_subscriptions_id_reactivate_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Reactivate a suspended subscription



        :param id: (required)
        :type id: int
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

        _param = self._post_subscriptions_id_reactivate_serialize(
            id=id,
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
    def post_subscriptions_id_reactivate_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Reactivate a suspended subscription



        :param id: (required)
        :type id: int
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

        _param = self._post_subscriptions_id_reactivate_serialize(
            id=id,
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


    def _post_subscriptions_id_reactivate_serialize(
        self,
        id,
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
        if id is not None:
            _path_params['id'] = id
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
            method='POST',
            resource_path='/subscriptions/{id}/reactivate',
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
    def post_subscriptions_id_suspend(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        suspension_creation_request: SuspensionCreationRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionSuspension:
        """Suspend a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param suspension_creation_request: (required)
        :type suspension_creation_request: SuspensionCreationRequest
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

        _param = self._post_subscriptions_id_suspend_serialize(
            id=id,
            space=space,
            suspension_creation_request=suspension_creation_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionSuspension",
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
    def post_subscriptions_id_suspend_with_http_info(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        suspension_creation_request: SuspensionCreationRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionSuspension]:
        """Suspend a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param suspension_creation_request: (required)
        :type suspension_creation_request: SuspensionCreationRequest
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

        _param = self._post_subscriptions_id_suspend_serialize(
            id=id,
            space=space,
            suspension_creation_request=suspension_creation_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionSuspension",
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
    def post_subscriptions_id_suspend_without_preload_content(
        self,
        id: StrictInt,
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        suspension_creation_request: SuspensionCreationRequest,
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Suspend a subscription



        :param id: (required)
        :type id: int
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
        :param suspension_creation_request: (required)
        :type suspension_creation_request: SuspensionCreationRequest
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

        _param = self._post_subscriptions_id_suspend_serialize(
            id=id,
            space=space,
            suspension_creation_request=suspension_creation_request,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionSuspension",
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


    def _post_subscriptions_id_suspend_serialize(
        self,
        id,
        space,
        suspension_creation_request,
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
        if space is not None:
            _header_params['Space'] = space
        # process the form parameters
        # process the body parameter
        if suspension_creation_request is not None:
            _body_params = suspension_creation_request


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
            resource_path='/subscriptions/{id}/suspend',
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
    def post_subscriptions_id_terminate(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> None:
        """Terminate a subscription



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
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

        _param = self._post_subscriptions_id_terminate_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
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
    def post_subscriptions_id_terminate_with_http_info(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[None]:
        """Terminate a subscription



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
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

        _param = self._post_subscriptions_id_terminate_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
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
    def post_subscriptions_id_terminate_without_preload_content(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Terminate a subscription



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
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

        _param = self._post_subscriptions_id_terminate_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
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


    def _post_subscriptions_id_terminate_serialize(
        self,
        id,
        respect_termination_period,
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
        if id is not None:
            _path_params['id'] = id
        # process the query parameters
        if respect_termination_period is not None:
            
            _query_params.append(('respectTerminationPeriod', respect_termination_period))
            
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
            resource_path='/subscriptions/{id}/terminate',
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
    def post_subscriptions_id_upgrade_product(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> SubscriptionVersion:
        """Upgrade a subscription's product



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_upgrade_product_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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
    def post_subscriptions_id_upgrade_product_with_http_info(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[SubscriptionVersion]:
        """Upgrade a subscription's product



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_upgrade_product_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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
    def post_subscriptions_id_upgrade_product_without_preload_content(
        self,
        id: StrictInt,
        respect_termination_period: Annotated[StrictBool, Field(description="Whether the product's termination period should be respected.")],
        space: Annotated[StrictInt, Field(description="Specifies the ID of the space the operation should be executed in.")],
        expand: Optional[List[StrictStr]] = None,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Upgrade a subscription's product



        :param id: (required)
        :type id: int
        :param respect_termination_period: Whether the product's termination period should be respected. (required)
        :type respect_termination_period: bool
        :param space: Specifies the ID of the space the operation should be executed in. (required)
        :type space: int
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

        _param = self._post_subscriptions_id_upgrade_product_serialize(
            id=id,
            respect_termination_period=respect_termination_period,
            space=space,
            expand=expand,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "SubscriptionVersion",
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


    def _post_subscriptions_id_upgrade_product_serialize(
        self,
        id,
        respect_termination_period,
        space,
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
        if respect_termination_period is not None:
            
            _query_params.append(('respectTerminationPeriod', respect_termination_period))
            
        if expand is not None:
            
            _query_params.append(('expand', expand))
            
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
            resource_path='/subscriptions/{id}/upgrade-product',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )



