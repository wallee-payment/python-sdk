# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionChangeRequest:

    swagger_types = {
    
        'component_configurations': 'list[SubscriptionComponentReferenceConfiguration]',
        'currency': 'str',
        'product': 'int',
        'respect_termination_period': 'bool',
        'selected_components': 'list[SubscriptionProductComponentReference]',
        'subscription': 'int',
    }

    attribute_map = {
        'component_configurations': 'componentConfigurations','currency': 'currency','product': 'product','respect_termination_period': 'respectTerminationPeriod','selected_components': 'selectedComponents','subscription': 'subscription',
    }

    
    _component_configurations = None
    _currency = None
    _product = None
    _respect_termination_period = None
    _selected_components = None
    _subscription = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component_configurations = kwargs.get('component_configurations', None)
        self.currency = kwargs.get('currency')

        self.product = kwargs.get('product')

        self.respect_termination_period = kwargs.get('respect_termination_period', None)
        self.selected_components = kwargs.get('selected_components', None)
        self.subscription = kwargs.get('subscription')

        

    
    @property
    def component_configurations(self):
        """Gets the component_configurations of this SubscriptionChangeRequest.

            

        :return: The component_configurations of this SubscriptionChangeRequest.
        :rtype: list[SubscriptionComponentReferenceConfiguration]
        """
        return self._component_configurations

    @component_configurations.setter
    def component_configurations(self, component_configurations):
        """Sets the component_configurations of this SubscriptionChangeRequest.

            

        :param component_configurations: The component_configurations of this SubscriptionChangeRequest.
        :type: list[SubscriptionComponentReferenceConfiguration]
        """

        self._component_configurations = component_configurations
    
    @property
    def currency(self):
        """Gets the currency of this SubscriptionChangeRequest.

            

        :return: The currency of this SubscriptionChangeRequest.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this SubscriptionChangeRequest.

            

        :param currency: The currency of this SubscriptionChangeRequest.
        :type: str
        """
        if currency is None:
            raise ValueError("Invalid value for `currency`, must not be `None`")

        self._currency = currency
    
    @property
    def product(self):
        """Gets the product of this SubscriptionChangeRequest.

            The subscription has to be linked with a product.

        :return: The product of this SubscriptionChangeRequest.
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionChangeRequest.

            The subscription has to be linked with a product.

        :param product: The product of this SubscriptionChangeRequest.
        :type: int
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")

        self._product = product
    
    @property
    def respect_termination_period(self):
        """Gets the respect_termination_period of this SubscriptionChangeRequest.

            The subscription version may be retired. The respect termination period controls whether the termination period configured on the product version should be respected or if the operation should take effect immediately.

        :return: The respect_termination_period of this SubscriptionChangeRequest.
        :rtype: bool
        """
        return self._respect_termination_period

    @respect_termination_period.setter
    def respect_termination_period(self, respect_termination_period):
        """Sets the respect_termination_period of this SubscriptionChangeRequest.

            The subscription version may be retired. The respect termination period controls whether the termination period configured on the product version should be respected or if the operation should take effect immediately.

        :param respect_termination_period: The respect_termination_period of this SubscriptionChangeRequest.
        :type: bool
        """

        self._respect_termination_period = respect_termination_period
    
    @property
    def selected_components(self):
        """Gets the selected_components of this SubscriptionChangeRequest.

            

        :return: The selected_components of this SubscriptionChangeRequest.
        :rtype: list[SubscriptionProductComponentReference]
        """
        return self._selected_components

    @selected_components.setter
    def selected_components(self, selected_components):
        """Sets the selected_components of this SubscriptionChangeRequest.

            

        :param selected_components: The selected_components of this SubscriptionChangeRequest.
        :type: list[SubscriptionProductComponentReference]
        """

        self._selected_components = selected_components
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionChangeRequest.

            

        :return: The subscription of this SubscriptionChangeRequest.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionChangeRequest.

            

        :param subscription: The subscription of this SubscriptionChangeRequest.
        :type: int
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription
    

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
        if issubclass(SubscriptionChangeRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionChangeRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
