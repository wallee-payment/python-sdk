# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductVersionRetirementCreate:

    swagger_types = {
    
        'product_version': 'int',
        'respect_terminiation_periods_enabled': 'bool',
        'target_product': 'int',
    }

    attribute_map = {
        'product_version': 'productVersion','respect_terminiation_periods_enabled': 'respectTerminiationPeriodsEnabled','target_product': 'targetProduct',
    }

    
    _product_version = None
    _respect_terminiation_periods_enabled = None
    _target_product = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.product_version = kwargs.get('product_version')

        self.respect_terminiation_periods_enabled = kwargs.get('respect_terminiation_periods_enabled', None)
        self.target_product = kwargs.get('target_product', None)
        

    
    @property
    def product_version(self):
        """Gets the product_version of this SubscriptionProductVersionRetirementCreate.

            

        :return: The product_version of this SubscriptionProductVersionRetirementCreate.
        :rtype: int
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this SubscriptionProductVersionRetirementCreate.

            

        :param product_version: The product_version of this SubscriptionProductVersionRetirementCreate.
        :type: int
        """
        if product_version is None:
            raise ValueError("Invalid value for `product_version`, must not be `None`")

        self._product_version = product_version
    
    @property
    def respect_terminiation_periods_enabled(self):
        """Gets the respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirementCreate.

            

        :return: The respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirementCreate.
        :rtype: bool
        """
        return self._respect_terminiation_periods_enabled

    @respect_terminiation_periods_enabled.setter
    def respect_terminiation_periods_enabled(self, respect_terminiation_periods_enabled):
        """Sets the respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirementCreate.

            

        :param respect_terminiation_periods_enabled: The respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirementCreate.
        :type: bool
        """

        self._respect_terminiation_periods_enabled = respect_terminiation_periods_enabled
    
    @property
    def target_product(self):
        """Gets the target_product of this SubscriptionProductVersionRetirementCreate.

            When a target product is not chosen, all customers with the retired product will be terminated.

        :return: The target_product of this SubscriptionProductVersionRetirementCreate.
        :rtype: int
        """
        return self._target_product

    @target_product.setter
    def target_product(self, target_product):
        """Sets the target_product of this SubscriptionProductVersionRetirementCreate.

            When a target product is not chosen, all customers with the retired product will be terminated.

        :param target_product: The target_product of this SubscriptionProductVersionRetirementCreate.
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
        if issubclass(SubscriptionProductVersionRetirementCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductVersionRetirementCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
