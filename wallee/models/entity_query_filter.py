# coding: utf-8
import pprint
import six
from enum import Enum



class EntityQueryFilter:

    swagger_types = {
    
        'children': 'list[EntityQueryFilter]',
        'field_name': 'str',
        'operator': 'CriteriaOperator',
        'type': 'EntityQueryFilterType',
        'value': 'object',
    }

    attribute_map = {
        'children': 'children','field_name': 'fieldName','operator': 'operator','type': 'type','value': 'value',
    }

    
    _children = None
    _field_name = None
    _operator = None
    _type = None
    _value = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.children = kwargs.get('children', None)
        self.field_name = kwargs.get('field_name', None)
        self.operator = kwargs.get('operator', None)
        self.type = kwargs.get('type')

        self.value = kwargs.get('value', None)
        

    
    @property
    def children(self):
        """Gets the children of this EntityQueryFilter.

            The 'children' can contain other filter nodes which are applied to the query. This property is only applicable on filter types 'OR' and 'AND'.

        :return: The children of this EntityQueryFilter.
        :rtype: list[EntityQueryFilter]
        """
        return self._children

    @children.setter
    def children(self, children):
        """Sets the children of this EntityQueryFilter.

            The 'children' can contain other filter nodes which are applied to the query. This property is only applicable on filter types 'OR' and 'AND'.

        :param children: The children of this EntityQueryFilter.
        :type: list[EntityQueryFilter]
        """

        self._children = children
    
    @property
    def field_name(self):
        """Gets the field_name of this EntityQueryFilter.

            The 'fieldName' indicates the property on the entity which should be filtered. This property is only applicable on filter type 'LEAF'.

        :return: The field_name of this EntityQueryFilter.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this EntityQueryFilter.

            The 'fieldName' indicates the property on the entity which should be filtered. This property is only applicable on filter type 'LEAF'.

        :param field_name: The field_name of this EntityQueryFilter.
        :type: str
        """

        self._field_name = field_name
    
    @property
    def operator(self):
        """Gets the operator of this EntityQueryFilter.

            The 'operator' indicates what kind of filtering on the 'fieldName' is executed on. This property is only applicable on filter type 'LEAF'.

        :return: The operator of this EntityQueryFilter.
        :rtype: CriteriaOperator
        """
        return self._operator

    @operator.setter
    def operator(self, operator):
        """Sets the operator of this EntityQueryFilter.

            The 'operator' indicates what kind of filtering on the 'fieldName' is executed on. This property is only applicable on filter type 'LEAF'.

        :param operator: The operator of this EntityQueryFilter.
        :type: CriteriaOperator
        """

        self._operator = operator
    
    @property
    def type(self):
        """Gets the type of this EntityQueryFilter.

            The filter type controls how the query node is interpreted. I.e. if the node acts as leaf node or as a filter group.

        :return: The type of this EntityQueryFilter.
        :rtype: EntityQueryFilterType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this EntityQueryFilter.

            The filter type controls how the query node is interpreted. I.e. if the node acts as leaf node or as a filter group.

        :param type: The type of this EntityQueryFilter.
        :type: EntityQueryFilterType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
    
    @property
    def value(self):
        """Gets the value of this EntityQueryFilter.

            The 'value' is used to compare with the 'fieldName' as defined by the 'operator'. This property is only applicable on filter type 'LEAF'.

        :return: The value of this EntityQueryFilter.
        :rtype: object
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this EntityQueryFilter.

            The 'value' is used to compare with the 'fieldName' as defined by the 'operator'. This property is only applicable on filter type 'LEAF'.

        :param value: The value of this EntityQueryFilter.
        :type: object
        """

        self._value = value
    

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
        if issubclass(EntityQueryFilter, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EntityQueryFilter):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
