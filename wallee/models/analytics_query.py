# coding: utf-8
import pprint
import six
from enum import Enum



class AnalyticsQuery:

    swagger_types = {
    
        'account_id': 'int',
        'external_id': 'str',
        'max_cache_age': 'int',
        'query_string': 'str',
        'scanned_data_limit': 'float',
        'space_ids': 'list[int]',
    }

    attribute_map = {
        'account_id': 'accountId','external_id': 'externalId','max_cache_age': 'maxCacheAge','query_string': 'queryString','scanned_data_limit': 'scannedDataLimit','space_ids': 'spaceIds',
    }

    
    _account_id = None
    _external_id = None
    _max_cache_age = None
    _query_string = None
    _scanned_data_limit = None
    _space_ids = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account_id = kwargs.get('account_id')

        self.external_id = kwargs.get('external_id', None)
        self.max_cache_age = kwargs.get('max_cache_age', None)
        self.query_string = kwargs.get('query_string', None)
        self.scanned_data_limit = kwargs.get('scanned_data_limit', None)
        self.space_ids = kwargs.get('space_ids', None)
        

    
    @property
    def account_id(self):
        """Gets the account_id of this AnalyticsQuery.

            The mandatory ID of an account in which the query shall be executed. Must be a valid account ID greater than 0.

        :return: The account_id of this AnalyticsQuery.
        :rtype: int
        """
        return self._account_id

    @account_id.setter
    def account_id(self, account_id):
        """Sets the account_id of this AnalyticsQuery.

            The mandatory ID of an account in which the query shall be executed. Must be a valid account ID greater than 0.

        :param account_id: The account_id of this AnalyticsQuery.
        :type: int
        """
        if account_id is None:
            raise ValueError("Invalid value for `account_id`, must not be `None`")

        self._account_id = account_id
    
    @property
    def external_id(self):
        """Gets the external_id of this AnalyticsQuery.

            A client generated nonce which uniquely identifies the query to be executed. Subsequent submissions with the same external ID will not re-execute the query but instead return the existing execution with that ID. Either the External ID or a Maximal Cache Age greater than 0 must be specified. If both are specified the External ID will have precedence and the Maximal Cache Age will be ignored.

        :return: The external_id of this AnalyticsQuery.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this AnalyticsQuery.

            A client generated nonce which uniquely identifies the query to be executed. Subsequent submissions with the same external ID will not re-execute the query but instead return the existing execution with that ID. Either the External ID or a Maximal Cache Age greater than 0 must be specified. If both are specified the External ID will have precedence and the Maximal Cache Age will be ignored.

        :param external_id: The external_id of this AnalyticsQuery.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def max_cache_age(self):
        """Gets the max_cache_age of this AnalyticsQuery.

            The maximal age in minutes of cached query executions to return. If an equivalent query execution with the same Query String, Account ID and Spaces parameters not older than the specified age is already available that execution will be returned instead of a newly started execution. Set to 0 or null (and set a unique, previously unused External ID) to force a new query execution irrespective of previous executions. Either the External ID or a Cache Duration greater than 0 must be specified. If both are specified, the External ID will be preferred (and the Maximal Cache Age ignored).

        :return: The max_cache_age of this AnalyticsQuery.
        :rtype: int
        """
        return self._max_cache_age

    @max_cache_age.setter
    def max_cache_age(self, max_cache_age):
        """Sets the max_cache_age of this AnalyticsQuery.

            The maximal age in minutes of cached query executions to return. If an equivalent query execution with the same Query String, Account ID and Spaces parameters not older than the specified age is already available that execution will be returned instead of a newly started execution. Set to 0 or null (and set a unique, previously unused External ID) to force a new query execution irrespective of previous executions. Either the External ID or a Cache Duration greater than 0 must be specified. If both are specified, the External ID will be preferred (and the Maximal Cache Age ignored).

        :param max_cache_age: The max_cache_age of this AnalyticsQuery.
        :type: int
        """

        self._max_cache_age = max_cache_age
    
    @property
    def query_string(self):
        """Gets the query_string of this AnalyticsQuery.

            The SQL statement which is being submitted for execution. Must be a valid PrestoDB/Athena SQL statement.

        :return: The query_string of this AnalyticsQuery.
        :rtype: str
        """
        return self._query_string

    @query_string.setter
    def query_string(self, query_string):
        """Sets the query_string of this AnalyticsQuery.

            The SQL statement which is being submitted for execution. Must be a valid PrestoDB/Athena SQL statement.

        :param query_string: The query_string of this AnalyticsQuery.
        :type: str
        """
        if query_string is not None and len(query_string) > 4096:
            raise ValueError("Invalid value for `query_string`, length must be less than or equal to `4096`")
        if query_string is not None and len(query_string) < 1:
            raise ValueError("Invalid value for `query_string`, length must be greater than or equal to `1`")

        self._query_string = query_string
    
    @property
    def scanned_data_limit(self):
        """Gets the scanned_data_limit of this AnalyticsQuery.

            The maximal amount of scanned data that this query is allowed to scan. After this limit is reached query will be canceled by the system. 

        :return: The scanned_data_limit of this AnalyticsQuery.
        :rtype: float
        """
        return self._scanned_data_limit

    @scanned_data_limit.setter
    def scanned_data_limit(self, scanned_data_limit):
        """Sets the scanned_data_limit of this AnalyticsQuery.

            The maximal amount of scanned data that this query is allowed to scan. After this limit is reached query will be canceled by the system. 

        :param scanned_data_limit: The scanned_data_limit of this AnalyticsQuery.
        :type: float
        """

        self._scanned_data_limit = scanned_data_limit
    
    @property
    def space_ids(self):
        """Gets the space_ids of this AnalyticsQuery.

            The IDs of the spaces in which the query shall be executed. At most 5 space IDs may be specified. All specified spaces must be owned by the account specified by the accountId property. The spaces property may be missing or empty to query all spaces of the specified account.

        :return: The space_ids of this AnalyticsQuery.
        :rtype: list[int]
        """
        return self._space_ids

    @space_ids.setter
    def space_ids(self, space_ids):
        """Sets the space_ids of this AnalyticsQuery.

            The IDs of the spaces in which the query shall be executed. At most 5 space IDs may be specified. All specified spaces must be owned by the account specified by the accountId property. The spaces property may be missing or empty to query all spaces of the specified account.

        :param space_ids: The space_ids of this AnalyticsQuery.
        :type: list[int]
        """

        self._space_ids = space_ids
    

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
        if issubclass(AnalyticsQuery, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AnalyticsQuery):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
