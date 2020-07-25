# coding: utf-8
import pprint
import six
from enum import Enum



class TenantDatabase:

    swagger_types = {
    
        'id': 'int',
        'name': 'str',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','name': 'name','version': 'version',
    }

    
    _id = None
    _name = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this TenantDatabase.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this TenantDatabase.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TenantDatabase.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this TenantDatabase.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this TenantDatabase.

            The name of the database.

        :return: The name of this TenantDatabase.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TenantDatabase.

            The name of the database.

        :param name: The name of this TenantDatabase.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")

        self._name = name
    
    @property
    def version(self):
        """Gets the version of this TenantDatabase.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TenantDatabase.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TenantDatabase.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this TenantDatabase.
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
        if issubclass(TenantDatabase, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TenantDatabase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
