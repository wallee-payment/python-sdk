# coding: utf-8
import pprint
import six
from enum import Enum
from . import User


class ApplicationUser(User):

    swagger_types = {
    
        'name': 'str',
        'primary_account': 'Account',
        'request_limit': 'int',
    }

    attribute_map = {
        'name': 'name','primary_account': 'primaryAccount','request_limit': 'requestLimit',
    }

    
    _name = None
    _primary_account = None
    _request_limit = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.name = kwargs.get('name', None)
        self.primary_account = kwargs.get('primary_account', None)
        self.request_limit = kwargs.get('request_limit', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def name(self):
        """Gets the name of this ApplicationUser.

            The user name is used to identify the application user in administrative interfaces.

        :return: The name of this ApplicationUser.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ApplicationUser.

            The user name is used to identify the application user in administrative interfaces.

        :param name: The name of this ApplicationUser.
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")

        self._name = name
    
    @property
    def primary_account(self):
        """Gets the primary_account of this ApplicationUser.

            The account that this user is associated with. The account owner will be able to manage this user.

        :return: The primary_account of this ApplicationUser.
        :rtype: Account
        """
        return self._primary_account

    @primary_account.setter
    def primary_account(self, primary_account):
        """Sets the primary_account of this ApplicationUser.

            The account that this user is associated with. The account owner will be able to manage this user.

        :param primary_account: The primary_account of this ApplicationUser.
        :type: Account
        """

        self._primary_account = primary_account
    
    @property
    def request_limit(self):
        """Gets the request_limit of this ApplicationUser.

            The request limit defines the maximum number of API request accepted within 2 minutes. This limit can only be changed with special privileges.

        :return: The request_limit of this ApplicationUser.
        :rtype: int
        """
        return self._request_limit

    @request_limit.setter
    def request_limit(self, request_limit):
        """Sets the request_limit of this ApplicationUser.

            The request limit defines the maximum number of API request accepted within 2 minutes. This limit can only be changed with special privileges.

        :param request_limit: The request_limit of this ApplicationUser.
        :type: int
        """

        self._request_limit = request_limit
    

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
        if issubclass(ApplicationUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ApplicationUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
