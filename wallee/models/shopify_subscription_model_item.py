# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionModelItem:

    swagger_types = {
    
        'price_including_tax': 'float',
        'product_id': 'int',
        'quantity': 'float',
        'recalculate_price': 'bool',
        'tax_lines': 'list[ShopifySubscriptionModelTaxLine]',
    }

    attribute_map = {
        'price_including_tax': 'priceIncludingTax','product_id': 'productId','quantity': 'quantity','recalculate_price': 'recalculatePrice','tax_lines': 'taxLines',
    }

    
    _price_including_tax = None
    _product_id = None
    _quantity = None
    _recalculate_price = None
    _tax_lines = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.price_including_tax = kwargs.get('price_including_tax', None)
        self.product_id = kwargs.get('product_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.recalculate_price = kwargs.get('recalculate_price', None)
        self.tax_lines = kwargs.get('tax_lines', None)
        

    
    @property
    def price_including_tax(self):
        """Gets the price_including_tax of this ShopifySubscriptionModelItem.

            

        :return: The price_including_tax of this ShopifySubscriptionModelItem.
        :rtype: float
        """
        return self._price_including_tax

    @price_including_tax.setter
    def price_including_tax(self, price_including_tax):
        """Sets the price_including_tax of this ShopifySubscriptionModelItem.

            

        :param price_including_tax: The price_including_tax of this ShopifySubscriptionModelItem.
        :type: float
        """

        self._price_including_tax = price_including_tax
    
    @property
    def product_id(self):
        """Gets the product_id of this ShopifySubscriptionModelItem.

            

        :return: The product_id of this ShopifySubscriptionModelItem.
        :rtype: int
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShopifySubscriptionModelItem.

            

        :param product_id: The product_id of this ShopifySubscriptionModelItem.
        :type: int
        """

        self._product_id = product_id
    
    @property
    def quantity(self):
        """Gets the quantity of this ShopifySubscriptionModelItem.

            

        :return: The quantity of this ShopifySubscriptionModelItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this ShopifySubscriptionModelItem.

            

        :param quantity: The quantity of this ShopifySubscriptionModelItem.
        :type: float
        """

        self._quantity = quantity
    
    @property
    def recalculate_price(self):
        """Gets the recalculate_price of this ShopifySubscriptionModelItem.

            

        :return: The recalculate_price of this ShopifySubscriptionModelItem.
        :rtype: bool
        """
        return self._recalculate_price

    @recalculate_price.setter
    def recalculate_price(self, recalculate_price):
        """Sets the recalculate_price of this ShopifySubscriptionModelItem.

            

        :param recalculate_price: The recalculate_price of this ShopifySubscriptionModelItem.
        :type: bool
        """

        self._recalculate_price = recalculate_price
    
    @property
    def tax_lines(self):
        """Gets the tax_lines of this ShopifySubscriptionModelItem.

            

        :return: The tax_lines of this ShopifySubscriptionModelItem.
        :rtype: list[ShopifySubscriptionModelTaxLine]
        """
        return self._tax_lines

    @tax_lines.setter
    def tax_lines(self, tax_lines):
        """Sets the tax_lines of this ShopifySubscriptionModelItem.

            

        :param tax_lines: The tax_lines of this ShopifySubscriptionModelItem.
        :type: list[ShopifySubscriptionModelTaxLine]
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
        if issubclass(ShopifySubscriptionModelItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionModelItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
