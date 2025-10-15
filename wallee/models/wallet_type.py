# coding: utf-8
import pprint
import six
from enum import Enum



class WalletType:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'feature': 'Feature',
        'id': 'int',
        'name': 'dict(str, str)',
        'navigation_path': 'str',
        'sort_order': 'int',
    }

    attribute_map = {
        'description': 'description','feature': 'feature','id': 'id','name': 'name','navigation_path': 'navigationPath','sort_order': 'sortOrder',
    }

    
    _description = None
    _feature = None
    _id = None
    _name = None
    _navigation_path = None
    _sort_order = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.feature = kwargs.get('feature', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.navigation_path = kwargs.get('navigation_path', None)
        self.sort_order = kwargs.get('sort_order', None)
        

    
    @property
    def description(self):
        """Gets the description of this WalletType.

            The localized description of the object.

        :return: The description of this WalletType.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this WalletType.

            The localized description of the object.

        :param description: The description of this WalletType.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def feature(self):
        """Gets the feature of this WalletType.

            

        :return: The feature of this WalletType.
        :rtype: Feature
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this WalletType.

            

        :param feature: The feature of this WalletType.
        :type: Feature
        """

        self._feature = feature
    
    @property
    def id(self):
        """Gets the id of this WalletType.

            A unique identifier for the object.

        :return: The id of this WalletType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WalletType.

            A unique identifier for the object.

        :param id: The id of this WalletType.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this WalletType.

            The localized name of the object.

        :return: The name of this WalletType.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WalletType.

            The localized name of the object.

        :param name: The name of this WalletType.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def navigation_path(self):
        """Gets the navigation_path of this WalletType.

            

        :return: The navigation_path of this WalletType.
        :rtype: str
        """
        return self._navigation_path

    @navigation_path.setter
    def navigation_path(self, navigation_path):
        """Sets the navigation_path of this WalletType.

            

        :param navigation_path: The navigation_path of this WalletType.
        :type: str
        """

        self._navigation_path = navigation_path
    
    @property
    def sort_order(self):
        """Gets the sort_order of this WalletType.

            

        :return: The sort_order of this WalletType.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this WalletType.

            

        :param sort_order: The sort_order of this WalletType.
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
        if issubclass(WalletType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WalletType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
