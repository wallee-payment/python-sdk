# coding: utf-8
import pprint
import six
from enum import Enum



class DatabaseTranslatedStringItemCreate:

    swagger_types = {
    
        'language': 'str',
        'translation': 'str',
    }

    attribute_map = {
        'language': 'language','translation': 'translation',
    }

    
    _language = None
    _translation = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.language = kwargs.get('language')

        self.translation = kwargs.get('translation', None)
        

    
    @property
    def language(self):
        """Gets the language of this DatabaseTranslatedStringItemCreate.

            

        :return: The language of this DatabaseTranslatedStringItemCreate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DatabaseTranslatedStringItemCreate.

            

        :param language: The language of this DatabaseTranslatedStringItemCreate.
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")

        self._language = language
    
    @property
    def translation(self):
        """Gets the translation of this DatabaseTranslatedStringItemCreate.

            

        :return: The translation of this DatabaseTranslatedStringItemCreate.
        :rtype: str
        """
        return self._translation

    @translation.setter
    def translation(self, translation):
        """Sets the translation of this DatabaseTranslatedStringItemCreate.

            

        :param translation: The translation of this DatabaseTranslatedStringItemCreate.
        :type: str
        """
        if translation is not None and len(translation) > 16777216:
            raise ValueError("Invalid value for `translation`, length must be less than or equal to `16777216`")

        self._translation = translation
    

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
        if issubclass(DatabaseTranslatedStringItemCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DatabaseTranslatedStringItemCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
