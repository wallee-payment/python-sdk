# coding: utf-8
import pprint
import six
from enum import Enum



class ServerError:

    swagger_types = {
    
        '_date': 'str',
        'id': 'str',
        'message': 'str',
    }

    attribute_map = {
        '_date': 'date','id': 'id','message': 'message',
    }

    
    __date = None
    _id = None
    _message = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self._date = kwargs.get('_date', None)
        self.id = kwargs.get('id', None)
        self.message = kwargs.get('message', None)
        

    
    @property
    def _date(self):
        """Gets the _date of this ServerError.

            Date when an error has occurred.

        :return: The _date of this ServerError.
        :rtype: str
        """
        return self.__date

    @_date.setter
    def _date(self, _date):
        """Sets the _date of this ServerError.

            Date when an error has occurred.

        :param _date: The _date of this ServerError.
        :type: str
        """

        self.__date = _date
    
    @property
    def id(self):
        """Gets the id of this ServerError.

            Unique identifier of an error.

        :return: The id of this ServerError.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ServerError.

            Unique identifier of an error.

        :param id: The id of this ServerError.
        :type: str
        """

        self._id = id
    
    @property
    def message(self):
        """Gets the message of this ServerError.

            This message describes an error.

        :return: The message of this ServerError.
        :rtype: str
        """
        return self._message

    @message.setter
    def message(self, message):
        """Sets the message of this ServerError.

            This message describes an error.

        :param message: The message of this ServerError.
        :type: str
        """

        self._message = message
    

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
        if issubclass(ServerError, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ServerError):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
