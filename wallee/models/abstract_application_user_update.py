# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractApplicationUserUpdate:

    swagger_types = {
    
        'name': 'str',
        'request_limit': 'int',
        'state': 'CreationEntityState',
    }

    attribute_map = {
        'name': 'name','request_limit': 'requestLimit','state': 'state',
    }

    
    _name = None
    _request_limit = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.name = kwargs.get('name', None)
        self.request_limit = kwargs.get('request_limit', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def name(self):
        """Gets the name of this AbstractApplicationUserUpdate.

            The user name is used to identify the application user in administrative interfaces.

        :return: The name of this AbstractApplicationUserUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractApplicationUserUpdate.

            The user name is used to identify the application user in administrative interfaces.

        :param name: The name of this AbstractApplicationUserUpdate.
        :type: str
        """
        if name is not None and len(name) > 256:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `256`")

        self._name = name
    
    @property
    def request_limit(self):
        """Gets the request_limit of this AbstractApplicationUserUpdate.

            The request limit defines the maximum number of API request accepted within 2 minutes. This limit can only be changed with special privileges.

        :return: The request_limit of this AbstractApplicationUserUpdate.
        :rtype: int
        """
        return self._request_limit

    @request_limit.setter
    def request_limit(self, request_limit):
        """Sets the request_limit of this AbstractApplicationUserUpdate.

            The request limit defines the maximum number of API request accepted within 2 minutes. This limit can only be changed with special privileges.

        :param request_limit: The request_limit of this AbstractApplicationUserUpdate.
        :type: int
        """

        self._request_limit = request_limit
    
    @property
    def state(self):
        """Gets the state of this AbstractApplicationUserUpdate.

            

        :return: The state of this AbstractApplicationUserUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractApplicationUserUpdate.

            

        :param state: The state of this AbstractApplicationUserUpdate.
        :type: CreationEntityState
        """

        self._state = state
    

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
        if issubclass(AbstractApplicationUserUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractApplicationUserUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
