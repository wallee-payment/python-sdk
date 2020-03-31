# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractShopifySubscriptionProductActive:

    swagger_types = {
    
        'absolute_price_adjustment': 'float',
        'billing_day_of_month': 'int',
        'billing_interval_amount': 'int',
        'billing_interval_unit': 'ShopifySubscriptionBillingIntervalUnit',
        'billing_weekday': 'ShopifySubscriptionWeekday',
        'fixed_price': 'float',
        'maximal_billing_cycles': 'int',
        'maximal_suspendable_cycles': 'int',
        'minimal_billing_cycles': 'int',
        'pricing_option': 'ShopifySubscriptionProductPricingOption',
        'relative_price_adjustment': 'float',
        'state': 'ShopifySubscriptionProductState',
        'store_order_confirmation_email_enabled': 'bool',
        'subscriber_suspension_allowed': 'bool',
        'termination_billing_cycles': 'int',
    }

    attribute_map = {
        'absolute_price_adjustment': 'absolutePriceAdjustment','billing_day_of_month': 'billingDayOfMonth','billing_interval_amount': 'billingIntervalAmount','billing_interval_unit': 'billingIntervalUnit','billing_weekday': 'billingWeekday','fixed_price': 'fixedPrice','maximal_billing_cycles': 'maximalBillingCycles','maximal_suspendable_cycles': 'maximalSuspendableCycles','minimal_billing_cycles': 'minimalBillingCycles','pricing_option': 'pricingOption','relative_price_adjustment': 'relativePriceAdjustment','state': 'state','store_order_confirmation_email_enabled': 'storeOrderConfirmationEmailEnabled','subscriber_suspension_allowed': 'subscriberSuspensionAllowed','termination_billing_cycles': 'terminationBillingCycles',
    }

    
    _absolute_price_adjustment = None
    _billing_day_of_month = None
    _billing_interval_amount = None
    _billing_interval_unit = None
    _billing_weekday = None
    _fixed_price = None
    _maximal_billing_cycles = None
    _maximal_suspendable_cycles = None
    _minimal_billing_cycles = None
    _pricing_option = None
    _relative_price_adjustment = None
    _state = None
    _store_order_confirmation_email_enabled = None
    _subscriber_suspension_allowed = None
    _termination_billing_cycles = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.absolute_price_adjustment = kwargs.get('absolute_price_adjustment', None)
        self.billing_day_of_month = kwargs.get('billing_day_of_month', None)
        self.billing_interval_amount = kwargs.get('billing_interval_amount', None)
        self.billing_interval_unit = kwargs.get('billing_interval_unit', None)
        self.billing_weekday = kwargs.get('billing_weekday', None)
        self.fixed_price = kwargs.get('fixed_price', None)
        self.maximal_billing_cycles = kwargs.get('maximal_billing_cycles', None)
        self.maximal_suspendable_cycles = kwargs.get('maximal_suspendable_cycles', None)
        self.minimal_billing_cycles = kwargs.get('minimal_billing_cycles', None)
        self.pricing_option = kwargs.get('pricing_option', None)
        self.relative_price_adjustment = kwargs.get('relative_price_adjustment', None)
        self.state = kwargs.get('state', None)
        self.store_order_confirmation_email_enabled = kwargs.get('store_order_confirmation_email_enabled', None)
        self.subscriber_suspension_allowed = kwargs.get('subscriber_suspension_allowed', None)
        self.termination_billing_cycles = kwargs.get('termination_billing_cycles', None)
        

    
    @property
    def absolute_price_adjustment(self):
        """Gets the absolute_price_adjustment of this AbstractShopifySubscriptionProductActive.

            

        :return: The absolute_price_adjustment of this AbstractShopifySubscriptionProductActive.
        :rtype: float
        """
        return self._absolute_price_adjustment

    @absolute_price_adjustment.setter
    def absolute_price_adjustment(self, absolute_price_adjustment):
        """Sets the absolute_price_adjustment of this AbstractShopifySubscriptionProductActive.

            

        :param absolute_price_adjustment: The absolute_price_adjustment of this AbstractShopifySubscriptionProductActive.
        :type: float
        """

        self._absolute_price_adjustment = absolute_price_adjustment
    
    @property
    def billing_day_of_month(self):
        """Gets the billing_day_of_month of this AbstractShopifySubscriptionProductActive.

            Define the day of the month on which the recurring orders should be created.

        :return: The billing_day_of_month of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._billing_day_of_month

    @billing_day_of_month.setter
    def billing_day_of_month(self, billing_day_of_month):
        """Sets the billing_day_of_month of this AbstractShopifySubscriptionProductActive.

            Define the day of the month on which the recurring orders should be created.

        :param billing_day_of_month: The billing_day_of_month of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._billing_day_of_month = billing_day_of_month
    
    @property
    def billing_interval_amount(self):
        """Gets the billing_interval_amount of this AbstractShopifySubscriptionProductActive.

            

        :return: The billing_interval_amount of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._billing_interval_amount

    @billing_interval_amount.setter
    def billing_interval_amount(self, billing_interval_amount):
        """Sets the billing_interval_amount of this AbstractShopifySubscriptionProductActive.

            

        :param billing_interval_amount: The billing_interval_amount of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._billing_interval_amount = billing_interval_amount
    
    @property
    def billing_interval_unit(self):
        """Gets the billing_interval_unit of this AbstractShopifySubscriptionProductActive.

            Define how frequently recurring orders should be created.

        :return: The billing_interval_unit of this AbstractShopifySubscriptionProductActive.
        :rtype: ShopifySubscriptionBillingIntervalUnit
        """
        return self._billing_interval_unit

    @billing_interval_unit.setter
    def billing_interval_unit(self, billing_interval_unit):
        """Sets the billing_interval_unit of this AbstractShopifySubscriptionProductActive.

            Define how frequently recurring orders should be created.

        :param billing_interval_unit: The billing_interval_unit of this AbstractShopifySubscriptionProductActive.
        :type: ShopifySubscriptionBillingIntervalUnit
        """

        self._billing_interval_unit = billing_interval_unit
    
    @property
    def billing_weekday(self):
        """Gets the billing_weekday of this AbstractShopifySubscriptionProductActive.

            Define the weekday on which the recurring orders should be created.

        :return: The billing_weekday of this AbstractShopifySubscriptionProductActive.
        :rtype: ShopifySubscriptionWeekday
        """
        return self._billing_weekday

    @billing_weekday.setter
    def billing_weekday(self, billing_weekday):
        """Sets the billing_weekday of this AbstractShopifySubscriptionProductActive.

            Define the weekday on which the recurring orders should be created.

        :param billing_weekday: The billing_weekday of this AbstractShopifySubscriptionProductActive.
        :type: ShopifySubscriptionWeekday
        """

        self._billing_weekday = billing_weekday
    
    @property
    def fixed_price(self):
        """Gets the fixed_price of this AbstractShopifySubscriptionProductActive.

            

        :return: The fixed_price of this AbstractShopifySubscriptionProductActive.
        :rtype: float
        """
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, fixed_price):
        """Sets the fixed_price of this AbstractShopifySubscriptionProductActive.

            

        :param fixed_price: The fixed_price of this AbstractShopifySubscriptionProductActive.
        :type: float
        """

        self._fixed_price = fixed_price
    
    @property
    def maximal_billing_cycles(self):
        """Gets the maximal_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the maximum number of orders the subscription will run for.

        :return: The maximal_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._maximal_billing_cycles

    @maximal_billing_cycles.setter
    def maximal_billing_cycles(self, maximal_billing_cycles):
        """Sets the maximal_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the maximum number of orders the subscription will run for.

        :param maximal_billing_cycles: The maximal_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._maximal_billing_cycles = maximal_billing_cycles
    
    @property
    def maximal_suspendable_cycles(self):
        """Gets the maximal_suspendable_cycles of this AbstractShopifySubscriptionProductActive.

            Define the maximum number of orders the subscription can be suspended for at a time.

        :return: The maximal_suspendable_cycles of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._maximal_suspendable_cycles

    @maximal_suspendable_cycles.setter
    def maximal_suspendable_cycles(self, maximal_suspendable_cycles):
        """Sets the maximal_suspendable_cycles of this AbstractShopifySubscriptionProductActive.

            Define the maximum number of orders the subscription can be suspended for at a time.

        :param maximal_suspendable_cycles: The maximal_suspendable_cycles of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._maximal_suspendable_cycles = maximal_suspendable_cycles
    
    @property
    def minimal_billing_cycles(self):
        """Gets the minimal_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the minimal number of orders the subscription will run for.

        :return: The minimal_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._minimal_billing_cycles

    @minimal_billing_cycles.setter
    def minimal_billing_cycles(self, minimal_billing_cycles):
        """Sets the minimal_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the minimal number of orders the subscription will run for.

        :param minimal_billing_cycles: The minimal_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._minimal_billing_cycles = minimal_billing_cycles
    
    @property
    def pricing_option(self):
        """Gets the pricing_option of this AbstractShopifySubscriptionProductActive.

            

        :return: The pricing_option of this AbstractShopifySubscriptionProductActive.
        :rtype: ShopifySubscriptionProductPricingOption
        """
        return self._pricing_option

    @pricing_option.setter
    def pricing_option(self, pricing_option):
        """Sets the pricing_option of this AbstractShopifySubscriptionProductActive.

            

        :param pricing_option: The pricing_option of this AbstractShopifySubscriptionProductActive.
        :type: ShopifySubscriptionProductPricingOption
        """

        self._pricing_option = pricing_option
    
    @property
    def relative_price_adjustment(self):
        """Gets the relative_price_adjustment of this AbstractShopifySubscriptionProductActive.

            

        :return: The relative_price_adjustment of this AbstractShopifySubscriptionProductActive.
        :rtype: float
        """
        return self._relative_price_adjustment

    @relative_price_adjustment.setter
    def relative_price_adjustment(self, relative_price_adjustment):
        """Sets the relative_price_adjustment of this AbstractShopifySubscriptionProductActive.

            

        :param relative_price_adjustment: The relative_price_adjustment of this AbstractShopifySubscriptionProductActive.
        :type: float
        """

        self._relative_price_adjustment = relative_price_adjustment
    
    @property
    def state(self):
        """Gets the state of this AbstractShopifySubscriptionProductActive.

            

        :return: The state of this AbstractShopifySubscriptionProductActive.
        :rtype: ShopifySubscriptionProductState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractShopifySubscriptionProductActive.

            

        :param state: The state of this AbstractShopifySubscriptionProductActive.
        :type: ShopifySubscriptionProductState
        """

        self._state = state
    
    @property
    def store_order_confirmation_email_enabled(self):
        """Gets the store_order_confirmation_email_enabled of this AbstractShopifySubscriptionProductActive.

            Define whether the order confirmation email of the Shopify shop is sent to the customer for recurring orders.

        :return: The store_order_confirmation_email_enabled of this AbstractShopifySubscriptionProductActive.
        :rtype: bool
        """
        return self._store_order_confirmation_email_enabled

    @store_order_confirmation_email_enabled.setter
    def store_order_confirmation_email_enabled(self, store_order_confirmation_email_enabled):
        """Sets the store_order_confirmation_email_enabled of this AbstractShopifySubscriptionProductActive.

            Define whether the order confirmation email of the Shopify shop is sent to the customer for recurring orders.

        :param store_order_confirmation_email_enabled: The store_order_confirmation_email_enabled of this AbstractShopifySubscriptionProductActive.
        :type: bool
        """

        self._store_order_confirmation_email_enabled = store_order_confirmation_email_enabled
    
    @property
    def subscriber_suspension_allowed(self):
        """Gets the subscriber_suspension_allowed of this AbstractShopifySubscriptionProductActive.

            Define whether the customer is allowed to suspend subscriptions.

        :return: The subscriber_suspension_allowed of this AbstractShopifySubscriptionProductActive.
        :rtype: bool
        """
        return self._subscriber_suspension_allowed

    @subscriber_suspension_allowed.setter
    def subscriber_suspension_allowed(self, subscriber_suspension_allowed):
        """Sets the subscriber_suspension_allowed of this AbstractShopifySubscriptionProductActive.

            Define whether the customer is allowed to suspend subscriptions.

        :param subscriber_suspension_allowed: The subscriber_suspension_allowed of this AbstractShopifySubscriptionProductActive.
        :type: bool
        """

        self._subscriber_suspension_allowed = subscriber_suspension_allowed
    
    @property
    def termination_billing_cycles(self):
        """Gets the termination_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the number of orders the subscription will keep running for after its termination has been requested.

        :return: The termination_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :rtype: int
        """
        return self._termination_billing_cycles

    @termination_billing_cycles.setter
    def termination_billing_cycles(self, termination_billing_cycles):
        """Sets the termination_billing_cycles of this AbstractShopifySubscriptionProductActive.

            Define the number of orders the subscription will keep running for after its termination has been requested.

        :param termination_billing_cycles: The termination_billing_cycles of this AbstractShopifySubscriptionProductActive.
        :type: int
        """

        self._termination_billing_cycles = termination_billing_cycles
    

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
        if issubclass(AbstractShopifySubscriptionProductActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractShopifySubscriptionProductActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
