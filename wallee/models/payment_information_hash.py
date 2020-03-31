# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentInformationHash:

    swagger_types = {
    
        'id': 'int',
        'type': 'PaymentInformationHashType',
        'value': 'str',
    }

    attribute_map = {
        'id': 'id','type': 'type','value': 'value',
    }

    
    _id = None
    _type = None
    _value = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.type = kwargs.get('type', None)
        self.value = kwargs.get('value', None)
        

    
    @property
    def id(self):
        """Gets the id of this PaymentInformationHash.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentInformationHash.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentInformationHash.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentInformationHash.
        :type: int
        """

        self._id = id
    
    @property
    def type(self):
        """Gets the type of this PaymentInformationHash.

            

        :return: The type of this PaymentInformationHash.
        :rtype: PaymentInformationHashType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentInformationHash.

            

        :param type: The type of this PaymentInformationHash.
        :type: PaymentInformationHashType
        """

        self._type = type
    
    @property
    def value(self):
        """Gets the value of this PaymentInformationHash.

            

        :return: The value of this PaymentInformationHash.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this PaymentInformationHash.

            

        :param value: The value of this PaymentInformationHash.
        :type: str
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
        if issubclass(PaymentInformationHash, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentInformationHash):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
