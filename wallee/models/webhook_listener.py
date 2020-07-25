# coding: utf-8
import pprint
import six
from enum import Enum



class WebhookListener:

    swagger_types = {
    
        'entity': 'int',
        'entity_states': 'list[str]',
        'id': 'int',
        'identity': 'WebhookIdentity',
        'linked_space_id': 'int',
        'name': 'str',
        'notify_every_change': 'bool',
        'planned_purge_date': 'datetime',
        'state': 'CreationEntityState',
        'url': 'WebhookUrl',
        'version': 'int',
    }

    attribute_map = {
        'entity': 'entity','entity_states': 'entityStates','id': 'id','identity': 'identity','linked_space_id': 'linkedSpaceId','name': 'name','notify_every_change': 'notifyEveryChange','planned_purge_date': 'plannedPurgeDate','state': 'state','url': 'url','version': 'version',
    }

    
    _entity = None
    _entity_states = None
    _id = None
    _identity = None
    _linked_space_id = None
    _name = None
    _notify_every_change = None
    _planned_purge_date = None
    _state = None
    _url = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.entity = kwargs.get('entity', None)
        self.entity_states = kwargs.get('entity_states', None)
        self.id = kwargs.get('id', None)
        self.identity = kwargs.get('identity', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.notify_every_change = kwargs.get('notify_every_change', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.url = kwargs.get('url', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def entity(self):
        """Gets the entity of this WebhookListener.

            The listener listens on state changes of the entity linked with the listener.

        :return: The entity of this WebhookListener.
        :rtype: int
        """
        return self._entity

    @entity.setter
    def entity(self, entity):
        """Sets the entity of this WebhookListener.

            The listener listens on state changes of the entity linked with the listener.

        :param entity: The entity of this WebhookListener.
        :type: int
        """

        self._entity = entity
    
    @property
    def entity_states(self):
        """Gets the entity_states of this WebhookListener.

            The target state identifies the state into which entities need to move into to trigger the webhook listener.

        :return: The entity_states of this WebhookListener.
        :rtype: list[str]
        """
        return self._entity_states

    @entity_states.setter
    def entity_states(self, entity_states):
        """Sets the entity_states of this WebhookListener.

            The target state identifies the state into which entities need to move into to trigger the webhook listener.

        :param entity_states: The entity_states of this WebhookListener.
        :type: list[str]
        """

        self._entity_states = entity_states
    
    @property
    def id(self):
        """Gets the id of this WebhookListener.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this WebhookListener.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookListener.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this WebhookListener.
        :type: int
        """

        self._id = id
    
    @property
    def identity(self):
        """Gets the identity of this WebhookListener.

            The identity which will be used to sign messages sent by this listener.

        :return: The identity of this WebhookListener.
        :rtype: WebhookIdentity
        """
        return self._identity

    @identity.setter
    def identity(self, identity):
        """Sets the identity of this WebhookListener.

            The identity which will be used to sign messages sent by this listener.

        :param identity: The identity of this WebhookListener.
        :type: WebhookIdentity
        """

        self._identity = identity
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this WebhookListener.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this WebhookListener.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this WebhookListener.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this WebhookListener.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this WebhookListener.

            The webhook listener name is used internally to identify the webhook listener in administrative interfaces.For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this WebhookListener.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookListener.

            The webhook listener name is used internally to identify the webhook listener in administrative interfaces.For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this WebhookListener.
        :type: str
        """
        if name is not None and len(name) > 50:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `50`")

        self._name = name
    
    @property
    def notify_every_change(self):
        """Gets the notify_every_change of this WebhookListener.

            Defines whether the webhook listener is to be informed about every change made to the entity in contrast to state transitions only.

        :return: The notify_every_change of this WebhookListener.
        :rtype: bool
        """
        return self._notify_every_change

    @notify_every_change.setter
    def notify_every_change(self, notify_every_change):
        """Sets the notify_every_change of this WebhookListener.

            Defines whether the webhook listener is to be informed about every change made to the entity in contrast to state transitions only.

        :param notify_every_change: The notify_every_change of this WebhookListener.
        :type: bool
        """

        self._notify_every_change = notify_every_change
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this WebhookListener.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this WebhookListener.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this WebhookListener.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this WebhookListener.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this WebhookListener.

            

        :return: The state of this WebhookListener.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this WebhookListener.

            

        :param state: The state of this WebhookListener.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def url(self):
        """Gets the url of this WebhookListener.

            The URL which is invoked by the listener to notify the application about the event.

        :return: The url of this WebhookListener.
        :rtype: WebhookUrl
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this WebhookListener.

            The URL which is invoked by the listener to notify the application about the event.

        :param url: The url of this WebhookListener.
        :type: WebhookUrl
        """

        self._url = url
    
    @property
    def version(self):
        """Gets the version of this WebhookListener.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this WebhookListener.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this WebhookListener.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this WebhookListener.
        :type: int
        """

        self._version = version
    

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
        if issubclass(WebhookListener, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebhookListener):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
