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


from enum import Enum

class ApiExceptionErrorCodes(Enum):
    """
    This class represents possible HTTP error codes which can be sent by the API.
    This list corresponds to https://app-wallee.com/en-us/doc/api/web-service#_errors
    """
    # The request was not accepted often due to missing or invalid parameters
    BAD_REQUEST = 400
    # The necessary authentication credentials are missing or incorrect
    UNAUTHORIZED = 401
    # The application user is missing the required permissions
    FORBIDDEN = 403
    # The requested resource was not found
    NOT_FOUND = 404
    # The requested response format is not supported
    NOT_ACCEPTABLE = 406
    # The request conflicts with another request often because of to optimistic locking
    CONFLICT = 409
    # Too many operations in a bulk request
    PAYLOAD_TOO_LARGE = 413
    # The request provides unsupported or invalid data
    UNSUPPORTED_MEDIA_TYPE = 415
    # The pagination offset exceeds the limit
    RANGE_NOT_SATISFIABLE = 416
    # The request is well-formed but contains semantic errors
    UNPROCESSABLE_ENTITY = 422
    # Too many requests hit the API too quickly
    TOO_MANY_REQUESTS = 429
    # An internal error occurred on the server
    INTERNAL_SERVER_ERROR = 500

    def __init__(self, http_code):
        self._http_code = http_code

    @property
    def http_code(self):
        return self._http_code

    def matches(self, api_exception):
        """
        Checks if the given exception matches this error code.
        """
        return api_exception.status == self.http_code