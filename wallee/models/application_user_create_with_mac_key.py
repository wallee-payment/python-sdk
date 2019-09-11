# coding: utf-8
import pprint
import six
from enum import Enum
from . import ApplicationUser


class ApplicationUserCreateWithMacKey(ApplicationUser):

    swagger_types = {
    
        'mac_key': 'str',
    }

    attribute_map = {
        'mac_key': 'macKey',
    }

    
    _mac_key = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.mac_key = kwargs.get('mac_key', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def mac_key(self):
        """Gets the mac_key of this ApplicationUserCreateWithMacKey.

            

        :return: The mac_key of this ApplicationUserCreateWithMacKey.
        :rtype: str
        """
        return self._mac_key

    @mac_key.setter
    def mac_key(self, mac_key):
        """Sets the mac_key of this ApplicationUserCreateWithMacKey.

            

        :param mac_key: The mac_key of this ApplicationUserCreateWithMacKey.
        :type: str
        """

        self._mac_key = mac_key
    

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
        if issubclass(ApplicationUserCreateWithMacKey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ApplicationUserCreateWithMacKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
