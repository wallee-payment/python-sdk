# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractHumanUserUpdate:

    swagger_types = {
    
        'email_address': 'str',
        'firstname': 'str',
        'language': 'str',
        'lastname': 'str',
        'mobile_phone_number': 'str',
        'state': 'CreationEntityState',
        'time_zone': 'str',
        'two_factor_enabled': 'bool',
    }

    attribute_map = {
        'email_address': 'emailAddress','firstname': 'firstname','language': 'language','lastname': 'lastname','mobile_phone_number': 'mobilePhoneNumber','state': 'state','time_zone': 'timeZone','two_factor_enabled': 'twoFactorEnabled',
    }

    
    _email_address = None
    _firstname = None
    _language = None
    _lastname = None
    _mobile_phone_number = None
    _state = None
    _time_zone = None
    _two_factor_enabled = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.email_address = kwargs.get('email_address', None)
        self.firstname = kwargs.get('firstname', None)
        self.language = kwargs.get('language', None)
        self.lastname = kwargs.get('lastname', None)
        self.mobile_phone_number = kwargs.get('mobile_phone_number', None)
        self.state = kwargs.get('state', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.two_factor_enabled = kwargs.get('two_factor_enabled', None)
        

    
    @property
    def email_address(self):
        """Gets the email_address of this AbstractHumanUserUpdate.

            The user's email address.

        :return: The email_address of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AbstractHumanUserUpdate.

            The user's email address.

        :param email_address: The email_address of this AbstractHumanUserUpdate.
        :type: str
        """
        if email_address is not None and len(email_address) > 128:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `128`")

        self._email_address = email_address
    
    @property
    def firstname(self):
        """Gets the firstname of this AbstractHumanUserUpdate.

            The user's first name.

        :return: The firstname of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this AbstractHumanUserUpdate.

            The user's first name.

        :param firstname: The firstname of this AbstractHumanUserUpdate.
        :type: str
        """
        if firstname is not None and len(firstname) > 100:
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `100`")

        self._firstname = firstname
    
    @property
    def language(self):
        """Gets the language of this AbstractHumanUserUpdate.

            The user's preferred language.

        :return: The language of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractHumanUserUpdate.

            The user's preferred language.

        :param language: The language of this AbstractHumanUserUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def lastname(self):
        """Gets the lastname of this AbstractHumanUserUpdate.

            The user's last name.

        :return: The lastname of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this AbstractHumanUserUpdate.

            The user's last name.

        :param lastname: The lastname of this AbstractHumanUserUpdate.
        :type: str
        """
        if lastname is not None and len(lastname) > 100:
            raise ValueError("Invalid value for `lastname`, length must be less than or equal to `100`")

        self._lastname = lastname
    
    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this AbstractHumanUserUpdate.

            The user's mobile phone number.

        :return: The mobile_phone_number of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this AbstractHumanUserUpdate.

            The user's mobile phone number.

        :param mobile_phone_number: The mobile_phone_number of this AbstractHumanUserUpdate.
        :type: str
        """
        if mobile_phone_number is not None and len(mobile_phone_number) > 30:
            raise ValueError("Invalid value for `mobile_phone_number`, length must be less than or equal to `30`")

        self._mobile_phone_number = mobile_phone_number
    
    @property
    def state(self):
        """Gets the state of this AbstractHumanUserUpdate.

            The object's current state.

        :return: The state of this AbstractHumanUserUpdate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractHumanUserUpdate.

            The object's current state.

        :param state: The state of this AbstractHumanUserUpdate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def time_zone(self):
        """Gets the time_zone of this AbstractHumanUserUpdate.

            The user's time zone. If none is specified, the one provided by the browser will be used.

        :return: The time_zone of this AbstractHumanUserUpdate.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AbstractHumanUserUpdate.

            The user's time zone. If none is specified, the one provided by the browser will be used.

        :param time_zone: The time_zone of this AbstractHumanUserUpdate.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def two_factor_enabled(self):
        """Gets the two_factor_enabled of this AbstractHumanUserUpdate.

            Whether two-factor authentication is enabled for this user.

        :return: The two_factor_enabled of this AbstractHumanUserUpdate.
        :rtype: bool
        """
        return self._two_factor_enabled

    @two_factor_enabled.setter
    def two_factor_enabled(self, two_factor_enabled):
        """Sets the two_factor_enabled of this AbstractHumanUserUpdate.

            Whether two-factor authentication is enabled for this user.

        :param two_factor_enabled: The two_factor_enabled of this AbstractHumanUserUpdate.
        :type: bool
        """

        self._two_factor_enabled = two_factor_enabled
    

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
        if issubclass(AbstractHumanUserUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractHumanUserUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
