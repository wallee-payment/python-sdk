# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractPaymentLinkUpdate:

    swagger_types = {
    
        'allowed_payment_method_configurations': 'list[PaymentMethodConfiguration]',
        'applied_space_view': 'int',
        'available_from': 'datetime',
        'available_until': 'datetime',
        'billing_address_handling_mode': 'PaymentLinkAddressHandlingMode',
        'currency': 'str',
        'language': 'str',
        'line_items': 'list[LineItemCreate]',
        'maximal_number_of_transactions': 'int',
        'name': 'str',
        'shipping_address_handling_mode': 'PaymentLinkAddressHandlingMode',
    }

    attribute_map = {
        'allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','applied_space_view': 'appliedSpaceView','available_from': 'availableFrom','available_until': 'availableUntil','billing_address_handling_mode': 'billingAddressHandlingMode','currency': 'currency','language': 'language','line_items': 'lineItems','maximal_number_of_transactions': 'maximalNumberOfTransactions','name': 'name','shipping_address_handling_mode': 'shippingAddressHandlingMode',
    }

    
    _allowed_payment_method_configurations = None
    _applied_space_view = None
    _available_from = None
    _available_until = None
    _billing_address_handling_mode = None
    _currency = None
    _language = None
    _line_items = None
    _maximal_number_of_transactions = None
    _name = None
    _shipping_address_handling_mode = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.applied_space_view = kwargs.get('applied_space_view', None)
        self.available_from = kwargs.get('available_from', None)
        self.available_until = kwargs.get('available_until', None)
        self.billing_address_handling_mode = kwargs.get('billing_address_handling_mode', None)
        self.currency = kwargs.get('currency', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.maximal_number_of_transactions = kwargs.get('maximal_number_of_transactions', None)
        self.name = kwargs.get('name', None)
        self.shipping_address_handling_mode = kwargs.get('shipping_address_handling_mode', None)
        

    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this AbstractPaymentLinkUpdate.

            The allowed payment method configurations restrict the payment methods which can be used with this payment link.

        :return: The allowed_payment_method_configurations of this AbstractPaymentLinkUpdate.
        :rtype: list[PaymentMethodConfiguration]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this AbstractPaymentLinkUpdate.

            The allowed payment method configurations restrict the payment methods which can be used with this payment link.

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this AbstractPaymentLinkUpdate.
        :type: list[PaymentMethodConfiguration]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def applied_space_view(self):
        """Gets the applied_space_view of this AbstractPaymentLinkUpdate.

            The payment link can be conducted in a specific space view. The space view may apply a specific design to the payment page.

        :return: The applied_space_view of this AbstractPaymentLinkUpdate.
        :rtype: int
        """
        return self._applied_space_view

    @applied_space_view.setter
    def applied_space_view(self, applied_space_view):
        """Sets the applied_space_view of this AbstractPaymentLinkUpdate.

            The payment link can be conducted in a specific space view. The space view may apply a specific design to the payment page.

        :param applied_space_view: The applied_space_view of this AbstractPaymentLinkUpdate.
        :type: int
        """

        self._applied_space_view = applied_space_view
    
    @property
    def available_from(self):
        """Gets the available_from of this AbstractPaymentLinkUpdate.

            The available from date defines the earliest date on which the payment link can be used. When no date is specified there will be no restriction.

        :return: The available_from of this AbstractPaymentLinkUpdate.
        :rtype: datetime
        """
        return self._available_from

    @available_from.setter
    def available_from(self, available_from):
        """Sets the available_from of this AbstractPaymentLinkUpdate.

            The available from date defines the earliest date on which the payment link can be used. When no date is specified there will be no restriction.

        :param available_from: The available_from of this AbstractPaymentLinkUpdate.
        :type: datetime
        """

        self._available_from = available_from
    
    @property
    def available_until(self):
        """Gets the available_until of this AbstractPaymentLinkUpdate.

            The available from date defines the latest date on which the payment link can be used to initialize a transaction. When no date is specified there will be no restriction.

        :return: The available_until of this AbstractPaymentLinkUpdate.
        :rtype: datetime
        """
        return self._available_until

    @available_until.setter
    def available_until(self, available_until):
        """Sets the available_until of this AbstractPaymentLinkUpdate.

            The available from date defines the latest date on which the payment link can be used to initialize a transaction. When no date is specified there will be no restriction.

        :param available_until: The available_until of this AbstractPaymentLinkUpdate.
        :type: datetime
        """

        self._available_until = available_until
    
    @property
    def billing_address_handling_mode(self):
        """Gets the billing_address_handling_mode of this AbstractPaymentLinkUpdate.

            The billing address handling mode controls if the address is collected or not and how it is collected.

        :return: The billing_address_handling_mode of this AbstractPaymentLinkUpdate.
        :rtype: PaymentLinkAddressHandlingMode
        """
        return self._billing_address_handling_mode

    @billing_address_handling_mode.setter
    def billing_address_handling_mode(self, billing_address_handling_mode):
        """Sets the billing_address_handling_mode of this AbstractPaymentLinkUpdate.

            The billing address handling mode controls if the address is collected or not and how it is collected.

        :param billing_address_handling_mode: The billing_address_handling_mode of this AbstractPaymentLinkUpdate.
        :type: PaymentLinkAddressHandlingMode
        """

        self._billing_address_handling_mode = billing_address_handling_mode
    
    @property
    def currency(self):
        """Gets the currency of this AbstractPaymentLinkUpdate.

            The currency defines in which currency the payment is executed in. If no currency is defined it has to be specified within the request parameter 'currency'.

        :return: The currency of this AbstractPaymentLinkUpdate.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this AbstractPaymentLinkUpdate.

            The currency defines in which currency the payment is executed in. If no currency is defined it has to be specified within the request parameter 'currency'.

        :param currency: The currency of this AbstractPaymentLinkUpdate.
        :type: str
        """

        self._currency = currency
    
    @property
    def language(self):
        """Gets the language of this AbstractPaymentLinkUpdate.

            The language defines the language of the payment page. If no language is provided it can be provided through the request parameter.

        :return: The language of this AbstractPaymentLinkUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractPaymentLinkUpdate.

            The language defines the language of the payment page. If no language is provided it can be provided through the request parameter.

        :param language: The language of this AbstractPaymentLinkUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this AbstractPaymentLinkUpdate.

            The line items allows to define the line items for this payment link. When the line items are defined they cannot be overridden through the request parameters.

        :return: The line_items of this AbstractPaymentLinkUpdate.
        :rtype: list[LineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this AbstractPaymentLinkUpdate.

            The line items allows to define the line items for this payment link. When the line items are defined they cannot be overridden through the request parameters.

        :param line_items: The line_items of this AbstractPaymentLinkUpdate.
        :type: list[LineItemCreate]
        """

        self._line_items = line_items
    
    @property
    def maximal_number_of_transactions(self):
        """Gets the maximal_number_of_transactions of this AbstractPaymentLinkUpdate.

            The maximal number of transactions limits the number of transactions which can be created with this payment link.

        :return: The maximal_number_of_transactions of this AbstractPaymentLinkUpdate.
        :rtype: int
        """
        return self._maximal_number_of_transactions

    @maximal_number_of_transactions.setter
    def maximal_number_of_transactions(self, maximal_number_of_transactions):
        """Sets the maximal_number_of_transactions of this AbstractPaymentLinkUpdate.

            The maximal number of transactions limits the number of transactions which can be created with this payment link.

        :param maximal_number_of_transactions: The maximal_number_of_transactions of this AbstractPaymentLinkUpdate.
        :type: int
        """

        self._maximal_number_of_transactions = maximal_number_of_transactions
    
    @property
    def name(self):
        """Gets the name of this AbstractPaymentLinkUpdate.

            The payment link name is used internally to identify the payment link. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this AbstractPaymentLinkUpdate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractPaymentLinkUpdate.

            The payment link name is used internally to identify the payment link. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this AbstractPaymentLinkUpdate.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def shipping_address_handling_mode(self):
        """Gets the shipping_address_handling_mode of this AbstractPaymentLinkUpdate.

            The shipping address handling mode controls if the address is collected or not and how it is collected.

        :return: The shipping_address_handling_mode of this AbstractPaymentLinkUpdate.
        :rtype: PaymentLinkAddressHandlingMode
        """
        return self._shipping_address_handling_mode

    @shipping_address_handling_mode.setter
    def shipping_address_handling_mode(self, shipping_address_handling_mode):
        """Sets the shipping_address_handling_mode of this AbstractPaymentLinkUpdate.

            The shipping address handling mode controls if the address is collected or not and how it is collected.

        :param shipping_address_handling_mode: The shipping_address_handling_mode of this AbstractPaymentLinkUpdate.
        :type: PaymentLinkAddressHandlingMode
        """

        self._shipping_address_handling_mode = shipping_address_handling_mode
    

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
        if issubclass(AbstractPaymentLinkUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractPaymentLinkUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
