# coding: utf-8
import pprint
import six
from enum import Enum



class ChargeFlowLevelConfiguration:

    swagger_types = {
    
        'flow': 'ChargeFlow',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'period': 'str',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'state': 'CreationEntityState',
        'type': 'int',
        'version': 'int',
    }

    attribute_map = {
        'flow': 'flow','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','period': 'period','planned_purge_date': 'plannedPurgeDate','priority': 'priority','state': 'state','type': 'type','version': 'version',
    }

    
    _flow = None
    _id = None
    _linked_space_id = None
    _name = None
    _period = None
    _planned_purge_date = None
    _priority = None
    _state = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.flow = kwargs.get('flow', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.period = kwargs.get('period', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.state = kwargs.get('state', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def flow(self):
        """Gets the flow of this ChargeFlowLevelConfiguration.

            The charge flow level configuration to which the flow is associated.

        :return: The flow of this ChargeFlowLevelConfiguration.
        :rtype: ChargeFlow
        """
        return self._flow

    @flow.setter
    def flow(self, flow):
        """Sets the flow of this ChargeFlowLevelConfiguration.

            The charge flow level configuration to which the flow is associated.

        :param flow: The flow of this ChargeFlowLevelConfiguration.
        :type: ChargeFlow
        """

        self._flow = flow
    
    @property
    def id(self):
        """Gets the id of this ChargeFlowLevelConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ChargeFlowLevelConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChargeFlowLevelConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ChargeFlowLevelConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ChargeFlowLevelConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ChargeFlowLevelConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ChargeFlowLevelConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ChargeFlowLevelConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this ChargeFlowLevelConfiguration.

            The charge flow level configuration name is used internally to identify the charge flow level configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this ChargeFlowLevelConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ChargeFlowLevelConfiguration.

            The charge flow level configuration name is used internally to identify the charge flow level configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this ChargeFlowLevelConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def period(self):
        """Gets the period of this ChargeFlowLevelConfiguration.

            The duration of the level before switching to the next one.

        :return: The period of this ChargeFlowLevelConfiguration.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this ChargeFlowLevelConfiguration.

            The duration of the level before switching to the next one.

        :param period: The period of this ChargeFlowLevelConfiguration.
        :type: str
        """

        self._period = period
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ChargeFlowLevelConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ChargeFlowLevelConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ChargeFlowLevelConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ChargeFlowLevelConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this ChargeFlowLevelConfiguration.

            The priority indicates the sort order of the level configurations. A low value indicates that the level configuration is executed before any level with a higher value. Any change to this value affects future level configuration selections.

        :return: The priority of this ChargeFlowLevelConfiguration.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this ChargeFlowLevelConfiguration.

            The priority indicates the sort order of the level configurations. A low value indicates that the level configuration is executed before any level with a higher value. Any change to this value affects future level configuration selections.

        :param priority: The priority of this ChargeFlowLevelConfiguration.
        :type: int
        """

        self._priority = priority
    
    @property
    def state(self):
        """Gets the state of this ChargeFlowLevelConfiguration.

            

        :return: The state of this ChargeFlowLevelConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChargeFlowLevelConfiguration.

            

        :param state: The state of this ChargeFlowLevelConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def type(self):
        """Gets the type of this ChargeFlowLevelConfiguration.

            The type determines how the payment link is delivered to the customer. Once the type is defined it cannot be changed anymore.

        :return: The type of this ChargeFlowLevelConfiguration.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ChargeFlowLevelConfiguration.

            The type determines how the payment link is delivered to the customer. Once the type is defined it cannot be changed anymore.

        :param type: The type of this ChargeFlowLevelConfiguration.
        :type: int
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this ChargeFlowLevelConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ChargeFlowLevelConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeFlowLevelConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ChargeFlowLevelConfiguration.
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
        if issubclass(ChargeFlowLevelConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeFlowLevelConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
