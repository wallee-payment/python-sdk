# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionSuspension:

    swagger_types = {
    
        'created_on': 'datetime',
        'effective_end_date': 'datetime',
        'end_action': 'SubscriptionSuspensionAction',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'note': 'str',
        'period_bill': 'int',
        'planned_end_date': 'datetime',
        'planned_purge_date': 'datetime',
        'reason': 'SubscriptionSuspensionReason',
        'state': 'SubscriptionSuspensionState',
        'subscription': 'int',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','effective_end_date': 'effectiveEndDate','end_action': 'endAction','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','note': 'note','period_bill': 'periodBill','planned_end_date': 'plannedEndDate','planned_purge_date': 'plannedPurgeDate','reason': 'reason','state': 'state','subscription': 'subscription','version': 'version',
    }

    
    _created_on = None
    _effective_end_date = None
    _end_action = None
    _id = None
    _language = None
    _linked_space_id = None
    _note = None
    _period_bill = None
    _planned_end_date = None
    _planned_purge_date = None
    _reason = None
    _state = None
    _subscription = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.effective_end_date = kwargs.get('effective_end_date', None)
        self.end_action = kwargs.get('end_action', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.note = kwargs.get('note', None)
        self.period_bill = kwargs.get('period_bill', None)
        self.planned_end_date = kwargs.get('planned_end_date', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.reason = kwargs.get('reason', None)
        self.state = kwargs.get('state', None)
        self.subscription = kwargs.get('subscription', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionSuspension.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this SubscriptionSuspension.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionSuspension.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this SubscriptionSuspension.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def effective_end_date(self):
        """Gets the effective_end_date of this SubscriptionSuspension.

            

        :return: The effective_end_date of this SubscriptionSuspension.
        :rtype: datetime
        """
        return self._effective_end_date

    @effective_end_date.setter
    def effective_end_date(self, effective_end_date):
        """Sets the effective_end_date of this SubscriptionSuspension.

            

        :param effective_end_date: The effective_end_date of this SubscriptionSuspension.
        :type: datetime
        """

        self._effective_end_date = effective_end_date
    
    @property
    def end_action(self):
        """Gets the end_action of this SubscriptionSuspension.

            When the suspension reaches the planned end date the end action will be carried out. This action is only executed when the suspension is ended automatically based on the end date.

        :return: The end_action of this SubscriptionSuspension.
        :rtype: SubscriptionSuspensionAction
        """
        return self._end_action

    @end_action.setter
    def end_action(self, end_action):
        """Sets the end_action of this SubscriptionSuspension.

            When the suspension reaches the planned end date the end action will be carried out. This action is only executed when the suspension is ended automatically based on the end date.

        :param end_action: The end_action of this SubscriptionSuspension.
        :type: SubscriptionSuspensionAction
        """

        self._end_action = end_action
    
    @property
    def id(self):
        """Gets the id of this SubscriptionSuspension.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionSuspension.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionSuspension.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionSuspension.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this SubscriptionSuspension.

            

        :return: The language of this SubscriptionSuspension.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriptionSuspension.

            

        :param language: The language of this SubscriptionSuspension.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionSuspension.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionSuspension.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionSuspension.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionSuspension.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def note(self):
        """Gets the note of this SubscriptionSuspension.

            The note may contain some internal information for the suspension. The note will not be disclosed to the subscriber.

        :return: The note of this SubscriptionSuspension.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this SubscriptionSuspension.

            The note may contain some internal information for the suspension. The note will not be disclosed to the subscriber.

        :param note: The note of this SubscriptionSuspension.
        :type: str
        """
        if note is not None and len(note) > 300:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `300`")

        self._note = note
    
    @property
    def period_bill(self):
        """Gets the period_bill of this SubscriptionSuspension.

            

        :return: The period_bill of this SubscriptionSuspension.
        :rtype: int
        """
        return self._period_bill

    @period_bill.setter
    def period_bill(self, period_bill):
        """Sets the period_bill of this SubscriptionSuspension.

            

        :param period_bill: The period_bill of this SubscriptionSuspension.
        :type: int
        """

        self._period_bill = period_bill
    
    @property
    def planned_end_date(self):
        """Gets the planned_end_date of this SubscriptionSuspension.

            The planned end date of the suspension identifies the date on which the suspension will be ended automatically.

        :return: The planned_end_date of this SubscriptionSuspension.
        :rtype: datetime
        """
        return self._planned_end_date

    @planned_end_date.setter
    def planned_end_date(self, planned_end_date):
        """Sets the planned_end_date of this SubscriptionSuspension.

            The planned end date of the suspension identifies the date on which the suspension will be ended automatically.

        :param planned_end_date: The planned_end_date of this SubscriptionSuspension.
        :type: datetime
        """

        self._planned_end_date = planned_end_date
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionSuspension.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionSuspension.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionSuspension.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionSuspension.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def reason(self):
        """Gets the reason of this SubscriptionSuspension.

            The suspension reason indicates why a suspension has been created.

        :return: The reason of this SubscriptionSuspension.
        :rtype: SubscriptionSuspensionReason
        """
        return self._reason

    @reason.setter
    def reason(self, reason):
        """Sets the reason of this SubscriptionSuspension.

            The suspension reason indicates why a suspension has been created.

        :param reason: The reason of this SubscriptionSuspension.
        :type: SubscriptionSuspensionReason
        """

        self._reason = reason
    
    @property
    def state(self):
        """Gets the state of this SubscriptionSuspension.

            

        :return: The state of this SubscriptionSuspension.
        :rtype: SubscriptionSuspensionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionSuspension.

            

        :param state: The state of this SubscriptionSuspension.
        :type: SubscriptionSuspensionState
        """

        self._state = state
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionSuspension.

            

        :return: The subscription of this SubscriptionSuspension.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionSuspension.

            

        :param subscription: The subscription of this SubscriptionSuspension.
        :type: int
        """

        self._subscription = subscription
    
    @property
    def version(self):
        """Gets the version of this SubscriptionSuspension.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionSuspension.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionSuspension.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionSuspension.
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
        if issubclass(SubscriptionSuspension, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionSuspension):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
