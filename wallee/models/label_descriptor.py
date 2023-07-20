# coding: utf-8
import pprint
import six
from enum import Enum



class LabelDescriptor:

    swagger_types = {
    
        'category': 'LabelDescriptorCategory',
        'description': 'dict(str, str)',
        'features': 'list[int]',
        'group': 'int',
        'id': 'int',
        'name': 'dict(str, str)',
        'type': 'int',
        'weight': 'int',
    }

    attribute_map = {
        'category': 'category','description': 'description','features': 'features','group': 'group','id': 'id','name': 'name','type': 'type','weight': 'weight',
    }

    
    _category = None
    _description = None
    _features = None
    _group = None
    _id = None
    _name = None
    _type = None
    _weight = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.features = kwargs.get('features', None)
        self.group = kwargs.get('group', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.type = kwargs.get('type', None)
        self.weight = kwargs.get('weight', None)
        

    
    @property
    def category(self):
        """Gets the category of this LabelDescriptor.

            The label's category.

        :return: The category of this LabelDescriptor.
        :rtype: LabelDescriptorCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this LabelDescriptor.

            The label's category.

        :param category: The category of this LabelDescriptor.
        :type: LabelDescriptorCategory
        """

        self._category = category
    
    @property
    def description(self):
        """Gets the description of this LabelDescriptor.

            The localized description of the object.

        :return: The description of this LabelDescriptor.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LabelDescriptor.

            The localized description of the object.

        :param description: The description of this LabelDescriptor.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def features(self):
        """Gets the features of this LabelDescriptor.

            The features that this label belongs to.

        :return: The features of this LabelDescriptor.
        :rtype: list[int]
        """
        return self._features

    @features.setter
    def features(self, features):
        """Sets the features of this LabelDescriptor.

            The features that this label belongs to.

        :param features: The features of this LabelDescriptor.
        :type: list[int]
        """

        self._features = features
    
    @property
    def group(self):
        """Gets the group of this LabelDescriptor.

            The group that this label belongs to.

        :return: The group of this LabelDescriptor.
        :rtype: int
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this LabelDescriptor.

            The group that this label belongs to.

        :param group: The group of this LabelDescriptor.
        :type: int
        """

        self._group = group
    
    @property
    def id(self):
        """Gets the id of this LabelDescriptor.

            A unique identifier for the object.

        :return: The id of this LabelDescriptor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LabelDescriptor.

            A unique identifier for the object.

        :param id: The id of this LabelDescriptor.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this LabelDescriptor.

            The localized name of the object.

        :return: The name of this LabelDescriptor.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LabelDescriptor.

            The localized name of the object.

        :param name: The name of this LabelDescriptor.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def type(self):
        """Gets the type of this LabelDescriptor.

            The type of the label's value.

        :return: The type of this LabelDescriptor.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LabelDescriptor.

            The type of the label's value.

        :param type: The type of this LabelDescriptor.
        :type: int
        """

        self._type = type
    
    @property
    def weight(self):
        """Gets the weight of this LabelDescriptor.

            When listing labels, they can be sorted by this number.

        :return: The weight of this LabelDescriptor.
        :rtype: int
        """
        return self._weight

    @weight.setter
    def weight(self, weight):
        """Sets the weight of this LabelDescriptor.

            When listing labels, they can be sorted by this number.

        :param weight: The weight of this LabelDescriptor.
        :type: int
        """

        self._weight = weight
    

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
        if issubclass(LabelDescriptor, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LabelDescriptor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
