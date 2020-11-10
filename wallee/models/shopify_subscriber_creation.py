# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriberCreation:

    swagger_types = {
    
        'email_address': 'str',
        'phone_number': 'str',
        'shopify_customer_id': 'str',
    }

    attribute_map = {
        'email_address': 'emailAddress','phone_number': 'phoneNumber','shopify_customer_id': 'shopifyCustomerId',
    }

    
    _email_address = None
    _phone_number = None
    _shopify_customer_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.email_address = kwargs.get('email_address', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.shopify_customer_id = kwargs.get('shopify_customer_id')

        

    
    @property
    def email_address(self):
        """Gets the email_address of this ShopifySubscriberCreation.

            

        :return: The email_address of this ShopifySubscriberCreation.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ShopifySubscriberCreation.

            

        :param email_address: The email_address of this ShopifySubscriberCreation.
        :type: str
        """

        self._email_address = email_address
    
    @property
    def phone_number(self):
        """Gets the phone_number of this ShopifySubscriberCreation.

            

        :return: The phone_number of this ShopifySubscriberCreation.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ShopifySubscriberCreation.

            

        :param phone_number: The phone_number of this ShopifySubscriberCreation.
        :type: str
        """

        self._phone_number = phone_number
    
    @property
    def shopify_customer_id(self):
        """Gets the shopify_customer_id of this ShopifySubscriberCreation.

            The customer ID has to correspond to the ID assigned to the customer by Shopify. When the subscriber already exists no new subscriber will be created.

        :return: The shopify_customer_id of this ShopifySubscriberCreation.
        :rtype: str
        """
        return self._shopify_customer_id

    @shopify_customer_id.setter
    def shopify_customer_id(self, shopify_customer_id):
        """Sets the shopify_customer_id of this ShopifySubscriberCreation.

            The customer ID has to correspond to the ID assigned to the customer by Shopify. When the subscriber already exists no new subscriber will be created.

        :param shopify_customer_id: The shopify_customer_id of this ShopifySubscriberCreation.
        :type: str
        """
        if shopify_customer_id is None:
            raise ValueError("Invalid value for `shopify_customer_id`, must not be `None`")

        self._shopify_customer_id = shopify_customer_id
    

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
        if issubclass(ShopifySubscriberCreation, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriberCreation):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
