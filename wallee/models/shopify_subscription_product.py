# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionProduct:

    swagger_types = {
    
        'absolute_price_adjustment': 'float',
        'billing_day_of_month': 'int',
        'billing_interval_amount': 'int',
        'billing_interval_unit': 'ShopifySubscriptionBillingIntervalUnit',
        'billing_weekday': 'ShopifySubscriptionWeekday',
        'fixed_price': 'float',
        'id': 'int',
        'linked_space_id': 'int',
        'maximal_billing_cycles': 'int',
        'maximal_suspendable_cycles': 'int',
        'minimal_billing_cycles': 'int',
        'planned_purge_date': 'datetime',
        'pricing_option': 'ShopifySubscriptionProductPricingOption',
        'product_id': 'str',
        'product_name': 'str',
        'product_price': 'float',
        'product_sku': 'str',
        'product_variant_id': 'str',
        'product_variant_name': 'str',
        'relative_price_adjustment': 'float',
        'shipping_required': 'bool',
        'shop': 'int',
        'state': 'ShopifySubscriptionProductState',
        'stock_check_required': 'bool',
        'store_order_confirmation_email_enabled': 'bool',
        'subscriber_suspension_allowed': 'bool',
        'termination_billing_cycles': 'int',
        'updated_at': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'absolute_price_adjustment': 'absolutePriceAdjustment','billing_day_of_month': 'billingDayOfMonth','billing_interval_amount': 'billingIntervalAmount','billing_interval_unit': 'billingIntervalUnit','billing_weekday': 'billingWeekday','fixed_price': 'fixedPrice','id': 'id','linked_space_id': 'linkedSpaceId','maximal_billing_cycles': 'maximalBillingCycles','maximal_suspendable_cycles': 'maximalSuspendableCycles','minimal_billing_cycles': 'minimalBillingCycles','planned_purge_date': 'plannedPurgeDate','pricing_option': 'pricingOption','product_id': 'productId','product_name': 'productName','product_price': 'productPrice','product_sku': 'productSku','product_variant_id': 'productVariantId','product_variant_name': 'productVariantName','relative_price_adjustment': 'relativePriceAdjustment','shipping_required': 'shippingRequired','shop': 'shop','state': 'state','stock_check_required': 'stockCheckRequired','store_order_confirmation_email_enabled': 'storeOrderConfirmationEmailEnabled','subscriber_suspension_allowed': 'subscriberSuspensionAllowed','termination_billing_cycles': 'terminationBillingCycles','updated_at': 'updatedAt','version': 'version',
    }

    
    _absolute_price_adjustment = None
    _billing_day_of_month = None
    _billing_interval_amount = None
    _billing_interval_unit = None
    _billing_weekday = None
    _fixed_price = None
    _id = None
    _linked_space_id = None
    _maximal_billing_cycles = None
    _maximal_suspendable_cycles = None
    _minimal_billing_cycles = None
    _planned_purge_date = None
    _pricing_option = None
    _product_id = None
    _product_name = None
    _product_price = None
    _product_sku = None
    _product_variant_id = None
    _product_variant_name = None
    _relative_price_adjustment = None
    _shipping_required = None
    _shop = None
    _state = None
    _stock_check_required = None
    _store_order_confirmation_email_enabled = None
    _subscriber_suspension_allowed = None
    _termination_billing_cycles = None
    _updated_at = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.absolute_price_adjustment = kwargs.get('absolute_price_adjustment', None)
        self.billing_day_of_month = kwargs.get('billing_day_of_month', None)
        self.billing_interval_amount = kwargs.get('billing_interval_amount', None)
        self.billing_interval_unit = kwargs.get('billing_interval_unit', None)
        self.billing_weekday = kwargs.get('billing_weekday', None)
        self.fixed_price = kwargs.get('fixed_price', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.maximal_billing_cycles = kwargs.get('maximal_billing_cycles', None)
        self.maximal_suspendable_cycles = kwargs.get('maximal_suspendable_cycles', None)
        self.minimal_billing_cycles = kwargs.get('minimal_billing_cycles', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.pricing_option = kwargs.get('pricing_option', None)
        self.product_id = kwargs.get('product_id', None)
        self.product_name = kwargs.get('product_name', None)
        self.product_price = kwargs.get('product_price', None)
        self.product_sku = kwargs.get('product_sku', None)
        self.product_variant_id = kwargs.get('product_variant_id', None)
        self.product_variant_name = kwargs.get('product_variant_name', None)
        self.relative_price_adjustment = kwargs.get('relative_price_adjustment', None)
        self.shipping_required = kwargs.get('shipping_required', None)
        self.shop = kwargs.get('shop', None)
        self.state = kwargs.get('state', None)
        self.stock_check_required = kwargs.get('stock_check_required', None)
        self.store_order_confirmation_email_enabled = kwargs.get('store_order_confirmation_email_enabled', None)
        self.subscriber_suspension_allowed = kwargs.get('subscriber_suspension_allowed', None)
        self.termination_billing_cycles = kwargs.get('termination_billing_cycles', None)
        self.updated_at = kwargs.get('updated_at', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def absolute_price_adjustment(self):
        """Gets the absolute_price_adjustment of this ShopifySubscriptionProduct.

            

        :return: The absolute_price_adjustment of this ShopifySubscriptionProduct.
        :rtype: float
        """
        return self._absolute_price_adjustment

    @absolute_price_adjustment.setter
    def absolute_price_adjustment(self, absolute_price_adjustment):
        """Sets the absolute_price_adjustment of this ShopifySubscriptionProduct.

            

        :param absolute_price_adjustment: The absolute_price_adjustment of this ShopifySubscriptionProduct.
        :type: float
        """

        self._absolute_price_adjustment = absolute_price_adjustment
    
    @property
    def billing_day_of_month(self):
        """Gets the billing_day_of_month of this ShopifySubscriptionProduct.

            Define the day of the month on which the recurring orders should be created.

        :return: The billing_day_of_month of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._billing_day_of_month

    @billing_day_of_month.setter
    def billing_day_of_month(self, billing_day_of_month):
        """Sets the billing_day_of_month of this ShopifySubscriptionProduct.

            Define the day of the month on which the recurring orders should be created.

        :param billing_day_of_month: The billing_day_of_month of this ShopifySubscriptionProduct.
        :type: int
        """

        self._billing_day_of_month = billing_day_of_month
    
    @property
    def billing_interval_amount(self):
        """Gets the billing_interval_amount of this ShopifySubscriptionProduct.

            

        :return: The billing_interval_amount of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._billing_interval_amount

    @billing_interval_amount.setter
    def billing_interval_amount(self, billing_interval_amount):
        """Sets the billing_interval_amount of this ShopifySubscriptionProduct.

            

        :param billing_interval_amount: The billing_interval_amount of this ShopifySubscriptionProduct.
        :type: int
        """

        self._billing_interval_amount = billing_interval_amount
    
    @property
    def billing_interval_unit(self):
        """Gets the billing_interval_unit of this ShopifySubscriptionProduct.

            Define how frequently recurring orders should be created.

        :return: The billing_interval_unit of this ShopifySubscriptionProduct.
        :rtype: ShopifySubscriptionBillingIntervalUnit
        """
        return self._billing_interval_unit

    @billing_interval_unit.setter
    def billing_interval_unit(self, billing_interval_unit):
        """Sets the billing_interval_unit of this ShopifySubscriptionProduct.

            Define how frequently recurring orders should be created.

        :param billing_interval_unit: The billing_interval_unit of this ShopifySubscriptionProduct.
        :type: ShopifySubscriptionBillingIntervalUnit
        """

        self._billing_interval_unit = billing_interval_unit
    
    @property
    def billing_weekday(self):
        """Gets the billing_weekday of this ShopifySubscriptionProduct.

            Define the weekday on which the recurring orders should be created.

        :return: The billing_weekday of this ShopifySubscriptionProduct.
        :rtype: ShopifySubscriptionWeekday
        """
        return self._billing_weekday

    @billing_weekday.setter
    def billing_weekday(self, billing_weekday):
        """Sets the billing_weekday of this ShopifySubscriptionProduct.

            Define the weekday on which the recurring orders should be created.

        :param billing_weekday: The billing_weekday of this ShopifySubscriptionProduct.
        :type: ShopifySubscriptionWeekday
        """

        self._billing_weekday = billing_weekday
    
    @property
    def fixed_price(self):
        """Gets the fixed_price of this ShopifySubscriptionProduct.

            

        :return: The fixed_price of this ShopifySubscriptionProduct.
        :rtype: float
        """
        return self._fixed_price

    @fixed_price.setter
    def fixed_price(self, fixed_price):
        """Sets the fixed_price of this ShopifySubscriptionProduct.

            

        :param fixed_price: The fixed_price of this ShopifySubscriptionProduct.
        :type: float
        """

        self._fixed_price = fixed_price
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriptionProduct.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriptionProduct.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscriptionProduct.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifySubscriptionProduct.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifySubscriptionProduct.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ShopifySubscriptionProduct.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def maximal_billing_cycles(self):
        """Gets the maximal_billing_cycles of this ShopifySubscriptionProduct.

            Define the maximum number of orders the subscription will run for.

        :return: The maximal_billing_cycles of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._maximal_billing_cycles

    @maximal_billing_cycles.setter
    def maximal_billing_cycles(self, maximal_billing_cycles):
        """Sets the maximal_billing_cycles of this ShopifySubscriptionProduct.

            Define the maximum number of orders the subscription will run for.

        :param maximal_billing_cycles: The maximal_billing_cycles of this ShopifySubscriptionProduct.
        :type: int
        """

        self._maximal_billing_cycles = maximal_billing_cycles
    
    @property
    def maximal_suspendable_cycles(self):
        """Gets the maximal_suspendable_cycles of this ShopifySubscriptionProduct.

            Define the maximum number of orders the subscription can be suspended for at a time.

        :return: The maximal_suspendable_cycles of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._maximal_suspendable_cycles

    @maximal_suspendable_cycles.setter
    def maximal_suspendable_cycles(self, maximal_suspendable_cycles):
        """Sets the maximal_suspendable_cycles of this ShopifySubscriptionProduct.

            Define the maximum number of orders the subscription can be suspended for at a time.

        :param maximal_suspendable_cycles: The maximal_suspendable_cycles of this ShopifySubscriptionProduct.
        :type: int
        """

        self._maximal_suspendable_cycles = maximal_suspendable_cycles
    
    @property
    def minimal_billing_cycles(self):
        """Gets the minimal_billing_cycles of this ShopifySubscriptionProduct.

            Define the minimal number of orders the subscription will run for.

        :return: The minimal_billing_cycles of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._minimal_billing_cycles

    @minimal_billing_cycles.setter
    def minimal_billing_cycles(self, minimal_billing_cycles):
        """Sets the minimal_billing_cycles of this ShopifySubscriptionProduct.

            Define the minimal number of orders the subscription will run for.

        :param minimal_billing_cycles: The minimal_billing_cycles of this ShopifySubscriptionProduct.
        :type: int
        """

        self._minimal_billing_cycles = minimal_billing_cycles
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ShopifySubscriptionProduct.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ShopifySubscriptionProduct.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifySubscriptionProduct.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ShopifySubscriptionProduct.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def pricing_option(self):
        """Gets the pricing_option of this ShopifySubscriptionProduct.

            

        :return: The pricing_option of this ShopifySubscriptionProduct.
        :rtype: ShopifySubscriptionProductPricingOption
        """
        return self._pricing_option

    @pricing_option.setter
    def pricing_option(self, pricing_option):
        """Sets the pricing_option of this ShopifySubscriptionProduct.

            

        :param pricing_option: The pricing_option of this ShopifySubscriptionProduct.
        :type: ShopifySubscriptionProductPricingOption
        """

        self._pricing_option = pricing_option
    
    @property
    def product_id(self):
        """Gets the product_id of this ShopifySubscriptionProduct.

            The ID of the Shopify product that is enabled to be ordered as subscription.

        :return: The product_id of this ShopifySubscriptionProduct.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShopifySubscriptionProduct.

            The ID of the Shopify product that is enabled to be ordered as subscription.

        :param product_id: The product_id of this ShopifySubscriptionProduct.
        :type: str
        """

        self._product_id = product_id
    
    @property
    def product_name(self):
        """Gets the product_name of this ShopifySubscriptionProduct.

            

        :return: The product_name of this ShopifySubscriptionProduct.
        :rtype: str
        """
        return self._product_name

    @product_name.setter
    def product_name(self, product_name):
        """Sets the product_name of this ShopifySubscriptionProduct.

            

        :param product_name: The product_name of this ShopifySubscriptionProduct.
        :type: str
        """

        self._product_name = product_name
    
    @property
    def product_price(self):
        """Gets the product_price of this ShopifySubscriptionProduct.

            

        :return: The product_price of this ShopifySubscriptionProduct.
        :rtype: float
        """
        return self._product_price

    @product_price.setter
    def product_price(self, product_price):
        """Sets the product_price of this ShopifySubscriptionProduct.

            

        :param product_price: The product_price of this ShopifySubscriptionProduct.
        :type: float
        """

        self._product_price = product_price
    
    @property
    def product_sku(self):
        """Gets the product_sku of this ShopifySubscriptionProduct.

            

        :return: The product_sku of this ShopifySubscriptionProduct.
        :rtype: str
        """
        return self._product_sku

    @product_sku.setter
    def product_sku(self, product_sku):
        """Sets the product_sku of this ShopifySubscriptionProduct.

            

        :param product_sku: The product_sku of this ShopifySubscriptionProduct.
        :type: str
        """

        self._product_sku = product_sku
    
    @property
    def product_variant_id(self):
        """Gets the product_variant_id of this ShopifySubscriptionProduct.

            

        :return: The product_variant_id of this ShopifySubscriptionProduct.
        :rtype: str
        """
        return self._product_variant_id

    @product_variant_id.setter
    def product_variant_id(self, product_variant_id):
        """Sets the product_variant_id of this ShopifySubscriptionProduct.

            

        :param product_variant_id: The product_variant_id of this ShopifySubscriptionProduct.
        :type: str
        """

        self._product_variant_id = product_variant_id
    
    @property
    def product_variant_name(self):
        """Gets the product_variant_name of this ShopifySubscriptionProduct.

            

        :return: The product_variant_name of this ShopifySubscriptionProduct.
        :rtype: str
        """
        return self._product_variant_name

    @product_variant_name.setter
    def product_variant_name(self, product_variant_name):
        """Sets the product_variant_name of this ShopifySubscriptionProduct.

            

        :param product_variant_name: The product_variant_name of this ShopifySubscriptionProduct.
        :type: str
        """

        self._product_variant_name = product_variant_name
    
    @property
    def relative_price_adjustment(self):
        """Gets the relative_price_adjustment of this ShopifySubscriptionProduct.

            

        :return: The relative_price_adjustment of this ShopifySubscriptionProduct.
        :rtype: float
        """
        return self._relative_price_adjustment

    @relative_price_adjustment.setter
    def relative_price_adjustment(self, relative_price_adjustment):
        """Sets the relative_price_adjustment of this ShopifySubscriptionProduct.

            

        :param relative_price_adjustment: The relative_price_adjustment of this ShopifySubscriptionProduct.
        :type: float
        """

        self._relative_price_adjustment = relative_price_adjustment
    
    @property
    def shipping_required(self):
        """Gets the shipping_required of this ShopifySubscriptionProduct.

            

        :return: The shipping_required of this ShopifySubscriptionProduct.
        :rtype: bool
        """
        return self._shipping_required

    @shipping_required.setter
    def shipping_required(self, shipping_required):
        """Sets the shipping_required of this ShopifySubscriptionProduct.

            

        :param shipping_required: The shipping_required of this ShopifySubscriptionProduct.
        :type: bool
        """

        self._shipping_required = shipping_required
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscriptionProduct.

            

        :return: The shop of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscriptionProduct.

            

        :param shop: The shop of this ShopifySubscriptionProduct.
        :type: int
        """

        self._shop = shop
    
    @property
    def state(self):
        """Gets the state of this ShopifySubscriptionProduct.

            

        :return: The state of this ShopifySubscriptionProduct.
        :rtype: ShopifySubscriptionProductState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifySubscriptionProduct.

            

        :param state: The state of this ShopifySubscriptionProduct.
        :type: ShopifySubscriptionProductState
        """

        self._state = state
    
    @property
    def stock_check_required(self):
        """Gets the stock_check_required of this ShopifySubscriptionProduct.

            

        :return: The stock_check_required of this ShopifySubscriptionProduct.
        :rtype: bool
        """
        return self._stock_check_required

    @stock_check_required.setter
    def stock_check_required(self, stock_check_required):
        """Sets the stock_check_required of this ShopifySubscriptionProduct.

            

        :param stock_check_required: The stock_check_required of this ShopifySubscriptionProduct.
        :type: bool
        """

        self._stock_check_required = stock_check_required
    
    @property
    def store_order_confirmation_email_enabled(self):
        """Gets the store_order_confirmation_email_enabled of this ShopifySubscriptionProduct.

            Define whether the order confirmation email of the Shopify shop is sent to the customer for recurring orders.

        :return: The store_order_confirmation_email_enabled of this ShopifySubscriptionProduct.
        :rtype: bool
        """
        return self._store_order_confirmation_email_enabled

    @store_order_confirmation_email_enabled.setter
    def store_order_confirmation_email_enabled(self, store_order_confirmation_email_enabled):
        """Sets the store_order_confirmation_email_enabled of this ShopifySubscriptionProduct.

            Define whether the order confirmation email of the Shopify shop is sent to the customer for recurring orders.

        :param store_order_confirmation_email_enabled: The store_order_confirmation_email_enabled of this ShopifySubscriptionProduct.
        :type: bool
        """

        self._store_order_confirmation_email_enabled = store_order_confirmation_email_enabled
    
    @property
    def subscriber_suspension_allowed(self):
        """Gets the subscriber_suspension_allowed of this ShopifySubscriptionProduct.

            Define whether the customer is allowed to suspend subscriptions.

        :return: The subscriber_suspension_allowed of this ShopifySubscriptionProduct.
        :rtype: bool
        """
        return self._subscriber_suspension_allowed

    @subscriber_suspension_allowed.setter
    def subscriber_suspension_allowed(self, subscriber_suspension_allowed):
        """Sets the subscriber_suspension_allowed of this ShopifySubscriptionProduct.

            Define whether the customer is allowed to suspend subscriptions.

        :param subscriber_suspension_allowed: The subscriber_suspension_allowed of this ShopifySubscriptionProduct.
        :type: bool
        """

        self._subscriber_suspension_allowed = subscriber_suspension_allowed
    
    @property
    def termination_billing_cycles(self):
        """Gets the termination_billing_cycles of this ShopifySubscriptionProduct.

            Define the number of orders the subscription will keep running for after its termination has been requested.

        :return: The termination_billing_cycles of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._termination_billing_cycles

    @termination_billing_cycles.setter
    def termination_billing_cycles(self, termination_billing_cycles):
        """Sets the termination_billing_cycles of this ShopifySubscriptionProduct.

            Define the number of orders the subscription will keep running for after its termination has been requested.

        :param termination_billing_cycles: The termination_billing_cycles of this ShopifySubscriptionProduct.
        :type: int
        """

        self._termination_billing_cycles = termination_billing_cycles
    
    @property
    def updated_at(self):
        """Gets the updated_at of this ShopifySubscriptionProduct.

            

        :return: The updated_at of this ShopifySubscriptionProduct.
        :rtype: datetime
        """
        return self._updated_at

    @updated_at.setter
    def updated_at(self, updated_at):
        """Sets the updated_at of this ShopifySubscriptionProduct.

            

        :param updated_at: The updated_at of this ShopifySubscriptionProduct.
        :type: datetime
        """

        self._updated_at = updated_at
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscriptionProduct.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscriptionProduct.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscriptionProduct.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscriptionProduct.
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
        if issubclass(ShopifySubscriptionProduct, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
