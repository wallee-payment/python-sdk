# coding: utf-8
import pprint
import six
from enum import Enum



class CardholderAuthenticationCreate:

    swagger_types = {
    
        'authentication_identifier': 'str',
        'authentication_response': 'CardAuthenticationResponse',
        'authentication_value': 'str',
        'electronic_commerce_indicator': 'str',
        'version': 'CardAuthenticationVersion',
    }

    attribute_map = {
        'authentication_identifier': 'authenticationIdentifier','authentication_response': 'authenticationResponse','authentication_value': 'authenticationValue','electronic_commerce_indicator': 'electronicCommerceIndicator','version': 'version',
    }

    
    _authentication_identifier = None
    _authentication_response = None
    _authentication_value = None
    _electronic_commerce_indicator = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.authentication_identifier = kwargs.get('authentication_identifier', None)
        self.authentication_response = kwargs.get('authentication_response')

        self.authentication_value = kwargs.get('authentication_value', None)
        self.electronic_commerce_indicator = kwargs.get('electronic_commerce_indicator', None)
        self.version = kwargs.get('version')

        

    
    @property
    def authentication_identifier(self):
        """Gets the authentication_identifier of this CardholderAuthenticationCreate.

            The authentication identifier as assigned by authentication system (e.g. XID or DSTransactionID).

        :return: The authentication_identifier of this CardholderAuthenticationCreate.
        :rtype: str
        """
        return self._authentication_identifier

    @authentication_identifier.setter
    def authentication_identifier(self, authentication_identifier):
        """Sets the authentication_identifier of this CardholderAuthenticationCreate.

            The authentication identifier as assigned by authentication system (e.g. XID or DSTransactionID).

        :param authentication_identifier: The authentication_identifier of this CardholderAuthenticationCreate.
        :type: str
        """

        self._authentication_identifier = authentication_identifier
    
    @property
    def authentication_response(self):
        """Gets the authentication_response of this CardholderAuthenticationCreate.

            

        :return: The authentication_response of this CardholderAuthenticationCreate.
        :rtype: CardAuthenticationResponse
        """
        return self._authentication_response

    @authentication_response.setter
    def authentication_response(self, authentication_response):
        """Sets the authentication_response of this CardholderAuthenticationCreate.

            

        :param authentication_response: The authentication_response of this CardholderAuthenticationCreate.
        :type: CardAuthenticationResponse
        """
        if authentication_response is None:
            raise ValueError("Invalid value for `authentication_response`, must not be `None`")

        self._authentication_response = authentication_response
    
    @property
    def authentication_value(self):
        """Gets the authentication_value of this CardholderAuthenticationCreate.

            The cardholder authentication value. Also known as Cardholder Authentication Verification Value (CAVV).

        :return: The authentication_value of this CardholderAuthenticationCreate.
        :rtype: str
        """
        return self._authentication_value

    @authentication_value.setter
    def authentication_value(self, authentication_value):
        """Sets the authentication_value of this CardholderAuthenticationCreate.

            The cardholder authentication value. Also known as Cardholder Authentication Verification Value (CAVV).

        :param authentication_value: The authentication_value of this CardholderAuthenticationCreate.
        :type: str
        """

        self._authentication_value = authentication_value
    
    @property
    def electronic_commerce_indicator(self):
        """Gets the electronic_commerce_indicator of this CardholderAuthenticationCreate.

            The Electronic Commerce Indicator (ECI) value. The ECI is returned by authentication system and indicates the outcome/status of authentication.

        :return: The electronic_commerce_indicator of this CardholderAuthenticationCreate.
        :rtype: str
        """
        return self._electronic_commerce_indicator

    @electronic_commerce_indicator.setter
    def electronic_commerce_indicator(self, electronic_commerce_indicator):
        """Sets the electronic_commerce_indicator of this CardholderAuthenticationCreate.

            The Electronic Commerce Indicator (ECI) value. The ECI is returned by authentication system and indicates the outcome/status of authentication.

        :param electronic_commerce_indicator: The electronic_commerce_indicator of this CardholderAuthenticationCreate.
        :type: str
        """

        self._electronic_commerce_indicator = electronic_commerce_indicator
    
    @property
    def version(self):
        """Gets the version of this CardholderAuthenticationCreate.

            

        :return: The version of this CardholderAuthenticationCreate.
        :rtype: CardAuthenticationVersion
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CardholderAuthenticationCreate.

            

        :param version: The version of this CardholderAuthenticationCreate.
        :type: CardAuthenticationVersion
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

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
        if issubclass(CardholderAuthenticationCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CardholderAuthenticationCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
