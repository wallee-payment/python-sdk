# coding: utf-8
import pprint
import six
from enum import Enum



class TokenizedCardData:

    swagger_types = {
    
        'cryptogram': 'CardCryptogram',
        'initial_recurring_transaction': 'bool',
        'recurring_indicator': 'RecurringIndicator',
        'token_requestor_id': 'str',
    }

    attribute_map = {
        'cryptogram': 'cryptogram','initial_recurring_transaction': 'initialRecurringTransaction','recurring_indicator': 'recurringIndicator','token_requestor_id': 'tokenRequestorId',
    }

    
    _cryptogram = None
    _initial_recurring_transaction = None
    _recurring_indicator = None
    _token_requestor_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.cryptogram = kwargs.get('cryptogram', None)
        self.initial_recurring_transaction = kwargs.get('initial_recurring_transaction', None)
        self.recurring_indicator = kwargs.get('recurring_indicator', None)
        self.token_requestor_id = kwargs.get('token_requestor_id', None)
        

    
    @property
    def cryptogram(self):
        """Gets the cryptogram of this TokenizedCardData.

            An additional authentication value that enhances the security of tokenized card transactions.

        :return: The cryptogram of this TokenizedCardData.
        :rtype: CardCryptogram
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """Sets the cryptogram of this TokenizedCardData.

            An additional authentication value that enhances the security of tokenized card transactions.

        :param cryptogram: The cryptogram of this TokenizedCardData.
        :type: CardCryptogram
        """

        self._cryptogram = cryptogram
    
    @property
    def initial_recurring_transaction(self):
        """Gets the initial_recurring_transaction of this TokenizedCardData.

            Whether the transaction is an initial recurring transaction, based on the recurring indicator. This is used to identify the first transaction in a recurring payment setup.

        :return: The initial_recurring_transaction of this TokenizedCardData.
        :rtype: bool
        """
        return self._initial_recurring_transaction

    @initial_recurring_transaction.setter
    def initial_recurring_transaction(self, initial_recurring_transaction):
        """Sets the initial_recurring_transaction of this TokenizedCardData.

            Whether the transaction is an initial recurring transaction, based on the recurring indicator. This is used to identify the first transaction in a recurring payment setup.

        :param initial_recurring_transaction: The initial_recurring_transaction of this TokenizedCardData.
        :type: bool
        """

        self._initial_recurring_transaction = initial_recurring_transaction
    
    @property
    def recurring_indicator(self):
        """Gets the recurring_indicator of this TokenizedCardData.

            The indicator used to distinguish between recurring and one-time transactions. If omitted, it will be automatically determined based on the transaction's properties.

        :return: The recurring_indicator of this TokenizedCardData.
        :rtype: RecurringIndicator
        """
        return self._recurring_indicator

    @recurring_indicator.setter
    def recurring_indicator(self, recurring_indicator):
        """Sets the recurring_indicator of this TokenizedCardData.

            The indicator used to distinguish between recurring and one-time transactions. If omitted, it will be automatically determined based on the transaction's properties.

        :param recurring_indicator: The recurring_indicator of this TokenizedCardData.
        :type: RecurringIndicator
        """

        self._recurring_indicator = recurring_indicator
    
    @property
    def token_requestor_id(self):
        """Gets the token_requestor_id of this TokenizedCardData.

            The token requestor identifier (TRID) identifies the entity requesting tokenization for a card transaction.

        :return: The token_requestor_id of this TokenizedCardData.
        :rtype: str
        """
        return self._token_requestor_id

    @token_requestor_id.setter
    def token_requestor_id(self, token_requestor_id):
        """Sets the token_requestor_id of this TokenizedCardData.

            The token requestor identifier (TRID) identifies the entity requesting tokenization for a card transaction.

        :param token_requestor_id: The token_requestor_id of this TokenizedCardData.
        :type: str
        """

        self._token_requestor_id = token_requestor_id
    

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
        if issubclass(TokenizedCardData, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TokenizedCardData):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
