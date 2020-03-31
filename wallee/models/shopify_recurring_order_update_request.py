# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifyRecurringOrderUpdateRequest:

    swagger_types = {
    
        'execution_date': 'datetime',
        'recurring_order_id': 'int',
    }

    attribute_map = {
        'execution_date': 'executionDate','recurring_order_id': 'recurringOrderId',
    }

    
    _execution_date = None
    _recurring_order_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.execution_date = kwargs.get('execution_date', None)
        self.recurring_order_id = kwargs.get('recurring_order_id', None)
        

    
    @property
    def execution_date(self):
        """Gets the execution_date of this ShopifyRecurringOrderUpdateRequest.

            

        :return: The execution_date of this ShopifyRecurringOrderUpdateRequest.
        :rtype: datetime
        """
        return self._execution_date

    @execution_date.setter
    def execution_date(self, execution_date):
        """Sets the execution_date of this ShopifyRecurringOrderUpdateRequest.

            

        :param execution_date: The execution_date of this ShopifyRecurringOrderUpdateRequest.
        :type: datetime
        """

        self._execution_date = execution_date
    
    @property
    def recurring_order_id(self):
        """Gets the recurring_order_id of this ShopifyRecurringOrderUpdateRequest.

            

        :return: The recurring_order_id of this ShopifyRecurringOrderUpdateRequest.
        :rtype: int
        """
        return self._recurring_order_id

    @recurring_order_id.setter
    def recurring_order_id(self, recurring_order_id):
        """Sets the recurring_order_id of this ShopifyRecurringOrderUpdateRequest.

            

        :param recurring_order_id: The recurring_order_id of this ShopifyRecurringOrderUpdateRequest.
        :type: int
        """

        self._recurring_order_id = recurring_order_id
    

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
        if issubclass(ShopifyRecurringOrderUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifyRecurringOrderUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
