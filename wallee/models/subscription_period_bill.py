# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionPeriodBill:

    swagger_types = {
    
        'created_on': 'datetime',
        'effective_period_end_date': 'datetime',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'period_start_date': 'datetime',
        'planned_period_end_date': 'datetime',
        'planned_purge_date': 'datetime',
        'state': 'SubscriptionPeriodBillState',
        'subscription_version': 'SubscriptionVersion',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','effective_period_end_date': 'effectivePeriodEndDate','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','period_start_date': 'periodStartDate','planned_period_end_date': 'plannedPeriodEndDate','planned_purge_date': 'plannedPurgeDate','state': 'state','subscription_version': 'subscriptionVersion','version': 'version',
    }

    
    _created_on = None
    _effective_period_end_date = None
    _id = None
    _language = None
    _linked_space_id = None
    _period_start_date = None
    _planned_period_end_date = None
    _planned_purge_date = None
    _state = None
    _subscription_version = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.effective_period_end_date = kwargs.get('effective_period_end_date', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.period_start_date = kwargs.get('period_start_date', None)
        self.planned_period_end_date = kwargs.get('planned_period_end_date', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.subscription_version = kwargs.get('subscription_version', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionPeriodBill.

            

        :return: The created_on of this SubscriptionPeriodBill.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionPeriodBill.

            

        :param created_on: The created_on of this SubscriptionPeriodBill.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def effective_period_end_date(self):
        """Gets the effective_period_end_date of this SubscriptionPeriodBill.

            

        :return: The effective_period_end_date of this SubscriptionPeriodBill.
        :rtype: datetime
        """
        return self._effective_period_end_date

    @effective_period_end_date.setter
    def effective_period_end_date(self, effective_period_end_date):
        """Sets the effective_period_end_date of this SubscriptionPeriodBill.

            

        :param effective_period_end_date: The effective_period_end_date of this SubscriptionPeriodBill.
        :type: datetime
        """

        self._effective_period_end_date = effective_period_end_date
    
    @property
    def id(self):
        """Gets the id of this SubscriptionPeriodBill.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionPeriodBill.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionPeriodBill.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionPeriodBill.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this SubscriptionPeriodBill.

            

        :return: The language of this SubscriptionPeriodBill.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionPeriodBill.

            

        :param language: The language of this SubscriptionPeriodBill.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionPeriodBill.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionPeriodBill.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionPeriodBill.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionPeriodBill.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def period_start_date(self):
        """Gets the period_start_date of this SubscriptionPeriodBill.

            

        :return: The period_start_date of this SubscriptionPeriodBill.
        :rtype: datetime
        """
        return self._period_start_date

    @period_start_date.setter
    def period_start_date(self, period_start_date):
        """Sets the period_start_date of this SubscriptionPeriodBill.

            

        :param period_start_date: The period_start_date of this SubscriptionPeriodBill.
        :type: datetime
        """

        self._period_start_date = period_start_date
    
    @property
    def planned_period_end_date(self):
        """Gets the planned_period_end_date of this SubscriptionPeriodBill.

            

        :return: The planned_period_end_date of this SubscriptionPeriodBill.
        :rtype: datetime
        """
        return self._planned_period_end_date

    @planned_period_end_date.setter
    def planned_period_end_date(self, planned_period_end_date):
        """Sets the planned_period_end_date of this SubscriptionPeriodBill.

            

        :param planned_period_end_date: The planned_period_end_date of this SubscriptionPeriodBill.
        :type: datetime
        """

        self._planned_period_end_date = planned_period_end_date
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionPeriodBill.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionPeriodBill.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionPeriodBill.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionPeriodBill.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this SubscriptionPeriodBill.

            

        :return: The state of this SubscriptionPeriodBill.
        :rtype: SubscriptionPeriodBillState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionPeriodBill.

            

        :param state: The state of this SubscriptionPeriodBill.
        :type: SubscriptionPeriodBillState
        """

        self._state = state
    
    @property
    def subscription_version(self):
        """Gets the subscription_version of this SubscriptionPeriodBill.

            

        :return: The subscription_version of this SubscriptionPeriodBill.
        :rtype: SubscriptionVersion
        """
        return self._subscription_version

    @subscription_version.setter
    def subscription_version(self, subscription_version):
        """Sets the subscription_version of this SubscriptionPeriodBill.

            

        :param subscription_version: The subscription_version of this SubscriptionPeriodBill.
        :type: SubscriptionVersion
        """

        self._subscription_version = subscription_version
    
    @property
    def version(self):
        """Gets the version of this SubscriptionPeriodBill.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionPeriodBill.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionPeriodBill.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionPeriodBill.
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
        if issubclass(SubscriptionPeriodBill, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionPeriodBill):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
