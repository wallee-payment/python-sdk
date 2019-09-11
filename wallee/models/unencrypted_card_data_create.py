# coding: utf-8
import pprint
import six
from enum import Enum



class UnencryptedCardDataCreate:

    swagger_types = {
    
        'card_holder_name': 'str',
        'card_verification_code': 'str',
        'expiry_date': 'str',
        'primary_account_number': 'str',
    }

    attribute_map = {
        'card_holder_name': 'cardHolderName','card_verification_code': 'cardVerificationCode','expiry_date': 'expiryDate','primary_account_number': 'primaryAccountNumber',
    }

    
    _card_holder_name = None
    _card_verification_code = None
    _expiry_date = None
    _primary_account_number = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.card_holder_name = kwargs.get('card_holder_name', None)
        self.card_verification_code = kwargs.get('card_verification_code', None)
        self.expiry_date = kwargs.get('expiry_date', None)
        self.primary_account_number = kwargs.get('primary_account_number')

        

    
    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this UnencryptedCardDataCreate.

            The card holder name is the name printed onto the card. It identifies the person who owns the card.

        :return: The card_holder_name of this UnencryptedCardDataCreate.
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """Sets the card_holder_name of this UnencryptedCardDataCreate.

            The card holder name is the name printed onto the card. It identifies the person who owns the card.

        :param card_holder_name: The card_holder_name of this UnencryptedCardDataCreate.
        :type: str
        """

        self._card_holder_name = card_holder_name
    
    @property
    def card_verification_code(self):
        """Gets the card_verification_code of this UnencryptedCardDataCreate.

            The card verification code (CVC) is a 3 to 4 digit code typically printed on the back of the card. It helps to ensure that the card holder is authorizing the transaction. For card not-present transactions this field is optional.

        :return: The card_verification_code of this UnencryptedCardDataCreate.
        :rtype: str
        """
        return self._card_verification_code

    @card_verification_code.setter
    def card_verification_code(self, card_verification_code):
        """Sets the card_verification_code of this UnencryptedCardDataCreate.

            The card verification code (CVC) is a 3 to 4 digit code typically printed on the back of the card. It helps to ensure that the card holder is authorizing the transaction. For card not-present transactions this field is optional.

        :param card_verification_code: The card_verification_code of this UnencryptedCardDataCreate.
        :type: str
        """

        self._card_verification_code = card_verification_code
    
    @property
    def expiry_date(self):
        """Gets the expiry_date of this UnencryptedCardDataCreate.

            The card expiry date indicates when the card expires. The format is the format yyyy-mm where yyyy is the year (e.g. 2019) and the mm is the month (e.g. 09).

        :return: The expiry_date of this UnencryptedCardDataCreate.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this UnencryptedCardDataCreate.

            The card expiry date indicates when the card expires. The format is the format yyyy-mm where yyyy is the year (e.g. 2019) and the mm is the month (e.g. 09).

        :param expiry_date: The expiry_date of this UnencryptedCardDataCreate.
        :type: str
        """

        self._expiry_date = expiry_date
    
    @property
    def primary_account_number(self):
        """Gets the primary_account_number of this UnencryptedCardDataCreate.

            The primary account number (PAN) identifies the card. The number is numeric and typically printed on the front of the card.

        :return: The primary_account_number of this UnencryptedCardDataCreate.
        :rtype: str
        """
        return self._primary_account_number

    @primary_account_number.setter
    def primary_account_number(self, primary_account_number):
        """Sets the primary_account_number of this UnencryptedCardDataCreate.

            The primary account number (PAN) identifies the card. The number is numeric and typically printed on the front of the card.

        :param primary_account_number: The primary_account_number of this UnencryptedCardDataCreate.
        :type: str
        """
        if primary_account_number is None:
            raise ValueError("Invalid value for `primary_account_number`, must not be `None`")

        self._primary_account_number = primary_account_number
    

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
        if issubclass(UnencryptedCardDataCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, UnencryptedCardDataCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
