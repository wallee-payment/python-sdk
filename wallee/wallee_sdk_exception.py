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


from wallee.error_code import ErrorCode

class WalleeSdkException(Exception):
    def __init__(self, error_code: ErrorCode, details: str):
        self.error_code = error_code
        self.details = details
        self.message = f"Error code: {error_code.code}. {details}"
        super().__init__(self.message)

    def __str__(self):
        return self.message
