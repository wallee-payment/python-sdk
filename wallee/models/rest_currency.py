# coding: utf-8
import pprint
import six
from enum import Enum



class RestCurrency:

    swagger_types = {
    
        'currency_code': 'str',
        'fraction_digits': 'int',
        'name': 'str',
        'numeric_code': 'int',
    }

    attribute_map = {
        'currency_code': 'currencyCode','fraction_digits': 'fractionDigits','name': 'name','numeric_code': 'numericCode',
    }

    
    _currency_code = None
    _fraction_digits = None
    _name = None
    _numeric_code = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.currency_code = kwargs.get('currency_code', None)
        self.fraction_digits = kwargs.get('fraction_digits', None)
        self.name = kwargs.get('name', None)
        self.numeric_code = kwargs.get('numeric_code', None)
        

    
    @property
    def currency_code(self):
        """Gets the currency_code of this RestCurrency.

            The currency's three-letter code (ISO 4217 format).

        :return: The currency_code of this RestCurrency.
        :rtype: str
        """
        return self._currency_code

    @currency_code.setter
    def currency_code(self, currency_code):
        """Sets the currency_code of this RestCurrency.

            The currency's three-letter code (ISO 4217 format).

        :param currency_code: The currency_code of this RestCurrency.
        :type: str
        """

        self._currency_code = currency_code
    
    @property
    def fraction_digits(self):
        """Gets the fraction_digits of this RestCurrency.

            The currency's number of decimals. When calculating amounts in this currency, the fraction digits determine the accuracy.

        :return: The fraction_digits of this RestCurrency.
        :rtype: int
        """
        return self._fraction_digits

    @fraction_digits.setter
    def fraction_digits(self, fraction_digits):
        """Sets the fraction_digits of this RestCurrency.

            The currency's number of decimals. When calculating amounts in this currency, the fraction digits determine the accuracy.

        :param fraction_digits: The fraction_digits of this RestCurrency.
        :type: int
        """

        self._fraction_digits = fraction_digits
    
    @property
    def name(self):
        """Gets the name of this RestCurrency.

            The name of the currency.

        :return: The name of this RestCurrency.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this RestCurrency.

            The name of the currency.

        :param name: The name of this RestCurrency.
        :type: str
        """

        self._name = name
    
    @property
    def numeric_code(self):
        """Gets the numeric_code of this RestCurrency.

            The currency's three-digit code (ISO 4217 format).

        :return: The numeric_code of this RestCurrency.
        :rtype: int
        """
        return self._numeric_code

    @numeric_code.setter
    def numeric_code(self, numeric_code):
        """Sets the numeric_code of this RestCurrency.

            The currency's three-digit code (ISO 4217 format).

        :param numeric_code: The numeric_code of this RestCurrency.
        :type: int
        """

        self._numeric_code = numeric_code
    

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
        if issubclass(RestCurrency, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RestCurrency):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
