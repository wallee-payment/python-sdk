# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractTokenUpdate:

    swagger_types = {
    
        'customer_email_address': 'str',
        'customer_id': 'str',
        'enabled_for_one_click_payment': 'bool',
        'language': 'str',
        'time_zone': 'str',
        'token_reference': 'str',
    }

    attribute_map = {
        'customer_email_address': 'customerEmailAddress','customer_id': 'customerId','enabled_for_one_click_payment': 'enabledForOneClickPayment','language': 'language','time_zone': 'timeZone','token_reference': 'tokenReference',
    }

    
    _customer_email_address = None
    _customer_id = None
    _enabled_for_one_click_payment = None
    _language = None
    _time_zone = None
    _token_reference = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.customer_email_address = kwargs.get('customer_email_address', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.enabled_for_one_click_payment = kwargs.get('enabled_for_one_click_payment', None)
        self.language = kwargs.get('language', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.token_reference = kwargs.get('token_reference', None)
        

    
    @property
    def customer_email_address(self):
        """Gets the customer_email_address of this AbstractTokenUpdate.

            The customer email address is the email address of the customer.

        :return: The customer_email_address of this AbstractTokenUpdate.
        :rtype: str
        """
        return self._customer_email_address

    @customer_email_address.setter
    def customer_email_address(self, customer_email_address):
        """Sets the customer_email_address of this AbstractTokenUpdate.

            The customer email address is the email address of the customer.

        :param customer_email_address: The customer_email_address of this AbstractTokenUpdate.
        :type: str
        """
        if customer_email_address is not None and len(customer_email_address) > 150:
            raise ValueError("Invalid value for `customer_email_address`, length must be less than or equal to `150`")

        self._customer_email_address = customer_email_address
    
    @property
    def customer_id(self):
        """Gets the customer_id of this AbstractTokenUpdate.

            The customer ID identifies the customer in the merchant system. In case the customer ID has been provided it has to correspond with the customer ID provided on the transaction. The customer ID will not be changed automatically. The merchant system has to provide it.

        :return: The customer_id of this AbstractTokenUpdate.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AbstractTokenUpdate.

            The customer ID identifies the customer in the merchant system. In case the customer ID has been provided it has to correspond with the customer ID provided on the transaction. The customer ID will not be changed automatically. The merchant system has to provide it.

        :param customer_id: The customer_id of this AbstractTokenUpdate.
        :type: str
        """

        self._customer_id = customer_id
    
    @property
    def enabled_for_one_click_payment(self):
        """Gets the enabled_for_one_click_payment of this AbstractTokenUpdate.

            When a token is enabled for one-click payments the buyer will be able to select the token within the iFrame or on the payment page to pay with the token. The usage of the token will reduce the number of steps the buyer has to go through. The buyer is linked via the customer ID on the transaction with the token. Means the token will be visible for buyers with the same customer ID. Additionally the payment method has to be configured to allow the one-click payments.

        :return: The enabled_for_one_click_payment of this AbstractTokenUpdate.
        :rtype: bool
        """
        return self._enabled_for_one_click_payment

    @enabled_for_one_click_payment.setter
    def enabled_for_one_click_payment(self, enabled_for_one_click_payment):
        """Sets the enabled_for_one_click_payment of this AbstractTokenUpdate.

            When a token is enabled for one-click payments the buyer will be able to select the token within the iFrame or on the payment page to pay with the token. The usage of the token will reduce the number of steps the buyer has to go through. The buyer is linked via the customer ID on the transaction with the token. Means the token will be visible for buyers with the same customer ID. Additionally the payment method has to be configured to allow the one-click payments.

        :param enabled_for_one_click_payment: The enabled_for_one_click_payment of this AbstractTokenUpdate.
        :type: bool
        """

        self._enabled_for_one_click_payment = enabled_for_one_click_payment
    
    @property
    def language(self):
        """Gets the language of this AbstractTokenUpdate.

            

        :return: The language of this AbstractTokenUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractTokenUpdate.

            

        :param language: The language of this AbstractTokenUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def time_zone(self):
        """Gets the time_zone of this AbstractTokenUpdate.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :return: The time_zone of this AbstractTokenUpdate.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AbstractTokenUpdate.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :param time_zone: The time_zone of this AbstractTokenUpdate.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def token_reference(self):
        """Gets the token_reference of this AbstractTokenUpdate.

            Use something that it is easy to identify and may help you find the token (e.g. customer id, email address).

        :return: The token_reference of this AbstractTokenUpdate.
        :rtype: str
        """
        return self._token_reference

    @token_reference.setter
    def token_reference(self, token_reference):
        """Sets the token_reference of this AbstractTokenUpdate.

            Use something that it is easy to identify and may help you find the token (e.g. customer id, email address).

        :param token_reference: The token_reference of this AbstractTokenUpdate.
        :type: str
        """
        if token_reference is not None and len(token_reference) > 100:
            raise ValueError("Invalid value for `token_reference`, length must be less than or equal to `100`")

        self._token_reference = token_reference
    

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
        if issubclass(AbstractTokenUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractTokenUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
