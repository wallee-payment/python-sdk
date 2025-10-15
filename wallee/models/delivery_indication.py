# coding: utf-8
import pprint
import six
from enum import Enum



class DeliveryIndication:

    swagger_types = {
    
        'automatic_decision_reason': 'DeliveryIndicationDecisionReason',
        'automatically_decided_on': 'datetime',
        'completion': 'int',
        'created_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'manual_decision_timeout_on': 'datetime',
        'manually_decided_by': 'int',
        'manually_decided_on': 'datetime',
        'planned_purge_date': 'datetime',
        'state': 'DeliveryIndicationState',
        'timeout_on': 'datetime',
        'transaction': 'Transaction',
    }

    attribute_map = {
        'automatic_decision_reason': 'automaticDecisionReason','automatically_decided_on': 'automaticallyDecidedOn','completion': 'completion','created_on': 'createdOn','id': 'id','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','manual_decision_timeout_on': 'manualDecisionTimeoutOn','manually_decided_by': 'manuallyDecidedBy','manually_decided_on': 'manuallyDecidedOn','planned_purge_date': 'plannedPurgeDate','state': 'state','timeout_on': 'timeoutOn','transaction': 'transaction',
    }

    
    _automatic_decision_reason = None
    _automatically_decided_on = None
    _completion = None
    _created_on = None
    _id = None
    _linked_space_id = None
    _linked_transaction = None
    _manual_decision_timeout_on = None
    _manually_decided_by = None
    _manually_decided_on = None
    _planned_purge_date = None
    _state = None
    _timeout_on = None
    _transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.automatic_decision_reason = kwargs.get('automatic_decision_reason', None)
        self.automatically_decided_on = kwargs.get('automatically_decided_on', None)
        self.completion = kwargs.get('completion', None)
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.manual_decision_timeout_on = kwargs.get('manual_decision_timeout_on', None)
        self.manually_decided_by = kwargs.get('manually_decided_by', None)
        self.manually_decided_on = kwargs.get('manually_decided_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.transaction = kwargs.get('transaction', None)
        

    
    @property
    def automatic_decision_reason(self):
        """Gets the automatic_decision_reason of this DeliveryIndication.

            The reason for the automatic system decision about the delivery indication.

        :return: The automatic_decision_reason of this DeliveryIndication.
        :rtype: DeliveryIndicationDecisionReason
        """
        return self._automatic_decision_reason

    @automatic_decision_reason.setter
    def automatic_decision_reason(self, automatic_decision_reason):
        """Sets the automatic_decision_reason of this DeliveryIndication.

            The reason for the automatic system decision about the delivery indication.

        :param automatic_decision_reason: The automatic_decision_reason of this DeliveryIndication.
        :type: DeliveryIndicationDecisionReason
        """

        self._automatic_decision_reason = automatic_decision_reason
    
    @property
    def automatically_decided_on(self):
        """Gets the automatically_decided_on of this DeliveryIndication.

            The date and time when an automatic decision was made.

        :return: The automatically_decided_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._automatically_decided_on

    @automatically_decided_on.setter
    def automatically_decided_on(self, automatically_decided_on):
        """Sets the automatically_decided_on of this DeliveryIndication.

            The date and time when an automatic decision was made.

        :param automatically_decided_on: The automatically_decided_on of this DeliveryIndication.
        :type: datetime
        """

        self._automatically_decided_on = automatically_decided_on
    
    @property
    def completion(self):
        """Gets the completion of this DeliveryIndication.

            The transaction completion that the delivery indication is linked to.

        :return: The completion of this DeliveryIndication.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this DeliveryIndication.

            The transaction completion that the delivery indication is linked to.

        :param completion: The completion of this DeliveryIndication.
        :type: int
        """

        self._completion = completion
    
    @property
    def created_on(self):
        """Gets the created_on of this DeliveryIndication.

            The date and time when the object was created.

        :return: The created_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeliveryIndication.

            The date and time when the object was created.

        :param created_on: The created_on of this DeliveryIndication.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this DeliveryIndication.

            A unique identifier for the object.

        :return: The id of this DeliveryIndication.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DeliveryIndication.

            A unique identifier for the object.

        :param id: The id of this DeliveryIndication.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DeliveryIndication.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this DeliveryIndication.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DeliveryIndication.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this DeliveryIndication.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this DeliveryIndication.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this DeliveryIndication.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this DeliveryIndication.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this DeliveryIndication.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def manual_decision_timeout_on(self):
        """Gets the manual_decision_timeout_on of this DeliveryIndication.

            The date and time by which a decision must be made before the system automatically proceeds according to the connector's predefined settings.

        :return: The manual_decision_timeout_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._manual_decision_timeout_on

    @manual_decision_timeout_on.setter
    def manual_decision_timeout_on(self, manual_decision_timeout_on):
        """Sets the manual_decision_timeout_on of this DeliveryIndication.

            The date and time by which a decision must be made before the system automatically proceeds according to the connector's predefined settings.

        :param manual_decision_timeout_on: The manual_decision_timeout_on of this DeliveryIndication.
        :type: datetime
        """

        self._manual_decision_timeout_on = manual_decision_timeout_on
    
    @property
    def manually_decided_by(self):
        """Gets the manually_decided_by of this DeliveryIndication.

            The ID of the user who manually decided the delivery indication's state.

        :return: The manually_decided_by of this DeliveryIndication.
        :rtype: int
        """
        return self._manually_decided_by

    @manually_decided_by.setter
    def manually_decided_by(self, manually_decided_by):
        """Sets the manually_decided_by of this DeliveryIndication.

            The ID of the user who manually decided the delivery indication's state.

        :param manually_decided_by: The manually_decided_by of this DeliveryIndication.
        :type: int
        """

        self._manually_decided_by = manually_decided_by
    
    @property
    def manually_decided_on(self):
        """Gets the manually_decided_on of this DeliveryIndication.

            The date and time when a manual decision was made.

        :return: The manually_decided_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._manually_decided_on

    @manually_decided_on.setter
    def manually_decided_on(self, manually_decided_on):
        """Sets the manually_decided_on of this DeliveryIndication.

            The date and time when a manual decision was made.

        :param manually_decided_on: The manually_decided_on of this DeliveryIndication.
        :type: datetime
        """

        self._manually_decided_on = manually_decided_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DeliveryIndication.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this DeliveryIndication.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DeliveryIndication.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this DeliveryIndication.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this DeliveryIndication.

            The object's current state.

        :return: The state of this DeliveryIndication.
        :rtype: DeliveryIndicationState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeliveryIndication.

            The object's current state.

        :param state: The state of this DeliveryIndication.
        :type: DeliveryIndicationState
        """

        self._state = state
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this DeliveryIndication.

            The date and time when the delivery indication will expire.

        :return: The timeout_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this DeliveryIndication.

            The date and time when the delivery indication will expire.

        :param timeout_on: The timeout_on of this DeliveryIndication.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def transaction(self):
        """Gets the transaction of this DeliveryIndication.

            The payment transaction that the delivery indication is linked to.

        :return: The transaction of this DeliveryIndication.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this DeliveryIndication.

            The payment transaction that the delivery indication is linked to.

        :param transaction: The transaction of this DeliveryIndication.
        :type: Transaction
        """

        self._transaction = transaction
    

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
        if issubclass(DeliveryIndication, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DeliveryIndication):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
