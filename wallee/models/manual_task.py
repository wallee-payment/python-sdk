# coding: utf-8
import pprint
import six
from enum import Enum



class ManualTask:

    swagger_types = {
    
        'actions': 'list[int]',
        'context_entity_id': 'int',
        'created_on': 'datetime',
        'expires_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'space_id': 'int',
        'state': 'ManualTaskState',
        'type': 'int',
    }

    attribute_map = {
        'actions': 'actions','context_entity_id': 'contextEntityId','created_on': 'createdOn','expires_on': 'expiresOn','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','space_id': 'spaceId','state': 'state','type': 'type',
    }

    
    _actions = None
    _context_entity_id = None
    _created_on = None
    _expires_on = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _space_id = None
    _state = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.actions = kwargs.get('actions', None)
        self.context_entity_id = kwargs.get('context_entity_id', None)
        self.created_on = kwargs.get('created_on', None)
        self.expires_on = kwargs.get('expires_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_id = kwargs.get('space_id', None)
        self.state = kwargs.get('state', None)
        self.type = kwargs.get('type', None)
        

    
    @property
    def actions(self):
        """Gets the actions of this ManualTask.

            

        :return: The actions of this ManualTask.
        :rtype: list[int]
        """
        return self._actions

    @actions.setter
    def actions(self, actions):
        """Sets the actions of this ManualTask.

            

        :param actions: The actions of this ManualTask.
        :type: list[int]
        """

        self._actions = actions
    
    @property
    def context_entity_id(self):
        """Gets the context_entity_id of this ManualTask.

            The context entity ID links the manual task to the entity which caused its creation.

        :return: The context_entity_id of this ManualTask.
        :rtype: int
        """
        return self._context_entity_id

    @context_entity_id.setter
    def context_entity_id(self, context_entity_id):
        """Sets the context_entity_id of this ManualTask.

            The context entity ID links the manual task to the entity which caused its creation.

        :param context_entity_id: The context_entity_id of this ManualTask.
        :type: int
        """

        self._context_entity_id = context_entity_id
    
    @property
    def created_on(self):
        """Gets the created_on of this ManualTask.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this ManualTask.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ManualTask.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this ManualTask.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def expires_on(self):
        """Gets the expires_on of this ManualTask.

            The expiry date indicates until when the manual task has to be executed.

        :return: The expires_on of this ManualTask.
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this ManualTask.

            The expiry date indicates until when the manual task has to be executed.

        :param expires_on: The expires_on of this ManualTask.
        :type: datetime
        """

        self._expires_on = expires_on
    
    @property
    def id(self):
        """Gets the id of this ManualTask.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ManualTask.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ManualTask.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ManualTask.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ManualTask.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ManualTask.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ManualTask.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ManualTask.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ManualTask.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ManualTask.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ManualTask.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ManualTask.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_id(self):
        """Gets the space_id of this ManualTask.

            

        :return: The space_id of this ManualTask.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ManualTask.

            

        :param space_id: The space_id of this ManualTask.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this ManualTask.

            

        :return: The state of this ManualTask.
        :rtype: ManualTaskState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ManualTask.

            

        :param state: The state of this ManualTask.
        :type: ManualTaskState
        """

        self._state = state
    
    @property
    def type(self):
        """Gets the type of this ManualTask.

            The type categorizes the manual task.

        :return: The type of this ManualTask.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ManualTask.

            The type categorizes the manual task.

        :param type: The type of this ManualTask.
        :type: int
        """

        self._type = type
    

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
        if issubclass(ManualTask, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ManualTask):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
