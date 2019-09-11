# coding: utf-8
import pprint
import six
from enum import Enum



class UserSpaceRole:

    swagger_types = {
    
        'id': 'int',
        'role': 'int',
        'space': 'int',
        'user': 'int',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','role': 'role','space': 'space','user': 'user','version': 'version',
    }

    
    _id = None
    _role = None
    _space = None
    _user = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.role = kwargs.get('role', None)
        self.space = kwargs.get('space', None)
        self.user = kwargs.get('user', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this UserSpaceRole.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this UserSpaceRole.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this UserSpaceRole.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this UserSpaceRole.
        :type: int
        """

        self._id = id
    
    @property
    def role(self):
        """Gets the role of this UserSpaceRole.

            

        :return: The role of this UserSpaceRole.
        :rtype: int
        """
        return self._role

    @role.setter
    def role(self, role):
        """Sets the role of this UserSpaceRole.

            

        :param role: The role of this UserSpaceRole.
        :type: int
        """

        self._role = role
    
    @property
    def space(self):
        """Gets the space of this UserSpaceRole.

            

        :return: The space of this UserSpaceRole.
        :rtype: int
        """
        return self._space

    @space.setter
    def space(self, space):
        """Sets the space of this UserSpaceRole.

            

        :param space: The space of this UserSpaceRole.
        :type: int
        """

        self._space = space
    
    @property
    def user(self):
        """Gets the user of this UserSpaceRole.

            

        :return: The user of this UserSpaceRole.
        :rtype: int
        """
        return self._user

    @user.setter
    def user(self, user):
        """Sets the user of this UserSpaceRole.

            

        :param user: The user of this UserSpaceRole.
        :type: int
        """

        self._user = user
    
    @property
    def version(self):
        """Gets the version of this UserSpaceRole.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this UserSpaceRole.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this UserSpaceRole.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this UserSpaceRole.
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
        if issubclass(UserSpaceRole, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, UserSpaceRole):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
