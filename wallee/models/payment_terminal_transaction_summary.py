# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalTransactionSummary:

    swagger_types = {
    
        'dcc_transaction_sums': 'list[PaymentTerminalDccTransactionSum]',
        'ended_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'number_of_transactions': 'int',
        'payment_terminal': 'int',
        'receipt': 'str',
        'started_on': 'datetime',
        'transaction_sums': 'list[PaymentTerminalTransactionSum]',
        'version': 'int',
    }

    attribute_map = {
        'dcc_transaction_sums': 'dccTransactionSums','ended_on': 'endedOn','id': 'id','linked_space_id': 'linkedSpaceId','number_of_transactions': 'numberOfTransactions','payment_terminal': 'paymentTerminal','receipt': 'receipt','started_on': 'startedOn','transaction_sums': 'transactionSums','version': 'version',
    }

    
    _dcc_transaction_sums = None
    _ended_on = None
    _id = None
    _linked_space_id = None
    _number_of_transactions = None
    _payment_terminal = None
    _receipt = None
    _started_on = None
    _transaction_sums = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.dcc_transaction_sums = kwargs.get('dcc_transaction_sums', None)
        self.ended_on = kwargs.get('ended_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.number_of_transactions = kwargs.get('number_of_transactions', None)
        self.payment_terminal = kwargs.get('payment_terminal', None)
        self.receipt = kwargs.get('receipt', None)
        self.started_on = kwargs.get('started_on', None)
        self.transaction_sums = kwargs.get('transaction_sums', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def dcc_transaction_sums(self):
        """Gets the dcc_transaction_sums of this PaymentTerminalTransactionSummary.

            

        :return: The dcc_transaction_sums of this PaymentTerminalTransactionSummary.
        :rtype: list[PaymentTerminalDccTransactionSum]
        """
        return self._dcc_transaction_sums

    @dcc_transaction_sums.setter
    def dcc_transaction_sums(self, dcc_transaction_sums):
        """Sets the dcc_transaction_sums of this PaymentTerminalTransactionSummary.

            

        :param dcc_transaction_sums: The dcc_transaction_sums of this PaymentTerminalTransactionSummary.
        :type: list[PaymentTerminalDccTransactionSum]
        """

        self._dcc_transaction_sums = dcc_transaction_sums
    
    @property
    def ended_on(self):
        """Gets the ended_on of this PaymentTerminalTransactionSummary.

            

        :return: The ended_on of this PaymentTerminalTransactionSummary.
        :rtype: datetime
        """
        return self._ended_on

    @ended_on.setter
    def ended_on(self, ended_on):
        """Sets the ended_on of this PaymentTerminalTransactionSummary.

            

        :param ended_on: The ended_on of this PaymentTerminalTransactionSummary.
        :type: datetime
        """

        self._ended_on = ended_on
    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalTransactionSummary.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentTerminalTransactionSummary.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalTransactionSummary.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentTerminalTransactionSummary.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalTransactionSummary.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentTerminalTransactionSummary.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalTransactionSummary.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalTransactionSummary.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def number_of_transactions(self):
        """Gets the number_of_transactions of this PaymentTerminalTransactionSummary.

            

        :return: The number_of_transactions of this PaymentTerminalTransactionSummary.
        :rtype: int
        """
        return self._number_of_transactions

    @number_of_transactions.setter
    def number_of_transactions(self, number_of_transactions):
        """Sets the number_of_transactions of this PaymentTerminalTransactionSummary.

            

        :param number_of_transactions: The number_of_transactions of this PaymentTerminalTransactionSummary.
        :type: int
        """

        self._number_of_transactions = number_of_transactions
    
    @property
    def payment_terminal(self):
        """Gets the payment_terminal of this PaymentTerminalTransactionSummary.

            

        :return: The payment_terminal of this PaymentTerminalTransactionSummary.
        :rtype: int
        """
        return self._payment_terminal

    @payment_terminal.setter
    def payment_terminal(self, payment_terminal):
        """Sets the payment_terminal of this PaymentTerminalTransactionSummary.

            

        :param payment_terminal: The payment_terminal of this PaymentTerminalTransactionSummary.
        :type: int
        """

        self._payment_terminal = payment_terminal
    
    @property
    def receipt(self):
        """Gets the receipt of this PaymentTerminalTransactionSummary.

            

        :return: The receipt of this PaymentTerminalTransactionSummary.
        :rtype: str
        """
        return self._receipt

    @receipt.setter
    def receipt(self, receipt):
        """Sets the receipt of this PaymentTerminalTransactionSummary.

            

        :param receipt: The receipt of this PaymentTerminalTransactionSummary.
        :type: str
        """

        self._receipt = receipt
    
    @property
    def started_on(self):
        """Gets the started_on of this PaymentTerminalTransactionSummary.

            

        :return: The started_on of this PaymentTerminalTransactionSummary.
        :rtype: datetime
        """
        return self._started_on

    @started_on.setter
    def started_on(self, started_on):
        """Sets the started_on of this PaymentTerminalTransactionSummary.

            

        :param started_on: The started_on of this PaymentTerminalTransactionSummary.
        :type: datetime
        """

        self._started_on = started_on
    
    @property
    def transaction_sums(self):
        """Gets the transaction_sums of this PaymentTerminalTransactionSummary.

            

        :return: The transaction_sums of this PaymentTerminalTransactionSummary.
        :rtype: list[PaymentTerminalTransactionSum]
        """
        return self._transaction_sums

    @transaction_sums.setter
    def transaction_sums(self, transaction_sums):
        """Sets the transaction_sums of this PaymentTerminalTransactionSummary.

            

        :param transaction_sums: The transaction_sums of this PaymentTerminalTransactionSummary.
        :type: list[PaymentTerminalTransactionSum]
        """

        self._transaction_sums = transaction_sums
    
    @property
    def version(self):
        """Gets the version of this PaymentTerminalTransactionSummary.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentTerminalTransactionSummary.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentTerminalTransactionSummary.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentTerminalTransactionSummary.
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
        if issubclass(PaymentTerminalTransactionSummary, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalTransactionSummary):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
