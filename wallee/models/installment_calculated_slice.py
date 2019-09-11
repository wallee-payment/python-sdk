# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentCalculatedSlice:

    swagger_types = {
    
        'amount_including_tax': 'float',
        'due_on': 'datetime',
        'line_items': 'list[LineItem]',
    }

    attribute_map = {
        'amount_including_tax': 'amountIncludingTax','due_on': 'dueOn','line_items': 'lineItems',
    }

    
    _amount_including_tax = None
    _due_on = None
    _line_items = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount_including_tax = kwargs.get('amount_including_tax', None)
        self.due_on = kwargs.get('due_on', None)
        self.line_items = kwargs.get('line_items', None)
        

    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this InstallmentCalculatedSlice.

            

        :return: The amount_including_tax of this InstallmentCalculatedSlice.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this InstallmentCalculatedSlice.

            

        :param amount_including_tax: The amount_including_tax of this InstallmentCalculatedSlice.
        :type: float
        """

        self._amount_including_tax = amount_including_tax
    
    @property
    def due_on(self):
        """Gets the due_on of this InstallmentCalculatedSlice.

            

        :return: The due_on of this InstallmentCalculatedSlice.
        :rtype: datetime
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this InstallmentCalculatedSlice.

            

        :param due_on: The due_on of this InstallmentCalculatedSlice.
        :type: datetime
        """

        self._due_on = due_on
    
    @property
    def line_items(self):
        """Gets the line_items of this InstallmentCalculatedSlice.

            

        :return: The line_items of this InstallmentCalculatedSlice.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this InstallmentCalculatedSlice.

            

        :param line_items: The line_items of this InstallmentCalculatedSlice.
        :type: list[LineItem]
        """

        self._line_items = line_items
    

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
        if issubclass(InstallmentCalculatedSlice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentCalculatedSlice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
