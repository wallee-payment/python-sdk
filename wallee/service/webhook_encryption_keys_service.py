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

from pydantic import StrictStr

from wallee.api_client import ApiClient, RequestSerialized
from wallee.api_response import ApiResponse
from wallee.rest import RESTResponseType

from wallee.utils.encryption_util import EncryptionUtil
from wallee.wallee_sdk_exception import WalleeSdkException
from wallee.sdk_exception_error_codes import SdkExceptionErrorCodes
import re


class WebhookEncryptionKeysService:
    def __init__(self, configuration):
        self.api_client = ApiClient(configuration=configuration)


    @validate_call
    def get_webhooks_encryption_keys_id(
        self,
        id: StrictStr,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> str:
        """Retrieve a webhook encryption key



        :param id: (required)
        :type id: str
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

        _param = self._get_webhooks_encryption_keys_id_serialize(
            id=id,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
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
    def get_webhooks_encryption_keys_id_with_http_info(
        self,
        id: StrictStr,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> ApiResponse[str]:
        """Retrieve a webhook encryption key



        :param id: (required)
        :type id: str
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

        _param = self._get_webhooks_encryption_keys_id_serialize(
            id=id,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
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
    def get_webhooks_encryption_keys_id_without_preload_content(
        self,
        id: StrictStr,
        _content_type: Optional[StrictStr] = None,
        _headers: Optional[Dict[StrictStr, Any]] = None,
        _host_index: Annotated[StrictInt, Field(ge=0, le=0)] = 0,
    ) -> RESTResponseType:
        """Retrieve a webhook encryption key



        :param id: (required)
        :type id: str
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

        _param = self._get_webhooks_encryption_keys_id_serialize(
            id=id,
            _content_type=_content_type,
            _headers=_headers,
            _host_index=_host_index
        )

        _response_types_map: Dict[str, Optional[str]] = {
            '200': "str",
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


    def _get_webhooks_encryption_keys_id_serialize(
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
                    'text/plain', 
                    'application/json'
                ]
            )


        return self.api_client.param_serialize(
            method='GET',
            resource_path='/webhooks/encryption-keys/{id}',
            path_params=_path_params,
            query_params=_query_params,
            header_params=_header_params,
            body=_body_params,
            post_params=_form_params,
            files=_files,
            collection_formats=_collection_formats,
            _host=_host
        )

    def is_content_valid(self, signature_header, content_to_verify):
        """Verify webhook content using signature header

        Verifies webhook content using signature header.

        :param str signature_header: Signature header 'X-Signature' value from the Http request
        :param str content_to_verify: Raw webhook content in String format
        :return: bool if webhook content body conforms with signature header
        """
        # Regular expression to extract algorithm, keyId, and signature from the signature_header
        regex = r"^algorithm=([a-zA-Z0-9]+),\skeyId=([a-z0-9\-]+),\s{1}signature=([a-zA-Z0-9+\/=]+)$"
        pattern = re.compile(regex)
        matcher = pattern.match(signature_header)

        if matcher:
            signature_algorithm = matcher.group(1)
            public_key_id = matcher.group(2)
            content_signature = matcher.group(3)

            public_key_response = WebhookEncryptionKeysService.get_webhooks_encryption_keys_id(self, public_key_id)

            if not public_key_response:
                raise WalleeSdkException(
                    SdkExceptionErrorCodes.UNKNOWN_WEBHOOK_ENCRYPTION_PUBLIC_KEY.code,
                    f"Could not find public key with id {public_key_id}"
                )

            return EncryptionUtil.is_content_valid(content_to_verify, content_signature, public_key_response,
                                                   signature_algorithm)
        else:
            raise WalleeSdkException(
                SdkExceptionErrorCodes.INVALID_WEBHOOK_ENCRYPTION_HEADER_FORMAT.code,
                "Invalid webhook signature header. Expected format: 'algorithm=<algorithm>, keyId=<keyId>, signature=<signature>'"
            )


