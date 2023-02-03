# coding: utf-8
import pprint
import six
from enum import Enum



class FailureReason:

    swagger_types = {
    
        'category': 'FailureCategory',
        'description': 'dict(str, str)',
        'features': 'list[int]',
        'id': 'int',
        'name': 'dict(str, str)',
    }

    attribute_map = {
        'category': 'category','description': 'description','features': 'features','id': 'id','name': 'name',
    }

    
    _category = None
    _description = None
    _features = None
    _id = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.features = kwargs.get('features', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def category(self):
        """Gets the category of this FailureReason.

            

        :return: The category of this FailureReason.
        :rtype: FailureCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this FailureReason.

            

        :param category: The category of this FailureReason.
        :type: FailureCategory
        """

        self._category = category
    
    @property
    def description(self):
        """Gets the description of this FailureReason.

            The description of the object translated into different languages.

        :return: The description of this FailureReason.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this FailureReason.

            The description of the object translated into different languages.

        :param description: The description of this FailureReason.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def features(self):
        """Gets the features of this FailureReason.

            

        :return: The features of this FailureReason.
        :rtype: list[int]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this FailureReason.

            

        :param features: The features of this FailureReason.
        :type: list[int]
        """

        self._features = features
    
    @property
    def id(self):
        """Gets the id of this FailureReason.

            A unique identifier for the object.

        :return: The id of this FailureReason.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this FailureReason.

            A unique identifier for the object.

        :param id: The id of this FailureReason.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this FailureReason.

            The name of the object translated into different languages.

        :return: The name of this FailureReason.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this FailureReason.

            The name of the object translated into different languages.

        :param name: The name of this FailureReason.
        :type: dict(str, str)
        """

        self._name = name
    

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
        if issubclass(FailureReason, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, FailureReason):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
