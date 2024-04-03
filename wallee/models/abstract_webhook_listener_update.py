# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractWebhookListenerUpdate:

    swagger_types = {
    
        'enable_payload_signature_and_state': 'bool',
        'entity_states': 'list[str]',
        'name': 'str',
        'notify_every_change': 'bool',
        'state': 'CreationEntityState',
    }

    attribute_map = {
        'enable_payload_signature_and_state': 'enablePayloadSignatureAndState','entity_states': 'entityStates','name': 'name','notify_every_change': 'notifyEveryChange','state': 'state',
    }

    
    _enable_payload_signature_and_state = None
    _entity_states = None
    _name = None
    _notify_every_change = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.enable_payload_signature_and_state = kwargs.get('enable_payload_signature_and_state', None)
        self.entity_states = kwargs.get('entity_states', None)
        self.name = kwargs.get('name', None)
        self.notify_every_change = kwargs.get('notify_every_change', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def enable_payload_signature_and_state(self):
        """Gets the enable_payload_signature_and_state of this AbstractWebhookListenerUpdate.

            Whether signature header and state property are enabled in webhook payload.

        :return: The enable_payload_signature_and_state of this AbstractWebhookListenerUpdate.
        :rtype: bool
        """
        return self._enable_payload_signature_and_state

    @enable_payload_signature_and_state.setter
    def enable_payload_signature_and_state(self, enable_payload_signature_and_state):
        """Sets the enable_payload_signature_and_state of this AbstractWebhookListenerUpdate.

            Whether signature header and state property are enabled in webhook payload.

        :param enable_payload_signature_and_state: The enable_payload_signature_and_state of this AbstractWebhookListenerUpdate.
        :type: bool
        """

        self._enable_payload_signature_and_state = enable_payload_signature_and_state
    
    @property
    def entity_states(self):
        """Gets the entity_states of this AbstractWebhookListenerUpdate.

            The entity's target states that are to be monitored.

        :return: The entity_states of this AbstractWebhookListenerUpdate.
        :rtype: list[str]
        """
        return self._entity_states

    @entity_states.setter
    def entity_states(self, entity_states):
        """Sets the entity_states of this AbstractWebhookListenerUpdate.

            The entity's target states that are to be monitored.

        :param entity_states: The entity_states of this AbstractWebhookListenerUpdate.
        :type: list[str]
        """

        self._entity_states = entity_states
    
    @property
    def name(self):
        """Gets the name of this AbstractWebhookListenerUpdate.

            The name used to identify the webhook listener.

        :return: The name of this AbstractWebhookListenerUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractWebhookListenerUpdate.

            The name used to identify the webhook listener.

        :param name: The name of this AbstractWebhookListenerUpdate.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name
    
    @property
    def notify_every_change(self):
        """Gets the notify_every_change of this AbstractWebhookListenerUpdate.

            Whether every update of the entity or only state changes are to be monitored.

        :return: The notify_every_change of this AbstractWebhookListenerUpdate.
        :rtype: bool
        """
        return self._notify_every_change

    @notify_every_change.setter
    def notify_every_change(self, notify_every_change):
        """Sets the notify_every_change of this AbstractWebhookListenerUpdate.

            Whether every update of the entity or only state changes are to be monitored.

        :param notify_every_change: The notify_every_change of this AbstractWebhookListenerUpdate.
        :type: bool
        """

        self._notify_every_change = notify_every_change
    
    @property
    def state(self):
        """Gets the state of this AbstractWebhookListenerUpdate.

            The object's current state.

        :return: The state of this AbstractWebhookListenerUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractWebhookListenerUpdate.

            The object's current state.

        :param state: The state of this AbstractWebhookListenerUpdate.
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
        if issubclass(AbstractWebhookListenerUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractWebhookListenerUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
