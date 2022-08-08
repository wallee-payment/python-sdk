# coding: utf-8
import pprint
import six
from enum import Enum



class AnalyticsQueryResultBatch:

    swagger_types = {
    
        'columns': 'list[AnalyticsSchemaColumn]',
        'next_token': 'str',
        'query_execution': 'AnalyticsQueryExecution',
        'rows': 'list[list[str]]',
    }

    attribute_map = {
        'columns': 'columns','next_token': 'nextToken','query_execution': 'queryExecution','rows': 'rows',
    }

    
    _columns = None
    _next_token = None
    _query_execution = None
    _rows = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.columns = kwargs.get('columns', None)
        self.next_token = kwargs.get('next_token', None)
        self.query_execution = kwargs.get('query_execution', None)
        self.rows = kwargs.get('rows', None)
        

    
    @property
    def columns(self):
        """Gets the columns of this AnalyticsQueryResultBatch.

            The schemas of the columns returned by the query (in order). Will be null if the results of the query are not (yet) available.

        :return: The columns of this AnalyticsQueryResultBatch.
        :rtype: list[AnalyticsSchemaColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this AnalyticsQueryResultBatch.

            The schemas of the columns returned by the query (in order). Will be null if the results of the query are not (yet) available.

        :param columns: The columns of this AnalyticsQueryResultBatch.
        :type: list[AnalyticsSchemaColumn]
        """

        self._columns = columns
    
    @property
    def next_token(self):
        """Gets the next_token of this AnalyticsQueryResultBatch.

            The token to be provided to fetch the next batch of results. May be null if no more result batches are available.

        :return: The next_token of this AnalyticsQueryResultBatch.
        :rtype: str
        """
        return self._next_token

    @next_token.setter
    def next_token(self, next_token):
        """Sets the next_token of this AnalyticsQueryResultBatch.

            The token to be provided to fetch the next batch of results. May be null if no more result batches are available.

        :param next_token: The next_token of this AnalyticsQueryResultBatch.
        :type: str
        """

        self._next_token = next_token
    
    @property
    def query_execution(self):
        """Gets the query_execution of this AnalyticsQueryResultBatch.

            The query execution which produced the result.

        :return: The query_execution of this AnalyticsQueryResultBatch.
        :rtype: AnalyticsQueryExecution
        """
        return self._query_execution

    @query_execution.setter
    def query_execution(self, query_execution):
        """Sets the query_execution of this AnalyticsQueryResultBatch.

            The query execution which produced the result.

        :param query_execution: The query_execution of this AnalyticsQueryResultBatch.
        :type: AnalyticsQueryExecution
        """

        self._query_execution = query_execution
    
    @property
    def rows(self):
        """Gets the rows of this AnalyticsQueryResultBatch.

            The rows of the result set contained in this batch where each row is a list of column values (in order of the columns specified in the query). Will be null if the results of the query are not (yet) available.

        :return: The rows of this AnalyticsQueryResultBatch.
        :rtype: list[list[str]]
        """
        return self._rows

    @rows.setter
    def rows(self, rows):
        """Sets the rows of this AnalyticsQueryResultBatch.

            The rows of the result set contained in this batch where each row is a list of column values (in order of the columns specified in the query). Will be null if the results of the query are not (yet) available.

        :param rows: The rows of this AnalyticsQueryResultBatch.
        :type: list[list[str]]
        """

        self._rows = rows
    

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
        if issubclass(AnalyticsQueryResultBatch, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AnalyticsQueryResultBatch):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
