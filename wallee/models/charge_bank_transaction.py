# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ChargeBankTransaction(TransactionAwareEntity):

    swagger_types = {
    
        'bank_transaction': 'BankTransaction',
        'completion': 'int',
        'language': 'str',
        'space_view_id': 'int',
        'transaction': 'Transaction',
        'transaction_currency_amount': 'float',
        'transaction_currency_value_amount': 'float',
        'version': 'int',
    }

    attribute_map = {
        'bank_transaction': 'bankTransaction','completion': 'completion','language': 'language','space_view_id': 'spaceViewId','transaction': 'transaction','transaction_currency_amount': 'transactionCurrencyAmount','transaction_currency_value_amount': 'transactionCurrencyValueAmount','version': 'version',
    }

    
    _bank_transaction = None
    _completion = None
    _language = None
    _space_view_id = None
    _transaction = None
    _transaction_currency_amount = None
    _transaction_currency_value_amount = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.bank_transaction = kwargs.get('bank_transaction', None)
        self.completion = kwargs.get('completion', None)
        self.language = kwargs.get('language', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.transaction = kwargs.get('transaction', None)
        self.transaction_currency_amount = kwargs.get('transaction_currency_amount', None)
        self.transaction_currency_value_amount = kwargs.get('transaction_currency_value_amount', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def bank_transaction(self):
        """Gets the bank_transaction of this ChargeBankTransaction.

            

        :return: The bank_transaction of this ChargeBankTransaction.
        :rtype: BankTransaction
        """
        return self._bank_transaction

    @bank_transaction.setter
    def bank_transaction(self, bank_transaction):
        """Sets the bank_transaction of this ChargeBankTransaction.

            

        :param bank_transaction: The bank_transaction of this ChargeBankTransaction.
        :type: BankTransaction
        """

        self._bank_transaction = bank_transaction
    
    @property
    def completion(self):
        """Gets the completion of this ChargeBankTransaction.

            

        :return: The completion of this ChargeBankTransaction.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this ChargeBankTransaction.

            

        :param completion: The completion of this ChargeBankTransaction.
        :type: int
        """

        self._completion = completion
    
    @property
    def language(self):
        """Gets the language of this ChargeBankTransaction.

            

        :return: The language of this ChargeBankTransaction.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ChargeBankTransaction.

            

        :param language: The language of this ChargeBankTransaction.
        :type: str
        """

        self._language = language
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this ChargeBankTransaction.

            

        :return: The space_view_id of this ChargeBankTransaction.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this ChargeBankTransaction.

            

        :param space_view_id: The space_view_id of this ChargeBankTransaction.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def transaction(self):
        """Gets the transaction of this ChargeBankTransaction.

            

        :return: The transaction of this ChargeBankTransaction.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ChargeBankTransaction.

            

        :param transaction: The transaction of this ChargeBankTransaction.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def transaction_currency_amount(self):
        """Gets the transaction_currency_amount of this ChargeBankTransaction.

            Specify the posting amount in the transaction's currency.

        :return: The transaction_currency_amount of this ChargeBankTransaction.
        :rtype: float
        """
        return self._transaction_currency_amount

    @transaction_currency_amount.setter
    def transaction_currency_amount(self, transaction_currency_amount):
        """Sets the transaction_currency_amount of this ChargeBankTransaction.

            Specify the posting amount in the transaction's currency.

        :param transaction_currency_amount: The transaction_currency_amount of this ChargeBankTransaction.
        :type: float
        """

        self._transaction_currency_amount = transaction_currency_amount
    
    @property
    def transaction_currency_value_amount(self):
        """Gets the transaction_currency_value_amount of this ChargeBankTransaction.

            

        :return: The transaction_currency_value_amount of this ChargeBankTransaction.
        :rtype: float
        """
        return self._transaction_currency_value_amount

    @transaction_currency_value_amount.setter
    def transaction_currency_value_amount(self, transaction_currency_value_amount):
        """Sets the transaction_currency_value_amount of this ChargeBankTransaction.

            

        :param transaction_currency_value_amount: The transaction_currency_value_amount of this ChargeBankTransaction.
        :type: float
        """

        self._transaction_currency_value_amount = transaction_currency_value_amount
    
    @property
    def version(self):
        """Gets the version of this ChargeBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ChargeBankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeBankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ChargeBankTransaction.
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
        if issubclass(ChargeBankTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeBankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
