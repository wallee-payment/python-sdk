# coding: utf-8
import pprint
import six
from enum import Enum



class Space:

    swagger_types = {
    
        'account': 'Account',
        'active': 'bool',
        'active_or_restricted_active': 'bool',
        'created_by': 'int',
        'created_on': 'datetime',
        'database': 'TenantDatabase',
        'deleted_by': 'int',
        'deleted_on': 'datetime',
        'id': 'int',
        'last_modified_date': 'datetime',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'postal_address': 'SpaceAddress',
        'primary_currency': 'str',
        'request_limit': 'int',
        'restricted_active': 'bool',
        'state': 'CreationEntityState',
        'technical_contact_addresses': 'list[str]',
        'time_zone': 'str',
        'version': 'int',
    }

    attribute_map = {
        'account': 'account','active': 'active','active_or_restricted_active': 'activeOrRestrictedActive','created_by': 'createdBy','created_on': 'createdOn','database': 'database','deleted_by': 'deletedBy','deleted_on': 'deletedOn','id': 'id','last_modified_date': 'lastModifiedDate','name': 'name','planned_purge_date': 'plannedPurgeDate','postal_address': 'postalAddress','primary_currency': 'primaryCurrency','request_limit': 'requestLimit','restricted_active': 'restrictedActive','state': 'state','technical_contact_addresses': 'technicalContactAddresses','time_zone': 'timeZone','version': 'version',
    }

    
    _account = None
    _active = None
    _active_or_restricted_active = None
    _created_by = None
    _created_on = None
    _database = None
    _deleted_by = None
    _deleted_on = None
    _id = None
    _last_modified_date = None
    _name = None
    _planned_purge_date = None
    _postal_address = None
    _primary_currency = None
    _request_limit = None
    _restricted_active = None
    _state = None
    _technical_contact_addresses = None
    _time_zone = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.account = kwargs.get('account', None)
        self.active = kwargs.get('active', None)
        self.active_or_restricted_active = kwargs.get('active_or_restricted_active', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.database = kwargs.get('database', None)
        self.deleted_by = kwargs.get('deleted_by', None)
        self.deleted_on = kwargs.get('deleted_on', None)
        self.id = kwargs.get('id', None)
        self.last_modified_date = kwargs.get('last_modified_date', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.postal_address = kwargs.get('postal_address', None)
        self.primary_currency = kwargs.get('primary_currency', None)
        self.request_limit = kwargs.get('request_limit', None)
        self.restricted_active = kwargs.get('restricted_active', None)
        self.state = kwargs.get('state', None)
        self.technical_contact_addresses = kwargs.get('technical_contact_addresses', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def account(self):
        """Gets the account of this Space.

            The account to which the space belongs to.

        :return: The account of this Space.
        :rtype: Account
        """
        return self._account

    @account.setter
    def account(self, account):
        """Sets the account of this Space.

            The account to which the space belongs to.

        :param account: The account of this Space.
        :type: Account
        """

        self._account = account
    
    @property
    def active(self):
        """Gets the active of this Space.

            Active means that this account and all accounts in the hierarchy are active.

        :return: The active of this Space.
        :rtype: bool
        """
        return self._active

    @active.setter
    def active(self, active):
        """Sets the active of this Space.

            Active means that this account and all accounts in the hierarchy are active.

        :param active: The active of this Space.
        :type: bool
        """

        self._active = active
    
    @property
    def active_or_restricted_active(self):
        """Gets the active_or_restricted_active of this Space.

            This property is true when all accounts in the hierarchy are active or restricted active.

        :return: The active_or_restricted_active of this Space.
        :rtype: bool
        """
        return self._active_or_restricted_active

    @active_or_restricted_active.setter
    def active_or_restricted_active(self, active_or_restricted_active):
        """Sets the active_or_restricted_active of this Space.

            This property is true when all accounts in the hierarchy are active or restricted active.

        :param active_or_restricted_active: The active_or_restricted_active of this Space.
        :type: bool
        """

        self._active_or_restricted_active = active_or_restricted_active
    
    @property
    def created_by(self):
        """Gets the created_by of this Space.

            The ID of the user who created this entity.

        :return: The created_by of this Space.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Space.

            The ID of the user who created this entity.

        :param created_by: The created_by of this Space.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this Space.

            The date and time when this entity was created.

        :return: The created_on of this Space.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Space.

            The date and time when this entity was created.

        :param created_on: The created_on of this Space.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def database(self):
        """Gets the database of this Space.

            The database in which the space's data are stored in.

        :return: The database of this Space.
        :rtype: TenantDatabase
        """
        return self._database

    @database.setter
    def database(self, database):
        """Sets the database of this Space.

            The database in which the space's data are stored in.

        :param database: The database of this Space.
        :type: TenantDatabase
        """

        self._database = database
    
    @property
    def deleted_by(self):
        """Gets the deleted_by of this Space.

            The ID of a user that deleted this entity.

        :return: The deleted_by of this Space.
        :rtype: int
        """
        return self._deleted_by

    @deleted_by.setter
    def deleted_by(self, deleted_by):
        """Sets the deleted_by of this Space.

            The ID of a user that deleted this entity.

        :param deleted_by: The deleted_by of this Space.
        :type: int
        """

        self._deleted_by = deleted_by
    
    @property
    def deleted_on(self):
        """Gets the deleted_on of this Space.

            The date and time when this entity was deleted.

        :return: The deleted_on of this Space.
        :rtype: datetime
        """
        return self._deleted_on

    @deleted_on.setter
    def deleted_on(self, deleted_on):
        """Sets the deleted_on of this Space.

            The date and time when this entity was deleted.

        :param deleted_on: The deleted_on of this Space.
        :type: datetime
        """

        self._deleted_on = deleted_on
    
    @property
    def id(self):
        """Gets the id of this Space.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Space.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Space.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Space.
        :type: int
        """

        self._id = id
    
    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this Space.

            

        :return: The last_modified_date of this Space.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this Space.

            

        :param last_modified_date: The last_modified_date of this Space.
        :type: datetime
        """

        self._last_modified_date = last_modified_date
    
    @property
    def name(self):
        """Gets the name of this Space.

            The space name is used internally to identify the space in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this Space.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Space.

            The space name is used internally to identify the space in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this Space.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Space.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Space.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Space.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Space.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def postal_address(self):
        """Gets the postal_address of this Space.

            The address to use in communication with clients for example in email, documents etc.

        :return: The postal_address of this Space.
        :rtype: SpaceAddress
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this Space.

            The address to use in communication with clients for example in email, documents etc.

        :param postal_address: The postal_address of this Space.
        :type: SpaceAddress
        """

        self._postal_address = postal_address
    
    @property
    def primary_currency(self):
        """Gets the primary_currency of this Space.

            This is the currency that is used to display aggregated amounts in the space.

        :return: The primary_currency of this Space.
        :rtype: str
        """
        return self._primary_currency

    @primary_currency.setter
    def primary_currency(self, primary_currency):
        """Sets the primary_currency of this Space.

            This is the currency that is used to display aggregated amounts in the space.

        :param primary_currency: The primary_currency of this Space.
        :type: str
        """

        self._primary_currency = primary_currency
    
    @property
    def request_limit(self):
        """Gets the request_limit of this Space.

            The request limit defines the maximum number of API request accepted within 2 minutes for this space. This limit can only be changed with special privileges.

        :return: The request_limit of this Space.
        :rtype: int
        """
        return self._request_limit

    @request_limit.setter
    def request_limit(self, request_limit):
        """Sets the request_limit of this Space.

            The request limit defines the maximum number of API request accepted within 2 minutes for this space. This limit can only be changed with special privileges.

        :param request_limit: The request_limit of this Space.
        :type: int
        """

        self._request_limit = request_limit
    
    @property
    def restricted_active(self):
        """Gets the restricted_active of this Space.

            Restricted active means that at least one account in the hierarchy is only restricted active, but all are either restricted active or active.

        :return: The restricted_active of this Space.
        :rtype: bool
        """
        return self._restricted_active

    @restricted_active.setter
    def restricted_active(self, restricted_active):
        """Sets the restricted_active of this Space.

            Restricted active means that at least one account in the hierarchy is only restricted active, but all are either restricted active or active.

        :param restricted_active: The restricted_active of this Space.
        :type: bool
        """

        self._restricted_active = restricted_active
    
    @property
    def state(self):
        """Gets the state of this Space.

            

        :return: The state of this Space.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Space.

            

        :param state: The state of this Space.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def technical_contact_addresses(self):
        """Gets the technical_contact_addresses of this Space.

            The email address provided as contact addresses will be informed about technical issues or errors triggered by the space.

        :return: The technical_contact_addresses of this Space.
        :rtype: list[str]
        """
        return self._technical_contact_addresses

    @technical_contact_addresses.setter
    def technical_contact_addresses(self, technical_contact_addresses):
        """Sets the technical_contact_addresses of this Space.

            The email address provided as contact addresses will be informed about technical issues or errors triggered by the space.

        :param technical_contact_addresses: The technical_contact_addresses of this Space.
        :type: list[str]
        """

        self._technical_contact_addresses = technical_contact_addresses
    
    @property
    def time_zone(self):
        """Gets the time_zone of this Space.

            The time zone assigned to the space determines the time offset for calculating dates within the space. This is typically used for background processed which needs to be triggered on a specific hour within the day. Changing the space time zone will not change the display of dates.

        :return: The time_zone of this Space.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Space.

            The time zone assigned to the space determines the time offset for calculating dates within the space. This is typically used for background processed which needs to be triggered on a specific hour within the day. Changing the space time zone will not change the display of dates.

        :param time_zone: The time_zone of this Space.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def version(self):
        """Gets the version of this Space.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Space.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Space.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Space.
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
        if issubclass(Space, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Space):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
