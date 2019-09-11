# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractHumanUserUpdate


class HumanUserCreate(AbstractHumanUserUpdate):

    swagger_types = {
    
        'primary_account': 'int',
    }

    attribute_map = {
        'primary_account': 'primaryAccount',
    }

    
    _primary_account = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.primary_account = kwargs.get('primary_account', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def primary_account(self):
        """Gets the primary_account of this HumanUserCreate.

            The primary account links the user to a specific account.

        :return: The primary_account of this HumanUserCreate.
        :rtype: int
        """
        return self._primary_account

    @primary_account.setter
    def primary_account(self, primary_account):
        """Sets the primary_account of this HumanUserCreate.

            The primary account links the user to a specific account.

        :param primary_account: The primary_account of this HumanUserCreate.
        :type: int
        """

        self._primary_account = primary_account
    

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
        if issubclass(HumanUserCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, HumanUserCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
