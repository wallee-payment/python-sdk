# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalDccTransactionSum:

    swagger_types = {
    
        'brand': 'str',
        'dcc_amount': 'float',
        'dcc_currency': 'str',
        'id': 'int',
        'transaction_amount': 'float',
        'transaction_count': 'int',
        'transaction_currency': 'str',
        'version': 'int',
    }

    attribute_map = {
        'brand': 'brand','dcc_amount': 'dccAmount','dcc_currency': 'dccCurrency','id': 'id','transaction_amount': 'transactionAmount','transaction_count': 'transactionCount','transaction_currency': 'transactionCurrency','version': 'version',
    }

    
    _brand = None
    _dcc_amount = None
    _dcc_currency = None
    _id = None
    _transaction_amount = None
    _transaction_count = None
    _transaction_currency = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.brand = kwargs.get('brand', None)
        self.dcc_amount = kwargs.get('dcc_amount', None)
        self.dcc_currency = kwargs.get('dcc_currency', None)
        self.id = kwargs.get('id', None)
        self.transaction_amount = kwargs.get('transaction_amount', None)
        self.transaction_count = kwargs.get('transaction_count', None)
        self.transaction_currency = kwargs.get('transaction_currency', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def brand(self):
        """Gets the brand of this PaymentTerminalDccTransactionSum.

            

        :return: The brand of this PaymentTerminalDccTransactionSum.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentTerminalDccTransactionSum.

            

        :param brand: The brand of this PaymentTerminalDccTransactionSum.
        :type: str
        """

        self._brand = brand
    
    @property
    def dcc_amount(self):
        """Gets the dcc_amount of this PaymentTerminalDccTransactionSum.

            

        :return: The dcc_amount of this PaymentTerminalDccTransactionSum.
        :rtype: float
        """
        return self._dcc_amount

    @dcc_amount.setter
    def dcc_amount(self, dcc_amount):
        """Sets the dcc_amount of this PaymentTerminalDccTransactionSum.

            

        :param dcc_amount: The dcc_amount of this PaymentTerminalDccTransactionSum.
        :type: float
        """

        self._dcc_amount = dcc_amount
    
    @property
    def dcc_currency(self):
        """Gets the dcc_currency of this PaymentTerminalDccTransactionSum.

            

        :return: The dcc_currency of this PaymentTerminalDccTransactionSum.
        :rtype: str
        """
        return self._dcc_currency

    @dcc_currency.setter
    def dcc_currency(self, dcc_currency):
        """Sets the dcc_currency of this PaymentTerminalDccTransactionSum.

            

        :param dcc_currency: The dcc_currency of this PaymentTerminalDccTransactionSum.
        :type: str
        """

        self._dcc_currency = dcc_currency
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalDccTransactionSum.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalDccTransactionSum.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalDccTransactionSum.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalDccTransactionSum.
        :type: int
        """

        self._id = id
    
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PaymentTerminalDccTransactionSum.

            

        :return: The transaction_amount of this PaymentTerminalDccTransactionSum.
        :rtype: float
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PaymentTerminalDccTransactionSum.

            

        :param transaction_amount: The transaction_amount of this PaymentTerminalDccTransactionSum.
        :type: float
        """

        self._transaction_amount = transaction_amount
    
    @property
    def transaction_count(self):
        """Gets the transaction_count of this PaymentTerminalDccTransactionSum.

            

        :return: The transaction_count of this PaymentTerminalDccTransactionSum.
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this PaymentTerminalDccTransactionSum.

            

        :param transaction_count: The transaction_count of this PaymentTerminalDccTransactionSum.
        :type: int
        """

        self._transaction_count = transaction_count
    
    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this PaymentTerminalDccTransactionSum.

            

        :return: The transaction_currency of this PaymentTerminalDccTransactionSum.
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this PaymentTerminalDccTransactionSum.

            

        :param transaction_currency: The transaction_currency of this PaymentTerminalDccTransactionSum.
        :type: str
        """

        self._transaction_currency = transaction_currency
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalDccTransactionSum.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalDccTransactionSum.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalDccTransactionSum.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalDccTransactionSum.
        :type: int
        """

        self._version = version
    

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
        if issubclass(PaymentTerminalDccTransactionSum, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalDccTransactionSum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
