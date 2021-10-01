# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalLocationVersion:

    swagger_types = {
    
        'address': 'PaymentTerminalAddress',
        'contact_address': 'PaymentTerminalAddress',
        'created_by': 'int',
        'created_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'location': 'PaymentTerminalLocation',
        'planned_purge_date': 'datetime',
        'state': 'PaymentTerminalLocationVersionState',
        'version': 'int',
        'version_applied_immediately': 'bool',
    }

    attribute_map = {
        'address': 'address','contact_address': 'contactAddress','created_by': 'createdBy','created_on': 'createdOn','id': 'id','linked_space_id': 'linkedSpaceId','location': 'location','planned_purge_date': 'plannedPurgeDate','state': 'state','version': 'version','version_applied_immediately': 'versionAppliedImmediately',
    }

    
    _address = None
    _contact_address = None
    _created_by = None
    _created_on = None
    _id = None
    _linked_space_id = None
    _location = None
    _planned_purge_date = None
    _state = None
    _version = None
    _version_applied_immediately = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.address = kwargs.get('address', None)
        self.contact_address = kwargs.get('contact_address', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.location = kwargs.get('location', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        self.version_applied_immediately = kwargs.get('version_applied_immediately', None)
        

    
    @property
    def address(self):
        """Gets the address of this PaymentTerminalLocationVersion.

            

        :return: The address of this PaymentTerminalLocationVersion.
        :rtype: PaymentTerminalAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this PaymentTerminalLocationVersion.

            

        :param address: The address of this PaymentTerminalLocationVersion.
        :type: PaymentTerminalAddress
        """

        self._address = address
    
    @property
    def contact_address(self):
        """Gets the contact_address of this PaymentTerminalLocationVersion.

            

        :return: The contact_address of this PaymentTerminalLocationVersion.
        :rtype: PaymentTerminalAddress
        """
        return self._contact_address

    @contact_address.setter
    def contact_address(self, contact_address):
        """Sets the contact_address of this PaymentTerminalLocationVersion.

            

        :param contact_address: The contact_address of this PaymentTerminalLocationVersion.
        :type: PaymentTerminalAddress
        """

        self._contact_address = contact_address
    
    @property
    def created_by(self):
        """Gets the created_by of this PaymentTerminalLocationVersion.

            

        :return: The created_by of this PaymentTerminalLocationVersion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PaymentTerminalLocationVersion.

            

        :param created_by: The created_by of this PaymentTerminalLocationVersion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentTerminalLocationVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentTerminalLocationVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentTerminalLocationVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentTerminalLocationVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalLocationVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalLocationVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalLocationVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalLocationVersion.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalLocationVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminalLocationVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalLocationVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalLocationVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def location(self):
        """Gets the location of this PaymentTerminalLocationVersion.

            

        :return: The location of this PaymentTerminalLocationVersion.
        :rtype: PaymentTerminalLocation
        """
        return self._location

    @location.setter
    def location(self, location):
        """Sets the location of this PaymentTerminalLocationVersion.

            

        :param location: The location of this PaymentTerminalLocationVersion.
        :type: PaymentTerminalLocation
        """

        self._location = location
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalLocationVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalLocationVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalLocationVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalLocationVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalLocationVersion.

            

        :return: The state of this PaymentTerminalLocationVersion.
        :rtype: PaymentTerminalLocationVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalLocationVersion.

            

        :param state: The state of this PaymentTerminalLocationVersion.
        :type: PaymentTerminalLocationVersionState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalLocationVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalLocationVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalLocationVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalLocationVersion.
        :type: int
        """

        self._version = version
    
    @property
    def version_applied_immediately(self):
        """Gets the version_applied_immediately of this PaymentTerminalLocationVersion.

            

        :return: The version_applied_immediately of this PaymentTerminalLocationVersion.
        :rtype: bool
        """
        return self._version_applied_immediately

    @version_applied_immediately.setter
    def version_applied_immediately(self, version_applied_immediately):
        """Sets the version_applied_immediately of this PaymentTerminalLocationVersion.

            

        :param version_applied_immediately: The version_applied_immediately of this PaymentTerminalLocationVersion.
        :type: bool
        """

        self._version_applied_immediately = version_applied_immediately
    

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
        if issubclass(PaymentTerminalLocationVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalLocationVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
