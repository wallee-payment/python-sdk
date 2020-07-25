# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionMetricUsageReportCreate:

    swagger_types = {
    
        'consumed_units': 'float',
        'description': 'str',
        'external_id': 'str',
        'metric': 'int',
        'subscription': 'int',
    }

    attribute_map = {
        'consumed_units': 'consumedUnits','description': 'description','external_id': 'externalId','metric': 'metric','subscription': 'subscription',
    }

    
    _consumed_units = None
    _description = None
    _external_id = None
    _metric = None
    _subscription = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.consumed_units = kwargs.get('consumed_units')

        self.description = kwargs.get('description', None)
        self.external_id = kwargs.get('external_id')

        self.metric = kwargs.get('metric')

        self.subscription = kwargs.get('subscription')

        

    
    @property
    def consumed_units(self):
        """Gets the consumed_units of this SubscriptionMetricUsageReportCreate.

            The consumed units describe the amount of resources consumed. Those consumed units will be billed in the next billing cycle.

        :return: The consumed_units of this SubscriptionMetricUsageReportCreate.
        :rtype: float
        """
        return self._consumed_units

    @consumed_units.setter
    def consumed_units(self, consumed_units):
        """Sets the consumed_units of this SubscriptionMetricUsageReportCreate.

            The consumed units describe the amount of resources consumed. Those consumed units will be billed in the next billing cycle.

        :param consumed_units: The consumed_units of this SubscriptionMetricUsageReportCreate.
        :type: float
        """
        if consumed_units is None:
            raise ValueError("Invalid value for `consumed_units`, must not be `None`")

        self._consumed_units = consumed_units
    
    @property
    def description(self):
        """Gets the description of this SubscriptionMetricUsageReportCreate.

            The metric usage report description describe the reported usage. This description may be shown to the end user.

        :return: The description of this SubscriptionMetricUsageReportCreate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionMetricUsageReportCreate.

            The metric usage report description describe the reported usage. This description may be shown to the end user.

        :param description: The description of this SubscriptionMetricUsageReportCreate.
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")

        self._description = description
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionMetricUsageReportCreate.

            The external id identifies the metric usage uniquely.

        :return: The external_id of this SubscriptionMetricUsageReportCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionMetricUsageReportCreate.

            The external id identifies the metric usage uniquely.

        :param external_id: The external_id of this SubscriptionMetricUsageReportCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def metric(self):
        """Gets the metric of this SubscriptionMetricUsageReportCreate.

            The metric usage report is linked to the metric for which the usage should be recorded.

        :return: The metric of this SubscriptionMetricUsageReportCreate.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this SubscriptionMetricUsageReportCreate.

            The metric usage report is linked to the metric for which the usage should be recorded.

        :param metric: The metric of this SubscriptionMetricUsageReportCreate.
        :type: int
        """
        if metric is None:
            raise ValueError("Invalid value for `metric`, must not be `None`")

        self._metric = metric
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionMetricUsageReportCreate.

            The subscription to which the usage is added to.

        :return: The subscription of this SubscriptionMetricUsageReportCreate.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionMetricUsageReportCreate.

            The subscription to which the usage is added to.

        :param subscription: The subscription of this SubscriptionMetricUsageReportCreate.
        :type: int
        """
        if subscription is None:
            raise ValueError("Invalid value for `subscription`, must not be `None`")

        self._subscription = subscription
    

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
        if issubclass(SubscriptionMetricUsageReportCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionMetricUsageReportCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
