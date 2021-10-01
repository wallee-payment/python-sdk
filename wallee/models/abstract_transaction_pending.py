# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractTransactionPending:

    swagger_types = {
    
        'allowed_payment_method_brands': 'list[PaymentMethodBrand]',
        'allowed_payment_method_configurations': 'list[int]',
        'billing_address': 'AddressCreate',
        'completion_behavior': 'TransactionCompletionBehavior',
        'currency': 'str',
        'customer_email_address': 'str',
        'customer_id': 'str',
        'failed_url': 'str',
        'invoice_merchant_reference': 'str',
        'language': 'str',
        'line_items': 'list[LineItemCreate]',
        'merchant_reference': 'str',
        'meta_data': 'dict(str, str)',
        'shipping_address': 'AddressCreate',
        'shipping_method': 'str',
        'success_url': 'str',
        'time_zone': 'str',
        'token': 'int',
        'tokenization_mode': 'TokenizationMode',
    }

    attribute_map = {
        'allowed_payment_method_brands': 'allowedPaymentMethodBrands','allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','billing_address': 'billingAddress','completion_behavior': 'completionBehavior','currency': 'currency','customer_email_address': 'customerEmailAddress','customer_id': 'customerId','failed_url': 'failedUrl','invoice_merchant_reference': 'invoiceMerchantReference','language': 'language','line_items': 'lineItems','merchant_reference': 'merchantReference','meta_data': 'metaData','shipping_address': 'shippingAddress','shipping_method': 'shippingMethod','success_url': 'successUrl','time_zone': 'timeZone','token': 'token','tokenization_mode': 'tokenizationMode',
    }

    
    _allowed_payment_method_brands = None
    _allowed_payment_method_configurations = None
    _billing_address = None
    _completion_behavior = None
    _currency = None
    _customer_email_address = None
    _customer_id = None
    _failed_url = None
    _invoice_merchant_reference = None
    _language = None
    _line_items = None
    _merchant_reference = None
    _meta_data = None
    _shipping_address = None
    _shipping_method = None
    _success_url = None
    _time_zone = None
    _token = None
    _tokenization_mode = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allowed_payment_method_brands = kwargs.get('allowed_payment_method_brands', None)
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.completion_behavior = kwargs.get('completion_behavior', None)
        self.currency = kwargs.get('currency', None)
        self.customer_email_address = kwargs.get('customer_email_address', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.failed_url = kwargs.get('failed_url', None)
        self.invoice_merchant_reference = kwargs.get('invoice_merchant_reference', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.shipping_method = kwargs.get('shipping_method', None)
        self.success_url = kwargs.get('success_url', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.token = kwargs.get('token', None)
        self.tokenization_mode = kwargs.get('tokenization_mode', None)
        

    
    @property
    def allowed_payment_method_brands(self):
        """Gets the allowed_payment_method_brands of this AbstractTransactionPending.

            

        :return: The allowed_payment_method_brands of this AbstractTransactionPending.
        :rtype: list[PaymentMethodBrand]
        """
        return self._allowed_payment_method_brands

    @allowed_payment_method_brands.setter
    def allowed_payment_method_brands(self, allowed_payment_method_brands):
        """Sets the allowed_payment_method_brands of this AbstractTransactionPending.

            

        :param allowed_payment_method_brands: The allowed_payment_method_brands of this AbstractTransactionPending.
        :type: list[PaymentMethodBrand]
        """

        self._allowed_payment_method_brands = allowed_payment_method_brands
    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this AbstractTransactionPending.

            

        :return: The allowed_payment_method_configurations of this AbstractTransactionPending.
        :rtype: list[int]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this AbstractTransactionPending.

            

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this AbstractTransactionPending.
        :type: list[int]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def billing_address(self):
        """Gets the billing_address of this AbstractTransactionPending.

            

        :return: The billing_address of this AbstractTransactionPending.
        :rtype: AddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this AbstractTransactionPending.

            

        :param billing_address: The billing_address of this AbstractTransactionPending.
        :type: AddressCreate
        """

        self._billing_address = billing_address
    
    @property
    def completion_behavior(self):
        """Gets the completion_behavior of this AbstractTransactionPending.

            The completion behavior controls when the transaction is completed.

        :return: The completion_behavior of this AbstractTransactionPending.
        :rtype: TransactionCompletionBehavior
        """
        return self._completion_behavior

    @completion_behavior.setter
    def completion_behavior(self, completion_behavior):
        """Sets the completion_behavior of this AbstractTransactionPending.

            The completion behavior controls when the transaction is completed.

        :param completion_behavior: The completion_behavior of this AbstractTransactionPending.
        :type: TransactionCompletionBehavior
        """

        self._completion_behavior = completion_behavior
    
    @property
    def currency(self):
        """Gets the currency of this AbstractTransactionPending.

            

        :return: The currency of this AbstractTransactionPending.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AbstractTransactionPending.

            

        :param currency: The currency of this AbstractTransactionPending.
        :type: str
        """

        self._currency = currency
    
    @property
    def customer_email_address(self):
        """Gets the customer_email_address of this AbstractTransactionPending.

            The customer email address is the email address of the customer. If no email address is provided on the shipping or billing address this address is used.

        :return: The customer_email_address of this AbstractTransactionPending.
        :rtype: str
        """
        return self._customer_email_address

    @customer_email_address.setter
    def customer_email_address(self, customer_email_address):
        """Sets the customer_email_address of this AbstractTransactionPending.

            The customer email address is the email address of the customer. If no email address is provided on the shipping or billing address this address is used.

        :param customer_email_address: The customer_email_address of this AbstractTransactionPending.
        :type: str
        """
        if customer_email_address is not None and len(customer_email_address) > 254:
            raise ValueError("Invalid value for `customer_email_address`, length must be less than or equal to `254`")

        self._customer_email_address = customer_email_address
    
    @property
    def customer_id(self):
        """Gets the customer_id of this AbstractTransactionPending.

            

        :return: The customer_id of this AbstractTransactionPending.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AbstractTransactionPending.

            

        :param customer_id: The customer_id of this AbstractTransactionPending.
        :type: str
        """

        self._customer_id = customer_id
    
    @property
    def failed_url(self):
        """Gets the failed_url of this AbstractTransactionPending.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :return: The failed_url of this AbstractTransactionPending.
        :rtype: str
        """
        return self._failed_url

    @failed_url.setter
    def failed_url(self, failed_url):
        """Sets the failed_url of this AbstractTransactionPending.

            The user will be redirected to failed URL when the transaction could not be authorized or completed. In case no failed URL is specified a default failed page will be displayed.

        :param failed_url: The failed_url of this AbstractTransactionPending.
        :type: str
        """
        if failed_url is not None and len(failed_url) > 2000:
            raise ValueError("Invalid value for `failed_url`, length must be less than or equal to `2000`")
        if failed_url is not None and len(failed_url) < 9:
            raise ValueError("Invalid value for `failed_url`, length must be greater than or equal to `9`")

        self._failed_url = failed_url
    
    @property
    def invoice_merchant_reference(self):
        """Gets the invoice_merchant_reference of this AbstractTransactionPending.

            

        :return: The invoice_merchant_reference of this AbstractTransactionPending.
        :rtype: str
        """
        return self._invoice_merchant_reference

    @invoice_merchant_reference.setter
    def invoice_merchant_reference(self, invoice_merchant_reference):
        """Sets the invoice_merchant_reference of this AbstractTransactionPending.

            

        :param invoice_merchant_reference: The invoice_merchant_reference of this AbstractTransactionPending.
        :type: str
        """
        if invoice_merchant_reference is not None and len(invoice_merchant_reference) > 100:
            raise ValueError("Invalid value for `invoice_merchant_reference`, length must be less than or equal to `100`")

        self._invoice_merchant_reference = invoice_merchant_reference
    
    @property
    def language(self):
        """Gets the language of this AbstractTransactionPending.

            

        :return: The language of this AbstractTransactionPending.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractTransactionPending.

            

        :param language: The language of this AbstractTransactionPending.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this AbstractTransactionPending.

            

        :return: The line_items of this AbstractTransactionPending.
        :rtype: list[LineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this AbstractTransactionPending.

            

        :param line_items: The line_items of this AbstractTransactionPending.
        :type: list[LineItemCreate]
        """

        self._line_items = line_items
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this AbstractTransactionPending.

            

        :return: The merchant_reference of this AbstractTransactionPending.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this AbstractTransactionPending.

            

        :param merchant_reference: The merchant_reference of this AbstractTransactionPending.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def meta_data(self):
        """Gets the meta_data of this AbstractTransactionPending.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this AbstractTransactionPending.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this AbstractTransactionPending.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this AbstractTransactionPending.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this AbstractTransactionPending.

            

        :return: The shipping_address of this AbstractTransactionPending.
        :rtype: AddressCreate
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this AbstractTransactionPending.

            

        :param shipping_address: The shipping_address of this AbstractTransactionPending.
        :type: AddressCreate
        """

        self._shipping_address = shipping_address
    
    @property
    def shipping_method(self):
        """Gets the shipping_method of this AbstractTransactionPending.

            

        :return: The shipping_method of this AbstractTransactionPending.
        :rtype: str
        """
        return self._shipping_method

    @shipping_method.setter
    def shipping_method(self, shipping_method):
        """Sets the shipping_method of this AbstractTransactionPending.

            

        :param shipping_method: The shipping_method of this AbstractTransactionPending.
        :type: str
        """
        if shipping_method is not None and len(shipping_method) > 200:
            raise ValueError("Invalid value for `shipping_method`, length must be less than or equal to `200`")

        self._shipping_method = shipping_method
    
    @property
    def success_url(self):
        """Gets the success_url of this AbstractTransactionPending.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :return: The success_url of this AbstractTransactionPending.
        :rtype: str
        """
        return self._success_url

    @success_url.setter
    def success_url(self, success_url):
        """Sets the success_url of this AbstractTransactionPending.

            The user will be redirected to success URL when the transaction could be authorized or completed. In case no success URL is specified a default success page will be displayed.

        :param success_url: The success_url of this AbstractTransactionPending.
        :type: str
        """
        if success_url is not None and len(success_url) > 2000:
            raise ValueError("Invalid value for `success_url`, length must be less than or equal to `2000`")
        if success_url is not None and len(success_url) < 9:
            raise ValueError("Invalid value for `success_url`, length must be greater than or equal to `9`")

        self._success_url = success_url
    
    @property
    def time_zone(self):
        """Gets the time_zone of this AbstractTransactionPending.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :return: The time_zone of this AbstractTransactionPending.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this AbstractTransactionPending.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :param time_zone: The time_zone of this AbstractTransactionPending.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def token(self):
        """Gets the token of this AbstractTransactionPending.

            

        :return: The token of this AbstractTransactionPending.
        :rtype: int
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this AbstractTransactionPending.

            

        :param token: The token of this AbstractTransactionPending.
        :type: int
        """

        self._token = token
    
    @property
    def tokenization_mode(self):
        """Gets the tokenization_mode of this AbstractTransactionPending.

            The tokenization mode controls if and how the tokenization of payment information is applied to the transaction.

        :return: The tokenization_mode of this AbstractTransactionPending.
        :rtype: TokenizationMode
        """
        return self._tokenization_mode

    @tokenization_mode.setter
    def tokenization_mode(self, tokenization_mode):
        """Sets the tokenization_mode of this AbstractTransactionPending.

            The tokenization mode controls if and how the tokenization of payment information is applied to the transaction.

        :param tokenization_mode: The tokenization_mode of this AbstractTransactionPending.
        :type: TokenizationMode
        """

        self._tokenization_mode = tokenization_mode
    

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
        if issubclass(AbstractTransactionPending, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractTransactionPending):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
