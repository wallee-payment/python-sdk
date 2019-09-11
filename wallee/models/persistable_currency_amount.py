# coding: utf-8
import pprint
import six
from enum import Enum



class PersistableCurrencyAmount:

    swagger_types = {
    
        'amount': 'float',
        'currency': 'str',
    }

    attribute_map = {
        'amount': 'amount','currency': 'currency',
    }

    
    _amount = None
    _currency = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.currency = kwargs.get('currency', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this PersistableCurrencyAmount.

            

        :return: The amount of this PersistableCurrencyAmount.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this PersistableCurrencyAmount.

            

        :param amount: The amount of this PersistableCurrencyAmount.
        :type: float
        """

        self._amount = amount
    
    @property
    def currency(self):
        """Gets the currency of this PersistableCurrencyAmount.

            

        :return: The currency of this PersistableCurrencyAmount.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PersistableCurrencyAmount.

            

        :param currency: The currency of this PersistableCurrencyAmount.
        :type: str
        """

        self._currency = currency
    

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
        if issubclass(PersistableCurrencyAmount, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PersistableCurrencyAmount):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
