# coding: utf-8
import pprint
import six
from enum import Enum



class AnalyticsQueryExecution:

    swagger_types = {
    
        'account': 'int',
        'external_id': 'str',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'processing_end_time': 'datetime',
        'processing_start_time': 'datetime',
        'query_string': 'str',
        'scanned_data_in_gb': 'float',
        'scanned_data_limit': 'float',
        'spaces': 'list[int]',
        'state': 'AnalyticsQueryExecutionState',
    }

    attribute_map = {
        'account': 'account','external_id': 'externalId','failure_reason': 'failureReason','id': 'id','processing_end_time': 'processingEndTime','processing_start_time': 'processingStartTime','query_string': 'queryString','scanned_data_in_gb': 'scannedDataInGb','scanned_data_limit': 'scannedDataLimit','spaces': 'spaces','state': 'state',
    }

    
    _account = None
    _external_id = None
    _failure_reason = None
    _id = None
    _processing_end_time = None
    _processing_start_time = None
    _query_string = None
    _scanned_data_in_gb = None
    _scanned_data_limit = None
    _spaces = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.external_id = kwargs.get('external_id', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.processing_end_time = kwargs.get('processing_end_time', None)
        self.processing_start_time = kwargs.get('processing_start_time', None)
        self.query_string = kwargs.get('query_string', None)
        self.scanned_data_in_gb = kwargs.get('scanned_data_in_gb', None)
        self.scanned_data_limit = kwargs.get('scanned_data_limit', None)
        self.spaces = kwargs.get('spaces', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def account(self):
        """Gets the account of this AnalyticsQueryExecution.

            The account in which the query has been executed.

        :return: The account of this AnalyticsQueryExecution.
        :rtype: int
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this AnalyticsQueryExecution.

            The account in which the query has been executed.

        :param account: The account of this AnalyticsQueryExecution.
        :type: int
        """

        self._account = account
    
    @property
    def external_id(self):
        """Gets the external_id of this AnalyticsQueryExecution.

            The External ID of the query if one had been specified; otherwise null.

        :return: The external_id of this AnalyticsQueryExecution.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AnalyticsQueryExecution.

            The External ID of the query if one had been specified; otherwise null.

        :param external_id: The external_id of this AnalyticsQueryExecution.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this AnalyticsQueryExecution.

            The reason of the failure if and only if the query has failed, otherwise null.

        :return: The failure_reason of this AnalyticsQueryExecution.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this AnalyticsQueryExecution.

            The reason of the failure if and only if the query has failed, otherwise null.

        :param failure_reason: The failure_reason of this AnalyticsQueryExecution.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this AnalyticsQueryExecution.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this AnalyticsQueryExecution.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this AnalyticsQueryExecution.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this AnalyticsQueryExecution.
        :type: int
        """

        self._id = id
    
    @property
    def processing_end_time(self):
        """Gets the processing_end_time of this AnalyticsQueryExecution.

            The time at which processing of the query has finished (either successfully or by failure or by cancelation). Will be null if the query execution has not finished yet.

        :return: The processing_end_time of this AnalyticsQueryExecution.
        :rtype: datetime
        """
        return self._processing_end_time

    @processing_end_time.setter
    def processing_end_time(self, processing_end_time):
        """Sets the processing_end_time of this AnalyticsQueryExecution.

            The time at which processing of the query has finished (either successfully or by failure or by cancelation). Will be null if the query execution has not finished yet.

        :param processing_end_time: The processing_end_time of this AnalyticsQueryExecution.
        :type: datetime
        """

        self._processing_end_time = processing_end_time
    
    @property
    def processing_start_time(self):
        """Gets the processing_start_time of this AnalyticsQueryExecution.

            The time at which processing of the query has started (never null).

        :return: The processing_start_time of this AnalyticsQueryExecution.
        :rtype: datetime
        """
        return self._processing_start_time

    @processing_start_time.setter
    def processing_start_time(self, processing_start_time):
        """Sets the processing_start_time of this AnalyticsQueryExecution.

            The time at which processing of the query has started (never null).

        :param processing_start_time: The processing_start_time of this AnalyticsQueryExecution.
        :type: datetime
        """

        self._processing_start_time = processing_start_time
    
    @property
    def query_string(self):
        """Gets the query_string of this AnalyticsQueryExecution.

            The SQL statement which has been submitted for execution.

        :return: The query_string of this AnalyticsQueryExecution.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this AnalyticsQueryExecution.

            The SQL statement which has been submitted for execution.

        :param query_string: The query_string of this AnalyticsQueryExecution.
        :type: str
        """

        self._query_string = query_string
    
    @property
    def scanned_data_in_gb(self):
        """Gets the scanned_data_in_gb of this AnalyticsQueryExecution.

            The amount of data scanned while processing the query (in GB). (Note that this amount may increase over time while the query is still being processed and not finished yet.)

        :return: The scanned_data_in_gb of this AnalyticsQueryExecution.
        :rtype: float
        """
        return self._scanned_data_in_gb

    @scanned_data_in_gb.setter
    def scanned_data_in_gb(self, scanned_data_in_gb):
        """Sets the scanned_data_in_gb of this AnalyticsQueryExecution.

            The amount of data scanned while processing the query (in GB). (Note that this amount may increase over time while the query is still being processed and not finished yet.)

        :param scanned_data_in_gb: The scanned_data_in_gb of this AnalyticsQueryExecution.
        :type: float
        """

        self._scanned_data_in_gb = scanned_data_in_gb
    
    @property
    def scanned_data_limit(self):
        """Gets the scanned_data_limit of this AnalyticsQueryExecution.

            The maximal amount of scanned data that this query is allowed to scan. After this limit is reached query will be canceled by the system. 

        :return: The scanned_data_limit of this AnalyticsQueryExecution.
        :rtype: float
        """
        return self._scanned_data_limit

    @scanned_data_limit.setter
    def scanned_data_limit(self, scanned_data_limit):
        """Sets the scanned_data_limit of this AnalyticsQueryExecution.

            The maximal amount of scanned data that this query is allowed to scan. After this limit is reached query will be canceled by the system. 

        :param scanned_data_limit: The scanned_data_limit of this AnalyticsQueryExecution.
        :type: float
        """

        self._scanned_data_limit = scanned_data_limit
    
    @property
    def spaces(self):
        """Gets the spaces of this AnalyticsQueryExecution.

            The spaces in which the query has been executed. May be empty if all spaces of the specified account have been queried.

        :return: The spaces of this AnalyticsQueryExecution.
        :rtype: list[int]
        """
        return self._spaces

    @spaces.setter
    def spaces(self, spaces):
        """Sets the spaces of this AnalyticsQueryExecution.

            The spaces in which the query has been executed. May be empty if all spaces of the specified account have been queried.

        :param spaces: The spaces of this AnalyticsQueryExecution.
        :type: list[int]
        """

        self._spaces = spaces
    
    @property
    def state(self):
        """Gets the state of this AnalyticsQueryExecution.

            The current state of the query execution.

        :return: The state of this AnalyticsQueryExecution.
        :rtype: AnalyticsQueryExecutionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AnalyticsQueryExecution.

            The current state of the query execution.

        :param state: The state of this AnalyticsQueryExecution.
        :type: AnalyticsQueryExecutionState
        """

        self._state = state
    

    def to_dict(self):
        result = {}

        for attr, _ in six.iteritems(self.swagger_types):
            value = getattr(self, attr)
            if isinstance(value, list):
                result[attr] = list(map(
                    lambda x: x.to_dict() if hasattr(x, "to_dict") else x,
                    value
                ))
            elif hasattr(value, "to_dict"):
                result[attr] = value.to_dict()
            elif isinstance(value, dict):
                result[attr] = dict(map(
                    lambda item: (item[0], item[1].to_dict())
                    if hasattr(item[1], "to_dict") else item,
                    value.items()
                ))
            elif isinstance(value, Enum):
                result[attr] = value.value
            else:
                result[attr] = value
        if issubclass(AnalyticsQueryExecution, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AnalyticsQueryExecution):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
