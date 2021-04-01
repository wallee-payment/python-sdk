# coding: utf-8
import pprint
import six
from enum import Enum



class AuthenticatedCardDataCreate:

    swagger_types = {
    
        'card_holder_name': 'str',
        'card_verification_code': 'str',
        'cardholder_authentication': 'CardholderAuthenticationCreate',
        'cryptogram': 'CardCryptogramCreate',
        'expiry_date': 'str',
        'primary_account_number': 'str',
        'recurring_indicator': 'RecurringIndicator',
        'scheme_transaction_reference': 'str',
        'token_requestor_id': 'str',
    }

    attribute_map = {
        'card_holder_name': 'cardHolderName','card_verification_code': 'cardVerificationCode','cardholder_authentication': 'cardholderAuthentication','cryptogram': 'cryptogram','expiry_date': 'expiryDate','primary_account_number': 'primaryAccountNumber','recurring_indicator': 'recurringIndicator','scheme_transaction_reference': 'schemeTransactionReference','token_requestor_id': 'tokenRequestorId',
    }

    
    _card_holder_name = None
    _card_verification_code = None
    _cardholder_authentication = None
    _cryptogram = None
    _expiry_date = None
    _primary_account_number = None
    _recurring_indicator = None
    _scheme_transaction_reference = None
    _token_requestor_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.card_holder_name = kwargs.get('card_holder_name', None)
        self.card_verification_code = kwargs.get('card_verification_code', None)
        self.cardholder_authentication = kwargs.get('cardholder_authentication', None)
        self.cryptogram = kwargs.get('cryptogram', None)
        self.expiry_date = kwargs.get('expiry_date', None)
        self.primary_account_number = kwargs.get('primary_account_number')

        self.recurring_indicator = kwargs.get('recurring_indicator', None)
        self.scheme_transaction_reference = kwargs.get('scheme_transaction_reference', None)
        self.token_requestor_id = kwargs.get('token_requestor_id', None)
        

    
    @property
    def card_holder_name(self):
        """Gets the card_holder_name of this AuthenticatedCardDataCreate.

            The card holder name is the name printed onto the card. It identifies the person who owns the card.

        :return: The card_holder_name of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._card_holder_name

    @card_holder_name.setter
    def card_holder_name(self, card_holder_name):
        """Sets the card_holder_name of this AuthenticatedCardDataCreate.

            The card holder name is the name printed onto the card. It identifies the person who owns the card.

        :param card_holder_name: The card_holder_name of this AuthenticatedCardDataCreate.
        :type: str
        """
        if card_holder_name is not None and len(card_holder_name) > 100:
            raise ValueError("Invalid value for `card_holder_name`, length must be less than or equal to `100`")

        self._card_holder_name = card_holder_name
    
    @property
    def card_verification_code(self):
        """Gets the card_verification_code of this AuthenticatedCardDataCreate.

            The card verification code (CVC) is a 3 to 4 digit code typically printed on the back of the card. It helps to ensure that the card holder is authorizing the transaction. For card not-present transactions this field is optional.

        :return: The card_verification_code of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._card_verification_code

    @card_verification_code.setter
    def card_verification_code(self, card_verification_code):
        """Sets the card_verification_code of this AuthenticatedCardDataCreate.

            The card verification code (CVC) is a 3 to 4 digit code typically printed on the back of the card. It helps to ensure that the card holder is authorizing the transaction. For card not-present transactions this field is optional.

        :param card_verification_code: The card_verification_code of this AuthenticatedCardDataCreate.
        :type: str
        """
        if card_verification_code is not None and len(card_verification_code) > 4:
            raise ValueError("Invalid value for `card_verification_code`, length must be less than or equal to `4`")
        if card_verification_code is not None and len(card_verification_code) < 3:
            raise ValueError("Invalid value for `card_verification_code`, length must be greater than or equal to `3`")

        self._card_verification_code = card_verification_code
    
    @property
    def cardholder_authentication(self):
        """Gets the cardholder_authentication of this AuthenticatedCardDataCreate.

            The cardholder authentication information. The authentication is optional and can be provided if the cardholder has been already authenticated (e.g. in 3-D Secure system).

        :return: The cardholder_authentication of this AuthenticatedCardDataCreate.
        :rtype: CardholderAuthenticationCreate
        """
        return self._cardholder_authentication

    @cardholder_authentication.setter
    def cardholder_authentication(self, cardholder_authentication):
        """Sets the cardholder_authentication of this AuthenticatedCardDataCreate.

            The cardholder authentication information. The authentication is optional and can be provided if the cardholder has been already authenticated (e.g. in 3-D Secure system).

        :param cardholder_authentication: The cardholder_authentication of this AuthenticatedCardDataCreate.
        :type: CardholderAuthenticationCreate
        """

        self._cardholder_authentication = cardholder_authentication
    
    @property
    def cryptogram(self):
        """Gets the cryptogram of this AuthenticatedCardDataCreate.

            The additional authentication value used to secure the tokenized card transactions.

        :return: The cryptogram of this AuthenticatedCardDataCreate.
        :rtype: CardCryptogramCreate
        """
        return self._cryptogram

    @cryptogram.setter
    def cryptogram(self, cryptogram):
        """Sets the cryptogram of this AuthenticatedCardDataCreate.

            The additional authentication value used to secure the tokenized card transactions.

        :param cryptogram: The cryptogram of this AuthenticatedCardDataCreate.
        :type: CardCryptogramCreate
        """

        self._cryptogram = cryptogram
    
    @property
    def expiry_date(self):
        """Gets the expiry_date of this AuthenticatedCardDataCreate.

            The card expiry date indicates when the card expires. The format is the format yyyy-mm where yyyy is the year (e.g. 2019) and the mm is the month (e.g. 09).

        :return: The expiry_date of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._expiry_date

    @expiry_date.setter
    def expiry_date(self, expiry_date):
        """Sets the expiry_date of this AuthenticatedCardDataCreate.

            The card expiry date indicates when the card expires. The format is the format yyyy-mm where yyyy is the year (e.g. 2019) and the mm is the month (e.g. 09).

        :param expiry_date: The expiry_date of this AuthenticatedCardDataCreate.
        :type: str
        """

        self._expiry_date = expiry_date
    
    @property
    def primary_account_number(self):
        """Gets the primary_account_number of this AuthenticatedCardDataCreate.

            The primary account number (PAN) identifies the card. The number is numeric and typically printed on the front of the card.

        :return: The primary_account_number of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._primary_account_number

    @primary_account_number.setter
    def primary_account_number(self, primary_account_number):
        """Sets the primary_account_number of this AuthenticatedCardDataCreate.

            The primary account number (PAN) identifies the card. The number is numeric and typically printed on the front of the card.

        :param primary_account_number: The primary_account_number of this AuthenticatedCardDataCreate.
        :type: str
        """
        if primary_account_number is None:
            raise ValueError("Invalid value for `primary_account_number`, must not be `None`")
        if primary_account_number is not None and len(primary_account_number) > 30:
            raise ValueError("Invalid value for `primary_account_number`, length must be less than or equal to `30`")
        if primary_account_number is not None and len(primary_account_number) < 10:
            raise ValueError("Invalid value for `primary_account_number`, length must be greater than or equal to `10`")

        self._primary_account_number = primary_account_number
    
    @property
    def recurring_indicator(self):
        """Gets the recurring_indicator of this AuthenticatedCardDataCreate.

            

        :return: The recurring_indicator of this AuthenticatedCardDataCreate.
        :rtype: RecurringIndicator
        """
        return self._recurring_indicator

    @recurring_indicator.setter
    def recurring_indicator(self, recurring_indicator):
        """Sets the recurring_indicator of this AuthenticatedCardDataCreate.

            

        :param recurring_indicator: The recurring_indicator of this AuthenticatedCardDataCreate.
        :type: RecurringIndicator
        """

        self._recurring_indicator = recurring_indicator
    
    @property
    def scheme_transaction_reference(self):
        """Gets the scheme_transaction_reference of this AuthenticatedCardDataCreate.

            

        :return: The scheme_transaction_reference of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._scheme_transaction_reference

    @scheme_transaction_reference.setter
    def scheme_transaction_reference(self, scheme_transaction_reference):
        """Sets the scheme_transaction_reference of this AuthenticatedCardDataCreate.

            

        :param scheme_transaction_reference: The scheme_transaction_reference of this AuthenticatedCardDataCreate.
        :type: str
        """
        if scheme_transaction_reference is not None and len(scheme_transaction_reference) > 100:
            raise ValueError("Invalid value for `scheme_transaction_reference`, length must be less than or equal to `100`")

        self._scheme_transaction_reference = scheme_transaction_reference
    
    @property
    def token_requestor_id(self):
        """Gets the token_requestor_id of this AuthenticatedCardDataCreate.

            

        :return: The token_requestor_id of this AuthenticatedCardDataCreate.
        :rtype: str
        """
        return self._token_requestor_id

    @token_requestor_id.setter
    def token_requestor_id(self, token_requestor_id):
        """Sets the token_requestor_id of this AuthenticatedCardDataCreate.

            

        :param token_requestor_id: The token_requestor_id of this AuthenticatedCardDataCreate.
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
        if issubclass(AuthenticatedCardDataCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AuthenticatedCardDataCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
