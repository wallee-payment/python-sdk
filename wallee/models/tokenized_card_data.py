# coding: utf-8
import pprint
import six
from enum import Enum



class TokenizedCardData:

    swagger_types = {
    
        'cryptogram': 'CardCryptogram',
        'recurring_indicator': 'RecurringIndicator',
        'token_requestor_id': 'str',
    }

    attribute_map = {
        'cryptogram': 'cryptogram','recurring_indicator': 'recurringIndicator','token_requestor_id': 'tokenRequestorId',
    }

    
    _cryptogram = None
    _recurring_indicator = None
    _token_requestor_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.cryptogram = kwargs.get('cryptogram', None)
        self.recurring_indicator = kwargs.get('recurring_indicator', None)
        self.token_requestor_id = kwargs.get('token_requestor_id', None)
        

    
    @property
    def cryptogram(self):
        """Gets the cryptogram of this TokenizedCardData.

            The additional authentication value used to secure the tokenized card transactions.

        :return: The cryptogram of this TokenizedCardData.
        :rtype: CardCryptogram
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """Sets the cryptogram of this TokenizedCardData.

            The additional authentication value used to secure the tokenized card transactions.

        :param cryptogram: The cryptogram of this TokenizedCardData.
        :type: CardCryptogram
        """

        self._cryptogram = cryptogram
    
    @property
    def recurring_indicator(self):
        """Gets the recurring_indicator of this TokenizedCardData.

            

        :return: The recurring_indicator of this TokenizedCardData.
        :rtype: RecurringIndicator
        """
        return self._recurring_indicator

    @recurring_indicator.setter
    def recurring_indicator(self, recurring_indicator):
        """Sets the recurring_indicator of this TokenizedCardData.

            

        :param recurring_indicator: The recurring_indicator of this TokenizedCardData.
        :type: RecurringIndicator
        """

        self._recurring_indicator = recurring_indicator
    
    @property
    def token_requestor_id(self):
        """Gets the token_requestor_id of this TokenizedCardData.

            

        :return: The token_requestor_id of this TokenizedCardData.
        :rtype: str
        """
        return self._token_requestor_id

    @token_requestor_id.setter
    def token_requestor_id(self, token_requestor_id):
        """Sets the token_requestor_id of this TokenizedCardData.

            

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
