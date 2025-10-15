# coding: utf-8
import pprint
import six
from enum import Enum
from . import TokenizedCardData


class AuthenticatedCardData(TokenizedCardData):

    swagger_types = {
    
        'cardholder_authentication': 'CardholderAuthentication',
    }

    attribute_map = {
        'cardholder_authentication': 'cardholderAuthentication',
    }

    
    _cardholder_authentication = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.cardholder_authentication = kwargs.get('cardholder_authentication', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def cardholder_authentication(self):
        """Gets the cardholder_authentication of this AuthenticatedCardData.

            Optional authentication details for the cardholder, such as 3D Secure authentication, used when the cardholder has already been verified during the transaction for added security.

        :return: The cardholder_authentication of this AuthenticatedCardData.
        :rtype: CardholderAuthentication
        """
        return self._cardholder_authentication

    @cardholder_authentication.setter
    def cardholder_authentication(self, cardholder_authentication):
        """Sets the cardholder_authentication of this AuthenticatedCardData.

            Optional authentication details for the cardholder, such as 3D Secure authentication, used when the cardholder has already been verified during the transaction for added security.

        :param cardholder_authentication: The cardholder_authentication of this AuthenticatedCardData.
        :type: CardholderAuthentication
        """

        self._cardholder_authentication = cardholder_authentication
    

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
        if issubclass(AuthenticatedCardData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AuthenticatedCardData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
