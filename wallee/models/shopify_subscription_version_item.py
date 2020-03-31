# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionVersionItem:

    swagger_types = {
    
        'price_including_tax': 'float',
        'price_strategy': 'ShopifySubscriptionVersionItemPriceStrategy',
        'product': 'int',
        'quantity': 'float',
        'tax_lines': 'list[ShopifyTaxLine]',
    }

    attribute_map = {
        'price_including_tax': 'priceIncludingTax','price_strategy': 'priceStrategy','product': 'product','quantity': 'quantity','tax_lines': 'taxLines',
    }

    
    _price_including_tax = None
    _price_strategy = None
    _product = None
    _quantity = None
    _tax_lines = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.price_including_tax = kwargs.get('price_including_tax', None)
        self.price_strategy = kwargs.get('price_strategy', None)
        self.product = kwargs.get('product', None)
        self.quantity = kwargs.get('quantity', None)
        self.tax_lines = kwargs.get('tax_lines', None)
        

    
    @property
    def price_including_tax(self):
        """Gets the price_including_tax of this ShopifySubscriptionVersionItem.

            

        :return: The price_including_tax of this ShopifySubscriptionVersionItem.
        :rtype: float
        """
        return self._price_including_tax

    @price_including_tax.setter
    def price_including_tax(self, price_including_tax):
        """Sets the price_including_tax of this ShopifySubscriptionVersionItem.

            

        :param price_including_tax: The price_including_tax of this ShopifySubscriptionVersionItem.
        :type: float
        """

        self._price_including_tax = price_including_tax
    
    @property
    def price_strategy(self):
        """Gets the price_strategy of this ShopifySubscriptionVersionItem.

            

        :return: The price_strategy of this ShopifySubscriptionVersionItem.
        :rtype: ShopifySubscriptionVersionItemPriceStrategy
        """
        return self._price_strategy

    @price_strategy.setter
    def price_strategy(self, price_strategy):
        """Sets the price_strategy of this ShopifySubscriptionVersionItem.

            

        :param price_strategy: The price_strategy of this ShopifySubscriptionVersionItem.
        :type: ShopifySubscriptionVersionItemPriceStrategy
        """

        self._price_strategy = price_strategy
    
    @property
    def product(self):
        """Gets the product of this ShopifySubscriptionVersionItem.

            

        :return: The product of this ShopifySubscriptionVersionItem.
        :rtype: int
        """
        return self._product

    @product.setter
    def product(self, product):
        """Sets the product of this ShopifySubscriptionVersionItem.

            

        :param product: The product of this ShopifySubscriptionVersionItem.
        :type: int
        """

        self._product = product
    
    @property
    def quantity(self):
        """Gets the quantity of this ShopifySubscriptionVersionItem.

            

        :return: The quantity of this ShopifySubscriptionVersionItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ShopifySubscriptionVersionItem.

            

        :param quantity: The quantity of this ShopifySubscriptionVersionItem.
        :type: float
        """

        self._quantity = quantity
    
    @property
    def tax_lines(self):
        """Gets the tax_lines of this ShopifySubscriptionVersionItem.

            

        :return: The tax_lines of this ShopifySubscriptionVersionItem.
        :rtype: list[ShopifyTaxLine]
        """
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        """Sets the tax_lines of this ShopifySubscriptionVersionItem.

            

        :param tax_lines: The tax_lines of this ShopifySubscriptionVersionItem.
        :type: list[ShopifyTaxLine]
        """

        self._tax_lines = tax_lines
    

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
        if issubclass(ShopifySubscriptionVersionItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionVersionItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
