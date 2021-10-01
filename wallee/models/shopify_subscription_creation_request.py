# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionCreationRequest:

    swagger_types = {
    
        'billing_address': 'ShopifySubscriptionAddressCreate',
        'billing_configuration': 'ShopifySubscriptionModelBillingConfiguration',
        'currency': 'str',
        'external_id': 'str',
        'initial_execution_date': 'datetime',
        'integration': 'int',
        'items': 'list[ShopifySubscriptionModelItem]',
        'language': 'str',
        'shipping_address': 'ShopifySubscriptionAddressCreate',
        'shipping_method_name': 'str',
        'space_view_id': 'int',
        'store_order_confirmation_email_enabled': 'bool',
        'subscriber': 'ShopifySubscriberCreation',
        'subscriber_suspension_allowed': 'bool',
    }

    attribute_map = {
        'billing_address': 'billingAddress','billing_configuration': 'billingConfiguration','currency': 'currency','external_id': 'externalId','initial_execution_date': 'initialExecutionDate','integration': 'integration','items': 'items','language': 'language','shipping_address': 'shippingAddress','shipping_method_name': 'shippingMethodName','space_view_id': 'spaceViewId','store_order_confirmation_email_enabled': 'storeOrderConfirmationEmailEnabled','subscriber': 'subscriber','subscriber_suspension_allowed': 'subscriberSuspensionAllowed',
    }

    
    _billing_address = None
    _billing_configuration = None
    _currency = None
    _external_id = None
    _initial_execution_date = None
    _integration = None
    _items = None
    _language = None
    _shipping_address = None
    _shipping_method_name = None
    _space_view_id = None
    _store_order_confirmation_email_enabled = None
    _subscriber = None
    _subscriber_suspension_allowed = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_address = kwargs.get('billing_address')

        self.billing_configuration = kwargs.get('billing_configuration', None)
        self.currency = kwargs.get('currency')

        self.external_id = kwargs.get('external_id')

        self.initial_execution_date = kwargs.get('initial_execution_date', None)
        self.integration = kwargs.get('integration')

        self.items = kwargs.get('items')

        self.language = kwargs.get('language')

        self.shipping_address = kwargs.get('shipping_address')

        self.shipping_method_name = kwargs.get('shipping_method_name', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.store_order_confirmation_email_enabled = kwargs.get('store_order_confirmation_email_enabled', None)
        self.subscriber = kwargs.get('subscriber')

        self.subscriber_suspension_allowed = kwargs.get('subscriber_suspension_allowed', None)
        

    
    @property
    def billing_address(self):
        """Gets the billing_address of this ShopifySubscriptionCreationRequest.

            

        :return: The billing_address of this ShopifySubscriptionCreationRequest.
        :rtype: ShopifySubscriptionAddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ShopifySubscriptionCreationRequest.

            

        :param billing_address: The billing_address of this ShopifySubscriptionCreationRequest.
        :type: ShopifySubscriptionAddressCreate
        """
        if billing_address is None:
            raise ValueError("Invalid value for `billing_address`, must not be `None`")

        self._billing_address = billing_address
    
    @property
    def billing_configuration(self):
        """Gets the billing_configuration of this ShopifySubscriptionCreationRequest.

            

        :return: The billing_configuration of this ShopifySubscriptionCreationRequest.
        :rtype: ShopifySubscriptionModelBillingConfiguration
        """
        return self._billing_configuration

    @billing_configuration.setter
    def billing_configuration(self, billing_configuration):
        """Sets the billing_configuration of this ShopifySubscriptionCreationRequest.

            

        :param billing_configuration: The billing_configuration of this ShopifySubscriptionCreationRequest.
        :type: ShopifySubscriptionModelBillingConfiguration
        """

        self._billing_configuration = billing_configuration
    
    @property
    def currency(self):
        """Gets the currency of this ShopifySubscriptionCreationRequest.

            

        :return: The currency of this ShopifySubscriptionCreationRequest.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShopifySubscriptionCreationRequest.

            

        :param currency: The currency of this ShopifySubscriptionCreationRequest.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency
    
    @property
    def external_id(self):
        """Gets the external_id of this ShopifySubscriptionCreationRequest.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this ShopifySubscriptionCreationRequest.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ShopifySubscriptionCreationRequest.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this ShopifySubscriptionCreationRequest.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def initial_execution_date(self):
        """Gets the initial_execution_date of this ShopifySubscriptionCreationRequest.

            

        :return: The initial_execution_date of this ShopifySubscriptionCreationRequest.
        :rtype: datetime
        """
        return self._initial_execution_date

    @initial_execution_date.setter
    def initial_execution_date(self, initial_execution_date):
        """Sets the initial_execution_date of this ShopifySubscriptionCreationRequest.

            

        :param initial_execution_date: The initial_execution_date of this ShopifySubscriptionCreationRequest.
        :type: datetime
        """

        self._initial_execution_date = initial_execution_date
    
    @property
    def integration(self):
        """Gets the integration of this ShopifySubscriptionCreationRequest.

            

        :return: The integration of this ShopifySubscriptionCreationRequest.
        :rtype: int
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ShopifySubscriptionCreationRequest.

            

        :param integration: The integration of this ShopifySubscriptionCreationRequest.
        :type: int
        """
        if integration is None:
            raise ValueError("Invalid value for `integration`, must not be `None`")

        self._integration = integration
    
    @property
    def items(self):
        """Gets the items of this ShopifySubscriptionCreationRequest.

            

        :return: The items of this ShopifySubscriptionCreationRequest.
        :rtype: list[ShopifySubscriptionModelItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ShopifySubscriptionCreationRequest.

            

        :param items: The items of this ShopifySubscriptionCreationRequest.
        :type: list[ShopifySubscriptionModelItem]
        """
        if items is None:
            raise ValueError("Invalid value for `items`, must not be `None`")

        self._items = items
    
    @property
    def language(self):
        """Gets the language of this ShopifySubscriptionCreationRequest.

            

        :return: The language of this ShopifySubscriptionCreationRequest.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShopifySubscriptionCreationRequest.

            

        :param language: The language of this ShopifySubscriptionCreationRequest.
        :type: str
        """
        if language is None:
            raise ValueError("Invalid value for `language`, must not be `None`")

        self._language = language
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this ShopifySubscriptionCreationRequest.

            

        :return: The shipping_address of this ShopifySubscriptionCreationRequest.
        :rtype: ShopifySubscriptionAddressCreate
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this ShopifySubscriptionCreationRequest.

            

        :param shipping_address: The shipping_address of this ShopifySubscriptionCreationRequest.
        :type: ShopifySubscriptionAddressCreate
        """
        if shipping_address is None:
            raise ValueError("Invalid value for `shipping_address`, must not be `None`")

        self._shipping_address = shipping_address
    
    @property
    def shipping_method_name(self):
        """Gets the shipping_method_name of this ShopifySubscriptionCreationRequest.

            

        :return: The shipping_method_name of this ShopifySubscriptionCreationRequest.
        :rtype: str
        """
        return self._shipping_method_name

    @shipping_method_name.setter
    def shipping_method_name(self, shipping_method_name):
        """Sets the shipping_method_name of this ShopifySubscriptionCreationRequest.

            

        :param shipping_method_name: The shipping_method_name of this ShopifySubscriptionCreationRequest.
        :type: str
        """

        self._shipping_method_name = shipping_method_name
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this ShopifySubscriptionCreationRequest.

            

        :return: The space_view_id of this ShopifySubscriptionCreationRequest.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this ShopifySubscriptionCreationRequest.

            

        :param space_view_id: The space_view_id of this ShopifySubscriptionCreationRequest.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def store_order_confirmation_email_enabled(self):
        """Gets the store_order_confirmation_email_enabled of this ShopifySubscriptionCreationRequest.

            

        :return: The store_order_confirmation_email_enabled of this ShopifySubscriptionCreationRequest.
        :rtype: bool
        """
        return self._store_order_confirmation_email_enabled

    @store_order_confirmation_email_enabled.setter
    def store_order_confirmation_email_enabled(self, store_order_confirmation_email_enabled):
        """Sets the store_order_confirmation_email_enabled of this ShopifySubscriptionCreationRequest.

            

        :param store_order_confirmation_email_enabled: The store_order_confirmation_email_enabled of this ShopifySubscriptionCreationRequest.
        :type: bool
        """

        self._store_order_confirmation_email_enabled = store_order_confirmation_email_enabled
    
    @property
    def subscriber(self):
        """Gets the subscriber of this ShopifySubscriptionCreationRequest.

            

        :return: The subscriber of this ShopifySubscriptionCreationRequest.
        :rtype: ShopifySubscriberCreation
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this ShopifySubscriptionCreationRequest.

            

        :param subscriber: The subscriber of this ShopifySubscriptionCreationRequest.
        :type: ShopifySubscriberCreation
        """
        if subscriber is None:
            raise ValueError("Invalid value for `subscriber`, must not be `None`")

        self._subscriber = subscriber
    
    @property
    def subscriber_suspension_allowed(self):
        """Gets the subscriber_suspension_allowed of this ShopifySubscriptionCreationRequest.

            

        :return: The subscriber_suspension_allowed of this ShopifySubscriptionCreationRequest.
        :rtype: bool
        """
        return self._subscriber_suspension_allowed

    @subscriber_suspension_allowed.setter
    def subscriber_suspension_allowed(self, subscriber_suspension_allowed):
        """Sets the subscriber_suspension_allowed of this ShopifySubscriptionCreationRequest.

            

        :param subscriber_suspension_allowed: The subscriber_suspension_allowed of this ShopifySubscriptionCreationRequest.
        :type: bool
        """

        self._subscriber_suspension_allowed = subscriber_suspension_allowed
    

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
        if issubclass(ShopifySubscriptionCreationRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
