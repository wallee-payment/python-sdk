# coding: utf-8
import pprint
import six
from enum import Enum



class SalesChannel:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'icon': 'str',
        'id': 'int',
        'name': 'dict(str, str)',
        'parent': 'SalesChannel',
        'sort_order': 'int',
    }

    attribute_map = {
        'description': 'description','icon': 'icon','id': 'id','name': 'name','parent': 'parent','sort_order': 'sortOrder',
    }

    
    _description = None
    _icon = None
    _id = None
    _name = None
    _parent = None
    _sort_order = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.icon = kwargs.get('icon', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.parent = kwargs.get('parent', None)
        self.sort_order = kwargs.get('sort_order', None)
        

    
    @property
    def description(self):
        """Gets the description of this SalesChannel.

            

        :return: The description of this SalesChannel.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SalesChannel.

            

        :param description: The description of this SalesChannel.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def icon(self):
        """Gets the icon of this SalesChannel.

            

        :return: The icon of this SalesChannel.
        :rtype: str
        """
        return self._icon

    @icon.setter
    def icon(self, icon):
        """Sets the icon of this SalesChannel.

            

        :param icon: The icon of this SalesChannel.
        :type: str
        """

        self._icon = icon
    
    @property
    def id(self):
        """Gets the id of this SalesChannel.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SalesChannel.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SalesChannel.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SalesChannel.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this SalesChannel.

            

        :return: The name of this SalesChannel.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SalesChannel.

            

        :param name: The name of this SalesChannel.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def parent(self):
        """Gets the parent of this SalesChannel.

            

        :return: The parent of this SalesChannel.
        :rtype: SalesChannel
        """
        return self._parent

    @parent.setter
    def parent(self, parent):
        """Sets the parent of this SalesChannel.

            

        :param parent: The parent of this SalesChannel.
        :type: SalesChannel
        """

        self._parent = parent
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SalesChannel.

            

        :return: The sort_order of this SalesChannel.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SalesChannel.

            

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
