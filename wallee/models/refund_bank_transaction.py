# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class RefundBankTransaction(TransactionAwareEntity):

    swagger_types = {
    
        'bank_transaction': 'BankTransaction',
        'language': 'str',
        'refund': 'Refund',
        'refund_currency_amount': 'float',
        'refund_currency_value_amount': 'float',
        'space_view_id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'bank_transaction': 'bankTransaction','language': 'language','refund': 'refund','refund_currency_amount': 'refundCurrencyAmount','refund_currency_value_amount': 'refundCurrencyValueAmount','space_view_id': 'spaceViewId','version': 'version',
    }

    
    _bank_transaction = None
    _language = None
    _refund = None
    _refund_currency_amount = None
    _refund_currency_value_amount = None
    _space_view_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.bank_transaction = kwargs.get('bank_transaction', None)
        self.language = kwargs.get('language', None)
        self.refund = kwargs.get('refund', None)
        self.refund_currency_amount = kwargs.get('refund_currency_amount', None)
        self.refund_currency_value_amount = kwargs.get('refund_currency_value_amount', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def bank_transaction(self):
        """Gets the bank_transaction of this RefundBankTransaction.

            

        :return: The bank_transaction of this RefundBankTransaction.
        :rtype: BankTransaction
        """
        return self._bank_transaction

    @bank_transaction.setter
    def bank_transaction(self, bank_transaction):
        """Sets the bank_transaction of this RefundBankTransaction.

            

        :param bank_transaction: The bank_transaction of this RefundBankTransaction.
        :type: BankTransaction
        """

        self._bank_transaction = bank_transaction
    
    @property
    def language(self):
        """Gets the language of this RefundBankTransaction.

            The language that is linked to the object.

        :return: The language of this RefundBankTransaction.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this RefundBankTransaction.

            The language that is linked to the object.

        :param language: The language of this RefundBankTransaction.
        :type: str
        """

        self._language = language
    
    @property
    def refund(self):
        """Gets the refund of this RefundBankTransaction.

            

        :return: The refund of this RefundBankTransaction.
        :rtype: Refund
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this RefundBankTransaction.

            

        :param refund: The refund of this RefundBankTransaction.
        :type: Refund
        """

        self._refund = refund
    
    @property
    def refund_currency_amount(self):
        """Gets the refund_currency_amount of this RefundBankTransaction.

            Specify the posting amount in the refund's currency.

        :return: The refund_currency_amount of this RefundBankTransaction.
        :rtype: float
        """
        return self._refund_currency_amount

    @refund_currency_amount.setter
    def refund_currency_amount(self, refund_currency_amount):
        """Sets the refund_currency_amount of this RefundBankTransaction.

            Specify the posting amount in the refund's currency.

        :param refund_currency_amount: The refund_currency_amount of this RefundBankTransaction.
        :type: float
        """

        self._refund_currency_amount = refund_currency_amount
    
    @property
    def refund_currency_value_amount(self):
        """Gets the refund_currency_value_amount of this RefundBankTransaction.

            

        :return: The refund_currency_value_amount of this RefundBankTransaction.
        :rtype: float
        """
        return self._refund_currency_value_amount

    @refund_currency_value_amount.setter
    def refund_currency_value_amount(self, refund_currency_value_amount):
        """Sets the refund_currency_value_amount of this RefundBankTransaction.

            

        :param refund_currency_value_amount: The refund_currency_value_amount of this RefundBankTransaction.
        :type: float
        """

        self._refund_currency_value_amount = refund_currency_value_amount
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this RefundBankTransaction.

            

        :return: The space_view_id of this RefundBankTransaction.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this RefundBankTransaction.

            

        :param space_view_id: The space_view_id of this RefundBankTransaction.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def version(self):
        """Gets the version of this RefundBankTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this RefundBankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this RefundBankTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this RefundBankTransaction.
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
        if issubclass(RefundBankTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RefundBankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
