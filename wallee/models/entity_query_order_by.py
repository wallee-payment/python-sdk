# coding: utf-8
import pprint
import six
from enum import Enum



class EntityQueryOrderBy:

    swagger_types = {
    
        'field_name': 'str',
        'sorting': 'EntityQueryOrderByType',
    }

    attribute_map = {
        'field_name': 'fieldName','sorting': 'sorting',
    }

    
    _field_name = None
    _sorting = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.field_name = kwargs.get('field_name')

        self.sorting = kwargs.get('sorting')

        

    
    @property
    def field_name(self):
        """Gets the field_name of this EntityQueryOrderBy.

            

        :return: The field_name of this EntityQueryOrderBy.
        :rtype: str
        """
        return self._field_name

    @field_name.setter
    def field_name(self, field_name):
        """Sets the field_name of this EntityQueryOrderBy.

            

        :param field_name: The field_name of this EntityQueryOrderBy.
        :type: str
        """
        if field_name is None:
            raise ValueError("Invalid value for `field_name`, must not be `None`")

        self._field_name = field_name
    
    @property
    def sorting(self):
        """Gets the sorting of this EntityQueryOrderBy.

            

        :return: The sorting of this EntityQueryOrderBy.
        :rtype: EntityQueryOrderByType
        """
        return self._sorting

    @sorting.setter
    def sorting(self, sorting):
        """Sets the sorting of this EntityQueryOrderBy.

            

        :param sorting: The sorting of this EntityQueryOrderBy.
        :type: EntityQueryOrderByType
        """
        if sorting is None:
            raise ValueError("Invalid value for `sorting`, must not be `None`")

        self._sorting = sorting
    

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
        if issubclass(EntityQueryOrderBy, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, EntityQueryOrderBy):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
