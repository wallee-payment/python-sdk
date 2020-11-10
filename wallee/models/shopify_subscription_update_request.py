# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionUpdateRequest:

    swagger_types = {
    
        'billing_configuration': 'ShopifySubscriptionModelBillingConfiguration',
        'id': 'int',
        'items': 'list[ShopifySubscriptionModelItem]',
        'store_order_confirmation_email_enabled': 'bool',
        'subscriber_suspension_allowed': 'bool',
    }

    attribute_map = {
        'billing_configuration': 'billingConfiguration','id': 'id','items': 'items','store_order_confirmation_email_enabled': 'storeOrderConfirmationEmailEnabled','subscriber_suspension_allowed': 'subscriberSuspensionAllowed',
    }

    
    _billing_configuration = None
    _id = None
    _items = None
    _store_order_confirmation_email_enabled = None
    _subscriber_suspension_allowed = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_configuration = kwargs.get('billing_configuration', None)
        self.id = kwargs.get('id', None)
        self.items = kwargs.get('items', None)
        self.store_order_confirmation_email_enabled = kwargs.get('store_order_confirmation_email_enabled', None)
        self.subscriber_suspension_allowed = kwargs.get('subscriber_suspension_allowed', None)
        

    
    @property
    def billing_configuration(self):
        """Gets the billing_configuration of this ShopifySubscriptionUpdateRequest.

            

        :return: The billing_configuration of this ShopifySubscriptionUpdateRequest.
        :rtype: ShopifySubscriptionModelBillingConfiguration
        """
        return self._billing_configuration

    @billing_configuration.setter
    def billing_configuration(self, billing_configuration):
        """Sets the billing_configuration of this ShopifySubscriptionUpdateRequest.

            

        :param billing_configuration: The billing_configuration of this ShopifySubscriptionUpdateRequest.
        :type: ShopifySubscriptionModelBillingConfiguration
        """

        self._billing_configuration = billing_configuration
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriptionUpdateRequest.

            

        :return: The id of this ShopifySubscriptionUpdateRequest.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriptionUpdateRequest.

            

        :param id: The id of this ShopifySubscriptionUpdateRequest.
        :type: int
        """

        self._id = id
    
    @property
    def items(self):
        """Gets the items of this ShopifySubscriptionUpdateRequest.

            

        :return: The items of this ShopifySubscriptionUpdateRequest.
        :rtype: list[ShopifySubscriptionModelItem]
        """
        return self._items

    @items.setter
    def items(self, items):
        """Sets the items of this ShopifySubscriptionUpdateRequest.

            

        :param items: The items of this ShopifySubscriptionUpdateRequest.
        :type: list[ShopifySubscriptionModelItem]
        """

        self._items = items
    
    @property
    def store_order_confirmation_email_enabled(self):
        """Gets the store_order_confirmation_email_enabled of this ShopifySubscriptionUpdateRequest.

            

        :return: The store_order_confirmation_email_enabled of this ShopifySubscriptionUpdateRequest.
        :rtype: bool
        """
        return self._store_order_confirmation_email_enabled

    @store_order_confirmation_email_enabled.setter
    def store_order_confirmation_email_enabled(self, store_order_confirmation_email_enabled):
        """Sets the store_order_confirmation_email_enabled of this ShopifySubscriptionUpdateRequest.

            

        :param store_order_confirmation_email_enabled: The store_order_confirmation_email_enabled of this ShopifySubscriptionUpdateRequest.
        :type: bool
        """

        self._store_order_confirmation_email_enabled = store_order_confirmation_email_enabled
    
    @property
    def subscriber_suspension_allowed(self):
        """Gets the subscriber_suspension_allowed of this ShopifySubscriptionUpdateRequest.

            

        :return: The subscriber_suspension_allowed of this ShopifySubscriptionUpdateRequest.
        :rtype: bool
        """
        return self._subscriber_suspension_allowed

    @subscriber_suspension_allowed.setter
    def subscriber_suspension_allowed(self, subscriber_suspension_allowed):
        """Sets the subscriber_suspension_allowed of this ShopifySubscriptionUpdateRequest.

            

        :param subscriber_suspension_allowed: The subscriber_suspension_allowed of this ShopifySubscriptionUpdateRequest.
        :type: bool
        """

        self._subscriber_suspension_allowed = subscriber_suspension_allowed
    

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
        if issubclass(ShopifySubscriptionUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
