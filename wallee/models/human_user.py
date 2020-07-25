# coding: utf-8
import pprint
import six
from enum import Enum



class HumanUser:

    swagger_types = {
    
        'email_address': 'str',
        'email_address_verified': 'bool',
        'firstname': 'str',
        'language': 'str',
        'lastname': 'str',
        'mobile_phone_number': 'str',
        'mobile_phone_verified': 'bool',
        'primary_account': 'Account',
        'scope': 'Scope',
        'time_zone': 'str',
        'two_factor_enabled': 'bool',
        'two_factor_type': 'TwoFactorAuthenticationType',
    }

    attribute_map = {
        'email_address': 'emailAddress','email_address_verified': 'emailAddressVerified','firstname': 'firstname','language': 'language','lastname': 'lastname','mobile_phone_number': 'mobilePhoneNumber','mobile_phone_verified': 'mobilePhoneVerified','primary_account': 'primaryAccount','scope': 'scope','time_zone': 'timeZone','two_factor_enabled': 'twoFactorEnabled','two_factor_type': 'twoFactorType',
    }

    
    _email_address = None
    _email_address_verified = None
    _firstname = None
    _language = None
    _lastname = None
    _mobile_phone_number = None
    _mobile_phone_verified = None
    _primary_account = None
    _scope = None
    _time_zone = None
    _two_factor_enabled = None
    _two_factor_type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.email_address = kwargs.get('email_address', None)
        self.email_address_verified = kwargs.get('email_address_verified', None)
        self.firstname = kwargs.get('firstname', None)
        self.language = kwargs.get('language', None)
        self.lastname = kwargs.get('lastname', None)
        self.mobile_phone_number = kwargs.get('mobile_phone_number', None)
        self.mobile_phone_verified = kwargs.get('mobile_phone_verified', None)
        self.primary_account = kwargs.get('primary_account', None)
        self.scope = kwargs.get('scope', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.two_factor_enabled = kwargs.get('two_factor_enabled', None)
        self.two_factor_type = kwargs.get('two_factor_type', None)
        

    
    @property
    def email_address(self):
        """Gets the email_address of this HumanUser.

            The email address of the user.

        :return: The email_address of this HumanUser.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this HumanUser.

            The email address of the user.

        :param email_address: The email_address of this HumanUser.
        :type: str
        """
        if email_address is not None and len(email_address) > 128:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `128`")

        self._email_address = email_address
    
    @property
    def email_address_verified(self):
        """Gets the email_address_verified of this HumanUser.

            Defines whether a user is verified or not.

        :return: The email_address_verified of this HumanUser.
        :rtype: bool
        """
        return self._email_address_verified

    @email_address_verified.setter
    def email_address_verified(self, email_address_verified):
        """Sets the email_address_verified of this HumanUser.

            Defines whether a user is verified or not.

        :param email_address_verified: The email_address_verified of this HumanUser.
        :type: bool
        """

        self._email_address_verified = email_address_verified
    
    @property
    def firstname(self):
        """Gets the firstname of this HumanUser.

            The first name of the user.

        :return: The firstname of this HumanUser.
        :rtype: str
        """
        return self._firstname

    @firstname.setter
    def firstname(self, firstname):
        """Sets the firstname of this HumanUser.

            The first name of the user.

        :param firstname: The firstname of this HumanUser.
        :type: str
        """
        if firstname is not None and len(firstname) > 100:
            raise ValueError("Invalid value for `firstname`, length must be less than or equal to `100`")

        self._firstname = firstname
    
    @property
    def language(self):
        """Gets the language of this HumanUser.

            The preferred language of the user.

        :return: The language of this HumanUser.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this HumanUser.

            The preferred language of the user.

        :param language: The language of this HumanUser.
        :type: str
        """

        self._language = language
    
    @property
    def lastname(self):
        """Gets the lastname of this HumanUser.

            The last name of the user.

        :return: The lastname of this HumanUser.
        :rtype: str
        """
        return self._lastname

    @lastname.setter
    def lastname(self, lastname):
        """Sets the lastname of this HumanUser.

            The last name of the user.

        :param lastname: The lastname of this HumanUser.
        :type: str
        """
        if lastname is not None and len(lastname) > 100:
            raise ValueError("Invalid value for `lastname`, length must be less than or equal to `100`")

        self._lastname = lastname
    
    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this HumanUser.

            

        :return: The mobile_phone_number of this HumanUser.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this HumanUser.

            

        :param mobile_phone_number: The mobile_phone_number of this HumanUser.
        :type: str
        """
        if mobile_phone_number is not None and len(mobile_phone_number) > 30:
            raise ValueError("Invalid value for `mobile_phone_number`, length must be less than or equal to `30`")

        self._mobile_phone_number = mobile_phone_number
    
    @property
    def mobile_phone_verified(self):
        """Gets the mobile_phone_verified of this HumanUser.

            Defines whether a users mobile phone number is verified or not.

        :return: The mobile_phone_verified of this HumanUser.
        :rtype: bool
        """
        return self._mobile_phone_verified

    @mobile_phone_verified.setter
    def mobile_phone_verified(self, mobile_phone_verified):
        """Sets the mobile_phone_verified of this HumanUser.

            Defines whether a users mobile phone number is verified or not.

        :param mobile_phone_verified: The mobile_phone_verified of this HumanUser.
        :type: bool
        """

        self._mobile_phone_verified = mobile_phone_verified
    
    @property
    def primary_account(self):
        """Gets the primary_account of this HumanUser.

            The primary account links the user to a specific account.

        :return: The primary_account of this HumanUser.
        :rtype: Account
        """
        return self._primary_account

    @primary_account.setter
    def primary_account(self, primary_account):
        """Sets the primary_account of this HumanUser.

            The primary account links the user to a specific account.

        :param primary_account: The primary_account of this HumanUser.
        :type: Account
        """

        self._primary_account = primary_account
    
    @property
    def scope(self):
        """Gets the scope of this HumanUser.

            The scope to which the user belongs to.

        :return: The scope of this HumanUser.
        :rtype: Scope
        """
        return self._scope

    @scope.setter
    def scope(self, scope):
        """Sets the scope of this HumanUser.

            The scope to which the user belongs to.

        :param scope: The scope of this HumanUser.
        :type: Scope
        """

        self._scope = scope
    
    @property
    def time_zone(self):
        """Gets the time_zone of this HumanUser.

            The time zone which is applied for the user. If no timezone is specified the browser is used to determine an appropriate time zone.

        :return: The time_zone of this HumanUser.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this HumanUser.

            The time zone which is applied for the user. If no timezone is specified the browser is used to determine an appropriate time zone.

        :param time_zone: The time_zone of this HumanUser.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def two_factor_enabled(self):
        """Gets the two_factor_enabled of this HumanUser.

            Defines whether two-factor authentication is enabled for this user.

        :return: The two_factor_enabled of this HumanUser.
        :rtype: bool
        """
        return self._two_factor_enabled

    @two_factor_enabled.setter
    def two_factor_enabled(self, two_factor_enabled):
        """Sets the two_factor_enabled of this HumanUser.

            Defines whether two-factor authentication is enabled for this user.

        :param two_factor_enabled: The two_factor_enabled of this HumanUser.
        :type: bool
        """

        self._two_factor_enabled = two_factor_enabled
    
    @property
    def two_factor_type(self):
        """Gets the two_factor_type of this HumanUser.

            

        :return: The two_factor_type of this HumanUser.
        :rtype: TwoFactorAuthenticationType
        """
        return self._two_factor_type

    @two_factor_type.setter
    def two_factor_type(self, two_factor_type):
        """Sets the two_factor_type of this HumanUser.

            

        :param two_factor_type: The two_factor_type of this HumanUser.
        :type: TwoFactorAuthenticationType
        """

        self._two_factor_type = two_factor_type
    

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
        if issubclass(HumanUser, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, HumanUser):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
