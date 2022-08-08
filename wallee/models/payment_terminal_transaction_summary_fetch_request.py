# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalTransactionSummaryFetchRequest:

    swagger_types = {
    
        'format': 'TerminalReceiptFormat',
        'summary_id': 'int',
        'width': 'int',
    }

    attribute_map = {
        'format': 'format','summary_id': 'summaryId','width': 'width',
    }

    
    _format = None
    _summary_id = None
    _width = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.format = kwargs.get('format')

        self.summary_id = kwargs.get('summary_id')

        self.width = kwargs.get('width', None)
        

    
    @property
    def format(self):
        """Gets the format of this PaymentTerminalTransactionSummaryFetchRequest.

            The format determines in what format the receipt will be returned in.

        :return: The format of this PaymentTerminalTransactionSummaryFetchRequest.
        :rtype: TerminalReceiptFormat
        """
        return self._format

    @format.setter
    def format(self, format):
        """Sets the format of this PaymentTerminalTransactionSummaryFetchRequest.

            The format determines in what format the receipt will be returned in.

        :param format: The format of this PaymentTerminalTransactionSummaryFetchRequest.
        :type: TerminalReceiptFormat
        """
        if format is None:
            raise ValueError("Invalid value for `format`, must not be `None`")

        self._format = format
    
    @property
    def summary_id(self):
        """Gets the summary_id of this PaymentTerminalTransactionSummaryFetchRequest.

            The id of the transaction summary receipt whose content should be returned.

        :return: The summary_id of this PaymentTerminalTransactionSummaryFetchRequest.
        :rtype: int
        """
        return self._summary_id

    @summary_id.setter
    def summary_id(self, summary_id):
        """Sets the summary_id of this PaymentTerminalTransactionSummaryFetchRequest.

            The id of the transaction summary receipt whose content should be returned.

        :param summary_id: The summary_id of this PaymentTerminalTransactionSummaryFetchRequest.
        :type: int
        """
        if summary_id is None:
            raise ValueError("Invalid value for `summary_id`, must not be `None`")

        self._summary_id = summary_id
    
    @property
    def width(self):
        """Gets the width of this PaymentTerminalTransactionSummaryFetchRequest.

            The width controls how width the document will be rendered. In case of the PDF format the width is in mm. In case of the text format the width is in the number of chars per line.

        :return: The width of this PaymentTerminalTransactionSummaryFetchRequest.
        :rtype: int
        """
        return self._width

    @width.setter
    def width(self, width):
        """Sets the width of this PaymentTerminalTransactionSummaryFetchRequest.

            The width controls how width the document will be rendered. In case of the PDF format the width is in mm. In case of the text format the width is in the number of chars per line.

        :param width: The width of this PaymentTerminalTransactionSummaryFetchRequest.
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
        if issubclass(PaymentTerminalTransactionSummaryFetchRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalTransactionSummaryFetchRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
