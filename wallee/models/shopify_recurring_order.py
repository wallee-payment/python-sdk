# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ShopifyRecurringOrder(TransactionAwareEntity):

    swagger_types = {
    
        'billed_on': 'datetime',
        'checkout_token': 'str',
        'created_on': 'datetime',
        'failure_reason': 'FailureReason',
        'order_id': 'str',
        'order_name': 'str',
        'planned_execution_date': 'datetime',
        'planned_purge_date': 'datetime',
        'recurrence_number': 'int',
        'shop': 'int',
        'started_processing_on': 'datetime',
        'state': 'ShopifyRecurringOrderState',
        'subscription_version': 'ShopifySubscriptionVersion',
        'transaction': 'ShopifyTransaction',
    }

    attribute_map = {
        'billed_on': 'billedOn','checkout_token': 'checkoutToken','created_on': 'createdOn','failure_reason': 'failureReason','order_id': 'orderId','order_name': 'orderName','planned_execution_date': 'plannedExecutionDate','planned_purge_date': 'plannedPurgeDate','recurrence_number': 'recurrenceNumber','shop': 'shop','started_processing_on': 'startedProcessingOn','state': 'state','subscription_version': 'subscriptionVersion','transaction': 'transaction',
    }

    
    _billed_on = None
    _checkout_token = None
    _created_on = None
    _failure_reason = None
    _order_id = None
    _order_name = None
    _planned_execution_date = None
    _planned_purge_date = None
    _recurrence_number = None
    _shop = None
    _started_processing_on = None
    _state = None
    _subscription_version = None
    _transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billed_on = kwargs.get('billed_on', None)
        self.checkout_token = kwargs.get('checkout_token', None)
        self.created_on = kwargs.get('created_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.order_id = kwargs.get('order_id', None)
        self.order_name = kwargs.get('order_name', None)
        self.planned_execution_date = kwargs.get('planned_execution_date', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.recurrence_number = kwargs.get('recurrence_number', None)
        self.shop = kwargs.get('shop', None)
        self.started_processing_on = kwargs.get('started_processing_on', None)
        self.state = kwargs.get('state', None)
        self.subscription_version = kwargs.get('subscription_version', None)
        self.transaction = kwargs.get('transaction', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def billed_on(self):
        """Gets the billed_on of this ShopifyRecurringOrder.

            

        :return: The billed_on of this ShopifyRecurringOrder.
        :rtype: datetime
        """
        return self._billed_on

    @billed_on.setter
    def billed_on(self, billed_on):
        """Sets the billed_on of this ShopifyRecurringOrder.

            

        :param billed_on: The billed_on of this ShopifyRecurringOrder.
        :type: datetime
        """

        self._billed_on = billed_on
    
    @property
    def checkout_token(self):
        """Gets the checkout_token of this ShopifyRecurringOrder.

            

        :return: The checkout_token of this ShopifyRecurringOrder.
        :rtype: str
        """
        return self._checkout_token

    @checkout_token.setter
    def checkout_token(self, checkout_token):
        """Sets the checkout_token of this ShopifyRecurringOrder.

            

        :param checkout_token: The checkout_token of this ShopifyRecurringOrder.
        :type: str
        """

        self._checkout_token = checkout_token
    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifyRecurringOrder.

            

        :return: The created_on of this ShopifyRecurringOrder.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifyRecurringOrder.

            

        :param created_on: The created_on of this ShopifyRecurringOrder.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this ShopifyRecurringOrder.

            

        :return: The failure_reason of this ShopifyRecurringOrder.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this ShopifyRecurringOrder.

            

        :param failure_reason: The failure_reason of this ShopifyRecurringOrder.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def order_id(self):
        """Gets the order_id of this ShopifyRecurringOrder.

            

        :return: The order_id of this ShopifyRecurringOrder.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShopifyRecurringOrder.

            

        :param order_id: The order_id of this ShopifyRecurringOrder.
        :type: str
        """

        self._order_id = order_id
    
    @property
    def order_name(self):
        """Gets the order_name of this ShopifyRecurringOrder.

            

        :return: The order_name of this ShopifyRecurringOrder.
        :rtype: str
        """
        return self._order_name

    @order_name.setter
    def order_name(self, order_name):
        """Sets the order_name of this ShopifyRecurringOrder.

            

        :param order_name: The order_name of this ShopifyRecurringOrder.
        :type: str
        """

        self._order_name = order_name
    
    @property
    def planned_execution_date(self):
        """Gets the planned_execution_date of this ShopifyRecurringOrder.

            

        :return: The planned_execution_date of this ShopifyRecurringOrder.
        :rtype: datetime
        """
        return self._planned_execution_date

    @planned_execution_date.setter
    def planned_execution_date(self, planned_execution_date):
        """Sets the planned_execution_date of this ShopifyRecurringOrder.

            

        :param planned_execution_date: The planned_execution_date of this ShopifyRecurringOrder.
        :type: datetime
        """

        self._planned_execution_date = planned_execution_date
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ShopifyRecurringOrder.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ShopifyRecurringOrder.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifyRecurringOrder.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ShopifyRecurringOrder.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def recurrence_number(self):
        """Gets the recurrence_number of this ShopifyRecurringOrder.

            

        :return: The recurrence_number of this ShopifyRecurringOrder.
        :rtype: int
        """
        return self._recurrence_number

    @recurrence_number.setter
    def recurrence_number(self, recurrence_number):
        """Sets the recurrence_number of this ShopifyRecurringOrder.

            

        :param recurrence_number: The recurrence_number of this ShopifyRecurringOrder.
        :type: int
        """

        self._recurrence_number = recurrence_number
    
    @property
    def shop(self):
        """Gets the shop of this ShopifyRecurringOrder.

            

        :return: The shop of this ShopifyRecurringOrder.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifyRecurringOrder.

            

        :param shop: The shop of this ShopifyRecurringOrder.
        :type: int
        """

        self._shop = shop
    
    @property
    def started_processing_on(self):
        """Gets the started_processing_on of this ShopifyRecurringOrder.

            

        :return: The started_processing_on of this ShopifyRecurringOrder.
        :rtype: datetime
        """
        return self._started_processing_on

    @started_processing_on.setter
    def started_processing_on(self, started_processing_on):
        """Sets the started_processing_on of this ShopifyRecurringOrder.

            

        :param started_processing_on: The started_processing_on of this ShopifyRecurringOrder.
        :type: datetime
        """

        self._started_processing_on = started_processing_on
    
    @property
    def state(self):
        """Gets the state of this ShopifyRecurringOrder.

            

        :return: The state of this ShopifyRecurringOrder.
        :rtype: ShopifyRecurringOrderState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifyRecurringOrder.

            

        :param state: The state of this ShopifyRecurringOrder.
        :type: ShopifyRecurringOrderState
        """

        self._state = state
    
    @property
    def subscription_version(self):
        """Gets the subscription_version of this ShopifyRecurringOrder.

            

        :return: The subscription_version of this ShopifyRecurringOrder.
        :rtype: ShopifySubscriptionVersion
        """
        return self._subscription_version

    @subscription_version.setter
    def subscription_version(self, subscription_version):
        """Sets the subscription_version of this ShopifyRecurringOrder.

            

        :param subscription_version: The subscription_version of this ShopifyRecurringOrder.
        :type: ShopifySubscriptionVersion
        """

        self._subscription_version = subscription_version
    
    @property
    def transaction(self):
        """Gets the transaction of this ShopifyRecurringOrder.

            

        :return: The transaction of this ShopifyRecurringOrder.
        :rtype: ShopifyTransaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ShopifyRecurringOrder.

            

        :param transaction: The transaction of this ShopifyRecurringOrder.
        :type: ShopifyTransaction
        """

        self._transaction = transaction
    

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
        if issubclass(ShopifyRecurringOrder, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifyRecurringOrder):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
