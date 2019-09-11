# coding: utf-8
import pprint
import six
from enum import Enum



class DatabaseTranslatedString:

    swagger_types = {
    
        'available_languages': 'list[str]',
        'display_name': 'str',
        'items': 'list[DatabaseTranslatedStringItem]',
    }

    attribute_map = {
        'available_languages': 'availableLanguages','display_name': 'displayName','items': 'items',
    }

    
    _available_languages = None
    _display_name = None
    _items = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.available_languages = kwargs.get('available_languages', None)
        self.display_name = kwargs.get('display_name', None)
        self.items = kwargs.get('items', None)
        

    
    @property
    def available_languages(self):
        """Gets the available_languages of this DatabaseTranslatedString.

            

        :return: The available_languages of this DatabaseTranslatedString.
        :rtype: list[str]
        """
        return self._available_languages

    @available_languages.setter
    def available_languages(self, available_languages):
        """Sets the available_languages of this DatabaseTranslatedString.

            

        :param available_languages: The available_languages of this DatabaseTranslatedString.
        :type: list[str]
        """

        self._available_languages = available_languages
    
    @property
    def display_name(self):
        """Gets the display_name of this DatabaseTranslatedString.

            

        :return: The display_name of this DatabaseTranslatedString.
        :rtype: str
        """
        return self._display_name

    @display_name.setter
    def display_name(self, display_name):
        """Sets the display_name of this DatabaseTranslatedString.

            

        :param display_name: The display_name of this DatabaseTranslatedString.
        :type: str
        """

        self._display_name = display_name
    
    @property
    def items(self):
        """Gets the items of this DatabaseTranslatedString.

            

        :return: The items of this DatabaseTranslatedString.
        :rtype: list[DatabaseTranslatedStringItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this DatabaseTranslatedString.

            

        :param items: The items of this DatabaseTranslatedString.
        :type: list[DatabaseTranslatedStringItem]
        """

        self._items = items
    

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
        if issubclass(DatabaseTranslatedString, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DatabaseTranslatedString):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
