# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionUpdateAddressesRequest:

    swagger_types = {
    
        'billing_address': 'ShopifySubscriptionAddressCreate',
        'id': 'int',
        'shipping_address': 'ShopifySubscriptionAddressCreate',
    }

    attribute_map = {
        'billing_address': 'billingAddress','id': 'id','shipping_address': 'shippingAddress',
    }

    
    _billing_address = None
    _id = None
    _shipping_address = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_address = kwargs.get('billing_address', None)
        self.id = kwargs.get('id', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        

    
    @property
    def billing_address(self):
        """Gets the billing_address of this ShopifySubscriptionUpdateAddressesRequest.

            

        :return: The billing_address of this ShopifySubscriptionUpdateAddressesRequest.
        :rtype: ShopifySubscriptionAddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this ShopifySubscriptionUpdateAddressesRequest.

            

        :param billing_address: The billing_address of this ShopifySubscriptionUpdateAddressesRequest.
        :type: ShopifySubscriptionAddressCreate
        """

        self._billing_address = billing_address
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriptionUpdateAddressesRequest.

            

        :return: The id of this ShopifySubscriptionUpdateAddressesRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriptionUpdateAddressesRequest.

            

        :param id: The id of this ShopifySubscriptionUpdateAddressesRequest.
        :type: int
        """

        self._id = id
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this ShopifySubscriptionUpdateAddressesRequest.

            

        :return: The shipping_address of this ShopifySubscriptionUpdateAddressesRequest.
        :rtype: ShopifySubscriptionAddressCreate
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this ShopifySubscriptionUpdateAddressesRequest.

            

        :param shipping_address: The shipping_address of this ShopifySubscriptionUpdateAddressesRequest.
        :type: ShopifySubscriptionAddressCreate
        """

        self._shipping_address = shipping_address
    

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
        if issubclass(ShopifySubscriptionUpdateAddressesRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionUpdateAddressesRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
