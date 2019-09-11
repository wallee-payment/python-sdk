# coding: utf-8
import pprint
import six
from enum import Enum



class InstallmentPlanSliceConfiguration:

    swagger_types = {
    
        'id': 'int',
        'line_item_title': 'DatabaseTranslatedString',
        'linked_space_id': 'int',
        'period': 'str',
        'plan': 'InstallmentPlanConfiguration',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'proportion': 'float',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','line_item_title': 'lineItemTitle','linked_space_id': 'linkedSpaceId','period': 'period','plan': 'plan','planned_purge_date': 'plannedPurgeDate','priority': 'priority','proportion': 'proportion','state': 'state','version': 'version',
    }

    
    _id = None
    _line_item_title = None
    _linked_space_id = None
    _period = None
    _plan = None
    _planned_purge_date = None
    _priority = None
    _proportion = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.line_item_title = kwargs.get('line_item_title', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.period = kwargs.get('period', None)
        self.plan = kwargs.get('plan', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.proportion = kwargs.get('proportion', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this InstallmentPlanSliceConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InstallmentPlanSliceConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InstallmentPlanSliceConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InstallmentPlanSliceConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def line_item_title(self):
        """Gets the line_item_title of this InstallmentPlanSliceConfiguration.

            The title of this slices line items. The title is visible to the buyer.

        :return: The line_item_title of this InstallmentPlanSliceConfiguration.
        :rtype: DatabaseTranslatedString
        """
        return self._line_item_title

    @line_item_title.setter
    def line_item_title(self, line_item_title):
        """Sets the line_item_title of this InstallmentPlanSliceConfiguration.

            The title of this slices line items. The title is visible to the buyer.

        :param line_item_title: The line_item_title of this InstallmentPlanSliceConfiguration.
        :type: DatabaseTranslatedString
        """

        self._line_item_title = line_item_title
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InstallmentPlanSliceConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InstallmentPlanSliceConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InstallmentPlanSliceConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InstallmentPlanSliceConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def period(self):
        """Gets the period of this InstallmentPlanSliceConfiguration.

            The period defines how much time passes between the last slice and this slice. The charge is triggered at the end of the period. When the slice should be charged immediately the period needs to be zero.

        :return: The period of this InstallmentPlanSliceConfiguration.
        :rtype: str
        """
        return self._period

    @period.setter
    def period(self, period):
        """Sets the period of this InstallmentPlanSliceConfiguration.

            The period defines how much time passes between the last slice and this slice. The charge is triggered at the end of the period. When the slice should be charged immediately the period needs to be zero.

        :param period: The period of this InstallmentPlanSliceConfiguration.
        :type: str
        """

        self._period = period
    
    @property
    def plan(self):
        """Gets the plan of this InstallmentPlanSliceConfiguration.

            The installment plan this slice belongs to.

        :return: The plan of this InstallmentPlanSliceConfiguration.
        :rtype: InstallmentPlanConfiguration
        """
        return self._plan

    @plan.setter
    def plan(self, plan):
        """Sets the plan of this InstallmentPlanSliceConfiguration.

            The installment plan this slice belongs to.

        :param plan: The plan of this InstallmentPlanSliceConfiguration.
        :type: InstallmentPlanConfiguration
        """

        self._plan = plan
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InstallmentPlanSliceConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this InstallmentPlanSliceConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InstallmentPlanSliceConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this InstallmentPlanSliceConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this InstallmentPlanSliceConfiguration.

            The priority controls in which order the slices are applied. The lower the value the higher the precedence.

        :return: The priority of this InstallmentPlanSliceConfiguration.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this InstallmentPlanSliceConfiguration.

            The priority controls in which order the slices are applied. The lower the value the higher the precedence.

        :param priority: The priority of this InstallmentPlanSliceConfiguration.
        :type: int
        """

        self._priority = priority
    
    @property
    def proportion(self):
        """Gets the proportion of this InstallmentPlanSliceConfiguration.

            The proportion defines how much of the total installment payment has to be paid in this slice. The value is summed up with the other slices and the ratio of all proportions compared to proportion of this slice determines how much the buyer has to pay in this slice.

        :return: The proportion of this InstallmentPlanSliceConfiguration.
        :rtype: float
        """
        return self._proportion

    @proportion.setter
    def proportion(self, proportion):
        """Sets the proportion of this InstallmentPlanSliceConfiguration.

            The proportion defines how much of the total installment payment has to be paid in this slice. The value is summed up with the other slices and the ratio of all proportions compared to proportion of this slice determines how much the buyer has to pay in this slice.

        :param proportion: The proportion of this InstallmentPlanSliceConfiguration.
        :type: float
        """

        self._proportion = proportion
    
    @property
    def state(self):
        """Gets the state of this InstallmentPlanSliceConfiguration.

            

        :return: The state of this InstallmentPlanSliceConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InstallmentPlanSliceConfiguration.

            

        :param state: The state of this InstallmentPlanSliceConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this InstallmentPlanSliceConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InstallmentPlanSliceConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InstallmentPlanSliceConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InstallmentPlanSliceConfiguration.
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
        if issubclass(InstallmentPlanSliceConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InstallmentPlanSliceConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
