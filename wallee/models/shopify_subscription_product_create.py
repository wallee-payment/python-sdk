# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractShopifySubscriptionProductUpdate


class ShopifySubscriptionProductCreate(AbstractShopifySubscriptionProductUpdate):

    swagger_types = {
    
        'product_id': 'str',
        'product_variant_id': 'str',
        'shop': 'int',
    }

    attribute_map = {
        'product_id': 'productId','product_variant_id': 'productVariantId','shop': 'shop',
    }

    
    _product_id = None
    _product_variant_id = None
    _shop = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.product_id = kwargs.get('product_id')

        self.product_variant_id = kwargs.get('product_variant_id')

        self.shop = kwargs.get('shop')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def product_id(self):
        """Gets the product_id of this ShopifySubscriptionProductCreate.

            The ID of the Shopify product that is enabled to be ordered as subscription.

        :return: The product_id of this ShopifySubscriptionProductCreate.
        :rtype: str
        """
        return self._product_id

    @product_id.setter
    def product_id(self, product_id):
        """Sets the product_id of this ShopifySubscriptionProductCreate.

            The ID of the Shopify product that is enabled to be ordered as subscription.

        :param product_id: The product_id of this ShopifySubscriptionProductCreate.
        :type: str
        """
        if product_id is None:
            raise ValueError("Invalid value for `product_id`, must not be `None`")

        self._product_id = product_id
    
    @property
    def product_variant_id(self):
        """Gets the product_variant_id of this ShopifySubscriptionProductCreate.

            

        :return: The product_variant_id of this ShopifySubscriptionProductCreate.
        :rtype: str
        """
        return self._product_variant_id

    @product_variant_id.setter
    def product_variant_id(self, product_variant_id):
        """Sets the product_variant_id of this ShopifySubscriptionProductCreate.

            

        :param product_variant_id: The product_variant_id of this ShopifySubscriptionProductCreate.
        :type: str
        """
        if product_variant_id is None:
            raise ValueError("Invalid value for `product_variant_id`, must not be `None`")

        self._product_variant_id = product_variant_id
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscriptionProductCreate.

            

        :return: The shop of this ShopifySubscriptionProductCreate.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscriptionProductCreate.

            

        :param shop: The shop of this ShopifySubscriptionProductCreate.
        :type: int
        """
        if shop is None:
            raise ValueError("Invalid value for `shop`, must not be `None`")

        self._shop = shop
    

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
        if issubclass(ShopifySubscriptionProductCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionProductCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
