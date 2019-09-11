# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractWebhookListenerUpdate


class WebhookListenerCreate(AbstractWebhookListenerUpdate):

    swagger_types = {
    
        'entity': 'int',
        'identity': 'int',
        'url': 'int',
    }

    attribute_map = {
        'entity': 'entity','identity': 'identity','url': 'url',
    }

    
    _entity = None
    _identity = None
    _url = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.entity = kwargs.get('entity')

        self.identity = kwargs.get('identity', None)
        self.url = kwargs.get('url')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def entity(self):
        """Gets the entity of this WebhookListenerCreate.

            The listener listens on state changes of the entity linked with the listener.

        :return: The entity of this WebhookListenerCreate.
        :rtype: int
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this WebhookListenerCreate.

            The listener listens on state changes of the entity linked with the listener.

        :param entity: The entity of this WebhookListenerCreate.
        :type: int
        """
        if entity is None:
            raise ValueError("Invalid value for `entity`, must not be `None`")

        self._entity = entity
    
    @property
    def identity(self):
        """Gets the identity of this WebhookListenerCreate.

            The identity which will be used to sign messages sent by this listener.

        :return: The identity of this WebhookListenerCreate.
        :rtype: int
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this WebhookListenerCreate.

            The identity which will be used to sign messages sent by this listener.

        :param identity: The identity of this WebhookListenerCreate.
        :type: int
        """

        self._identity = identity
    
    @property
    def url(self):
        """Gets the url of this WebhookListenerCreate.

            The URL which is invoked by the listener to notify the application about the event.

        :return: The url of this WebhookListenerCreate.
        :rtype: int
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookListenerCreate.

            The URL which is invoked by the listener to notify the application about the event.

        :param url: The url of this WebhookListenerCreate.
        :type: int
        """
        if url is None:
            raise ValueError("Invalid value for `url`, must not be `None`")

        self._url = url
    

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
        if issubclass(WebhookListenerCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebhookListenerCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
