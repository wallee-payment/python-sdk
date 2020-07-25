# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionSuspensionCreate:

    swagger_types = {
    
        'end_action': 'SubscriptionSuspensionAction',
        'note': 'str',
        'planned_end_date': 'datetime',
        'subscription': 'int',
    }

    attribute_map = {
        'end_action': 'endAction','note': 'note','planned_end_date': 'plannedEndDate','subscription': 'subscription',
    }

    
    _end_action = None
    _note = None
    _planned_end_date = None
    _subscription = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.end_action = kwargs.get('end_action')

        self.note = kwargs.get('note', None)
        self.planned_end_date = kwargs.get('planned_end_date')

        self.subscription = kwargs.get('subscription')

        

    
    @property
    def end_action(self):
        """Gets the end_action of this SubscriptionSuspensionCreate.

            When the suspension reaches the planned end date the end action will be carried out. This action is only executed when the suspension is ended automatically based on the end date.

        :return: The end_action of this SubscriptionSuspensionCreate.
        :rtype: SubscriptionSuspensionAction
        """
        return self._end_action

    @end_action.setter
    def end_action(self, end_action):
        """Sets the end_action of this SubscriptionSuspensionCreate.

            When the suspension reaches the planned end date the end action will be carried out. This action is only executed when the suspension is ended automatically based on the end date.

        :param end_action: The end_action of this SubscriptionSuspensionCreate.
        :type: SubscriptionSuspensionAction
        """
        if end_action is None:
            raise ValueError("Invalid value for `end_action`, must not be `None`")

        self._end_action = end_action
    
    @property
    def note(self):
        """Gets the note of this SubscriptionSuspensionCreate.

            The note may contain some internal information for the suspension. The note will not be disclosed to the subscriber.

        :return: The note of this SubscriptionSuspensionCreate.
        :rtype: str
        """
        return self._note

    @note.setter
    def note(self, note):
        """Sets the note of this SubscriptionSuspensionCreate.

            The note may contain some internal information for the suspension. The note will not be disclosed to the subscriber.

        :param note: The note of this SubscriptionSuspensionCreate.
        :type: str
        """
        if note is not None and len(note) > 300:
            raise ValueError("Invalid value for `note`, length must be less than or equal to `300`")

        self._note = note
    
    @property
    def planned_end_date(self):
        """Gets the planned_end_date of this SubscriptionSuspensionCreate.

            The planned end date of the suspension identifies the date on which the suspension will be ended automatically.

        :return: The planned_end_date of this SubscriptionSuspensionCreate.
        :rtype: datetime
        """
        return self._planned_end_date

    @planned_end_date.setter
    def planned_end_date(self, planned_end_date):
        """Sets the planned_end_date of this SubscriptionSuspensionCreate.

            The planned end date of the suspension identifies the date on which the suspension will be ended automatically.

        :param planned_end_date: The planned_end_date of this SubscriptionSuspensionCreate.
        :type: datetime
        """
        if planned_end_date is None:
            raise ValueError("Invalid value for `planned_end_date`, must not be `None`")

        self._planned_end_date = planned_end_date
    
    @property
    def subscription(self):
        """Gets the subscription of this SubscriptionSuspensionCreate.

            

        :return: The subscription of this SubscriptionSuspensionCreate.
        :rtype: int
        """
        return self._subscription

    @subscription.setter
    def subscription(self, subscription):
        """Sets the subscription of this SubscriptionSuspensionCreate.

            

        :param subscription: The subscription of this SubscriptionSuspensionCreate.
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
        if issubclass(SubscriptionSuspensionCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionSuspensionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
