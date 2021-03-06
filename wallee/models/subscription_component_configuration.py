# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionComponentConfiguration:

    swagger_types = {
    
        'component': 'int',
        'quantity': 'float',
    }

    attribute_map = {
        'component': 'component','quantity': 'quantity',
    }

    
    _component = None
    _quantity = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component = kwargs.get('component', None)
        self.quantity = kwargs.get('quantity', None)
        

    
    @property
    def component(self):
        """Gets the component of this SubscriptionComponentConfiguration.

            

        :return: The component of this SubscriptionComponentConfiguration.
        :rtype: int
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this SubscriptionComponentConfiguration.

            

        :param component: The component of this SubscriptionComponentConfiguration.
        :type: int
        """

        self._component = component
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionComponentConfiguration.

            

        :return: The quantity of this SubscriptionComponentConfiguration.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionComponentConfiguration.

            

        :param quantity: The quantity of this SubscriptionComponentConfiguration.
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
        if issubclass(SubscriptionComponentConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionComponentConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
