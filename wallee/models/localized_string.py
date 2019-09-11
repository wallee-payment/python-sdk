# coding: utf-8
import pprint
import six
from enum import Enum



class LocalizedString:

    swagger_types = {
    
        'display_name': 'str',
        'language': 'str',
        'string': 'str',
    }

    attribute_map = {
        'display_name': 'displayName','language': 'language','string': 'string',
    }

    
    _display_name = None
    _language = None
    _string = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.display_name = kwargs.get('display_name', None)
        self.language = kwargs.get('language', None)
        self.string = kwargs.get('string', None)
        

    
    @property
    def display_name(self):
        """Gets the display_name of this LocalizedString.

            

        :return: The display_name of this LocalizedString.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this LocalizedString.

            

        :param display_name: The display_name of this LocalizedString.
        :type: str
        """

        self._display_name = display_name
    
    @property
    def language(self):
        """Gets the language of this LocalizedString.

            

        :return: The language of this LocalizedString.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this LocalizedString.

            

        :param language: The language of this LocalizedString.
        :type: str
        """

        self._language = language
    
    @property
    def string(self):
        """Gets the string of this LocalizedString.

            

        :return: The string of this LocalizedString.
        :rtype: str
        """
        return self._string

    @string.setter
    def string(self, string):
        """Sets the string of this LocalizedString.

            

        :param string: The string of this LocalizedString.
        :type: str
        """

        self._string = string
    

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
        if issubclass(LocalizedString, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LocalizedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
