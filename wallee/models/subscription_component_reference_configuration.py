# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionComponentReferenceConfiguration:

    swagger_types = {
    
        'product_component_reference_id': 'int',
        'quantity': 'float',
    }

    attribute_map = {
        'product_component_reference_id': 'productComponentReferenceId','quantity': 'quantity',
    }

    
    _product_component_reference_id = None
    _quantity = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.product_component_reference_id = kwargs.get('product_component_reference_id', None)
        self.quantity = kwargs.get('quantity', None)
        

    
    @property
    def product_component_reference_id(self):
        """Gets the product_component_reference_id of this SubscriptionComponentReferenceConfiguration.

            

        :return: The product_component_reference_id of this SubscriptionComponentReferenceConfiguration.
        :rtype: int
        """
        return self._product_component_reference_id

    @product_component_reference_id.setter
    def product_component_reference_id(self, product_component_reference_id):
        """Sets the product_component_reference_id of this SubscriptionComponentReferenceConfiguration.

            

        :param product_component_reference_id: The product_component_reference_id of this SubscriptionComponentReferenceConfiguration.
        :type: int
        """

        self._product_component_reference_id = product_component_reference_id
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionComponentReferenceConfiguration.

            

        :return: The quantity of this SubscriptionComponentReferenceConfiguration.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionComponentReferenceConfiguration.

            

        :param quantity: The quantity of this SubscriptionComponentReferenceConfiguration.
        :type: float
        """

        self._quantity = quantity
    

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
        if issubclass(SubscriptionComponentReferenceConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionComponentReferenceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
