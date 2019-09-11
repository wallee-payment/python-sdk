# coding: utf-8
import pprint
import six
from enum import Enum



class MetricUsage:

    swagger_types = {
    
        'consumed_units': 'float',
        'metric_description': 'dict(str, str)',
        'metric_id': 'int',
        'metric_name': 'dict(str, str)',
    }

    attribute_map = {
        'consumed_units': 'consumedUnits','metric_description': 'metricDescription','metric_id': 'metricId','metric_name': 'metricName',
    }

    
    _consumed_units = None
    _metric_description = None
    _metric_id = None
    _metric_name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.consumed_units = kwargs.get('consumed_units', None)
        self.metric_description = kwargs.get('metric_description', None)
        self.metric_id = kwargs.get('metric_id', None)
        self.metric_name = kwargs.get('metric_name', None)
        

    
    @property
    def consumed_units(self):
        """Gets the consumed_units of this MetricUsage.

            The consumed units provide the value of how much has been consumed of the particular metric.

        :return: The consumed_units of this MetricUsage.
        :rtype: float
        """
        return self._consumed_units

    @consumed_units.setter
    def consumed_units(self, consumed_units):
        """Sets the consumed_units of this MetricUsage.

            The consumed units provide the value of how much has been consumed of the particular metric.

        :param consumed_units: The consumed_units of this MetricUsage.
        :type: float
        """

        self._consumed_units = consumed_units
    
    @property
    def metric_description(self):
        """Gets the metric_description of this MetricUsage.

            The metric description describes the metric.

        :return: The metric_description of this MetricUsage.
        :rtype: dict(str, str)
        """
        return self._metric_description

    @metric_description.setter
    def metric_description(self, metric_description):
        """Sets the metric_description of this MetricUsage.

            The metric description describes the metric.

        :param metric_description: The metric_description of this MetricUsage.
        :type: dict(str, str)
        """

        self._metric_description = metric_description
    
    @property
    def metric_id(self):
        """Gets the metric_id of this MetricUsage.

            The metric ID identifies the metric for consumed units.

        :return: The metric_id of this MetricUsage.
        :rtype: int
        """
        return self._metric_id

    @metric_id.setter
    def metric_id(self, metric_id):
        """Sets the metric_id of this MetricUsage.

            The metric ID identifies the metric for consumed units.

        :param metric_id: The metric_id of this MetricUsage.
        :type: int
        """

        self._metric_id = metric_id
    
    @property
    def metric_name(self):
        """Gets the metric_name of this MetricUsage.

            The metric name defines the name of the consumed units.

        :return: The metric_name of this MetricUsage.
        :rtype: dict(str, str)
        """
        return self._metric_name

    @metric_name.setter
    def metric_name(self, metric_name):
        """Sets the metric_name of this MetricUsage.

            The metric name defines the name of the consumed units.

        :param metric_name: The metric_name of this MetricUsage.
        :type: dict(str, str)
        """

        self._metric_name = metric_name
    

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
        if issubclass(MetricUsage, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, MetricUsage):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
