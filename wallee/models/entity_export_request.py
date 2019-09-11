# coding: utf-8
import pprint
import six
from enum import Enum



class EntityExportRequest:

    swagger_types = {
    
        'properties': 'list[str]',
        'query': 'EntityQuery',
    }

    attribute_map = {
        'properties': 'properties','query': 'query',
    }

    
    _properties = None
    _query = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.properties = kwargs.get('properties')

        self.query = kwargs.get('query', None)
        

    
    @property
    def properties(self):
        """Gets the properties of this EntityExportRequest.

            The properties is a list of property paths which should be exported.

        :return: The properties of this EntityExportRequest.
        :rtype: list[str]
        """
        return self._properties

    @properties.setter
    def properties(self, properties):
        """Sets the properties of this EntityExportRequest.

            The properties is a list of property paths which should be exported.

        :param properties: The properties of this EntityExportRequest.
        :type: list[str]
        """
        if properties is None:
            raise ValueError("Invalid value for `properties`, must not be `None`")

        self._properties = properties
    
    @property
    def query(self):
        """Gets the query of this EntityExportRequest.

            The query limits the returned entries. The query allows to restrict the entries to return and it allows to control the order of them.

        :return: The query of this EntityExportRequest.
        :rtype: EntityQuery
        """
        return self._query

    @query.setter
    def query(self, query):
        """Sets the query of this EntityExportRequest.

            The query limits the returned entries. The query allows to restrict the entries to return and it allows to control the order of them.

        :param query: The query of this EntityExportRequest.
        :type: EntityQuery
        """

        self._query = query
    

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
        if issubclass(EntityExportRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EntityExportRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
