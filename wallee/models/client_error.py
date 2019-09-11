# coding: utf-8
import pprint
import six
from enum import Enum



class ClientError:

    swagger_types = {
    
        '_date': 'str',
        'default_message': 'str',
        'id': 'str',
        'message': 'str',
        'type': 'ClientErrorType',
    }

    attribute_map = {
        '_date': 'date','default_message': 'defaultMessage','id': 'id','message': 'message','type': 'type',
    }

    
    __date = None
    _default_message = None
    _id = None
    _message = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self._date = kwargs.get('_date', None)
        self.default_message = kwargs.get('default_message', None)
        self.id = kwargs.get('id', None)
        self.message = kwargs.get('message', None)
        self.type = kwargs.get('type', None)
        

    
    @property
    def _date(self):
        """Gets the _date of this ClientError.

            Date when an error has occurred.

        :return: The _date of this ClientError.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ClientError.

            Date when an error has occurred.

        :param _date: The _date of this ClientError.
        :type: str
        """

        self.__date = _date
    
    @property
    def default_message(self):
        """Gets the default_message of this ClientError.

            The error message which is translated into the default language (i.e. English).

        :return: The default_message of this ClientError.
        :rtype: str
        """
        return self._default_message

    @default_message.setter
    def default_message(self, default_message):
        """Sets the default_message of this ClientError.

            The error message which is translated into the default language (i.e. English).

        :param default_message: The default_message of this ClientError.
        :type: str
        """

        self._default_message = default_message
    
    @property
    def id(self):
        """Gets the id of this ClientError.

            Unique identifier of an error.

        :return: The id of this ClientError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ClientError.

            Unique identifier of an error.

        :param id: The id of this ClientError.
        :type: str
        """

        self._id = id
    
    @property
    def message(self):
        """Gets the message of this ClientError.

            The error message which is translated in into the language of the client.

        :return: The message of this ClientError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ClientError.

            The error message which is translated in into the language of the client.

        :param message: The message of this ClientError.
        :type: str
        """

        self._message = message
    
    @property
    def type(self):
        """Gets the type of this ClientError.

            The type of the client error.

        :return: The type of this ClientError.
        :rtype: ClientErrorType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ClientError.

            The type of the client error.

        :param type: The type of this ClientError.
        :type: ClientErrorType
        """

        self._type = type
    

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
        if issubclass(ClientError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ClientError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
