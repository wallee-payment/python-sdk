# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentContractType:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'feature': 'Feature',
        'id': 'int',
        'name': 'dict(str, str)',
    }

    attribute_map = {
        'description': 'description','feature': 'feature','id': 'id','name': 'name',
    }

    
    _description = None
    _feature = None
    _id = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.feature = kwargs.get('feature', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def description(self):
        """Gets the description of this PaymentContractType.

            

        :return: The description of this PaymentContractType.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentContractType.

            

        :param description: The description of this PaymentContractType.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def feature(self):
        """Gets the feature of this PaymentContractType.

            

        :return: The feature of this PaymentContractType.
        :rtype: Feature
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this PaymentContractType.

            

        :param feature: The feature of this PaymentContractType.
        :type: Feature
        """

        self._feature = feature
    
    @property
    def id(self):
        """Gets the id of this PaymentContractType.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentContractType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentContractType.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentContractType.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this PaymentContractType.

            

        :return: The name of this PaymentContractType.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentContractType.

            

        :param name: The name of this PaymentContractType.
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
        if issubclass(PaymentContractType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentContractType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
