# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionVersion:

    swagger_types = {
    
        'billing_address': 'ShopifySubscriptionAddress',
        'billing_day_of_month': 'int',
        'billing_interval_amount': 'int',
        'billing_interval_unit': 'ShopifySubscriptionBillingIntervalUnit',
        'billing_reference_date': 'datetime',
        'billing_weekday': 'ShopifySubscriptionWeekday',
        'created_by': 'int',
        'created_on': 'datetime',
        'currency': 'str',
        'discharged_by': 'int',
        'discharged_on': 'datetime',
        'id': 'int',
        'items': 'list[ShopifySubscriptionVersionItem]',
        'linked_space_id': 'int',
        'maximal_billing_cycles': 'int',
        'maximal_suspendable_cycles': 'int',
        'minimal_billing_cycles': 'int',
        'payment_gateway': 'str',
        'shipping_address': 'ShopifySubscriptionAddress',
        'shipping_rate': 'str',
        'shop': 'int',
        'state': 'ShopifySubscriptionVersionState',
        'store_order_confirmation_email_enabled': 'bool',
        'subscriber_suspension_allowed': 'bool',
        'subscription': 'ShopifySubscription',
        'termination_billing_cycles': 'int',
        'token': 'int',
        'version': 'int',
    }

    attribute_map = {
        'billing_address': 'billingAddress','billing_day_of_month': 'billingDayOfMonth','billing_interval_amount': 'billingIntervalAmount','billing_interval_unit': 'billingIntervalUnit','billing_reference_date': 'billingReferenceDate','billing_weekday': 'billingWeekday','created_by': 'createdBy','created_on': 'createdOn','currency': 'currency','discharged_by': 'dischargedBy','discharged_on': 'dischargedOn','id': 'id','items': 'items','linked_space_id': 'linkedSpaceId','maximal_billing_cycles': 'maximalBillingCycles','maximal_suspendable_cycles': 'maximalSuspendableCycles','minimal_billing_cycles': 'minimalBillingCycles','payment_gateway': 'paymentGateway','shipping_address': 'shippingAddress','shipping_rate': 'shippingRate','shop': 'shop','state': 'state','store_order_confirmation_email_enabled': 'storeOrderConfirmationEmailEnabled','subscriber_suspension_allowed': 'subscriberSuspensionAllowed','subscription': 'subscription','termination_billing_cycles': 'terminationBillingCycles','token': 'token','version': 'version',
    }

    
    _billing_address = None
    _billing_day_of_month = None
    _billing_interval_amount = None
    _billing_interval_unit = None
    _billing_reference_date = None
    _billing_weekday = None
    _created_by = None
    _created_on = None
    _currency = None
    _discharged_by = None
    _discharged_on = None
    _id = None
    _items = None
    _linked_space_id = None
    _maximal_billing_cycles = None
    _maximal_suspendable_cycles = None
    _minimal_billing_cycles = None
    _payment_gateway = None
    _shipping_address = None
    _shipping_rate = None
    _shop = None
    _state = None
    _store_order_confirmation_email_enabled = None
    _subscriber_suspension_allowed = None
    _subscription = None
    _termination_billing_cycles = None
    _token = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_address = kwargs.get('billing_address', None)
        self.billing_day_of_month = kwargs.get('billing_day_of_month', None)
        self.billing_interval_amount = kwargs.get('billing_interval_amount', None)
        self.billing_interval_unit = kwargs.get('billing_interval_unit', None)
        self.billing_reference_date = kwargs.get('billing_reference_date', None)
        self.billing_weekday = kwargs.get('billing_weekday', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.currency = kwargs.get('currency', None)
        self.discharged_by = kwargs.get('discharged_by', None)
        self.discharged_on = kwargs.get('discharged_on', None)
        self.id = kwargs.get('id', None)
        self.items = kwargs.get('items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.maximal_billing_cycles = kwargs.get('maximal_billing_cycles', None)
        self.maximal_suspendable_cycles = kwargs.get('maximal_suspendable_cycles', None)
        self.minimal_billing_cycles = kwargs.get('minimal_billing_cycles', None)
        self.payment_gateway = kwargs.get('payment_gateway', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.shipping_rate = kwargs.get('shipping_rate', None)
        self.shop = kwargs.get('shop', None)
        self.state = kwargs.get('state', None)
        self.store_order_confirmation_email_enabled = kwargs.get('store_order_confirmation_email_enabled', None)
        self.subscriber_suspension_allowed = kwargs.get('subscriber_suspension_allowed', None)
        self.subscription = kwargs.get('subscription', None)
        self.termination_billing_cycles = kwargs.get('termination_billing_cycles', None)
        self.token = kwargs.get('token', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def billing_address(self):
        """Gets the billing_address of this ShopifySubscriptionVersion.

            

        :return: The billing_address of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscriptionAddress
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ShopifySubscriptionVersion.

            

        :param billing_address: The billing_address of this ShopifySubscriptionVersion.
        :type: ShopifySubscriptionAddress
        """

        self._billing_address = billing_address
    
    @property
    def billing_day_of_month(self):
        """Gets the billing_day_of_month of this ShopifySubscriptionVersion.

            

        :return: The billing_day_of_month of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._billing_day_of_month

    @billing_day_of_month.setter
    def billing_day_of_month(self, billing_day_of_month):
        """Sets the billing_day_of_month of this ShopifySubscriptionVersion.

            

        :param billing_day_of_month: The billing_day_of_month of this ShopifySubscriptionVersion.
        :type: int
        """

        self._billing_day_of_month = billing_day_of_month
    
    @property
    def billing_interval_amount(self):
        """Gets the billing_interval_amount of this ShopifySubscriptionVersion.

            

        :return: The billing_interval_amount of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._billing_interval_amount

    @billing_interval_amount.setter
    def billing_interval_amount(self, billing_interval_amount):
        """Sets the billing_interval_amount of this ShopifySubscriptionVersion.

            

        :param billing_interval_amount: The billing_interval_amount of this ShopifySubscriptionVersion.
        :type: int
        """

        self._billing_interval_amount = billing_interval_amount
    
    @property
    def billing_interval_unit(self):
        """Gets the billing_interval_unit of this ShopifySubscriptionVersion.

            

        :return: The billing_interval_unit of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscriptionBillingIntervalUnit
        """
        return self._billing_interval_unit

    @billing_interval_unit.setter
    def billing_interval_unit(self, billing_interval_unit):
        """Sets the billing_interval_unit of this ShopifySubscriptionVersion.

            

        :param billing_interval_unit: The billing_interval_unit of this ShopifySubscriptionVersion.
        :type: ShopifySubscriptionBillingIntervalUnit
        """

        self._billing_interval_unit = billing_interval_unit
    
    @property
    def billing_reference_date(self):
        """Gets the billing_reference_date of this ShopifySubscriptionVersion.

            

        :return: The billing_reference_date of this ShopifySubscriptionVersion.
        :rtype: datetime
        """
        return self._billing_reference_date

    @billing_reference_date.setter
    def billing_reference_date(self, billing_reference_date):
        """Sets the billing_reference_date of this ShopifySubscriptionVersion.

            

        :param billing_reference_date: The billing_reference_date of this ShopifySubscriptionVersion.
        :type: datetime
        """

        self._billing_reference_date = billing_reference_date
    
    @property
    def billing_weekday(self):
        """Gets the billing_weekday of this ShopifySubscriptionVersion.

            

        :return: The billing_weekday of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscriptionWeekday
        """
        return self._billing_weekday

    @billing_weekday.setter
    def billing_weekday(self, billing_weekday):
        """Sets the billing_weekday of this ShopifySubscriptionVersion.

            

        :param billing_weekday: The billing_weekday of this ShopifySubscriptionVersion.
        :type: ShopifySubscriptionWeekday
        """

        self._billing_weekday = billing_weekday
    
    @property
    def created_by(self):
        """Gets the created_by of this ShopifySubscriptionVersion.

            

        :return: The created_by of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShopifySubscriptionVersion.

            

        :param created_by: The created_by of this ShopifySubscriptionVersion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifySubscriptionVersion.

            

        :return: The created_on of this ShopifySubscriptionVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifySubscriptionVersion.

            

        :param created_on: The created_on of this ShopifySubscriptionVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def currency(self):
        """Gets the currency of this ShopifySubscriptionVersion.

            

        :return: The currency of this ShopifySubscriptionVersion.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this ShopifySubscriptionVersion.

            

        :param currency: The currency of this ShopifySubscriptionVersion.
        :type: str
        """

        self._currency = currency
    
    @property
    def discharged_by(self):
        """Gets the discharged_by of this ShopifySubscriptionVersion.

            

        :return: The discharged_by of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._discharged_by

    @discharged_by.setter
    def discharged_by(self, discharged_by):
        """Sets the discharged_by of this ShopifySubscriptionVersion.

            

        :param discharged_by: The discharged_by of this ShopifySubscriptionVersion.
        :type: int
        """

        self._discharged_by = discharged_by
    
    @property
    def discharged_on(self):
        """Gets the discharged_on of this ShopifySubscriptionVersion.

            

        :return: The discharged_on of this ShopifySubscriptionVersion.
        :rtype: datetime
        """
        return self._discharged_on

    @discharged_on.setter
    def discharged_on(self, discharged_on):
        """Sets the discharged_on of this ShopifySubscriptionVersion.

            

        :param discharged_on: The discharged_on of this ShopifySubscriptionVersion.
        :type: datetime
        """

        self._discharged_on = discharged_on
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriptionVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriptionVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscriptionVersion.
        :type: int
        """

        self._id = id
    
    @property
    def items(self):
        """Gets the items of this ShopifySubscriptionVersion.

            

        :return: The items of this ShopifySubscriptionVersion.
        :rtype: list[ShopifySubscriptionVersionItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ShopifySubscriptionVersion.

            

        :param items: The items of this ShopifySubscriptionVersion.
        :type: list[ShopifySubscriptionVersionItem]
        """

        self._items = items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifySubscriptionVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifySubscriptionVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ShopifySubscriptionVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def maximal_billing_cycles(self):
        """Gets the maximal_billing_cycles of this ShopifySubscriptionVersion.

            

        :return: The maximal_billing_cycles of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._maximal_billing_cycles

    @maximal_billing_cycles.setter
    def maximal_billing_cycles(self, maximal_billing_cycles):
        """Sets the maximal_billing_cycles of this ShopifySubscriptionVersion.

            

        :param maximal_billing_cycles: The maximal_billing_cycles of this ShopifySubscriptionVersion.
        :type: int
        """

        self._maximal_billing_cycles = maximal_billing_cycles
    
    @property
    def maximal_suspendable_cycles(self):
        """Gets the maximal_suspendable_cycles of this ShopifySubscriptionVersion.

            

        :return: The maximal_suspendable_cycles of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._maximal_suspendable_cycles

    @maximal_suspendable_cycles.setter
    def maximal_suspendable_cycles(self, maximal_suspendable_cycles):
        """Sets the maximal_suspendable_cycles of this ShopifySubscriptionVersion.

            

        :param maximal_suspendable_cycles: The maximal_suspendable_cycles of this ShopifySubscriptionVersion.
        :type: int
        """

        self._maximal_suspendable_cycles = maximal_suspendable_cycles
    
    @property
    def minimal_billing_cycles(self):
        """Gets the minimal_billing_cycles of this ShopifySubscriptionVersion.

            

        :return: The minimal_billing_cycles of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._minimal_billing_cycles

    @minimal_billing_cycles.setter
    def minimal_billing_cycles(self, minimal_billing_cycles):
        """Sets the minimal_billing_cycles of this ShopifySubscriptionVersion.

            

        :param minimal_billing_cycles: The minimal_billing_cycles of this ShopifySubscriptionVersion.
        :type: int
        """

        self._minimal_billing_cycles = minimal_billing_cycles
    
    @property
    def payment_gateway(self):
        """Gets the payment_gateway of this ShopifySubscriptionVersion.

            

        :return: The payment_gateway of this ShopifySubscriptionVersion.
        :rtype: str
        """
        return self._payment_gateway

    @payment_gateway.setter
    def payment_gateway(self, payment_gateway):
        """Sets the payment_gateway of this ShopifySubscriptionVersion.

            

        :param payment_gateway: The payment_gateway of this ShopifySubscriptionVersion.
        :type: str
        """

        self._payment_gateway = payment_gateway
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this ShopifySubscriptionVersion.

            

        :return: The shipping_address of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscriptionAddress
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this ShopifySubscriptionVersion.

            

        :param shipping_address: The shipping_address of this ShopifySubscriptionVersion.
        :type: ShopifySubscriptionAddress
        """

        self._shipping_address = shipping_address
    
    @property
    def shipping_rate(self):
        """Gets the shipping_rate of this ShopifySubscriptionVersion.

            

        :return: The shipping_rate of this ShopifySubscriptionVersion.
        :rtype: str
        """
        return self._shipping_rate

    @shipping_rate.setter
    def shipping_rate(self, shipping_rate):
        """Sets the shipping_rate of this ShopifySubscriptionVersion.

            

        :param shipping_rate: The shipping_rate of this ShopifySubscriptionVersion.
        :type: str
        """

        self._shipping_rate = shipping_rate
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscriptionVersion.

            

        :return: The shop of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscriptionVersion.

            

        :param shop: The shop of this ShopifySubscriptionVersion.
        :type: int
        """

        self._shop = shop
    
    @property
    def state(self):
        """Gets the state of this ShopifySubscriptionVersion.

            

        :return: The state of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscriptionVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifySubscriptionVersion.

            

        :param state: The state of this ShopifySubscriptionVersion.
        :type: ShopifySubscriptionVersionState
        """

        self._state = state
    
    @property
    def store_order_confirmation_email_enabled(self):
        """Gets the store_order_confirmation_email_enabled of this ShopifySubscriptionVersion.

            

        :return: The store_order_confirmation_email_enabled of this ShopifySubscriptionVersion.
        :rtype: bool
        """
        return self._store_order_confirmation_email_enabled

    @store_order_confirmation_email_enabled.setter
    def store_order_confirmation_email_enabled(self, store_order_confirmation_email_enabled):
        """Sets the store_order_confirmation_email_enabled of this ShopifySubscriptionVersion.

            

        :param store_order_confirmation_email_enabled: The store_order_confirmation_email_enabled of this ShopifySubscriptionVersion.
        :type: bool
        """

        self._store_order_confirmation_email_enabled = store_order_confirmation_email_enabled
    
    @property
    def subscriber_suspension_allowed(self):
        """Gets the subscriber_suspension_allowed of this ShopifySubscriptionVersion.

            

        :return: The subscriber_suspension_allowed of this ShopifySubscriptionVersion.
        :rtype: bool
        """
        return self._subscriber_suspension_allowed

    @subscriber_suspension_allowed.setter
    def subscriber_suspension_allowed(self, subscriber_suspension_allowed):
        """Sets the subscriber_suspension_allowed of this ShopifySubscriptionVersion.

            

        :param subscriber_suspension_allowed: The subscriber_suspension_allowed of this ShopifySubscriptionVersion.
        :type: bool
        """

        self._subscriber_suspension_allowed = subscriber_suspension_allowed
    
    @property
    def subscription(self):
        """Gets the subscription of this ShopifySubscriptionVersion.

            

        :return: The subscription of this ShopifySubscriptionVersion.
        :rtype: ShopifySubscription
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this ShopifySubscriptionVersion.

            

        :param subscription: The subscription of this ShopifySubscriptionVersion.
        :type: ShopifySubscription
        """

        self._subscription = subscription
    
    @property
    def termination_billing_cycles(self):
        """Gets the termination_billing_cycles of this ShopifySubscriptionVersion.

            

        :return: The termination_billing_cycles of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._termination_billing_cycles

    @termination_billing_cycles.setter
    def termination_billing_cycles(self, termination_billing_cycles):
        """Sets the termination_billing_cycles of this ShopifySubscriptionVersion.

            

        :param termination_billing_cycles: The termination_billing_cycles of this ShopifySubscriptionVersion.
        :type: int
        """

        self._termination_billing_cycles = termination_billing_cycles
    
    @property
    def token(self):
        """Gets the token of this ShopifySubscriptionVersion.

            

        :return: The token of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this ShopifySubscriptionVersion.

            

        :param token: The token of this ShopifySubscriptionVersion.
        :type: int
        """

        self._token = token
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscriptionVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscriptionVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscriptionVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscriptionVersion.
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
        if issubclass(ShopifySubscriptionVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
