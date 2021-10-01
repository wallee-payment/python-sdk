# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminal:

    swagger_types = {
    
        'configuration_version': 'PaymentTerminalConfigurationVersion',
        'default_currency': 'str',
        'external_id': 'str',
        'id': 'int',
        'identifier': 'str',
        'linked_space_id': 'int',
        'location_version': 'PaymentTerminalLocationVersion',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'PaymentTerminalState',
        'type': 'PaymentTerminalType',
        'version': 'int',
    }

    attribute_map = {
        'configuration_version': 'configurationVersion','default_currency': 'defaultCurrency','external_id': 'externalId','id': 'id','identifier': 'identifier','linked_space_id': 'linkedSpaceId','location_version': 'locationVersion','name': 'name','planned_purge_date': 'plannedPurgeDate','state': 'state','type': 'type','version': 'version',
    }

    
    _configuration_version = None
    _default_currency = None
    _external_id = None
    _id = None
    _identifier = None
    _linked_space_id = None
    _location_version = None
    _name = None
    _planned_purge_date = None
    _state = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.configuration_version = kwargs.get('configuration_version', None)
        self.default_currency = kwargs.get('default_currency', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.identifier = kwargs.get('identifier', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.location_version = kwargs.get('location_version', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def configuration_version(self):
        """Gets the configuration_version of this PaymentTerminal.

            

        :return: The configuration_version of this PaymentTerminal.
        :rtype: PaymentTerminalConfigurationVersion
        """
        return self._configuration_version

    @configuration_version.setter
    def configuration_version(self, configuration_version):
        """Sets the configuration_version of this PaymentTerminal.

            

        :param configuration_version: The configuration_version of this PaymentTerminal.
        :type: PaymentTerminalConfigurationVersion
        """

        self._configuration_version = configuration_version
    
    @property
    def default_currency(self):
        """Gets the default_currency of this PaymentTerminal.

            

        :return: The default_currency of this PaymentTerminal.
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this PaymentTerminal.

            

        :param default_currency: The default_currency of this PaymentTerminal.
        :type: str
        """

        self._default_currency = default_currency
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentTerminal.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this PaymentTerminal.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentTerminal.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this PaymentTerminal.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminal.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminal.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminal.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminal.
        :type: int
        """

        self._id = id
    
    @property
    def identifier(self):
        """Gets the identifier of this PaymentTerminal.

            The identifier uniquely identifies the terminal. Normally it is visible on the device or in the display of the device.

        :return: The identifier of this PaymentTerminal.
        :rtype: str
        """
        return self._identifier

    @identifier.setter
    def identifier(self, identifier):
        """Sets the identifier of this PaymentTerminal.

            The identifier uniquely identifies the terminal. Normally it is visible on the device or in the display of the device.

        :param identifier: The identifier of this PaymentTerminal.
        :type: str
        """

        self._identifier = identifier
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminal.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminal.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminal.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminal.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def location_version(self):
        """Gets the location_version of this PaymentTerminal.

            

        :return: The location_version of this PaymentTerminal.
        :rtype: PaymentTerminalLocationVersion
        """
        return self._location_version

    @location_version.setter
    def location_version(self, location_version):
        """Sets the location_version of this PaymentTerminal.

            

        :param location_version: The location_version of this PaymentTerminal.
        :type: PaymentTerminalLocationVersion
        """

        self._location_version = location_version
    
    @property
    def name(self):
        """Gets the name of this PaymentTerminal.

            The terminal name is used internally to identify the terminal in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentTerminal.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentTerminal.

            The terminal name is used internally to identify the terminal in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentTerminal.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminal.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminal.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminal.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminal.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminal.

            

        :return: The state of this PaymentTerminal.
        :rtype: PaymentTerminalState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminal.

            

        :param state: The state of this PaymentTerminal.
        :type: PaymentTerminalState
        """

        self._state = state
    
    @property
    def type(self):
        """Gets the type of this PaymentTerminal.

            

        :return: The type of this PaymentTerminal.
        :rtype: PaymentTerminalType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentTerminal.

            

        :param type: The type of this PaymentTerminal.
        :type: PaymentTerminalType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminal.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminal.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminal.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminal.
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
        if issubclass(PaymentTerminal, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminal):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
