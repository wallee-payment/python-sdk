# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalConfigurationVersion:

    swagger_types = {
    
        'configuration': 'PaymentTerminalConfiguration',
        'connector_configurations': 'list[int]',
        'created_by': 'int',
        'created_on': 'datetime',
        'default_currency': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'maintenance_window_duration': 'str',
        'maintenance_window_start': 'str',
        'planned_purge_date': 'datetime',
        'state': 'PaymentTerminalConfigurationVersionState',
        'time_zone': 'str',
        'version': 'int',
        'version_applied_immediately': 'bool',
    }

    attribute_map = {
        'configuration': 'configuration','connector_configurations': 'connectorConfigurations','created_by': 'createdBy','created_on': 'createdOn','default_currency': 'defaultCurrency','id': 'id','linked_space_id': 'linkedSpaceId','maintenance_window_duration': 'maintenanceWindowDuration','maintenance_window_start': 'maintenanceWindowStart','planned_purge_date': 'plannedPurgeDate','state': 'state','time_zone': 'timeZone','version': 'version','version_applied_immediately': 'versionAppliedImmediately',
    }

    
    _configuration = None
    _connector_configurations = None
    _created_by = None
    _created_on = None
    _default_currency = None
    _id = None
    _linked_space_id = None
    _maintenance_window_duration = None
    _maintenance_window_start = None
    _planned_purge_date = None
    _state = None
    _time_zone = None
    _version = None
    _version_applied_immediately = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.configuration = kwargs.get('configuration', None)
        self.connector_configurations = kwargs.get('connector_configurations', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.default_currency = kwargs.get('default_currency', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.maintenance_window_duration = kwargs.get('maintenance_window_duration', None)
        self.maintenance_window_start = kwargs.get('maintenance_window_start', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.version = kwargs.get('version', None)
        self.version_applied_immediately = kwargs.get('version_applied_immediately', None)
        

    
    @property
    def configuration(self):
        """Gets the configuration of this PaymentTerminalConfigurationVersion.

            

        :return: The configuration of this PaymentTerminalConfigurationVersion.
        :rtype: PaymentTerminalConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this PaymentTerminalConfigurationVersion.

            

        :param configuration: The configuration of this PaymentTerminalConfigurationVersion.
        :type: PaymentTerminalConfiguration
        """

        self._configuration = configuration
    
    @property
    def connector_configurations(self):
        """Gets the connector_configurations of this PaymentTerminalConfigurationVersion.

            

        :return: The connector_configurations of this PaymentTerminalConfigurationVersion.
        :rtype: list[int]
        """
        return self._connector_configurations

    @connector_configurations.setter
    def connector_configurations(self, connector_configurations):
        """Sets the connector_configurations of this PaymentTerminalConfigurationVersion.

            

        :param connector_configurations: The connector_configurations of this PaymentTerminalConfigurationVersion.
        :type: list[int]
        """

        self._connector_configurations = connector_configurations
    
    @property
    def created_by(self):
        """Gets the created_by of this PaymentTerminalConfigurationVersion.

            

        :return: The created_by of this PaymentTerminalConfigurationVersion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this PaymentTerminalConfigurationVersion.

            

        :param created_by: The created_by of this PaymentTerminalConfigurationVersion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentTerminalConfigurationVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this PaymentTerminalConfigurationVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentTerminalConfigurationVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this PaymentTerminalConfigurationVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def default_currency(self):
        """Gets the default_currency of this PaymentTerminalConfigurationVersion.

            The currency is derived by default from the terminal location. By setting a specific currency the derived currency is overridden.

        :return: The default_currency of this PaymentTerminalConfigurationVersion.
        :rtype: str
        """
        return self._default_currency

    @default_currency.setter
    def default_currency(self, default_currency):
        """Sets the default_currency of this PaymentTerminalConfigurationVersion.

            The currency is derived by default from the terminal location. By setting a specific currency the derived currency is overridden.

        :param default_currency: The default_currency of this PaymentTerminalConfigurationVersion.
        :type: str
        """

        self._default_currency = default_currency
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalConfigurationVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalConfigurationVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalConfigurationVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalConfigurationVersion.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalConfigurationVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminalConfigurationVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalConfigurationVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalConfigurationVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def maintenance_window_duration(self):
        """Gets the maintenance_window_duration of this PaymentTerminalConfigurationVersion.

            

        :return: The maintenance_window_duration of this PaymentTerminalConfigurationVersion.
        :rtype: str
        """
        return self._maintenance_window_duration

    @maintenance_window_duration.setter
    def maintenance_window_duration(self, maintenance_window_duration):
        """Sets the maintenance_window_duration of this PaymentTerminalConfigurationVersion.

            

        :param maintenance_window_duration: The maintenance_window_duration of this PaymentTerminalConfigurationVersion.
        :type: str
        """

        self._maintenance_window_duration = maintenance_window_duration
    
    @property
    def maintenance_window_start(self):
        """Gets the maintenance_window_start of this PaymentTerminalConfigurationVersion.

            

        :return: The maintenance_window_start of this PaymentTerminalConfigurationVersion.
        :rtype: str
        """
        return self._maintenance_window_start

    @maintenance_window_start.setter
    def maintenance_window_start(self, maintenance_window_start):
        """Sets the maintenance_window_start of this PaymentTerminalConfigurationVersion.

            

        :param maintenance_window_start: The maintenance_window_start of this PaymentTerminalConfigurationVersion.
        :type: str
        """

        self._maintenance_window_start = maintenance_window_start
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentTerminalConfigurationVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentTerminalConfigurationVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentTerminalConfigurationVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentTerminalConfigurationVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this PaymentTerminalConfigurationVersion.

            

        :return: The state of this PaymentTerminalConfigurationVersion.
        :rtype: PaymentTerminalConfigurationVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentTerminalConfigurationVersion.

            

        :param state: The state of this PaymentTerminalConfigurationVersion.
        :type: PaymentTerminalConfigurationVersionState
        """

        self._state = state
    
    @property
    def time_zone(self):
        """Gets the time_zone of this PaymentTerminalConfigurationVersion.

            

        :return: The time_zone of this PaymentTerminalConfigurationVersion.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this PaymentTerminalConfigurationVersion.

            

        :param time_zone: The time_zone of this PaymentTerminalConfigurationVersion.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalConfigurationVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalConfigurationVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalConfigurationVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalConfigurationVersion.
        :type: int
        """

        self._version = version
    
    @property
    def version_applied_immediately(self):
        """Gets the version_applied_immediately of this PaymentTerminalConfigurationVersion.

            

        :return: The version_applied_immediately of this PaymentTerminalConfigurationVersion.
        :rtype: bool
        """
        return self._version_applied_immediately

    @version_applied_immediately.setter
    def version_applied_immediately(self, version_applied_immediately):
        """Sets the version_applied_immediately of this PaymentTerminalConfigurationVersion.

            

        :param version_applied_immediately: The version_applied_immediately of this PaymentTerminalConfigurationVersion.
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
        if issubclass(PaymentTerminalConfigurationVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalConfigurationVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
