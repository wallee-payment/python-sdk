# coding: utf-8
import pprint
import six
from enum import Enum



class DebtCollectionCaseSource:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'forced_preparing_state': 'bool',
        'id': 'int',
        'name': 'dict(str, str)',
    }

    attribute_map = {
        'description': 'description','forced_preparing_state': 'forcedPreparingState','id': 'id','name': 'name',
    }

    
    _description = None
    _forced_preparing_state = None
    _id = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.forced_preparing_state = kwargs.get('forced_preparing_state', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def description(self):
        """Gets the description of this DebtCollectionCaseSource.

            

        :return: The description of this DebtCollectionCaseSource.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DebtCollectionCaseSource.

            

        :param description: The description of this DebtCollectionCaseSource.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def forced_preparing_state(self):
        """Gets the forced_preparing_state of this DebtCollectionCaseSource.

            

        :return: The forced_preparing_state of this DebtCollectionCaseSource.
        :rtype: bool
        """
        return self._forced_preparing_state

    @forced_preparing_state.setter
    def forced_preparing_state(self, forced_preparing_state):
        """Sets the forced_preparing_state of this DebtCollectionCaseSource.

            

        :param forced_preparing_state: The forced_preparing_state of this DebtCollectionCaseSource.
        :type: bool
        """

        self._forced_preparing_state = forced_preparing_state
    
    @property
    def id(self):
        """Gets the id of this DebtCollectionCaseSource.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DebtCollectionCaseSource.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DebtCollectionCaseSource.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DebtCollectionCaseSource.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this DebtCollectionCaseSource.

            

        :return: The name of this DebtCollectionCaseSource.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DebtCollectionCaseSource.

            

        :param name: The name of this DebtCollectionCaseSource.
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
        if issubclass(DebtCollectionCaseSource, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectionCaseSource):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
