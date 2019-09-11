# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentConnectorFeature:

    swagger_types = {
    
        'display_name': 'str',
        'feature': 'Feature',
        'id': 'int',
    }

    attribute_map = {
        'display_name': 'displayName','feature': 'feature','id': 'id',
    }

    
    _display_name = None
    _feature = None
    _id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.display_name = kwargs.get('display_name', None)
        self.feature = kwargs.get('feature', None)
        self.id = kwargs.get('id', None)
        

    
    @property
    def display_name(self):
        """Gets the display_name of this PaymentConnectorFeature.

            

        :return: The display_name of this PaymentConnectorFeature.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this PaymentConnectorFeature.

            

        :param display_name: The display_name of this PaymentConnectorFeature.
        :type: str
        """

        self._display_name = display_name
    
    @property
    def feature(self):
        """Gets the feature of this PaymentConnectorFeature.

            

        :return: The feature of this PaymentConnectorFeature.
        :rtype: Feature
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this PaymentConnectorFeature.

            

        :param feature: The feature of this PaymentConnectorFeature.
        :type: Feature
        """

        self._feature = feature
    
    @property
    def id(self):
        """Gets the id of this PaymentConnectorFeature.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentConnectorFeature.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentConnectorFeature.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentConnectorFeature.
        :type: int
        """

        self._id = id
    

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
        if issubclass(PaymentConnectorFeature, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentConnectorFeature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
