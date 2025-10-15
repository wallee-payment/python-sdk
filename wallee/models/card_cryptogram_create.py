# coding: utf-8
import pprint
import six
from enum import Enum



class CardCryptogramCreate:

    swagger_types = {
    
        'eci': 'str',
        'value': 'str',
    }

    attribute_map = {
        'eci': 'eci','value': 'value',
    }

    
    _eci = None
    _value = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.eci = kwargs.get('eci', None)
        self.value = kwargs.get('value')

        

    
    @property
    def eci(self):
        """Gets the eci of this CardCryptogramCreate.

            The Electronic Commerce Indicator (ECI) represents the authentication level and indicates liability shift during online or card-not-present transactions.

        :return: The eci of this CardCryptogramCreate.
        :rtype: str
        """
        return self._eci

    @eci.setter
    def eci(self, eci):
        """Sets the eci of this CardCryptogramCreate.

            The Electronic Commerce Indicator (ECI) represents the authentication level and indicates liability shift during online or card-not-present transactions.

        :param eci: The eci of this CardCryptogramCreate.
        :type: str
        """

        self._eci = eci
    
    @property
    def value(self):
        """Gets the value of this CardCryptogramCreate.

            The cryptogram value used for securing card transactions, format varying based on the PAN type.

        :return: The value of this CardCryptogramCreate.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this CardCryptogramCreate.

            The cryptogram value used for securing card transactions, format varying based on the PAN type.

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
