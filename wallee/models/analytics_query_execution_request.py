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


from __future__ import annotations
import pprint
import re
import json

from pydantic import BaseModel, ConfigDict, Field, StrictInt, StrictStr
from typing import Any, ClassVar, Dict, List, Optional
from typing_extensions import Annotated
from typing import Optional, Set
from typing_extensions import Self

class AnalyticsQueryExecutionRequest(BaseModel):
    """
    AnalyticsQueryExecutionRequest
    """
    sftp_dispatch_settings_id: Optional[StrictInt] = Field(default=None, description="Optional. Active SFTP Dispatch connection settings ID (dispatch settings ID) associated with the target account. Only required if the Analytics query result file is scheduled for delivery to a remote SFTP server.", alias="sftpDispatchSettingsId")
    sftp_dispatch_result_file_rename_pattern: Optional[StrictStr] = Field(default=None, description="Optional. Renaming pattern for Analytics query result file (may be used when Analytics query results file is scheduled for SFTP delivery). Pattern may look like Latin alphabet string with some timestamp placeholder: \"transaction_report_{YYYMMDD_hhmmss}\". Supported placeholder formats are just these: DDMMYY , MMDDYY , YYYYMMDD , DD_MM_YY , DD-MM-YY , YYYY-MM-DD , YYYY_MM_DD , YYYYMMDD_hhmmss , YYYY-MM-DD_hh-mm-ss", alias="sftpDispatchResultFileRenamePattern")
    sql: Optional[Annotated[str, Field(min_length=3, strict=True, max_length=100000)]] = Field(default=None, description="The SQL query (in PrestoDB dialect) to be executed against the analytics database. This query defines the data retrieval operation.")
    __properties: ClassVar[List[str]] = ["sftpDispatchSettingsId", "sftpDispatchResultFileRenamePattern", "sql"]

    model_config = ConfigDict(
        populate_by_name=True,
        validate_assignment=True,
        protected_namespaces=(),
    )


    def to_str(self) -> str:
        """Returns the string representation of the model using alias"""
        return pprint.pformat(self.model_dump(by_alias=True))

    def to_json(self) -> str:
        """Returns the JSON representation of the model using alias"""
        # TODO: pydantic v2: use .model_dump_json(by_alias=True, exclude_unset=True) instead
        return json.dumps(self.to_dict())

    @classmethod
    def from_json(cls, json_str: str) -> Optional[Self]:
        """Create an instance of AnalyticsQueryExecutionRequest from a JSON string"""
        return cls.from_dict(json.loads(json_str))

    def to_dict(self) -> Dict[str, Any]:
        """Return the dictionary representation of the model using alias.

        This has the following differences from calling pydantic's
        `self.model_dump(by_alias=True)`:

        * `None` is only added to the output dict for nullable fields that
          were set at model initialization. Other fields with value `None`
          are ignored.
        """
        excluded_fields: Set[str] = set([
        ])

        _dict = self.model_dump(
            by_alias=True,
            exclude=excluded_fields,
            exclude_none=True,
        )
        return _dict

    @classmethod
    def from_dict(cls, obj: Optional[Dict[str, Any]]) -> Optional[Self]:
        """Create an instance of AnalyticsQueryExecutionRequest from a dict"""
        if obj is None:
            return None

        if not isinstance(obj, dict):
            return cls.model_validate(obj)

        _obj = cls.model_validate({
            "sftpDispatchSettingsId": obj.get("sftpDispatchSettingsId"),
            "sftpDispatchResultFileRenamePattern": obj.get("sftpDispatchResultFileRenamePattern"),
            "sql": obj.get("sql")
        })
        return _obj


