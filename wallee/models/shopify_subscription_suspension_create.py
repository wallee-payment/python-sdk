# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriptionSuspensionCreate:

    swagger_types = {
    
        'planned_end_date': 'datetime',
        'subscription': 'int',
        'type': 'ShopifySubscriptionSuspensionType',
    }

    attribute_map = {
        'planned_end_date': 'plannedEndDate','subscription': 'subscription','type': 'type',
    }

    
    _planned_end_date = None
    _subscription = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.planned_end_date = kwargs.get('planned_end_date')

        self.subscription = kwargs.get('subscription')

        self.type = kwargs.get('type')

        

    
    @property
    def planned_end_date(self):
        """Gets the planned_end_date of this ShopifySubscriptionSuspensionCreate.

            

        :return: The planned_end_date of this ShopifySubscriptionSuspensionCreate.
        :rtype: datetime
        """
        return self._planned_end_date

    @planned_end_date.setter
    def planned_end_date(self, planned_end_date):
        """Sets the planned_end_date of this ShopifySubscriptionSuspensionCreate.

            

        :param planned_end_date: The planned_end_date of this ShopifySubscriptionSuspensionCreate.
        :type: datetime
        """
        if planned_end_date is None:
            raise ValueError("Invalid value for `planned_end_date`, must not be `None`")

        self._planned_end_date = planned_end_date
    
    @property
    def subscription(self):
        """Gets the subscription of this ShopifySubscriptionSuspensionCreate.

            

        :return: The subscription of this ShopifySubscriptionSuspensionCreate.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this ShopifySubscriptionSuspensionCreate.

            

        :param subscription: The subscription of this ShopifySubscriptionSuspensionCreate.
        :type: int
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription
    
    @property
    def type(self):
        """Gets the type of this ShopifySubscriptionSuspensionCreate.

            

        :return: The type of this ShopifySubscriptionSuspensionCreate.
        :rtype: ShopifySubscriptionSuspensionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ShopifySubscriptionSuspensionCreate.

            

        :param type: The type of this ShopifySubscriptionSuspensionCreate.
        :type: ShopifySubscriptionSuspensionType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
    

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
        if issubclass(ShopifySubscriptionSuspensionCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriptionSuspensionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
