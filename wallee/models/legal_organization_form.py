# coding: utf-8
import pprint
import six
from enum import Enum



class LegalOrganizationForm:

    swagger_types = {
    
        'country': 'str',
        'description': 'list[LocalizedString]',
        'english_description': 'str',
        'id': 'int',
        'shortcut': 'list[LocalizedString]',
    }

    attribute_map = {
        'country': 'country','description': 'description','english_description': 'englishDescription','id': 'id','shortcut': 'shortcut',
    }

    
    _country = None
    _description = None
    _english_description = None
    _id = None
    _shortcut = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.country = kwargs.get('country', None)
        self.description = kwargs.get('description', None)
        self.english_description = kwargs.get('english_description', None)
        self.id = kwargs.get('id', None)
        self.shortcut = kwargs.get('shortcut', None)
        

    
    @property
    def country(self):
        """Gets the country of this LegalOrganizationForm.

            

        :return: The country of this LegalOrganizationForm.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this LegalOrganizationForm.

            

        :param country: The country of this LegalOrganizationForm.
        :type: str
        """

        self._country = country
    
    @property
    def description(self):
        """Gets the description of this LegalOrganizationForm.

            

        :return: The description of this LegalOrganizationForm.
        :rtype: list[LocalizedString]
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this LegalOrganizationForm.

            

        :param description: The description of this LegalOrganizationForm.
        :type: list[LocalizedString]
        """

        self._description = description
    
    @property
    def english_description(self):
        """Gets the english_description of this LegalOrganizationForm.

            

        :return: The english_description of this LegalOrganizationForm.
        :rtype: str
        """
        return self._english_description

    @english_description.setter
    def english_description(self, english_description):
        """Sets the english_description of this LegalOrganizationForm.

            

        :param english_description: The english_description of this LegalOrganizationForm.
        :type: str
        """

        self._english_description = english_description
    
    @property
    def id(self):
        """Gets the id of this LegalOrganizationForm.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this LegalOrganizationForm.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this LegalOrganizationForm.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this LegalOrganizationForm.
        :type: int
        """

        self._id = id
    
    @property
    def shortcut(self):
        """Gets the shortcut of this LegalOrganizationForm.

            

        :return: The shortcut of this LegalOrganizationForm.
        :rtype: list[LocalizedString]
        """
        return self._shortcut

    @shortcut.setter
    def shortcut(self, shortcut):
        """Sets the shortcut of this LegalOrganizationForm.

            

        :param shortcut: The shortcut of this LegalOrganizationForm.
        :type: list[LocalizedString]
        """

        self._shortcut = shortcut
    

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
        if issubclass(LegalOrganizationForm, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LegalOrganizationForm):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
