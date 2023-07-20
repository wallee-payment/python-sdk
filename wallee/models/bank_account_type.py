# coding: utf-8
import pprint
import six
from enum import Enum



class BankAccountType:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'id': 'int',
        'identifier_name': 'dict(str, str)',
        'name': 'dict(str, str)',
    }

    attribute_map = {
        'description': 'description','id': 'id','identifier_name': 'identifierName','name': 'name',
    }

    
    _description = None
    _id = None
    _identifier_name = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.identifier_name = kwargs.get('identifier_name', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def description(self):
        """Gets the description of this BankAccountType.

            The localized description of the object.

        :return: The description of this BankAccountType.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this BankAccountType.

            The localized description of the object.

        :param description: The description of this BankAccountType.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this BankAccountType.

            A unique identifier for the object.

        :return: The id of this BankAccountType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankAccountType.

            A unique identifier for the object.

        :param id: The id of this BankAccountType.
        :type: int
        """

        self._id = id
    
    @property
    def identifier_name(self):
        """Gets the identifier_name of this BankAccountType.

            

        :return: The identifier_name of this BankAccountType.
        :rtype: dict(str, str)
        """
        return self._identifier_name

    @identifier_name.setter
    def identifier_name(self, identifier_name):
        """Sets the identifier_name of this BankAccountType.

            

        :param identifier_name: The identifier_name of this BankAccountType.
        :type: dict(str, str)
        """

        self._identifier_name = identifier_name
    
    @property
    def name(self):
        """Gets the name of this BankAccountType.

            The localized name of the object.

        :return: The name of this BankAccountType.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this BankAccountType.

            The localized name of the object.

        :param name: The name of this BankAccountType.
        :type: dict(str, str)
        """

        self._name = name
    

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
        if issubclass(BankAccountType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, BankAccountType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
