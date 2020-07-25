# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionMetricUsageReport:

    swagger_types = {
    
        'consumed_units': 'float',
        'created_by_user_id': 'int',
        'created_on': 'datetime',
        'description': 'str',
        'external_id': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'metric': 'int',
        'planned_purge_date': 'datetime',
        'subscription': 'int',
        'version': 'int',
    }

    attribute_map = {
        'consumed_units': 'consumedUnits','created_by_user_id': 'createdByUserId','created_on': 'createdOn','description': 'description','external_id': 'externalId','id': 'id','linked_space_id': 'linkedSpaceId','metric': 'metric','planned_purge_date': 'plannedPurgeDate','subscription': 'subscription','version': 'version',
    }

    
    _consumed_units = None
    _created_by_user_id = None
    _created_on = None
    _description = None
    _external_id = None
    _id = None
    _linked_space_id = None
    _metric = None
    _planned_purge_date = None
    _subscription = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.consumed_units = kwargs.get('consumed_units', None)
        self.created_by_user_id = kwargs.get('created_by_user_id', None)
        self.created_on = kwargs.get('created_on', None)
        self.description = kwargs.get('description', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.metric = kwargs.get('metric', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.subscription = kwargs.get('subscription', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def consumed_units(self):
        """Gets the consumed_units of this SubscriptionMetricUsageReport.

            The consumed units describe the amount of resources consumed. Those consumed units will be billed in the next billing cycle.

        :return: The consumed_units of this SubscriptionMetricUsageReport.
        :rtype: float
        """
        return self._consumed_units

    @consumed_units.setter
    def consumed_units(self, consumed_units):
        """Sets the consumed_units of this SubscriptionMetricUsageReport.

            The consumed units describe the amount of resources consumed. Those consumed units will be billed in the next billing cycle.

        :param consumed_units: The consumed_units of this SubscriptionMetricUsageReport.
        :type: float
        """

        self._consumed_units = consumed_units
    
    @property
    def created_by_user_id(self):
        """Gets the created_by_user_id of this SubscriptionMetricUsageReport.

            

        :return: The created_by_user_id of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._created_by_user_id

    @created_by_user_id.setter
    def created_by_user_id(self, created_by_user_id):
        """Sets the created_by_user_id of this SubscriptionMetricUsageReport.

            

        :param created_by_user_id: The created_by_user_id of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._created_by_user_id = created_by_user_id
    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionMetricUsageReport.

            

        :return: The created_on of this SubscriptionMetricUsageReport.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionMetricUsageReport.

            

        :param created_on: The created_on of this SubscriptionMetricUsageReport.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def description(self):
        """Gets the description of this SubscriptionMetricUsageReport.

            The metric usage report description describe the reported usage. This description may be shown to the end user.

        :return: The description of this SubscriptionMetricUsageReport.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionMetricUsageReport.

            The metric usage report description describe the reported usage. This description may be shown to the end user.

        :param description: The description of this SubscriptionMetricUsageReport.
        :type: str
        """
        if description is not None and len(description) > 100:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `100`")

        self._description = description
    
    @property
    def external_id(self):
        """Gets the external_id of this SubscriptionMetricUsageReport.

            The external id identifies the metric usage uniquely.

        :return: The external_id of this SubscriptionMetricUsageReport.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this SubscriptionMetricUsageReport.

            The external id identifies the metric usage uniquely.

        :param external_id: The external_id of this SubscriptionMetricUsageReport.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this SubscriptionMetricUsageReport.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionMetricUsageReport.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionMetricUsageReport.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionMetricUsageReport.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def metric(self):
        """Gets the metric of this SubscriptionMetricUsageReport.

            The metric usage report is linked to the metric for which the usage should be recorded.

        :return: The metric of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this SubscriptionMetricUsageReport.

            The metric usage report is linked to the metric for which the usage should be recorded.

        :param metric: The metric of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._metric = metric
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionMetricUsageReport.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionMetricUsageReport.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionMetricUsageReport.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionMetricUsageReport.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionMetricUsageReport.

            The subscription to which the usage is added to.

        :return: The subscription of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionMetricUsageReport.

            The subscription to which the usage is added to.

        :param subscription: The subscription of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._subscription = subscription
    
    @property
    def version(self):
        """Gets the version of this SubscriptionMetricUsageReport.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionMetricUsageReport.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionMetricUsageReport.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionMetricUsageReport.
        :type: int
        """

        self._version = version
    

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
        if issubclass(SubscriptionMetricUsageReport, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionMetricUsageReport):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
