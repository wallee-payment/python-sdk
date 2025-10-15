# coding: utf-8
import pprint
import six
from enum import Enum



class ChargeBankTransaction:

    swagger_types = {
    
        'bank_transaction': 'BankTransaction',
        'completion': 'int',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'space_view_id': 'int',
        'transaction': 'Transaction',
        'transaction_currency_amount': 'float',
        'transaction_currency_value_amount': 'float',
        'version': 'int',
    }

    attribute_map = {
        'bank_transaction': 'bankTransaction','completion': 'completion','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','space_view_id': 'spaceViewId','transaction': 'transaction','transaction_currency_amount': 'transactionCurrencyAmount','transaction_currency_value_amount': 'transactionCurrencyValueAmount','version': 'version',
    }

    
    _bank_transaction = None
    _completion = None
    _id = None
    _language = None
    _linked_space_id = None
    _linked_transaction = None
    _space_view_id = None
    _transaction = None
    _transaction_currency_amount = None
    _transaction_currency_value_amount = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.bank_transaction = kwargs.get('bank_transaction', None)
        self.completion = kwargs.get('completion', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.transaction = kwargs.get('transaction', None)
        self.transaction_currency_amount = kwargs.get('transaction_currency_amount', None)
        self.transaction_currency_value_amount = kwargs.get('transaction_currency_value_amount', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def bank_transaction(self):
        """Gets the bank_transaction of this ChargeBankTransaction.

            Provides general information about the bank transaction.

        :return: The bank_transaction of this ChargeBankTransaction.
        :rtype: BankTransaction
        """
        return self._bank_transaction

    @bank_transaction.setter
    def bank_transaction(self, bank_transaction):
        """Sets the bank_transaction of this ChargeBankTransaction.

            Provides general information about the bank transaction.

        :param bank_transaction: The bank_transaction of this ChargeBankTransaction.
        :type: BankTransaction
        """

        self._bank_transaction = bank_transaction
    
    @property
    def completion(self):
        """Gets the completion of this ChargeBankTransaction.

            The transaction completion this bank transaction is belongs to.

        :return: The completion of this ChargeBankTransaction.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this ChargeBankTransaction.

            The transaction completion this bank transaction is belongs to.

        :param completion: The completion of this ChargeBankTransaction.
        :type: int
        """

        self._completion = completion
    
    @property
    def id(self):
        """Gets the id of this ChargeBankTransaction.

            A unique identifier for the object.

        :return: The id of this ChargeBankTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChargeBankTransaction.

            A unique identifier for the object.

        :param id: The id of this ChargeBankTransaction.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this ChargeBankTransaction.

            The language that is linked to the object.

        :return: The language of this ChargeBankTransaction.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ChargeBankTransaction.

            The language that is linked to the object.

        :param language: The language of this ChargeBankTransaction.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ChargeBankTransaction.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this ChargeBankTransaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ChargeBankTransaction.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this ChargeBankTransaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this ChargeBankTransaction.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this ChargeBankTransaction.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this ChargeBankTransaction.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this ChargeBankTransaction.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this ChargeBankTransaction.

            The ID of the space view this object is linked to.

        :return: The space_view_id of this ChargeBankTransaction.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this ChargeBankTransaction.

            The ID of the space view this object is linked to.

        :param space_view_id: The space_view_id of this ChargeBankTransaction.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def transaction(self):
        """Gets the transaction of this ChargeBankTransaction.

            The payment transaction this bank transaction belongs to.

        :return: The transaction of this ChargeBankTransaction.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ChargeBankTransaction.

            The payment transaction this bank transaction belongs to.

        :param transaction: The transaction of this ChargeBankTransaction.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def transaction_currency_amount(self):
        """Gets the transaction_currency_amount of this ChargeBankTransaction.

            The posting amount represents the monetary value of the bank transaction, recorded in the payment transaction's currency, before applying any adjustments.

        :return: The transaction_currency_amount of this ChargeBankTransaction.
        :rtype: float
        """
        return self._transaction_currency_amount

    @transaction_currency_amount.setter
    def transaction_currency_amount(self, transaction_currency_amount):
        """Sets the transaction_currency_amount of this ChargeBankTransaction.

            The posting amount represents the monetary value of the bank transaction, recorded in the payment transaction's currency, before applying any adjustments.

        :param transaction_currency_amount: The transaction_currency_amount of this ChargeBankTransaction.
        :type: float
        """

        self._transaction_currency_amount = transaction_currency_amount
    
    @property
    def transaction_currency_value_amount(self):
        """Gets the transaction_currency_value_amount of this ChargeBankTransaction.

            The value amount represents the net monetary value of the bank transaction, recorded in the payment transaction's currency, after applicable deductions.

        :return: The transaction_currency_value_amount of this ChargeBankTransaction.
        :rtype: float
        """
        return self._transaction_currency_value_amount

    @transaction_currency_value_amount.setter
    def transaction_currency_value_amount(self, transaction_currency_value_amount):
        """Sets the transaction_currency_value_amount of this ChargeBankTransaction.

            The value amount represents the net monetary value of the bank transaction, recorded in the payment transaction's currency, after applicable deductions.

        :param transaction_currency_value_amount: The transaction_currency_value_amount of this ChargeBankTransaction.
        :type: float
        """

        self._transaction_currency_value_amount = transaction_currency_value_amount
    
    @property
    def version(self):
        """Gets the version of this ChargeBankTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this ChargeBankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeBankTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

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
