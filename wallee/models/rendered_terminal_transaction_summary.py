# coding: utf-8
import pprint
import six
from enum import Enum



class RenderedTerminalTransactionSummary:

    swagger_types = {
    
        'data': 'list[str]',
        'mime_type': 'str',
    }

    attribute_map = {
        'data': 'data','mime_type': 'mimeType',
    }

    
    _data = None
    _mime_type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.data = kwargs.get('data', None)
        self.mime_type = kwargs.get('mime_type', None)
        

    
    @property
    def data(self):
        """Gets the data of this RenderedTerminalTransactionSummary.

            The data property contains the binary data of the receipt document encoded as base 64 encoded string.

        :return: The data of this RenderedTerminalTransactionSummary.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RenderedTerminalTransactionSummary.

            The data property contains the binary data of the receipt document encoded as base 64 encoded string.

        :param data: The data of this RenderedTerminalTransactionSummary.
        :type: list[str]
        """

        self._data = data
    
    @property
    def mime_type(self):
        """Gets the mime_type of this RenderedTerminalTransactionSummary.

            The mime type indicates the format of the receipt document. The mime type depends on the requested receipt format.

        :return: The mime_type of this RenderedTerminalTransactionSummary.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this RenderedTerminalTransactionSummary.

            The mime type indicates the format of the receipt document. The mime type depends on the requested receipt format.

        :param mime_type: The mime_type of this RenderedTerminalTransactionSummary.
        :type: str
        """

        self._mime_type = mime_type
    

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
        if issubclass(RenderedTerminalTransactionSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RenderedTerminalTransactionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
