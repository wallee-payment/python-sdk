# coding: utf-8
import pprint
import six
from enum import Enum



class TerminalReceiptFetchRequest:

    swagger_types = {
    
        'format': 'TerminalReceiptFormat',
        'transaction': 'int',
        'width': 'int',
    }

    attribute_map = {
        'format': 'format','transaction': 'transaction','width': 'width',
    }

    
    _format = None
    _transaction = None
    _width = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.format = kwargs.get('format')

        self.transaction = kwargs.get('transaction')

        self.width = kwargs.get('width', None)
        

    
    @property
    def format(self):
        """Gets the format of this TerminalReceiptFetchRequest.

            The format determines in what format the receipts will be returned in.

        :return: The format of this TerminalReceiptFetchRequest.
        :rtype: TerminalReceiptFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this TerminalReceiptFetchRequest.

            The format determines in what format the receipts will be returned in.

        :param format: The format of this TerminalReceiptFetchRequest.
        :type: TerminalReceiptFormat
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")

        self._format = format
    
    @property
    def transaction(self):
        """Gets the transaction of this TerminalReceiptFetchRequest.

            Provide here the ID of the transaction for which the receipts should be fetched.

        :return: The transaction of this TerminalReceiptFetchRequest.
        :rtype: int
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TerminalReceiptFetchRequest.

            Provide here the ID of the transaction for which the receipts should be fetched.

        :param transaction: The transaction of this TerminalReceiptFetchRequest.
        :type: int
        """
        if transaction is None:
            raise ValueError("Invalid value for `transaction`, must not be `None`")

        self._transaction = transaction
    
    @property
    def width(self):
        """Gets the width of this TerminalReceiptFetchRequest.

            The width controls how width the document will be rendered. In case of the PDF format the width is in mm. In case of the text format the width is in the number of chars per line.

        :return: The width of this TerminalReceiptFetchRequest.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this TerminalReceiptFetchRequest.

            The width controls how width the document will be rendered. In case of the PDF format the width is in mm. In case of the text format the width is in the number of chars per line.

        :param width: The width of this TerminalReceiptFetchRequest.
        :type: int
        """

        self._width = width
    

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
        if issubclass(TerminalReceiptFetchRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TerminalReceiptFetchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
