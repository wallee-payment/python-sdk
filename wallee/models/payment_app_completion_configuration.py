# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppCompletionConfiguration:

    swagger_types = {
    
        'completion_endpoint': 'str',
        'completion_timeout_in_minutes': 'int',
        'maximal_completion_delay_in_days': 'int',
        'multiple_completions_supported': 'bool',
        'void_endpoint': 'str',
    }

    attribute_map = {
        'completion_endpoint': 'completionEndpoint','completion_timeout_in_minutes': 'completionTimeoutInMinutes','maximal_completion_delay_in_days': 'maximalCompletionDelayInDays','multiple_completions_supported': 'multipleCompletionsSupported','void_endpoint': 'voidEndpoint',
    }

    
    _completion_endpoint = None
    _completion_timeout_in_minutes = None
    _maximal_completion_delay_in_days = None
    _multiple_completions_supported = None
    _void_endpoint = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.completion_endpoint = kwargs.get('completion_endpoint', None)
        self.completion_timeout_in_minutes = kwargs.get('completion_timeout_in_minutes', None)
        self.maximal_completion_delay_in_days = kwargs.get('maximal_completion_delay_in_days', None)
        self.multiple_completions_supported = kwargs.get('multiple_completions_supported', None)
        self.void_endpoint = kwargs.get('void_endpoint', None)
        

    
    @property
    def completion_endpoint(self):
        """Gets the completion_endpoint of this PaymentAppCompletionConfiguration.

            The URL that the payment service provider will invoke to process a completion request. This endpoint handles communication with the provider for initiating and managing completions.

        :return: The completion_endpoint of this PaymentAppCompletionConfiguration.
        :rtype: str
        """
        return self._completion_endpoint

    @completion_endpoint.setter
    def completion_endpoint(self, completion_endpoint):
        """Sets the completion_endpoint of this PaymentAppCompletionConfiguration.

            The URL that the payment service provider will invoke to process a completion request. This endpoint handles communication with the provider for initiating and managing completions.

        :param completion_endpoint: The completion_endpoint of this PaymentAppCompletionConfiguration.
        :type: str
        """

        self._completion_endpoint = completion_endpoint
    
    @property
    def completion_timeout_in_minutes(self):
        """Gets the completion_timeout_in_minutes of this PaymentAppCompletionConfiguration.

            The maximum time (in minutes) to wait for a response from the payment service provider after a completion request is triggered. If no feedback or final status is received within this period, the completion is considered failed.

        :return: The completion_timeout_in_minutes of this PaymentAppCompletionConfiguration.
        :rtype: int
        """
        return self._completion_timeout_in_minutes

    @completion_timeout_in_minutes.setter
    def completion_timeout_in_minutes(self, completion_timeout_in_minutes):
        """Sets the completion_timeout_in_minutes of this PaymentAppCompletionConfiguration.

            The maximum time (in minutes) to wait for a response from the payment service provider after a completion request is triggered. If no feedback or final status is received within this period, the completion is considered failed.

        :param completion_timeout_in_minutes: The completion_timeout_in_minutes of this PaymentAppCompletionConfiguration.
        :type: int
        """

        self._completion_timeout_in_minutes = completion_timeout_in_minutes
    
    @property
    def maximal_completion_delay_in_days(self):
        """Gets the maximal_completion_delay_in_days of this PaymentAppCompletionConfiguration.

            The maximum number of days after a transaction's authorization during which a completion or void action can be triggered. Once this period has passed, neither action can be executed.

        :return: The maximal_completion_delay_in_days of this PaymentAppCompletionConfiguration.
        :rtype: int
        """
        return self._maximal_completion_delay_in_days

    @maximal_completion_delay_in_days.setter
    def maximal_completion_delay_in_days(self, maximal_completion_delay_in_days):
        """Sets the maximal_completion_delay_in_days of this PaymentAppCompletionConfiguration.

            The maximum number of days after a transaction's authorization during which a completion or void action can be triggered. Once this period has passed, neither action can be executed.

        :param maximal_completion_delay_in_days: The maximal_completion_delay_in_days of this PaymentAppCompletionConfiguration.
        :type: int
        """

        self._maximal_completion_delay_in_days = maximal_completion_delay_in_days
    
    @property
    def multiple_completions_supported(self):
        """Gets the multiple_completions_supported of this PaymentAppCompletionConfiguration.

            Whether the payment connector can process multiple completions for a single transaction.

        :return: The multiple_completions_supported of this PaymentAppCompletionConfiguration.
        :rtype: bool
        """
        return self._multiple_completions_supported

    @multiple_completions_supported.setter
    def multiple_completions_supported(self, multiple_completions_supported):
        """Sets the multiple_completions_supported of this PaymentAppCompletionConfiguration.

            Whether the payment connector can process multiple completions for a single transaction.

        :param multiple_completions_supported: The multiple_completions_supported of this PaymentAppCompletionConfiguration.
        :type: bool
        """

        self._multiple_completions_supported = multiple_completions_supported
    
    @property
    def void_endpoint(self):
        """Gets the void_endpoint of this PaymentAppCompletionConfiguration.

            The URL that the payment service provider will invoke to process a void request. This endpoint handles communication with the provider for initiating and managing voids.

        :return: The void_endpoint of this PaymentAppCompletionConfiguration.
        :rtype: str
        """
        return self._void_endpoint

    @void_endpoint.setter
    def void_endpoint(self, void_endpoint):
        """Sets the void_endpoint of this PaymentAppCompletionConfiguration.

            The URL that the payment service provider will invoke to process a void request. This endpoint handles communication with the provider for initiating and managing voids.

        :param void_endpoint: The void_endpoint of this PaymentAppCompletionConfiguration.
        :type: str
        """

        self._void_endpoint = void_endpoint
    

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
        if issubclass(PaymentAppCompletionConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppCompletionConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
