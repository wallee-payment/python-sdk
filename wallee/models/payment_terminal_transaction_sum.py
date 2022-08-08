# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalTransactionSum:

    swagger_types = {
    
        'brand': 'str',
        'dcc_tip_amount': 'float',
        'dcc_transaction_amount': 'float',
        'dcc_transaction_count': 'int',
        'id': 'int',
        'product': 'str',
        'transaction_amount': 'float',
        'transaction_count': 'int',
        'transaction_currency': 'str',
        'transaction_tip_amount': 'float',
        'version': 'int',
    }

    attribute_map = {
        'brand': 'brand','dcc_tip_amount': 'dccTipAmount','dcc_transaction_amount': 'dccTransactionAmount','dcc_transaction_count': 'dccTransactionCount','id': 'id','product': 'product','transaction_amount': 'transactionAmount','transaction_count': 'transactionCount','transaction_currency': 'transactionCurrency','transaction_tip_amount': 'transactionTipAmount','version': 'version',
    }

    
    _brand = None
    _dcc_tip_amount = None
    _dcc_transaction_amount = None
    _dcc_transaction_count = None
    _id = None
    _product = None
    _transaction_amount = None
    _transaction_count = None
    _transaction_currency = None
    _transaction_tip_amount = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.brand = kwargs.get('brand', None)
        self.dcc_tip_amount = kwargs.get('dcc_tip_amount', None)
        self.dcc_transaction_amount = kwargs.get('dcc_transaction_amount', None)
        self.dcc_transaction_count = kwargs.get('dcc_transaction_count', None)
        self.id = kwargs.get('id', None)
        self.product = kwargs.get('product', None)
        self.transaction_amount = kwargs.get('transaction_amount', None)
        self.transaction_count = kwargs.get('transaction_count', None)
        self.transaction_currency = kwargs.get('transaction_currency', None)
        self.transaction_tip_amount = kwargs.get('transaction_tip_amount', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def brand(self):
        """Gets the brand of this PaymentTerminalTransactionSum.

            

        :return: The brand of this PaymentTerminalTransactionSum.
        :rtype: str
        """
        return self._brand

    @brand.setter
    def brand(self, brand):
        """Sets the brand of this PaymentTerminalTransactionSum.

            

        :param brand: The brand of this PaymentTerminalTransactionSum.
        :type: str
        """

        self._brand = brand
    
    @property
    def dcc_tip_amount(self):
        """Gets the dcc_tip_amount of this PaymentTerminalTransactionSum.

            

        :return: The dcc_tip_amount of this PaymentTerminalTransactionSum.
        :rtype: float
        """
        return self._dcc_tip_amount

    @dcc_tip_amount.setter
    def dcc_tip_amount(self, dcc_tip_amount):
        """Sets the dcc_tip_amount of this PaymentTerminalTransactionSum.

            

        :param dcc_tip_amount: The dcc_tip_amount of this PaymentTerminalTransactionSum.
        :type: float
        """

        self._dcc_tip_amount = dcc_tip_amount
    
    @property
    def dcc_transaction_amount(self):
        """Gets the dcc_transaction_amount of this PaymentTerminalTransactionSum.

            

        :return: The dcc_transaction_amount of this PaymentTerminalTransactionSum.
        :rtype: float
        """
        return self._dcc_transaction_amount

    @dcc_transaction_amount.setter
    def dcc_transaction_amount(self, dcc_transaction_amount):
        """Sets the dcc_transaction_amount of this PaymentTerminalTransactionSum.

            

        :param dcc_transaction_amount: The dcc_transaction_amount of this PaymentTerminalTransactionSum.
        :type: float
        """

        self._dcc_transaction_amount = dcc_transaction_amount
    
    @property
    def dcc_transaction_count(self):
        """Gets the dcc_transaction_count of this PaymentTerminalTransactionSum.

            

        :return: The dcc_transaction_count of this PaymentTerminalTransactionSum.
        :rtype: int
        """
        return self._dcc_transaction_count

    @dcc_transaction_count.setter
    def dcc_transaction_count(self, dcc_transaction_count):
        """Sets the dcc_transaction_count of this PaymentTerminalTransactionSum.

            

        :param dcc_transaction_count: The dcc_transaction_count of this PaymentTerminalTransactionSum.
        :type: int
        """

        self._dcc_transaction_count = dcc_transaction_count
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalTransactionSum.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalTransactionSum.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalTransactionSum.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalTransactionSum.
        :type: int
        """

        self._id = id
    
    @property
    def product(self):
        """Gets the product of this PaymentTerminalTransactionSum.

            

        :return: The product of this PaymentTerminalTransactionSum.
        :rtype: str
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this PaymentTerminalTransactionSum.

            

        :param product: The product of this PaymentTerminalTransactionSum.
        :type: str
        """

        self._product = product
    
    @property
    def transaction_amount(self):
        """Gets the transaction_amount of this PaymentTerminalTransactionSum.

            

        :return: The transaction_amount of this PaymentTerminalTransactionSum.
        :rtype: float
        """
        return self._transaction_amount

    @transaction_amount.setter
    def transaction_amount(self, transaction_amount):
        """Sets the transaction_amount of this PaymentTerminalTransactionSum.

            

        :param transaction_amount: The transaction_amount of this PaymentTerminalTransactionSum.
        :type: float
        """

        self._transaction_amount = transaction_amount
    
    @property
    def transaction_count(self):
        """Gets the transaction_count of this PaymentTerminalTransactionSum.

            

        :return: The transaction_count of this PaymentTerminalTransactionSum.
        :rtype: int
        """
        return self._transaction_count

    @transaction_count.setter
    def transaction_count(self, transaction_count):
        """Sets the transaction_count of this PaymentTerminalTransactionSum.

            

        :param transaction_count: The transaction_count of this PaymentTerminalTransactionSum.
        :type: int
        """

        self._transaction_count = transaction_count
    
    @property
    def transaction_currency(self):
        """Gets the transaction_currency of this PaymentTerminalTransactionSum.

            

        :return: The transaction_currency of this PaymentTerminalTransactionSum.
        :rtype: str
        """
        return self._transaction_currency

    @transaction_currency.setter
    def transaction_currency(self, transaction_currency):
        """Sets the transaction_currency of this PaymentTerminalTransactionSum.

            

        :param transaction_currency: The transaction_currency of this PaymentTerminalTransactionSum.
        :type: str
        """

        self._transaction_currency = transaction_currency
    
    @property
    def transaction_tip_amount(self):
        """Gets the transaction_tip_amount of this PaymentTerminalTransactionSum.

            

        :return: The transaction_tip_amount of this PaymentTerminalTransactionSum.
        :rtype: float
        """
        return self._transaction_tip_amount

    @transaction_tip_amount.setter
    def transaction_tip_amount(self, transaction_tip_amount):
        """Sets the transaction_tip_amount of this PaymentTerminalTransactionSum.

            

        :param transaction_tip_amount: The transaction_tip_amount of this PaymentTerminalTransactionSum.
        :type: float
        """

        self._transaction_tip_amount = transaction_tip_amount
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalTransactionSum.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalTransactionSum.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalTransactionSum.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalTransactionSum.
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
        if issubclass(PaymentTerminalTransactionSum, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalTransactionSum):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
