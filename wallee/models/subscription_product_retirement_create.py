# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductRetirementCreate:

    swagger_types = {
    
        'product': 'int',
        'respect_termination_periods': 'bool',
        'target_product': 'int',
    }

    attribute_map = {
        'product': 'product','respect_termination_periods': 'respectTerminationPeriods','target_product': 'targetProduct',
    }

    
    _product = None
    _respect_termination_periods = None
    _target_product = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.product = kwargs.get('product')

        self.respect_termination_periods = kwargs.get('respect_termination_periods', None)
        self.target_product = kwargs.get('target_product', None)
        

    
    @property
    def product(self):
        """Gets the product of this SubscriptionProductRetirementCreate.

            The product that is to be retired.

        :return: The product of this SubscriptionProductRetirementCreate.
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this SubscriptionProductRetirementCreate.

            The product that is to be retired.

        :param product: The product of this SubscriptionProductRetirementCreate.
        :type: int
        """
        if product is None:
            raise ValueError("Invalid value for `product`, must not be `None`")

        self._product = product
    
    @property
    def respect_termination_periods(self):
        """Gets the respect_termination_periods of this SubscriptionProductRetirementCreate.

            Whether the subscriptions' termination periods should be respected.

        :return: The respect_termination_periods of this SubscriptionProductRetirementCreate.
        :rtype: bool
        """
        return self._respect_termination_periods

    @respect_termination_periods.setter
    def respect_termination_periods(self, respect_termination_periods):
        """Sets the respect_termination_periods of this SubscriptionProductRetirementCreate.

            Whether the subscriptions' termination periods should be respected.

        :param respect_termination_periods: The respect_termination_periods of this SubscriptionProductRetirementCreate.
        :type: bool
        """

        self._respect_termination_periods = respect_termination_periods
    
    @property
    def target_product(self):
        """Gets the target_product of this SubscriptionProductRetirementCreate.

            The product to which the subscriptions with the retiring product are to be migrated. If none is defined, the subscriptions are terminated.

        :return: The target_product of this SubscriptionProductRetirementCreate.
        :rtype: int
        """
        return self._target_product

    @target_product.setter
    def target_product(self, target_product):
        """Sets the target_product of this SubscriptionProductRetirementCreate.

            The product to which the subscriptions with the retiring product are to be migrated. If none is defined, the subscriptions are terminated.

        :param target_product: The target_product of this SubscriptionProductRetirementCreate.
        :type: int
        """

        self._target_product = target_product
    

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
        if issubclass(SubscriptionProductRetirementCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductRetirementCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
