# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractSubscriptionProductActive:

    swagger_types = {
    
        'allowed_payment_method_configurations': 'list[int]',
        'failed_payment_suspension_period': 'str',
        'name': 'str',
        'product_locked': 'bool',
        'sort_order': 'int',
        'state': 'SubscriptionProductState',
    }

    attribute_map = {
        'allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','failed_payment_suspension_period': 'failedPaymentSuspensionPeriod','name': 'name','product_locked': 'productLocked','sort_order': 'sortOrder','state': 'state',
    }

    
    _allowed_payment_method_configurations = None
    _failed_payment_suspension_period = None
    _name = None
    _product_locked = None
    _sort_order = None
    _state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.failed_payment_suspension_period = kwargs.get('failed_payment_suspension_period', None)
        self.name = kwargs.get('name', None)
        self.product_locked = kwargs.get('product_locked', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.state = kwargs.get('state', None)
        

    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this AbstractSubscriptionProductActive.

            The payment methods that can be used to subscribe to this product. If none are selected, no restriction is applied.

        :return: The allowed_payment_method_configurations of this AbstractSubscriptionProductActive.
        :rtype: list[int]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this AbstractSubscriptionProductActive.

            The payment methods that can be used to subscribe to this product. If none are selected, no restriction is applied.

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this AbstractSubscriptionProductActive.
        :type: list[int]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def failed_payment_suspension_period(self):
        """Gets the failed_payment_suspension_period of this AbstractSubscriptionProductActive.

            The period after which a subscription that has been suspended due to a failed payment is terminated.

        :return: The failed_payment_suspension_period of this AbstractSubscriptionProductActive.
        :rtype: str
        """
        return self._failed_payment_suspension_period

    @failed_payment_suspension_period.setter
    def failed_payment_suspension_period(self, failed_payment_suspension_period):
        """Sets the failed_payment_suspension_period of this AbstractSubscriptionProductActive.

            The period after which a subscription that has been suspended due to a failed payment is terminated.

        :param failed_payment_suspension_period: The failed_payment_suspension_period of this AbstractSubscriptionProductActive.
        :type: str
        """

        self._failed_payment_suspension_period = failed_payment_suspension_period
    
    @property
    def name(self):
        """Gets the name of this AbstractSubscriptionProductActive.

            The name used to identify the product.

        :return: The name of this AbstractSubscriptionProductActive.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractSubscriptionProductActive.

            The name used to identify the product.

        :param name: The name of this AbstractSubscriptionProductActive.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def product_locked(self):
        """Gets the product_locked of this AbstractSubscriptionProductActive.

            Whether subscriptions can be switched to or from this product, or whether they are locked in.

        :return: The product_locked of this AbstractSubscriptionProductActive.
        :rtype: bool
        """
        return self._product_locked

    @product_locked.setter
    def product_locked(self, product_locked):
        """Sets the product_locked of this AbstractSubscriptionProductActive.

            Whether subscriptions can be switched to or from this product, or whether they are locked in.

        :param product_locked: The product_locked of this AbstractSubscriptionProductActive.
        :type: bool
        """

        self._product_locked = product_locked
    
    @property
    def sort_order(self):
        """Gets the sort_order of this AbstractSubscriptionProductActive.

            When listing products, they can be sorted by this number.

        :return: The sort_order of this AbstractSubscriptionProductActive.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this AbstractSubscriptionProductActive.

            When listing products, they can be sorted by this number.

        :param sort_order: The sort_order of this AbstractSubscriptionProductActive.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def state(self):
        """Gets the state of this AbstractSubscriptionProductActive.

            The object's current state.

        :return: The state of this AbstractSubscriptionProductActive.
        :rtype: SubscriptionProductState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this AbstractSubscriptionProductActive.

            The object's current state.

        :param state: The state of this AbstractSubscriptionProductActive.
        :type: SubscriptionProductState
        """

        self._state = state
    

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
        if issubclass(AbstractSubscriptionProductActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractSubscriptionProductActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
