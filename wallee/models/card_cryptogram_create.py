# coding: utf-8
import pprint
import six
from enum import Enum



class CardCryptogramCreate:

    swagger_types = {
    
        'type': 'CardCryptogramType',
        'value': 'str',
    }

    attribute_map = {
        'type': 'type','value': 'value',
    }

    
    _type = None
    _value = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.type = kwargs.get('type')

        self.value = kwargs.get('value')

        

    
    @property
    def type(self):
        """Gets the type of this CardCryptogramCreate.

            

        :return: The type of this CardCryptogramCreate.
        :rtype: CardCryptogramType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this CardCryptogramCreate.

            

        :param type: The type of this CardCryptogramCreate.
        :type: CardCryptogramType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
    
    @property
    def value(self):
        """Gets the value of this CardCryptogramCreate.

            

        :return: The value of this CardCryptogramCreate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CardCryptogramCreate.

            

        :param value: The value of this CardCryptogramCreate.
        :type: str
        """
        if value is None:
            raise ValueError("Invalid value for `value`, must not be `None`")

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
        if issubclass(CardCryptogramCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CardCryptogramCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
