# coding: utf-8
import pprint
import six
from enum import Enum



class User:

    swagger_types = {
    
        'id': 'int',
        'planned_purge_date': 'datetime',
        'scope': 'int',
        'state': 'CreationEntityState',
        'user_type': 'UserType',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','planned_purge_date': 'plannedPurgeDate','scope': 'scope','state': 'state','user_type': 'userType','version': 'version',
    }

    
    _id = None
    _planned_purge_date = None
    _scope = None
    _state = None
    _user_type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.scope = kwargs.get('scope', None)
        self.state = kwargs.get('state', None)
        self.user_type = kwargs.get('user_type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this User.

            A unique identifier for the object.

        :return: The id of this User.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this User.

            A unique identifier for the object.

        :param id: The id of this User.
        :type: int
        """

        self._id = id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this User.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this User.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this User.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this User.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def scope(self):
        """Gets the scope of this User.

            The scope that the user belongs to.

        :return: The scope of this User.
        :rtype: int
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this User.

            The scope that the user belongs to.

        :param scope: The scope of this User.
        :type: int
        """

        self._scope = scope
    
    @property
    def state(self):
        """Gets the state of this User.

            The object's current state.

        :return: The state of this User.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this User.

            The object's current state.

        :param state: The state of this User.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def user_type(self):
        """Gets the user_type of this User.

            The user's type which defines its role and capabilities.

        :return: The user_type of this User.
        :rtype: UserType
        """
        return self._user_type

    @user_type.setter
    def user_type(self, user_type):
        """Sets the user_type of this User.

            The user's type which defines its role and capabilities.

        :param user_type: The user_type of this User.
        :type: UserType
        """

        self._user_type = user_type
    
    @property
    def version(self):
        """Gets the version of this User.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this User.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this User.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this User.
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
        if issubclass(User, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, User):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
