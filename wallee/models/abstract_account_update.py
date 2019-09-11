# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractAccountUpdate:

    swagger_types = {
    
        'name': 'str',
        'subaccount_limit': 'int',
    }

    attribute_map = {
        'name': 'name','subaccount_limit': 'subaccountLimit',
    }

    
    _name = None
    _subaccount_limit = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.name = kwargs.get('name', None)
        self.subaccount_limit = kwargs.get('subaccount_limit', None)
        

    
    @property
    def name(self):
        """Gets the name of this AbstractAccountUpdate.

            The name of the account identifies the account within the administrative interface.

        :return: The name of this AbstractAccountUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractAccountUpdate.

            The name of the account identifies the account within the administrative interface.

        :param name: The name of this AbstractAccountUpdate.
        :type: str
        """

        self._name = name
    
    @property
    def subaccount_limit(self):
        """Gets the subaccount_limit of this AbstractAccountUpdate.

            This property restricts the number of subaccounts which can be created within this account.

        :return: The subaccount_limit of this AbstractAccountUpdate.
        :rtype: int
        """
        return self._subaccount_limit

    @subaccount_limit.setter
    def subaccount_limit(self, subaccount_limit):
        """Sets the subaccount_limit of this AbstractAccountUpdate.

            This property restricts the number of subaccounts which can be created within this account.

        :param subaccount_limit: The subaccount_limit of this AbstractAccountUpdate.
        :type: int
        """

        self._subaccount_limit = subaccount_limit
    

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
        if issubclass(AbstractAccountUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractAccountUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
