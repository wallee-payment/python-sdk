# coding: utf-8
import pprint
import six
from enum import Enum



class ChargeFlow:

    swagger_types = {
    
        'conditions': 'list[int]',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'conditions': 'conditions','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','priority': 'priority','state': 'state','version': 'version',
    }

    
    _conditions = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _priority = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.conditions = kwargs.get('conditions', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def conditions(self):
        """Gets the conditions of this ChargeFlow.

            If a transaction meets all selected conditions, the charge flow will be used to process the transaction. If the conditions are not met the next charge flow in line will be chosen according to the priorities.

        :return: The conditions of this ChargeFlow.
        :rtype: list[int]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this ChargeFlow.

            If a transaction meets all selected conditions, the charge flow will be used to process the transaction. If the conditions are not met the next charge flow in line will be chosen according to the priorities.

        :param conditions: The conditions of this ChargeFlow.
        :type: list[int]
        """

        self._conditions = conditions
    
    @property
    def id(self):
        """Gets the id of this ChargeFlow.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ChargeFlow.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChargeFlow.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ChargeFlow.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ChargeFlow.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ChargeFlow.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ChargeFlow.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ChargeFlow.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this ChargeFlow.

            The charge flow name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this ChargeFlow.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChargeFlow.

            The charge flow name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this ChargeFlow.
        :type: str
        """

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ChargeFlow.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ChargeFlow.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ChargeFlow.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ChargeFlow.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this ChargeFlow.

            The priority orders the charge flows. As such the priority determines together with the conditions the charge flow the selection mechanism for a particular transaction. A change of the priority affects all future selections.

        :return: The priority of this ChargeFlow.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ChargeFlow.

            The priority orders the charge flows. As such the priority determines together with the conditions the charge flow the selection mechanism for a particular transaction. A change of the priority affects all future selections.

        :param priority: The priority of this ChargeFlow.
        :type: int
        """

        self._priority = priority
    
    @property
    def state(self):
        """Gets the state of this ChargeFlow.

            

        :return: The state of this ChargeFlow.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChargeFlow.

            

        :param state: The state of this ChargeFlow.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this ChargeFlow.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ChargeFlow.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeFlow.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ChargeFlow.
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
        if issubclass(ChargeFlow, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeFlow):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
