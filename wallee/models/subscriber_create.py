# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractSubscriberUpdate


class SubscriberCreate(AbstractSubscriberUpdate):

    swagger_types = {
    
        'state': 'CreationEntityState',
        'external_id': 'str',
    }

    attribute_map = {
        'state': 'state','external_id': 'externalId',
    }

    
    _state = None
    _external_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.state = kwargs.get('state', None)
        self.external_id = kwargs.get('external_id')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def state(self):
        """Gets the state of this SubscriberCreate.

            

        :return: The state of this SubscriberCreate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriberCreate.

            

        :param state: The state of this SubscriberCreate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriberCreate.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this SubscriberCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriberCreate.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this SubscriberCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    

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
        if issubclass(SubscriberCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriberCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
