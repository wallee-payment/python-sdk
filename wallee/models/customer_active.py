# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractCustomerActive


class CustomerActive(AbstractCustomerActive):

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','version': 'version',
    }

    
    _id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def id(self):
        """Gets the id of this CustomerActive.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this CustomerActive.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerActive.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this CustomerActive.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this CustomerActive.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this CustomerActive.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomerActive.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this CustomerActive.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

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
        if issubclass(CustomerActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CustomerActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
