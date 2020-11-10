# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractAccountUpdate:

    swagger_types = {
    
        'last_modified_date': 'datetime',
        'name': 'str',
        'subaccount_limit': 'int',
    }

    attribute_map = {
        'last_modified_date': 'lastModifiedDate','name': 'name','subaccount_limit': 'subaccountLimit',
    }

    
    _last_modified_date = None
    _name = None
    _subaccount_limit = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.last_modified_date = kwargs.get('last_modified_date', None)
        self.name = kwargs.get('name', None)
        self.subaccount_limit = kwargs.get('subaccount_limit', None)
        

    
    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this AbstractAccountUpdate.

            

        :return: The last_modified_date of this AbstractAccountUpdate.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this AbstractAccountUpdate.

            

        :param last_modified_date: The last_modified_date of this AbstractAccountUpdate.
        :type: datetime
        """

        self._last_modified_date = last_modified_date
    
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
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

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
