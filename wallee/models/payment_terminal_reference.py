# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalReference:

    swagger_types = {
    
        'created_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'space': 'Space',
        'state': 'PaymentTerminalState',
        'terminal_id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','space': 'space','state': 'state','terminal_id': 'terminalId','version': 'version',
    }

    
    _created_on = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _space = None
    _state = None
    _terminal_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space = kwargs.get('space', None)
        self.state = kwargs.get('state', None)
        self.terminal_id = kwargs.get('terminal_id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentTerminalReference.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentTerminalReference.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentTerminalReference.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentTerminalReference.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalReference.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalReference.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalReference.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalReference.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalReference.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminalReference.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalReference.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalReference.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalReference.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalReference.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalReference.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalReference.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space(self):
        """Gets the space of this PaymentTerminalReference.

            

        :return: The space of this PaymentTerminalReference.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this PaymentTerminalReference.

            

        :param space: The space of this PaymentTerminalReference.
        :type: Space
        """

        self._space = space
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalReference.

            

        :return: The state of this PaymentTerminalReference.
        :rtype: PaymentTerminalState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalReference.

            

        :param state: The state of this PaymentTerminalReference.
        :type: PaymentTerminalState
        """

        self._state = state
    
    @property
    def terminal_id(self):
        """Gets the terminal_id of this PaymentTerminalReference.

            

        :return: The terminal_id of this PaymentTerminalReference.
        :rtype: int
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this PaymentTerminalReference.

            

        :param terminal_id: The terminal_id of this PaymentTerminalReference.
        :type: int
        """

        self._terminal_id = terminal_id
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalReference.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalReference.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalReference.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalReference.
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
        if issubclass(PaymentTerminalReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
