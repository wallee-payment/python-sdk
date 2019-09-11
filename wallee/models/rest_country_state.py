# coding: utf-8
import pprint
import six
from enum import Enum



class RestCountryState:

    swagger_types = {
    
        'code': 'str',
        'country_code': 'str',
        'id': 'str',
        'name': 'str',
    }

    attribute_map = {
        'code': 'code','country_code': 'countryCode','id': 'id','name': 'name',
    }

    
    _code = None
    _country_code = None
    _id = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.code = kwargs.get('code', None)
        self.country_code = kwargs.get('country_code', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def code(self):
        """Gets the code of this RestCountryState.

            The code of the state identifies the state. The code is typically used within addresses. Some countries may not provide a code. For those the field is null.

        :return: The code of this RestCountryState.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this RestCountryState.

            The code of the state identifies the state. The code is typically used within addresses. Some countries may not provide a code. For those the field is null.

        :param code: The code of this RestCountryState.
        :type: str
        """

        self._code = code
    
    @property
    def country_code(self):
        """Gets the country_code of this RestCountryState.

            The country code in ISO two letter format (e.g. UK, DE, CH, US).

        :return: The country_code of this RestCountryState.
        :rtype: str
        """
        return self._country_code

    @country_code.setter
    def country_code(self, country_code):
        """Sets the country_code of this RestCountryState.

            The country code in ISO two letter format (e.g. UK, DE, CH, US).

        :param country_code: The country_code of this RestCountryState.
        :type: str
        """

        self._country_code = country_code
    
    @property
    def id(self):
        """Gets the id of this RestCountryState.

            The ID of the state corresponds to the subdivision identifier defined in ISO 3166-2. The format consists of the country code followed by a dash and a subdivision identifier.

        :return: The id of this RestCountryState.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this RestCountryState.

            The ID of the state corresponds to the subdivision identifier defined in ISO 3166-2. The format consists of the country code followed by a dash and a subdivision identifier.

        :param id: The id of this RestCountryState.
        :type: str
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this RestCountryState.

            The name is a human readable label of the state in the language of the region.

        :return: The name of this RestCountryState.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestCountryState.

            The name is a human readable label of the state in the language of the region.

        :param name: The name of this RestCountryState.
        :type: str
        """

        self._name = name
    

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
        if issubclass(RestCountryState, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RestCountryState):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
