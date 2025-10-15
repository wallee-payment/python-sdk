# coding: utf-8
import pprint
import six
from enum import Enum



class SalesChannel:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'id': 'int',
        'name': 'dict(str, str)',
        'sort_order': 'int',
    }

    attribute_map = {
        'description': 'description','id': 'id','name': 'name','sort_order': 'sortOrder',
    }

    
    _description = None
    _id = None
    _name = None
    _sort_order = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.sort_order = kwargs.get('sort_order', None)
        

    
    @property
    def description(self):
        """Gets the description of this SalesChannel.

            The localized description of the object.

        :return: The description of this SalesChannel.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SalesChannel.

            The localized description of the object.

        :param description: The description of this SalesChannel.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this SalesChannel.

            A unique identifier for the object.

        :return: The id of this SalesChannel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SalesChannel.

            A unique identifier for the object.

        :param id: The id of this SalesChannel.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this SalesChannel.

            The localized name of the object.

        :return: The name of this SalesChannel.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SalesChannel.

            The localized name of the object.

        :param name: The name of this SalesChannel.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SalesChannel.

            When listing sales channels, they can be sorted by this number.

        :return: The sort_order of this SalesChannel.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SalesChannel.

            When listing sales channels, they can be sorted by this number.

        :param sort_order: The sort_order of this SalesChannel.
        :type: int
        """

        self._sort_order = sort_order
    

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
        if issubclass(SalesChannel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SalesChannel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
