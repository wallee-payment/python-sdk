# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractSpaceUpdate:

    swagger_types = {
    
        'last_modified_date': 'datetime',
        'name': 'str',
        'postal_address': 'SpaceAddressCreate',
        'primary_currency': 'str',
        'request_limit': 'int',
        'state': 'CreationEntityState',
        'technical_contact_addresses': 'list[str]',
        'time_zone': 'str',
    }

    attribute_map = {
        'last_modified_date': 'lastModifiedDate','name': 'name','postal_address': 'postalAddress','primary_currency': 'primaryCurrency','request_limit': 'requestLimit','state': 'state','technical_contact_addresses': 'technicalContactAddresses','time_zone': 'timeZone',
    }

    
    _last_modified_date = None
    _name = None
    _postal_address = None
    _primary_currency = None
    _request_limit = None
    _state = None
    _technical_contact_addresses = None
    _time_zone = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.last_modified_date = kwargs.get('last_modified_date', None)
        self.name = kwargs.get('name', None)
        self.postal_address = kwargs.get('postal_address', None)
        self.primary_currency = kwargs.get('primary_currency', None)
        self.request_limit = kwargs.get('request_limit', None)
        self.state = kwargs.get('state', None)
        self.technical_contact_addresses = kwargs.get('technical_contact_addresses', None)
        self.time_zone = kwargs.get('time_zone', None)
        

    
    @property
    def last_modified_date(self):
        """Gets the last_modified_date of this AbstractSpaceUpdate.

            

        :return: The last_modified_date of this AbstractSpaceUpdate.
        :rtype: datetime
        """
        return self._last_modified_date

    @last_modified_date.setter
    def last_modified_date(self, last_modified_date):
        """Sets the last_modified_date of this AbstractSpaceUpdate.

            

        :param last_modified_date: The last_modified_date of this AbstractSpaceUpdate.
        :type: datetime
        """

        self._last_modified_date = last_modified_date
    
    @property
    def name(self):
        """Gets the name of this AbstractSpaceUpdate.

            The space name is used internally to identify the space in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this AbstractSpaceUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractSpaceUpdate.

            The space name is used internally to identify the space in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this AbstractSpaceUpdate.
        :type: str
        """
        if name is not None and len(name) > 200:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `200`")
        if name is not None and len(name) < 3:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `3`")

        self._name = name
    
    @property
    def postal_address(self):
        """Gets the postal_address of this AbstractSpaceUpdate.

            The address to use in communication with clients for example in email, documents etc.

        :return: The postal_address of this AbstractSpaceUpdate.
        :rtype: SpaceAddressCreate
        """
        return self._postal_address

    @postal_address.setter
    def postal_address(self, postal_address):
        """Sets the postal_address of this AbstractSpaceUpdate.

            The address to use in communication with clients for example in email, documents etc.

        :param postal_address: The postal_address of this AbstractSpaceUpdate.
        :type: SpaceAddressCreate
        """

        self._postal_address = postal_address
    
    @property
    def primary_currency(self):
        """Gets the primary_currency of this AbstractSpaceUpdate.

            This is the currency that is used to display aggregated amounts in the space.

        :return: The primary_currency of this AbstractSpaceUpdate.
        :rtype: str
        """
        return self._primary_currency

    @primary_currency.setter
    def primary_currency(self, primary_currency):
        """Sets the primary_currency of this AbstractSpaceUpdate.

            This is the currency that is used to display aggregated amounts in the space.

        :param primary_currency: The primary_currency of this AbstractSpaceUpdate.
        :type: str
        """

        self._primary_currency = primary_currency
    
    @property
    def request_limit(self):
        """Gets the request_limit of this AbstractSpaceUpdate.

            The request limit defines the maximum number of API request accepted within 2 minutes for this space. This limit can only be changed with special privileges.

        :return: The request_limit of this AbstractSpaceUpdate.
        :rtype: int
        """
        return self._request_limit

    @request_limit.setter
    def request_limit(self, request_limit):
        """Sets the request_limit of this AbstractSpaceUpdate.

            The request limit defines the maximum number of API request accepted within 2 minutes for this space. This limit can only be changed with special privileges.

        :param request_limit: The request_limit of this AbstractSpaceUpdate.
        :type: int
        """

        self._request_limit = request_limit
    
    @property
    def state(self):
        """Gets the state of this AbstractSpaceUpdate.

            

        :return: The state of this AbstractSpaceUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractSpaceUpdate.

            

        :param state: The state of this AbstractSpaceUpdate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def technical_contact_addresses(self):
        """Gets the technical_contact_addresses of this AbstractSpaceUpdate.

            The email address provided as contact addresses will be informed about technical issues or errors triggered by the space.

        :return: The technical_contact_addresses of this AbstractSpaceUpdate.
        :rtype: list[str]
        """
        return self._technical_contact_addresses

    @technical_contact_addresses.setter
    def technical_contact_addresses(self, technical_contact_addresses):
        """Sets the technical_contact_addresses of this AbstractSpaceUpdate.

            The email address provided as contact addresses will be informed about technical issues or errors triggered by the space.

        :param technical_contact_addresses: The technical_contact_addresses of this AbstractSpaceUpdate.
        :type: list[str]
        """

        self._technical_contact_addresses = technical_contact_addresses
    
    @property
    def time_zone(self):
        """Gets the time_zone of this AbstractSpaceUpdate.

            The time zone assigned to the space determines the time offset for calculating dates within the space. This is typically used for background processed which needs to be triggered on a specific hour within the day. Changing the space time zone will not change the display of dates.

        :return: The time_zone of this AbstractSpaceUpdate.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AbstractSpaceUpdate.

            The time zone assigned to the space determines the time offset for calculating dates within the space. This is typically used for background processed which needs to be triggered on a specific hour within the day. Changing the space time zone will not change the display of dates.

        :param time_zone: The time_zone of this AbstractSpaceUpdate.
        :type: str
        """

        self._time_zone = time_zone
    

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
        if issubclass(AbstractSpaceUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractSpaceUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
