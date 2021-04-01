# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAdjustment:

    swagger_types = {
    
        'amount_excluding_tax': 'float',
        'amount_including_tax': 'float',
        'rate_in_percentage': 'float',
        'tax': 'Tax',
        'type': 'int',
    }

    attribute_map = {
        'amount_excluding_tax': 'amountExcludingTax','amount_including_tax': 'amountIncludingTax','rate_in_percentage': 'rateInPercentage','tax': 'tax','type': 'type',
    }

    
    _amount_excluding_tax = None
    _amount_including_tax = None
    _rate_in_percentage = None
    _tax = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount_excluding_tax = kwargs.get('amount_excluding_tax', None)
        self.amount_including_tax = kwargs.get('amount_including_tax', None)
        self.rate_in_percentage = kwargs.get('rate_in_percentage', None)
        self.tax = kwargs.get('tax', None)
        self.type = kwargs.get('type', None)
        

    
    @property
    def amount_excluding_tax(self):
        """Gets the amount_excluding_tax of this PaymentAdjustment.

            

        :return: The amount_excluding_tax of this PaymentAdjustment.
        :rtype: float
        """
        return self._amount_excluding_tax

    @amount_excluding_tax.setter
    def amount_excluding_tax(self, amount_excluding_tax):
        """Sets the amount_excluding_tax of this PaymentAdjustment.

            

        :param amount_excluding_tax: The amount_excluding_tax of this PaymentAdjustment.
        :type: float
        """

        self._amount_excluding_tax = amount_excluding_tax
    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this PaymentAdjustment.

            The total amount of this adjustment including taxes.

        :return: The amount_including_tax of this PaymentAdjustment.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this PaymentAdjustment.

            The total amount of this adjustment including taxes.

        :param amount_including_tax: The amount_including_tax of this PaymentAdjustment.
        :type: float
        """

        self._amount_including_tax = amount_including_tax
    
    @property
    def rate_in_percentage(self):
        """Gets the rate_in_percentage of this PaymentAdjustment.

            The rate in percentage is the rate on which the adjustment amount was calculated with.

        :return: The rate_in_percentage of this PaymentAdjustment.
        :rtype: float
        """
        return self._rate_in_percentage

    @rate_in_percentage.setter
    def rate_in_percentage(self, rate_in_percentage):
        """Sets the rate_in_percentage of this PaymentAdjustment.

            The rate in percentage is the rate on which the adjustment amount was calculated with.

        :param rate_in_percentage: The rate_in_percentage of this PaymentAdjustment.
        :type: float
        """

        self._rate_in_percentage = rate_in_percentage
    
    @property
    def tax(self):
        """Gets the tax of this PaymentAdjustment.

            

        :return: The tax of this PaymentAdjustment.
        :rtype: Tax
        """
        return self._tax

    @tax.setter
    def tax(self, tax):
        """Sets the tax of this PaymentAdjustment.

            

        :param tax: The tax of this PaymentAdjustment.
        :type: Tax
        """

        self._tax = tax
    
    @property
    def type(self):
        """Gets the type of this PaymentAdjustment.

            

        :return: The type of this PaymentAdjustment.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this PaymentAdjustment.

            

        :param type: The type of this PaymentAdjustment.
        :type: int
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
        if issubclass(PaymentAdjustment, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAdjustment):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
