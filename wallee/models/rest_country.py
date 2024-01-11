# coding: utf-8
import pprint
import six
from enum import Enum



class RestCountry:

    swagger_types = {
    
        'address_format': 'RestAddressFormat',
        'iso_code2': 'str',
        'iso_code3': 'str',
        'name': 'str',
        'numeric_code': 'str',
        'state_codes': 'list[str]',
    }

    attribute_map = {
        'address_format': 'addressFormat','iso_code2': 'isoCode2','iso_code3': 'isoCode3','name': 'name','numeric_code': 'numericCode','state_codes': 'stateCodes',
    }

    
    _address_format = None
    _iso_code2 = None
    _iso_code3 = None
    _name = None
    _numeric_code = None
    _state_codes = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.address_format = kwargs.get('address_format', None)
        self.iso_code2 = kwargs.get('iso_code2', None)
        self.iso_code3 = kwargs.get('iso_code3', None)
        self.name = kwargs.get('name', None)
        self.numeric_code = kwargs.get('numeric_code', None)
        self.state_codes = kwargs.get('state_codes', None)
        

    
    @property
    def address_format(self):
        """Gets the address_format of this RestCountry.

            Specifies the country's way of formatting addresses.

        :return: The address_format of this RestCountry.
        :rtype: RestAddressFormat
        """
        return self._address_format

    @address_format.setter
    def address_format(self, address_format):
        """Sets the address_format of this RestCountry.

            Specifies the country's way of formatting addresses.

        :param address_format: The address_format of this RestCountry.
        :type: RestAddressFormat
        """

        self._address_format = address_format
    
    @property
    def iso_code2(self):
        """Gets the iso_code2 of this RestCountry.

            The country's two-letter code (ISO 3166-1 alpha-2 format).

        :return: The iso_code2 of this RestCountry.
        :rtype: str
        """
        return self._iso_code2

    @iso_code2.setter
    def iso_code2(self, iso_code2):
        """Sets the iso_code2 of this RestCountry.

            The country's two-letter code (ISO 3166-1 alpha-2 format).

        :param iso_code2: The iso_code2 of this RestCountry.
        :type: str
        """

        self._iso_code2 = iso_code2
    
    @property
    def iso_code3(self):
        """Gets the iso_code3 of this RestCountry.

            The country's three-letter code (ISO 3166-1 alpha-3 format).

        :return: The iso_code3 of this RestCountry.
        :rtype: str
        """
        return self._iso_code3

    @iso_code3.setter
    def iso_code3(self, iso_code3):
        """Sets the iso_code3 of this RestCountry.

            The country's three-letter code (ISO 3166-1 alpha-3 format).

        :param iso_code3: The iso_code3 of this RestCountry.
        :type: str
        """

        self._iso_code3 = iso_code3
    
    @property
    def name(self):
        """Gets the name of this RestCountry.

            The name of the country.

        :return: The name of this RestCountry.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestCountry.

            The name of the country.

        :param name: The name of this RestCountry.
        :type: str
        """

        self._name = name
    
    @property
    def numeric_code(self):
        """Gets the numeric_code of this RestCountry.

            The country's three-digit code (ISO 3166-1 numeric format).

        :return: The numeric_code of this RestCountry.
        :rtype: str
        """
        return self._numeric_code

    @numeric_code.setter
    def numeric_code(self, numeric_code):
        """Sets the numeric_code of this RestCountry.

            The country's three-digit code (ISO 3166-1 numeric format).

        :param numeric_code: The numeric_code of this RestCountry.
        :type: str
        """

        self._numeric_code = numeric_code
    
    @property
    def state_codes(self):
        """Gets the state_codes of this RestCountry.

            The codes of all regions (e.g. states, provinces) of the country (ISO 3166-2 format).

        :return: The state_codes of this RestCountry.
        :rtype: list[str]
        """
        return self._state_codes

    @state_codes.setter
    def state_codes(self, state_codes):
        """Sets the state_codes of this RestCountry.

            The codes of all regions (e.g. states, provinces) of the country (ISO 3166-2 format).

        :param state_codes: The state_codes of this RestCountry.
        :type: list[str]
        """

        self._state_codes = state_codes
    

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
        if issubclass(RestCountry, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RestCountry):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
