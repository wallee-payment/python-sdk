# coding: utf-8
import pprint
import six
from enum import Enum



class RestLanguage:

    swagger_types = {
    
        'country_code': 'str',
        'ietf_code': 'str',
        'iso2_code': 'str',
        'iso3_code': 'str',
        'name': 'str',
        'plural_expression': 'str',
        'primary_of_group': 'bool',
    }

    attribute_map = {
        'country_code': 'countryCode','ietf_code': 'ietfCode','iso2_code': 'iso2Code','iso3_code': 'iso3Code','name': 'name','plural_expression': 'pluralExpression','primary_of_group': 'primaryOfGroup',
    }

    
    _country_code = None
    _ietf_code = None
    _iso2_code = None
    _iso3_code = None
    _name = None
    _plural_expression = None
    _primary_of_group = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.country_code = kwargs.get('country_code', None)
        self.ietf_code = kwargs.get('ietf_code', None)
        self.iso2_code = kwargs.get('iso2_code', None)
        self.iso3_code = kwargs.get('iso3_code', None)
        self.name = kwargs.get('name', None)
        self.plural_expression = kwargs.get('plural_expression', None)
        self.primary_of_group = kwargs.get('primary_of_group', None)
        

    
    @property
    def country_code(self):
        """Gets the country_code of this RestLanguage.

            The two-letter code of the language's region (ISO 3166-1 alpha-2 format).

        :return: The country_code of this RestLanguage.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RestLanguage.

            The two-letter code of the language's region (ISO 3166-1 alpha-2 format).

        :param country_code: The country_code of this RestLanguage.
        :type: str
        """

        self._country_code = country_code
    
    @property
    def ietf_code(self):
        """Gets the ietf_code of this RestLanguage.

            The language's IETF tag consisting of the two-letter ISO code and region e.g. en-US, de-CH.

        :return: The ietf_code of this RestLanguage.
        :rtype: str
        """
        return self._ietf_code

    @ietf_code.setter
    def ietf_code(self, ietf_code):
        """Sets the ietf_code of this RestLanguage.

            The language's IETF tag consisting of the two-letter ISO code and region e.g. en-US, de-CH.

        :param ietf_code: The ietf_code of this RestLanguage.
        :type: str
        """

        self._ietf_code = ietf_code
    
    @property
    def iso2_code(self):
        """Gets the iso2_code of this RestLanguage.

            The language's two-letter code (ISO 639-1 format).

        :return: The iso2_code of this RestLanguage.
        :rtype: str
        """
        return self._iso2_code

    @iso2_code.setter
    def iso2_code(self, iso2_code):
        """Sets the iso2_code of this RestLanguage.

            The language's two-letter code (ISO 639-1 format).

        :param iso2_code: The iso2_code of this RestLanguage.
        :type: str
        """

        self._iso2_code = iso2_code
    
    @property
    def iso3_code(self):
        """Gets the iso3_code of this RestLanguage.

            The language's three-letter code (ISO 639-2/T format).

        :return: The iso3_code of this RestLanguage.
        :rtype: str
        """
        return self._iso3_code

    @iso3_code.setter
    def iso3_code(self, iso3_code):
        """Sets the iso3_code of this RestLanguage.

            The language's three-letter code (ISO 639-2/T format).

        :param iso3_code: The iso3_code of this RestLanguage.
        :type: str
        """

        self._iso3_code = iso3_code
    
    @property
    def name(self):
        """Gets the name of this RestLanguage.

            The name of the language.

        :return: The name of this RestLanguage.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestLanguage.

            The name of the language.

        :param name: The name of this RestLanguage.
        :type: str
        """

        self._name = name
    
    @property
    def plural_expression(self):
        """Gets the plural_expression of this RestLanguage.

            The expression to determine the plural index for a given number of items used to find the proper plural form for translations.

        :return: The plural_expression of this RestLanguage.
        :rtype: str
        """
        return self._plural_expression

    @plural_expression.setter
    def plural_expression(self, plural_expression):
        """Sets the plural_expression of this RestLanguage.

            The expression to determine the plural index for a given number of items used to find the proper plural form for translations.

        :param plural_expression: The plural_expression of this RestLanguage.
        :type: str
        """

        self._plural_expression = plural_expression
    
    @property
    def primary_of_group(self):
        """Gets the primary_of_group of this RestLanguage.

            Whether this is the primary language in a group of languages.

        :return: The primary_of_group of this RestLanguage.
        :rtype: bool
        """
        return self._primary_of_group

    @primary_of_group.setter
    def primary_of_group(self, primary_of_group):
        """Sets the primary_of_group of this RestLanguage.

            Whether this is the primary language in a group of languages.

        :param primary_of_group: The primary_of_group of this RestLanguage.
        :type: bool
        """

        self._primary_of_group = primary_of_group
    

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
        if issubclass(RestLanguage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RestLanguage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
