# coding: utf-8
import pprint
import six
from enum import Enum



class Charge:

    swagger_types = {
    
        'created_on': 'datetime',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'space_view_id': 'int',
        'state': 'ChargeState',
        'time_zone': 'str',
        'timeout_on': 'datetime',
        'transaction': 'Transaction',
        'type': 'ChargeType',
        'user_failure_message': 'str',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','failure_reason': 'failureReason','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','space_view_id': 'spaceViewId','state': 'state','time_zone': 'timeZone','timeout_on': 'timeoutOn','transaction': 'transaction','type': 'type','user_failure_message': 'userFailureMessage','version': 'version',
    }

    
    _created_on = None
    _failure_reason = None
    _id = None
    _language = None
    _linked_space_id = None
    _planned_purge_date = None
    _space_view_id = None
    _state = None
    _time_zone = None
    _timeout_on = None
    _transaction = None
    _type = None
    _user_failure_message = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.transaction = kwargs.get('transaction', None)
        self.type = kwargs.get('type', None)
        self.user_failure_message = kwargs.get('user_failure_message', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this Charge.

            The date and time when the object was created.

        :return: The created_on of this Charge.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Charge.

            The date and time when the object was created.

        :param created_on: The created_on of this Charge.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this Charge.

            The reason for the failure of the charge.

        :return: The failure_reason of this Charge.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this Charge.

            The reason for the failure of the charge.

        :param failure_reason: The failure_reason of this Charge.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this Charge.

            A unique identifier for the object.

        :return: The id of this Charge.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Charge.

            A unique identifier for the object.

        :param id: The id of this Charge.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this Charge.

            The language that is linked to the object.

        :return: The language of this Charge.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Charge.

            The language that is linked to the object.

        :param language: The language of this Charge.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Charge.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this Charge.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Charge.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this Charge.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Charge.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this Charge.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Charge.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this Charge.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this Charge.

            The ID of the space view this object is linked to.

        :return: The space_view_id of this Charge.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this Charge.

            The ID of the space view this object is linked to.

        :param space_view_id: The space_view_id of this Charge.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this Charge.

            The object's current state.

        :return: The state of this Charge.
        :rtype: ChargeState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Charge.

            The object's current state.

        :param state: The state of this Charge.
        :type: ChargeState
        """

        self._state = state
    
    @property
    def time_zone(self):
        """Gets the time_zone of this Charge.

            The time zone that this object is associated with.

        :return: The time_zone of this Charge.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Charge.

            The time zone that this object is associated with.

        :param time_zone: The time_zone of this Charge.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this Charge.

            The date and time when the charge will expire.

        :return: The timeout_on of this Charge.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this Charge.

            The date and time when the charge will expire.

        :param timeout_on: The timeout_on of this Charge.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def transaction(self):
        """Gets the transaction of this Charge.

            The transaction that the charge belongs to.

        :return: The transaction of this Charge.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this Charge.

            The transaction that the charge belongs to.

        :param transaction: The transaction of this Charge.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def type(self):
        """Gets the type of this Charge.

            The type specifying how the customer was charged.

        :return: The type of this Charge.
        :rtype: ChargeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Charge.

            The type specifying how the customer was charged.

        :param type: The type of this Charge.
        :type: ChargeType
        """

        self._type = type
    
    @property
    def user_failure_message(self):
        """Gets the user_failure_message of this Charge.

            The message that can be displayed to the customer explaining why the charge failed, in the customer's language.

        :return: The user_failure_message of this Charge.
        :rtype: str
        """
        return self._user_failure_message

    @user_failure_message.setter
    def user_failure_message(self, user_failure_message):
        """Sets the user_failure_message of this Charge.

            The message that can be displayed to the customer explaining why the charge failed, in the customer's language.

        :param user_failure_message: The user_failure_message of this Charge.
        :type: str
        """

        self._user_failure_message = user_failure_message
    
    @property
    def version(self):
        """Gets the version of this Charge.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this Charge.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Charge.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this Charge.
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
        if issubclass(Charge, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Charge):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
