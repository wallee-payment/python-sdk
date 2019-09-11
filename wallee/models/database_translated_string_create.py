# coding: utf-8
import pprint
import six
from enum import Enum



class DatabaseTranslatedStringCreate:

    swagger_types = {
    
        'items': 'list[DatabaseTranslatedStringItemCreate]',
    }

    attribute_map = {
        'items': 'items',
    }

    
    _items = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.items = kwargs.get('items', None)
        

    
    @property
    def items(self):
        """Gets the items of this DatabaseTranslatedStringCreate.

            

        :return: The items of this DatabaseTranslatedStringCreate.
        :rtype: list[DatabaseTranslatedStringItemCreate]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this DatabaseTranslatedStringCreate.

            

        :param items: The items of this DatabaseTranslatedStringCreate.
        :type: list[DatabaseTranslatedStringItemCreate]
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
        if issubclass(DatabaseTranslatedStringCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DatabaseTranslatedStringCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
