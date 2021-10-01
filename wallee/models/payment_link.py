# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentLink:

    swagger_types = {
    
        'allowed_payment_method_configurations': 'list[PaymentMethodConfiguration]',
        'applied_space_view': 'int',
        'available_from': 'datetime',
        'available_until': 'datetime',
        'billing_address_handling_mode': 'PaymentLinkAddressHandlingMode',
        'currency': 'str',
        'external_id': 'str',
        'id': 'int',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'maximal_number_of_transactions': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'protection_mode': 'PaymentLinkProtectionMode',
        'shipping_address_handling_mode': 'PaymentLinkAddressHandlingMode',
        'state': 'CreationEntityState',
        'url': 'str',
        'version': 'int',
    }

    attribute_map = {
        'allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','applied_space_view': 'appliedSpaceView','available_from': 'availableFrom','available_until': 'availableUntil','billing_address_handling_mode': 'billingAddressHandlingMode','currency': 'currency','external_id': 'externalId','id': 'id','language': 'language','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','maximal_number_of_transactions': 'maximalNumberOfTransactions','name': 'name','planned_purge_date': 'plannedPurgeDate','protection_mode': 'protectionMode','shipping_address_handling_mode': 'shippingAddressHandlingMode','state': 'state','url': 'url','version': 'version',
    }

    
    _allowed_payment_method_configurations = None
    _applied_space_view = None
    _available_from = None
    _available_until = None
    _billing_address_handling_mode = None
    _currency = None
    _external_id = None
    _id = None
    _language = None
    _line_items = None
    _linked_space_id = None
    _maximal_number_of_transactions = None
    _name = None
    _planned_purge_date = None
    _protection_mode = None
    _shipping_address_handling_mode = None
    _state = None
    _url = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.applied_space_view = kwargs.get('applied_space_view', None)
        self.available_from = kwargs.get('available_from', None)
        self.available_until = kwargs.get('available_until', None)
        self.billing_address_handling_mode = kwargs.get('billing_address_handling_mode', None)
        self.currency = kwargs.get('currency', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.maximal_number_of_transactions = kwargs.get('maximal_number_of_transactions', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.protection_mode = kwargs.get('protection_mode', None)
        self.shipping_address_handling_mode = kwargs.get('shipping_address_handling_mode', None)
        self.state = kwargs.get('state', None)
        self.url = kwargs.get('url', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this PaymentLink.

            The allowed payment method configurations restrict the payment methods which can be used with this payment link.

        :return: The allowed_payment_method_configurations of this PaymentLink.
        :rtype: list[PaymentMethodConfiguration]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this PaymentLink.

            The allowed payment method configurations restrict the payment methods which can be used with this payment link.

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this PaymentLink.
        :type: list[PaymentMethodConfiguration]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def applied_space_view(self):
        """Gets the applied_space_view of this PaymentLink.

            The payment link can be conducted in a specific space view. The space view may apply a specific design to the payment page.

        :return: The applied_space_view of this PaymentLink.
        :rtype: int
        """
        return self._applied_space_view

    @applied_space_view.setter
    def applied_space_view(self, applied_space_view):
        """Sets the applied_space_view of this PaymentLink.

            The payment link can be conducted in a specific space view. The space view may apply a specific design to the payment page.

        :param applied_space_view: The applied_space_view of this PaymentLink.
        :type: int
        """

        self._applied_space_view = applied_space_view
    
    @property
    def available_from(self):
        """Gets the available_from of this PaymentLink.

            The available from date defines the earliest date on which the payment link can be used. When no date is specified there will be no restriction.

        :return: The available_from of this PaymentLink.
        :rtype: datetime
        """
        return self._available_from

    @available_from.setter
    def available_from(self, available_from):
        """Sets the available_from of this PaymentLink.

            The available from date defines the earliest date on which the payment link can be used. When no date is specified there will be no restriction.

        :param available_from: The available_from of this PaymentLink.
        :type: datetime
        """

        self._available_from = available_from
    
    @property
    def available_until(self):
        """Gets the available_until of this PaymentLink.

            The available from date defines the latest date on which the payment link can be used to initialize a transaction. When no date is specified there will be no restriction.

        :return: The available_until of this PaymentLink.
        :rtype: datetime
        """
        return self._available_until

    @available_until.setter
    def available_until(self, available_until):
        """Sets the available_until of this PaymentLink.

            The available from date defines the latest date on which the payment link can be used to initialize a transaction. When no date is specified there will be no restriction.

        :param available_until: The available_until of this PaymentLink.
        :type: datetime
        """

        self._available_until = available_until
    
    @property
    def billing_address_handling_mode(self):
        """Gets the billing_address_handling_mode of this PaymentLink.

            The billing address handling mode controls if the address is collected or not and how it is collected.

        :return: The billing_address_handling_mode of this PaymentLink.
        :rtype: PaymentLinkAddressHandlingMode
        """
        return self._billing_address_handling_mode

    @billing_address_handling_mode.setter
    def billing_address_handling_mode(self, billing_address_handling_mode):
        """Sets the billing_address_handling_mode of this PaymentLink.

            The billing address handling mode controls if the address is collected or not and how it is collected.

        :param billing_address_handling_mode: The billing_address_handling_mode of this PaymentLink.
        :type: PaymentLinkAddressHandlingMode
        """

        self._billing_address_handling_mode = billing_address_handling_mode
    
    @property
    def currency(self):
        """Gets the currency of this PaymentLink.

            The currency defines in which currency the payment is executed in. If no currency is defined it has to be specified within the request parameter 'currency'.

        :return: The currency of this PaymentLink.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this PaymentLink.

            The currency defines in which currency the payment is executed in. If no currency is defined it has to be specified within the request parameter 'currency'.

        :param currency: The currency of this PaymentLink.
        :type: str
        """

        self._currency = currency
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentLink.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this PaymentLink.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentLink.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this PaymentLink.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this PaymentLink.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentLink.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentLink.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentLink.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this PaymentLink.

            The language defines the language of the payment page. If no language is provided it can be provided through the request parameter.

        :return: The language of this PaymentLink.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this PaymentLink.

            The language defines the language of the payment page. If no language is provided it can be provided through the request parameter.

        :param language: The language of this PaymentLink.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this PaymentLink.

            The line items allows to define the line items for this payment link. When the line items are defined they cannot be overridden through the request parameters.

        :return: The line_items of this PaymentLink.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this PaymentLink.

            The line items allows to define the line items for this payment link. When the line items are defined they cannot be overridden through the request parameters.

        :param line_items: The line_items of this PaymentLink.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentLink.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentLink.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentLink.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentLink.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def maximal_number_of_transactions(self):
        """Gets the maximal_number_of_transactions of this PaymentLink.

            The maximal number of transactions limits the number of transactions which can be created with this payment link.

        :return: The maximal_number_of_transactions of this PaymentLink.
        :rtype: int
        """
        return self._maximal_number_of_transactions

    @maximal_number_of_transactions.setter
    def maximal_number_of_transactions(self, maximal_number_of_transactions):
        """Sets the maximal_number_of_transactions of this PaymentLink.

            The maximal number of transactions limits the number of transactions which can be created with this payment link.

        :param maximal_number_of_transactions: The maximal_number_of_transactions of this PaymentLink.
        :type: int
        """

        self._maximal_number_of_transactions = maximal_number_of_transactions
    
    @property
    def name(self):
        """Gets the name of this PaymentLink.

            The payment link name is used internally to identify the payment link. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentLink.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentLink.

            The payment link name is used internally to identify the payment link. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentLink.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentLink.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentLink.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentLink.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentLink.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def protection_mode(self):
        """Gets the protection_mode of this PaymentLink.

            The protection mode determines if the payment link is protected against tampering and in what way.

        :return: The protection_mode of this PaymentLink.
        :rtype: PaymentLinkProtectionMode
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """Sets the protection_mode of this PaymentLink.

            The protection mode determines if the payment link is protected against tampering and in what way.

        :param protection_mode: The protection_mode of this PaymentLink.
        :type: PaymentLinkProtectionMode
        """

        self._protection_mode = protection_mode
    
    @property
    def shipping_address_handling_mode(self):
        """Gets the shipping_address_handling_mode of this PaymentLink.

            The shipping address handling mode controls if the address is collected or not and how it is collected.

        :return: The shipping_address_handling_mode of this PaymentLink.
        :rtype: PaymentLinkAddressHandlingMode
        """
        return self._shipping_address_handling_mode

    @shipping_address_handling_mode.setter
    def shipping_address_handling_mode(self, shipping_address_handling_mode):
        """Sets the shipping_address_handling_mode of this PaymentLink.

            The shipping address handling mode controls if the address is collected or not and how it is collected.

        :param shipping_address_handling_mode: The shipping_address_handling_mode of this PaymentLink.
        :type: PaymentLinkAddressHandlingMode
        """

        self._shipping_address_handling_mode = shipping_address_handling_mode
    
    @property
    def state(self):
        """Gets the state of this PaymentLink.

            

        :return: The state of this PaymentLink.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentLink.

            

        :param state: The state of this PaymentLink.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def url(self):
        """Gets the url of this PaymentLink.

            The URL defines the URL to which the user has to be forwarded to initialize the payment.

        :return: The url of this PaymentLink.
        :rtype: str
        """
        return self._url

    @url.setter
    def url(self, url):
        """Sets the url of this PaymentLink.

            The URL defines the URL to which the user has to be forwarded to initialize the payment.

        :param url: The url of this PaymentLink.
        :type: str
        """

        self._url = url
    
    @property
    def version(self):
        """Gets the version of this PaymentLink.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentLink.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentLink.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentLink.
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
        if issubclass(PaymentLink, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
