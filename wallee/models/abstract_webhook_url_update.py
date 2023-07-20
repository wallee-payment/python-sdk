# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractWebhookUrlUpdate:

    swagger_types = {
    
        'name': 'str',
        'state': 'CreationEntityState',
        'url': 'str',
    }

    attribute_map = {
        'name': 'name','state': 'state','url': 'url',
    }

    
    _name = None
    _state = None
    _url = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.name = kwargs.get('name', None)
        self.state = kwargs.get('state', None)
        self.url = kwargs.get('url', None)
        

    
    @property
    def name(self):
        """Gets the name of this AbstractWebhookUrlUpdate.

            The name used to identify the webhook URL.

        :return: The name of this AbstractWebhookUrlUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractWebhookUrlUpdate.

            The name used to identify the webhook URL.

        :param name: The name of this AbstractWebhookUrlUpdate.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name
    
    @property
    def state(self):
        """Gets the state of this AbstractWebhookUrlUpdate.

            The object's current state.

        :return: The state of this AbstractWebhookUrlUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractWebhookUrlUpdate.

            The object's current state.

        :param state: The state of this AbstractWebhookUrlUpdate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def url(self):
        """Gets the url of this AbstractWebhookUrlUpdate.

            The actual URL where notifications about entity changes are sent to.

        :return: The url of this AbstractWebhookUrlUpdate.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this AbstractWebhookUrlUpdate.

            The actual URL where notifications about entity changes are sent to.

        :param url: The url of this AbstractWebhookUrlUpdate.
        :type: str
        """
        if url is not None and len(url) > 500:
            raise ValueError("Invalid value for `url`, length must be less than or equal to `500`")
        if url is not None and len(url) < 9:
            raise ValueError("Invalid value for `url`, length must be greater than or equal to `9`")

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
        if issubclass(AbstractWebhookUrlUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractWebhookUrlUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
