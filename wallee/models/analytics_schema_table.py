# coding: utf-8
import pprint
import six
from enum import Enum



class AnalyticsSchemaTable:

    swagger_types = {
    
        'columns': 'list[AnalyticsSchemaColumn]',
        'description': 'dict(str, str)',
        'table_name': 'str',
    }

    attribute_map = {
        'columns': 'columns','description': 'description','table_name': 'tableName',
    }

    
    _columns = None
    _description = None
    _table_name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.columns = kwargs.get('columns', None)
        self.description = kwargs.get('description', None)
        self.table_name = kwargs.get('table_name', None)
        

    
    @property
    def columns(self):
        """Gets the columns of this AnalyticsSchemaTable.

            The schemas of all columns of this table.

        :return: The columns of this AnalyticsSchemaTable.
        :rtype: list[AnalyticsSchemaColumn]
        """
        return self._columns

    @columns.setter
    def columns(self, columns):
        """Sets the columns of this AnalyticsSchemaTable.

            The schemas of all columns of this table.

        :param columns: The columns of this AnalyticsSchemaTable.
        :type: list[AnalyticsSchemaColumn]
        """

        self._columns = columns
    
    @property
    def description(self):
        """Gets the description of this AnalyticsSchemaTable.

            A human readable description of the entity type contained in this table.

        :return: The description of this AnalyticsSchemaTable.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalyticsSchemaTable.

            A human readable description of the entity type contained in this table.

        :param description: The description of this AnalyticsSchemaTable.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def table_name(self):
        """Gets the table_name of this AnalyticsSchemaTable.

            The name of this table.

        :return: The table_name of this AnalyticsSchemaTable.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this AnalyticsSchemaTable.

            The name of this table.

        :param table_name: The table_name of this AnalyticsSchemaTable.
        :type: str
        """

        self._table_name = table_name
    

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
        if issubclass(AnalyticsSchemaTable, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AnalyticsSchemaTable):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
