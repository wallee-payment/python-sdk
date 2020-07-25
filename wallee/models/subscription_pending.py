# coding: utf-8
import pprint
import six
from enum import Enum
from . import SubscriptionUpdate


class SubscriptionPending(SubscriptionUpdate):

    swagger_types = {
    
        'reference': 'str',
        'subscriber': 'int',
        'token': 'int',
    }

    attribute_map = {
        'reference': 'reference','subscriber': 'subscriber','token': 'token',
    }

    
    _reference = None
    _subscriber = None
    _token = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.reference = kwargs.get('reference', None)
        self.subscriber = kwargs.get('subscriber', None)
        self.token = kwargs.get('token', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionPending.

            

        :return: The reference of this SubscriptionPending.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionPending.

            

        :param reference: The reference of this SubscriptionPending.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def subscriber(self):
        """Gets the subscriber of this SubscriptionPending.

            

        :return: The subscriber of this SubscriptionPending.
        :rtype: int
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this SubscriptionPending.

            

        :param subscriber: The subscriber of this SubscriptionPending.
        :type: int
        """

        self._subscriber = subscriber
    
    @property
    def token(self):
        """Gets the token of this SubscriptionPending.

            

        :return: The token of this SubscriptionPending.
        :rtype: int
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this SubscriptionPending.

            

        :param token: The token of this SubscriptionPending.
        :type: int
        """

        self._token = token
    

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
        if issubclass(SubscriptionPending, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionPending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
