# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppRefundConfigurationCreate:

    swagger_types = {
    
        'multiple_refunds_supported': 'bool',
        'refund_endpoint': 'str',
        'refund_timeout_in_minutes': 'int',
    }

    attribute_map = {
        'multiple_refunds_supported': 'multipleRefundsSupported','refund_endpoint': 'refundEndpoint','refund_timeout_in_minutes': 'refundTimeoutInMinutes',
    }

    
    _multiple_refunds_supported = None
    _refund_endpoint = None
    _refund_timeout_in_minutes = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.multiple_refunds_supported = kwargs.get('multiple_refunds_supported', None)
        self.refund_endpoint = kwargs.get('refund_endpoint', None)
        self.refund_timeout_in_minutes = kwargs.get('refund_timeout_in_minutes', None)
        

    
    @property
    def multiple_refunds_supported(self):
        """Gets the multiple_refunds_supported of this PaymentAppRefundConfigurationCreate.

            This flag indicates whether the connector supports multiple refunds for a single transaction or not.

        :return: The multiple_refunds_supported of this PaymentAppRefundConfigurationCreate.
        :rtype: bool
        """
        return self._multiple_refunds_supported

    @multiple_refunds_supported.setter
    def multiple_refunds_supported(self, multiple_refunds_supported):
        """Sets the multiple_refunds_supported of this PaymentAppRefundConfigurationCreate.

            This flag indicates whether the connector supports multiple refunds for a single transaction or not.

        :param multiple_refunds_supported: The multiple_refunds_supported of this PaymentAppRefundConfigurationCreate.
        :type: bool
        """

        self._multiple_refunds_supported = multiple_refunds_supported
    
    @property
    def refund_endpoint(self):
        """Gets the refund_endpoint of this PaymentAppRefundConfigurationCreate.

            The refund endpoint is invoked to request the payment service provider to execute a refund.

        :return: The refund_endpoint of this PaymentAppRefundConfigurationCreate.
        :rtype: str
        """
        return self._refund_endpoint

    @refund_endpoint.setter
    def refund_endpoint(self, refund_endpoint):
        """Sets the refund_endpoint of this PaymentAppRefundConfigurationCreate.

            The refund endpoint is invoked to request the payment service provider to execute a refund.

        :param refund_endpoint: The refund_endpoint of this PaymentAppRefundConfigurationCreate.
        :type: str
        """

        self._refund_endpoint = refund_endpoint
    
    @property
    def refund_timeout_in_minutes(self):
        """Gets the refund_timeout_in_minutes of this PaymentAppRefundConfigurationCreate.

            When the refund is triggered we expect a feedback about the state of it. This timeout defines after how long we consider the refund as failed without receiving a final state update.

        :return: The refund_timeout_in_minutes of this PaymentAppRefundConfigurationCreate.
        :rtype: int
        """
        return self._refund_timeout_in_minutes

    @refund_timeout_in_minutes.setter
    def refund_timeout_in_minutes(self, refund_timeout_in_minutes):
        """Sets the refund_timeout_in_minutes of this PaymentAppRefundConfigurationCreate.

            When the refund is triggered we expect a feedback about the state of it. This timeout defines after how long we consider the refund as failed without receiving a final state update.

        :param refund_timeout_in_minutes: The refund_timeout_in_minutes of this PaymentAppRefundConfigurationCreate.
        :type: int
        """

        self._refund_timeout_in_minutes = refund_timeout_in_minutes
    

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
        if issubclass(PaymentAppRefundConfigurationCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppRefundConfigurationCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
