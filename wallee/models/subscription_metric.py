# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionMetric:

    swagger_types = {
    
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'DatabaseTranslatedString',
        'planned_purge_date': 'datetime',
        'state': 'CreationEntityState',
        'type': 'SubscriptionMetricType',
        'version': 'int',
    }

    attribute_map = {
        'description': 'description','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','state': 'state','type': 'type','version': 'version',
    }

    
    _description = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _state = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def description(self):
        """Gets the description of this SubscriptionMetric.

            

        :return: The description of this SubscriptionMetric.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionMetric.

            

        :param description: The description of this SubscriptionMetric.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this SubscriptionMetric.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionMetric.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionMetric.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionMetric.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionMetric.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionMetric.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionMetric.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionMetric.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this SubscriptionMetric.

            

        :return: The name of this SubscriptionMetric.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionMetric.

            

        :param name: The name of this SubscriptionMetric.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionMetric.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionMetric.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionMetric.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionMetric.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this SubscriptionMetric.

            

        :return: The state of this SubscriptionMetric.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionMetric.

            

        :param state: The state of this SubscriptionMetric.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def type(self):
        """Gets the type of this SubscriptionMetric.

            

        :return: The type of this SubscriptionMetric.
        :rtype: SubscriptionMetricType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionMetric.

            

        :param type: The type of this SubscriptionMetric.
        :type: SubscriptionMetricType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this SubscriptionMetric.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionMetric.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionMetric.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionMetric.
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
        if issubclass(SubscriptionMetric, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionMetric):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
