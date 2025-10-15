# coding: utf-8
import pprint
import six
from enum import Enum



class BillingCycleModel:

    swagger_types = {
    
        'billing_cycle_type': 'BillingCycleType',
        'customization': 'BillingDayCustomization',
        'day_of_month': 'int',
        'month': 'DisplayableMonth',
        'number_of_periods': 'int',
        'weekly_day': 'DisplayableDayOfWeek',
    }

    attribute_map = {
        'billing_cycle_type': 'billingCycleType','customization': 'customization','day_of_month': 'dayOfMonth','month': 'month','number_of_periods': 'numberOfPeriods','weekly_day': 'weeklyDay',
    }

    
    _billing_cycle_type = None
    _customization = None
    _day_of_month = None
    _month = None
    _number_of_periods = None
    _weekly_day = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_cycle_type = kwargs.get('billing_cycle_type')

        self.customization = kwargs.get('customization', None)
        self.day_of_month = kwargs.get('day_of_month', None)
        self.month = kwargs.get('month', None)
        self.number_of_periods = kwargs.get('number_of_periods')

        self.weekly_day = kwargs.get('weekly_day', None)
        

    
    @property
    def billing_cycle_type(self):
        """Gets the billing_cycle_type of this BillingCycleModel.

            

        :return: The billing_cycle_type of this BillingCycleModel.
        :rtype: BillingCycleType
        """
        return self._billing_cycle_type

    @billing_cycle_type.setter
    def billing_cycle_type(self, billing_cycle_type):
        """Sets the billing_cycle_type of this BillingCycleModel.

            

        :param billing_cycle_type: The billing_cycle_type of this BillingCycleModel.
        :type: BillingCycleType
        """
        if billing_cycle_type is None:
            raise ValueError("Invalid value for `billing_cycle_type`, must not be `None`")

        self._billing_cycle_type = billing_cycle_type
    
    @property
    def customization(self):
        """Gets the customization of this BillingCycleModel.

            

        :return: The customization of this BillingCycleModel.
        :rtype: BillingDayCustomization
        """
        return self._customization

    @customization.setter
    def customization(self, customization):
        """Sets the customization of this BillingCycleModel.

            

        :param customization: The customization of this BillingCycleModel.
        :type: BillingDayCustomization
        """

        self._customization = customization
    
    @property
    def day_of_month(self):
        """Gets the day_of_month of this BillingCycleModel.

            

        :return: The day_of_month of this BillingCycleModel.
        :rtype: int
        """
        return self._day_of_month

    @day_of_month.setter
    def day_of_month(self, day_of_month):
        """Sets the day_of_month of this BillingCycleModel.

            

        :param day_of_month: The day_of_month of this BillingCycleModel.
        :type: int
        """

        self._day_of_month = day_of_month
    
    @property
    def month(self):
        """Gets the month of this BillingCycleModel.

            

        :return: The month of this BillingCycleModel.
        :rtype: DisplayableMonth
        """
        return self._month

    @month.setter
    def month(self, month):
        """Sets the month of this BillingCycleModel.

            

        :param month: The month of this BillingCycleModel.
        :type: DisplayableMonth
        """

        self._month = month
    
    @property
    def number_of_periods(self):
        """Gets the number_of_periods of this BillingCycleModel.

            Billing Cycle type multiplied by Number of Periods defines billing cycle duration, e.g. 3 months. Monthly types require 1-12; weekly and yearly types require 1-9 periods; and daily types require 1-30.

        :return: The number_of_periods of this BillingCycleModel.
        :rtype: int
        """
        return self._number_of_periods

    @number_of_periods.setter
    def number_of_periods(self, number_of_periods):
        """Sets the number_of_periods of this BillingCycleModel.

            Billing Cycle type multiplied by Number of Periods defines billing cycle duration, e.g. 3 months. Monthly types require 1-12; weekly and yearly types require 1-9 periods; and daily types require 1-30.

        :param number_of_periods: The number_of_periods of this BillingCycleModel.
        :type: int
        """
        if number_of_periods is None:
            raise ValueError("Invalid value for `number_of_periods`, must not be `None`")

        self._number_of_periods = number_of_periods
    
    @property
    def weekly_day(self):
        """Gets the weekly_day of this BillingCycleModel.

            

        :return: The weekly_day of this BillingCycleModel.
        :rtype: DisplayableDayOfWeek
        """
        return self._weekly_day

    @weekly_day.setter
    def weekly_day(self, weekly_day):
        """Sets the weekly_day of this BillingCycleModel.

            

        :param weekly_day: The weekly_day of this BillingCycleModel.
        :type: DisplayableDayOfWeek
        """

        self._weekly_day = weekly_day
    

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
        if issubclass(BillingCycleModel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, BillingCycleModel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
