# coding: utf-8
import pprint
import six
from enum import Enum



class ResourcePath:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'path': 'str',
        'planned_purge_date': 'datetime',
        'space_id': 'int',
        'state': 'ResourceState',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','path': 'path','planned_purge_date': 'plannedPurgeDate','space_id': 'spaceId','state': 'state','version': 'version',
    }

    
    _id = None
    _linked_space_id = None
    _path = None
    _planned_purge_date = None
    _space_id = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.path = kwargs.get('path', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_id = kwargs.get('space_id', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this ResourcePath.

            A unique identifier for the object.

        :return: The id of this ResourcePath.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ResourcePath.

            A unique identifier for the object.

        :param id: The id of this ResourcePath.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ResourcePath.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this ResourcePath.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ResourcePath.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this ResourcePath.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def path(self):
        """Gets the path of this ResourcePath.

            

        :return: The path of this ResourcePath.
        :rtype: str
        """
        return self._path

    @path.setter
    def path(self, path):
        """Sets the path of this ResourcePath.

            

        :param path: The path of this ResourcePath.
        :type: str
        """
        if path is not None and len(path) > 500:
            raise ValueError("Invalid value for `path`, length must be less than or equal to `500`")
        if path is not None and len(path) < 4:
            raise ValueError("Invalid value for `path`, length must be greater than or equal to `4`")

        self._path = path
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ResourcePath.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this ResourcePath.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ResourcePath.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this ResourcePath.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_id(self):
        """Gets the space_id of this ResourcePath.

            

        :return: The space_id of this ResourcePath.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this ResourcePath.

            

        :param space_id: The space_id of this ResourcePath.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this ResourcePath.

            The object's current state.

        :return: The state of this ResourcePath.
        :rtype: ResourceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ResourcePath.

            The object's current state.

        :param state: The state of this ResourcePath.
        :type: ResourceState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this ResourcePath.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this ResourcePath.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ResourcePath.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this ResourcePath.
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
        if issubclass(ResourcePath, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ResourcePath):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
