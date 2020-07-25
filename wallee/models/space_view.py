# coding: utf-8
import pprint
import six
from enum import Enum



class SpaceView:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'space': 'Space',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','space': 'space','state': 'state','version': 'version',
    }

    
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _space = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space = kwargs.get('space', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this SpaceView.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SpaceView.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SpaceView.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SpaceView.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SpaceView.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SpaceView.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SpaceView.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SpaceView.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this SpaceView.

            The space view name is used internally to identify the space view in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this SpaceView.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SpaceView.

            The space view name is used internally to identify the space view in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this SpaceView.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SpaceView.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SpaceView.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SpaceView.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SpaceView.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space(self):
        """Gets the space of this SpaceView.

            The space to which the view belongs to.

        :return: The space of this SpaceView.
        :rtype: Space
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this SpaceView.

            The space to which the view belongs to.

        :param space: The space of this SpaceView.
        :type: Space
        """

        self._space = space
    
    @property
    def state(self):
        """Gets the state of this SpaceView.

            

        :return: The state of this SpaceView.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SpaceView.

            

        :param state: The state of this SpaceView.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this SpaceView.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SpaceView.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SpaceView.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SpaceView.
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
        if issubclass(SpaceView, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SpaceView):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
