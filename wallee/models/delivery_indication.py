# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class DeliveryIndication(TransactionAwareEntity):

    swagger_types = {
    
        'automatic_decision_reason': 'DeliveryIndicationDecisionReason',
        'automatically_decided_on': 'datetime',
        'completion': 'int',
        'created_on': 'datetime',
        'manual_decision_timeout_on': 'datetime',
        'manually_decided_by': 'int',
        'manually_decided_on': 'datetime',
        'planned_purge_date': 'datetime',
        'state': 'DeliveryIndicationState',
        'timeout_on': 'datetime',
        'transaction': 'Transaction',
    }

    attribute_map = {
        'automatic_decision_reason': 'automaticDecisionReason','automatically_decided_on': 'automaticallyDecidedOn','completion': 'completion','created_on': 'createdOn','manual_decision_timeout_on': 'manualDecisionTimeoutOn','manually_decided_by': 'manuallyDecidedBy','manually_decided_on': 'manuallyDecidedOn','planned_purge_date': 'plannedPurgeDate','state': 'state','timeout_on': 'timeoutOn','transaction': 'transaction',
    }

    
    _automatic_decision_reason = None
    _automatically_decided_on = None
    _completion = None
    _created_on = None
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
        self.manual_decision_timeout_on = kwargs.get('manual_decision_timeout_on', None)
        self.manually_decided_by = kwargs.get('manually_decided_by', None)
        self.manually_decided_on = kwargs.get('manually_decided_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.transaction = kwargs.get('transaction', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def automatic_decision_reason(self):
        """Gets the automatic_decision_reason of this DeliveryIndication.

            

        :return: The automatic_decision_reason of this DeliveryIndication.
        :rtype: DeliveryIndicationDecisionReason
        """
        return self._automatic_decision_reason

    @automatic_decision_reason.setter
    def automatic_decision_reason(self, automatic_decision_reason):
        """Sets the automatic_decision_reason of this DeliveryIndication.

            

        :param automatic_decision_reason: The automatic_decision_reason of this DeliveryIndication.
        :type: DeliveryIndicationDecisionReason
        """

        self._automatic_decision_reason = automatic_decision_reason
    
    @property
    def automatically_decided_on(self):
        """Gets the automatically_decided_on of this DeliveryIndication.

            

        :return: The automatically_decided_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._automatically_decided_on

    @automatically_decided_on.setter
    def automatically_decided_on(self, automatically_decided_on):
        """Sets the automatically_decided_on of this DeliveryIndication.

            

        :param automatically_decided_on: The automatically_decided_on of this DeliveryIndication.
        :type: datetime
        """

        self._automatically_decided_on = automatically_decided_on
    
    @property
    def completion(self):
        """Gets the completion of this DeliveryIndication.

            

        :return: The completion of this DeliveryIndication.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this DeliveryIndication.

            

        :param completion: The completion of this DeliveryIndication.
        :type: int
        """

        self._completion = completion
    
    @property
    def created_on(self):
        """Gets the created_on of this DeliveryIndication.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DeliveryIndication.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this DeliveryIndication.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def manual_decision_timeout_on(self):
        """Gets the manual_decision_timeout_on of this DeliveryIndication.

            

        :return: The manual_decision_timeout_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._manual_decision_timeout_on

    @manual_decision_timeout_on.setter
    def manual_decision_timeout_on(self, manual_decision_timeout_on):
        """Sets the manual_decision_timeout_on of this DeliveryIndication.

            

        :param manual_decision_timeout_on: The manual_decision_timeout_on of this DeliveryIndication.
        :type: datetime
        """

        self._manual_decision_timeout_on = manual_decision_timeout_on
    
    @property
    def manually_decided_by(self):
        """Gets the manually_decided_by of this DeliveryIndication.

            

        :return: The manually_decided_by of this DeliveryIndication.
        :rtype: int
        """
        return self._manually_decided_by

    @manually_decided_by.setter
    def manually_decided_by(self, manually_decided_by):
        """Sets the manually_decided_by of this DeliveryIndication.

            

        :param manually_decided_by: The manually_decided_by of this DeliveryIndication.
        :type: int
        """

        self._manually_decided_by = manually_decided_by
    
    @property
    def manually_decided_on(self):
        """Gets the manually_decided_on of this DeliveryIndication.

            

        :return: The manually_decided_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._manually_decided_on

    @manually_decided_on.setter
    def manually_decided_on(self, manually_decided_on):
        """Sets the manually_decided_on of this DeliveryIndication.

            

        :param manually_decided_on: The manually_decided_on of this DeliveryIndication.
        :type: datetime
        """

        self._manually_decided_on = manually_decided_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DeliveryIndication.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DeliveryIndication.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DeliveryIndication.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DeliveryIndication.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this DeliveryIndication.

            

        :return: The state of this DeliveryIndication.
        :rtype: DeliveryIndicationState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DeliveryIndication.

            

        :param state: The state of this DeliveryIndication.
        :type: DeliveryIndicationState
        """

        self._state = state
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this DeliveryIndication.

            

        :return: The timeout_on of this DeliveryIndication.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this DeliveryIndication.

            

        :param timeout_on: The timeout_on of this DeliveryIndication.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def transaction(self):
        """Gets the transaction of this DeliveryIndication.

            

        :return: The transaction of this DeliveryIndication.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this DeliveryIndication.

            

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
