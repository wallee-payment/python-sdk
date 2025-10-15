# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionVoid:

    swagger_types = {
    
        'created_by': 'int',
        'created_on': 'datetime',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'labels': 'list[Label]',
        'language': 'str',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'mode': 'TransactionVoidMode',
        'next_update_on': 'datetime',
        'planned_purge_date': 'datetime',
        'processor_reference': 'str',
        'space_view_id': 'int',
        'state': 'TransactionVoidState',
        'succeeded_on': 'datetime',
        'timeout_on': 'datetime',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'created_by': 'createdBy','created_on': 'createdOn','failed_on': 'failedOn','failure_reason': 'failureReason','id': 'id','labels': 'labels','language': 'language','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','mode': 'mode','next_update_on': 'nextUpdateOn','planned_purge_date': 'plannedPurgeDate','processor_reference': 'processorReference','space_view_id': 'spaceViewId','state': 'state','succeeded_on': 'succeededOn','timeout_on': 'timeoutOn','transaction': 'transaction','version': 'version',
    }

    
    _created_by = None
    _created_on = None
    _failed_on = None
    _failure_reason = None
    _id = None
    _labels = None
    _language = None
    _linked_space_id = None
    _linked_transaction = None
    _mode = None
    _next_update_on = None
    _planned_purge_date = None
    _processor_reference = None
    _space_view_id = None
    _state = None
    _succeeded_on = None
    _timeout_on = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.mode = kwargs.get('mode', None)
        self.next_update_on = kwargs.get('next_update_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processor_reference = kwargs.get('processor_reference', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_by(self):
        """Gets the created_by of this TransactionVoid.

            The ID of the user the transaction void was created by.

        :return: The created_by of this TransactionVoid.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransactionVoid.

            The ID of the user the transaction void was created by.

        :param created_by: The created_by of this TransactionVoid.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionVoid.

            The date and time when the object was created.

        :return: The created_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionVoid.

            The date and time when the object was created.

        :param created_on: The created_on of this TransactionVoid.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def failed_on(self):
        """Gets the failed_on of this TransactionVoid.

            The date and time when the transaction void failed.

        :return: The failed_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this TransactionVoid.

            The date and time when the transaction void failed.

        :param failed_on: The failed_on of this TransactionVoid.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this TransactionVoid.

            The reason for the failure of the transaction void.

        :return: The failure_reason of this TransactionVoid.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this TransactionVoid.

            The reason for the failure of the transaction void.

        :param failure_reason: The failure_reason of this TransactionVoid.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this TransactionVoid.

            A unique identifier for the object.

        :return: The id of this TransactionVoid.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionVoid.

            A unique identifier for the object.

        :param id: The id of this TransactionVoid.
        :type: int
        """

        self._id = id
    
    @property
    def labels(self):
        """Gets the labels of this TransactionVoid.

            The labels providing additional information about the object.

        :return: The labels of this TransactionVoid.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TransactionVoid.

            The labels providing additional information about the object.

        :param labels: The labels of this TransactionVoid.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this TransactionVoid.

            The language that is linked to the object.

        :return: The language of this TransactionVoid.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionVoid.

            The language that is linked to the object.

        :param language: The language of this TransactionVoid.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this TransactionVoid.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this TransactionVoid.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this TransactionVoid.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this TransactionVoid.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this TransactionVoid.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this TransactionVoid.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this TransactionVoid.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this TransactionVoid.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def mode(self):
        """Gets the mode of this TransactionVoid.

            The mode of transaction void, such as online or offline, determining how the void process is executed.

        :return: The mode of this TransactionVoid.
        :rtype: TransactionVoidMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TransactionVoid.

            The mode of transaction void, such as online or offline, determining how the void process is executed.

        :param mode: The mode of this TransactionVoid.
        :type: TransactionVoidMode
        """

        self._mode = mode
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this TransactionVoid.

            The date and time when the next update of the object's state is planned.

        :return: The next_update_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this TransactionVoid.

            The date and time when the next update of the object's state is planned.

        :param next_update_on: The next_update_on of this TransactionVoid.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionVoid.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this TransactionVoid.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionVoid.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionVoid.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processor_reference(self):
        """Gets the processor_reference of this TransactionVoid.

            The reference ID provided by the payment processor, used to trace the void through the external payment system.

        :return: The processor_reference of this TransactionVoid.
        :rtype: str
        """
        return self._processor_reference

    @processor_reference.setter
    def processor_reference(self, processor_reference):
        """Sets the processor_reference of this TransactionVoid.

            The reference ID provided by the payment processor, used to trace the void through the external payment system.

        :param processor_reference: The processor_reference of this TransactionVoid.
        :type: str
        """

        self._processor_reference = processor_reference
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionVoid.

            The ID of the space view this object is linked to.

        :return: The space_view_id of this TransactionVoid.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionVoid.

            The ID of the space view this object is linked to.

        :param space_view_id: The space_view_id of this TransactionVoid.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this TransactionVoid.

            The object's current state.

        :return: The state of this TransactionVoid.
        :rtype: TransactionVoidState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionVoid.

            The object's current state.

        :param state: The state of this TransactionVoid.
        :type: TransactionVoidState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this TransactionVoid.

            The date and time when the transaction void succeeded.

        :return: The succeeded_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this TransactionVoid.

            The date and time when the transaction void succeeded.

        :param succeeded_on: The succeeded_on of this TransactionVoid.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this TransactionVoid.

            The date and time when the object will expire.

        :return: The timeout_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this TransactionVoid.

            The date and time when the object will expire.

        :param timeout_on: The timeout_on of this TransactionVoid.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def transaction(self):
        """Gets the transaction of this TransactionVoid.

            The transaction that the void belongs to.

        :return: The transaction of this TransactionVoid.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionVoid.

            The transaction that the void belongs to.

        :param transaction: The transaction of this TransactionVoid.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this TransactionVoid.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this TransactionVoid.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionVoid.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this TransactionVoid.
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
        if issubclass(TransactionVoid, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionVoid):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
