# coding: utf-8
import pprint
import six
from enum import Enum



class AnalyticsSchemaColumn:

    swagger_types = {
    
        'alias_name': 'str',
        'column_name': 'str',
        'description': 'dict(str, str)',
        'precision': 'int',
        'referenced_table': 'str',
        'scale': 'int',
        'table_name': 'str',
        'type': 'str',
    }

    attribute_map = {
        'alias_name': 'aliasName','column_name': 'columnName','description': 'description','precision': 'precision','referenced_table': 'referencedTable','scale': 'scale','table_name': 'tableName','type': 'type',
    }

    
    _alias_name = None
    _column_name = None
    _description = None
    _precision = None
    _referenced_table = None
    _scale = None
    _table_name = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.alias_name = kwargs.get('alias_name', None)
        self.column_name = kwargs.get('column_name', None)
        self.description = kwargs.get('description', None)
        self.precision = kwargs.get('precision', None)
        self.referenced_table = kwargs.get('referenced_table', None)
        self.scale = kwargs.get('scale', None)
        self.table_name = kwargs.get('table_name', None)
        self.type = kwargs.get('type', None)
        

    
    @property
    def alias_name(self):
        """Gets the alias_name of this AnalyticsSchemaColumn.

            The name of the alias defined for the column in the query or null if none is defined.

        :return: The alias_name of this AnalyticsSchemaColumn.
        :rtype: str
        """
        return self._alias_name

    @alias_name.setter
    def alias_name(self, alias_name):
        """Sets the alias_name of this AnalyticsSchemaColumn.

            The name of the alias defined for the column in the query or null if none is defined.

        :param alias_name: The alias_name of this AnalyticsSchemaColumn.
        :type: str
        """

        self._alias_name = alias_name
    
    @property
    def column_name(self):
        """Gets the column_name of this AnalyticsSchemaColumn.

            The name of the column in the table or null if this is a synthetic column which is the result of some SQL expression.

        :return: The column_name of this AnalyticsSchemaColumn.
        :rtype: str
        """
        return self._column_name

    @column_name.setter
    def column_name(self, column_name):
        """Sets the column_name of this AnalyticsSchemaColumn.

            The name of the column in the table or null if this is a synthetic column which is the result of some SQL expression.

        :param column_name: The column_name of this AnalyticsSchemaColumn.
        :type: str
        """

        self._column_name = column_name
    
    @property
    def description(self):
        """Gets the description of this AnalyticsSchemaColumn.

            A human readable description of the property contained in this column or null if this is a synthetic column which is the result of some SQL expression.

        :return: The description of this AnalyticsSchemaColumn.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AnalyticsSchemaColumn.

            A human readable description of the property contained in this column or null if this is a synthetic column which is the result of some SQL expression.

        :param description: The description of this AnalyticsSchemaColumn.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def precision(self):
        """Gets the precision of this AnalyticsSchemaColumn.

            The precision (maximal number of digits) for decimal data types, otherwise 0.

        :return: The precision of this AnalyticsSchemaColumn.
        :rtype: int
        """
        return self._precision

    @precision.setter
    def precision(self, precision):
        """Sets the precision of this AnalyticsSchemaColumn.

            The precision (maximal number of digits) for decimal data types, otherwise 0.

        :param precision: The precision of this AnalyticsSchemaColumn.
        :type: int
        """

        self._precision = precision
    
    @property
    def referenced_table(self):
        """Gets the referenced_table of this AnalyticsSchemaColumn.

            The name of the referenced table if this column represents a foreign-key relation to the IDs of another table, otherwise null.

        :return: The referenced_table of this AnalyticsSchemaColumn.
        :rtype: str
        """
        return self._referenced_table

    @referenced_table.setter
    def referenced_table(self, referenced_table):
        """Sets the referenced_table of this AnalyticsSchemaColumn.

            The name of the referenced table if this column represents a foreign-key relation to the IDs of another table, otherwise null.

        :param referenced_table: The referenced_table of this AnalyticsSchemaColumn.
        :type: str
        """

        self._referenced_table = referenced_table
    
    @property
    def scale(self):
        """Gets the scale of this AnalyticsSchemaColumn.

            The scale (maximal number number of digits in the fractional part) in case of a decimal data type, otherwise 0.

        :return: The scale of this AnalyticsSchemaColumn.
        :rtype: int
        """
        return self._scale

    @scale.setter
    def scale(self, scale):
        """Sets the scale of this AnalyticsSchemaColumn.

            The scale (maximal number number of digits in the fractional part) in case of a decimal data type, otherwise 0.

        :param scale: The scale of this AnalyticsSchemaColumn.
        :type: int
        """

        self._scale = scale
    
    @property
    def table_name(self):
        """Gets the table_name of this AnalyticsSchemaColumn.

            The name of the table which defines this column.

        :return: The table_name of this AnalyticsSchemaColumn.
        :rtype: str
        """
        return self._table_name

    @table_name.setter
    def table_name(self, table_name):
        """Sets the table_name of this AnalyticsSchemaColumn.

            The name of the table which defines this column.

        :param table_name: The table_name of this AnalyticsSchemaColumn.
        :type: str
        """

        self._table_name = table_name
    
    @property
    def type(self):
        """Gets the type of this AnalyticsSchemaColumn.

            The ORC data type of the column value.

        :return: The type of this AnalyticsSchemaColumn.
        :rtype: str
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this AnalyticsSchemaColumn.

            The ORC data type of the column value.

        :param type: The type of this AnalyticsSchemaColumn.
        :type: str
        """

        self._type = type
    

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
        if issubclass(AnalyticsSchemaColumn, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AnalyticsSchemaColumn):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
