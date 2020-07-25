# coding: utf-8
import pprint
import six
from enum import Enum



class DebtCollectorConfiguration:

    swagger_types = {
    
        'collector': 'int',
        'conditions': 'list[int]',
        'enabled_space_views': 'list[int]',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'skip_review_enabled': 'bool',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'collector': 'collector','conditions': 'conditions','enabled_space_views': 'enabledSpaceViews','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','priority': 'priority','skip_review_enabled': 'skipReviewEnabled','state': 'state','version': 'version',
    }

    
    _collector = None
    _conditions = None
    _enabled_space_views = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _priority = None
    _skip_review_enabled = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.collector = kwargs.get('collector', None)
        self.conditions = kwargs.get('conditions', None)
        self.enabled_space_views = kwargs.get('enabled_space_views', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.skip_review_enabled = kwargs.get('skip_review_enabled', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def collector(self):
        """Gets the collector of this DebtCollectorConfiguration.

            The collector handles the debt collection case based on the settings of this configuration.

        :return: The collector of this DebtCollectorConfiguration.
        :rtype: int
        """
        return self._collector

    @collector.setter
    def collector(self, collector):
        """Sets the collector of this DebtCollectorConfiguration.

            The collector handles the debt collection case based on the settings of this configuration.

        :param collector: The collector of this DebtCollectorConfiguration.
        :type: int
        """

        self._collector = collector
    
    @property
    def conditions(self):
        """Gets the conditions of this DebtCollectorConfiguration.

            The conditions applied to the collector configuration restricts the application of this configuration onto a particular debt collection case.

        :return: The conditions of this DebtCollectorConfiguration.
        :rtype: list[int]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this DebtCollectorConfiguration.

            The conditions applied to the collector configuration restricts the application of this configuration onto a particular debt collection case.

        :param conditions: The conditions of this DebtCollectorConfiguration.
        :type: list[int]
        """

        self._conditions = conditions
    
    @property
    def enabled_space_views(self):
        """Gets the enabled_space_views of this DebtCollectorConfiguration.

            The collector configuration is only enabled for the selected space views. In case the set is empty the collector configuration is enabled for all space views.

        :return: The enabled_space_views of this DebtCollectorConfiguration.
        :rtype: list[int]
        """
        return self._enabled_space_views

    @enabled_space_views.setter
    def enabled_space_views(self, enabled_space_views):
        """Sets the enabled_space_views of this DebtCollectorConfiguration.

            The collector configuration is only enabled for the selected space views. In case the set is empty the collector configuration is enabled for all space views.

        :param enabled_space_views: The enabled_space_views of this DebtCollectorConfiguration.
        :type: list[int]
        """

        self._enabled_space_views = enabled_space_views
    
    @property
    def id(self):
        """Gets the id of this DebtCollectorConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DebtCollectorConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DebtCollectorConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DebtCollectorConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DebtCollectorConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this DebtCollectorConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DebtCollectorConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this DebtCollectorConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this DebtCollectorConfiguration.

            The collector configuration name is used internally to identify a specific collector configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this DebtCollectorConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this DebtCollectorConfiguration.

            The collector configuration name is used internally to identify a specific collector configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this DebtCollectorConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DebtCollectorConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DebtCollectorConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DebtCollectorConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DebtCollectorConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this DebtCollectorConfiguration.

            The priority defines the order in which the collector configuration is tried to be applied onto a debt collection case. The higher the value the less likely the configuration is applied on a case.

        :return: The priority of this DebtCollectorConfiguration.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this DebtCollectorConfiguration.

            The priority defines the order in which the collector configuration is tried to be applied onto a debt collection case. The higher the value the less likely the configuration is applied on a case.

        :param priority: The priority of this DebtCollectorConfiguration.
        :type: int
        """

        self._priority = priority
    
    @property
    def skip_review_enabled(self):
        """Gets the skip_review_enabled of this DebtCollectorConfiguration.

            When the review is skipped there will be no review for cases which use this configuration.

        :return: The skip_review_enabled of this DebtCollectorConfiguration.
        :rtype: bool
        """
        return self._skip_review_enabled

    @skip_review_enabled.setter
    def skip_review_enabled(self, skip_review_enabled):
        """Sets the skip_review_enabled of this DebtCollectorConfiguration.

            When the review is skipped there will be no review for cases which use this configuration.

        :param skip_review_enabled: The skip_review_enabled of this DebtCollectorConfiguration.
        :type: bool
        """

        self._skip_review_enabled = skip_review_enabled
    
    @property
    def state(self):
        """Gets the state of this DebtCollectorConfiguration.

            

        :return: The state of this DebtCollectorConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DebtCollectorConfiguration.

            

        :param state: The state of this DebtCollectorConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this DebtCollectorConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this DebtCollectorConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DebtCollectorConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this DebtCollectorConfiguration.
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
        if issubclass(DebtCollectorConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectorConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
