# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalDeviceManufacturer:

    swagger_types = {
    
        'id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'scope': 'Scope',
        'state': 'CreationEntityState',
        'title': 'DatabaseTranslatedString',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','name': 'name','planned_purge_date': 'plannedPurgeDate','scope': 'scope','state': 'state','title': 'title','version': 'version',
    }

    
    _id = None
    _name = None
    _planned_purge_date = None
    _scope = None
    _state = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.scope = kwargs.get('scope', None)
        self.state = kwargs.get('state', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalDeviceManufacturer.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalDeviceManufacturer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalDeviceManufacturer.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalDeviceManufacturer.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this PaymentTerminalDeviceManufacturer.

            

        :return: The name of this PaymentTerminalDeviceManufacturer.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentTerminalDeviceManufacturer.

            

        :param name: The name of this PaymentTerminalDeviceManufacturer.
        :type: str
        """

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalDeviceManufacturer.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalDeviceManufacturer.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalDeviceManufacturer.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalDeviceManufacturer.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def scope(self):
        """Gets the scope of this PaymentTerminalDeviceManufacturer.

            

        :return: The scope of this PaymentTerminalDeviceManufacturer.
        :rtype: Scope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this PaymentTerminalDeviceManufacturer.

            

        :param scope: The scope of this PaymentTerminalDeviceManufacturer.
        :type: Scope
        """

        self._scope = scope
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalDeviceManufacturer.

            

        :return: The state of this PaymentTerminalDeviceManufacturer.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalDeviceManufacturer.

            

        :param state: The state of this PaymentTerminalDeviceManufacturer.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def title(self):
        """Gets the title of this PaymentTerminalDeviceManufacturer.

            

        :return: The title of this PaymentTerminalDeviceManufacturer.
        :rtype: DatabaseTranslatedString
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this PaymentTerminalDeviceManufacturer.

            

        :param title: The title of this PaymentTerminalDeviceManufacturer.
        :type: DatabaseTranslatedString
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalDeviceManufacturer.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalDeviceManufacturer.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalDeviceManufacturer.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalDeviceManufacturer.
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
        if issubclass(PaymentTerminalDeviceManufacturer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalDeviceManufacturer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
