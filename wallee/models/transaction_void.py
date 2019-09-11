# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class TransactionVoid(TransactionAwareEntity):

    swagger_types = {
    
        'created_by': 'int',
        'created_on': 'datetime',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'labels': 'list[Label]',
        'language': 'str',
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
        'created_by': 'createdBy','created_on': 'createdOn','failed_on': 'failedOn','failure_reason': 'failureReason','labels': 'labels','language': 'language','mode': 'mode','next_update_on': 'nextUpdateOn','planned_purge_date': 'plannedPurgeDate','processor_reference': 'processorReference','space_view_id': 'spaceViewId','state': 'state','succeeded_on': 'succeededOn','timeout_on': 'timeoutOn','transaction': 'transaction','version': 'version',
    }

    
    _created_by = None
    _created_on = None
    _failed_on = None
    _failure_reason = None
    _labels = None
    _language = None
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
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
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
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def created_by(self):
        """Gets the created_by of this TransactionVoid.

            

        :return: The created_by of this TransactionVoid.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransactionVoid.

            

        :param created_by: The created_by of this TransactionVoid.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionVoid.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionVoid.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this TransactionVoid.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def failed_on(self):
        """Gets the failed_on of this TransactionVoid.

            

        :return: The failed_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this TransactionVoid.

            

        :param failed_on: The failed_on of this TransactionVoid.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this TransactionVoid.

            

        :return: The failure_reason of this TransactionVoid.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this TransactionVoid.

            

        :param failure_reason: The failure_reason of this TransactionVoid.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def labels(self):
        """Gets the labels of this TransactionVoid.

            

        :return: The labels of this TransactionVoid.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TransactionVoid.

            

        :param labels: The labels of this TransactionVoid.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this TransactionVoid.

            

        :return: The language of this TransactionVoid.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionVoid.

            

        :param language: The language of this TransactionVoid.
        :type: str
        """

        self._language = language
    
    @property
    def mode(self):
        """Gets the mode of this TransactionVoid.

            

        :return: The mode of this TransactionVoid.
        :rtype: TransactionVoidMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TransactionVoid.

            

        :param mode: The mode of this TransactionVoid.
        :type: TransactionVoidMode
        """

        self._mode = mode
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this TransactionVoid.

            

        :return: The next_update_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this TransactionVoid.

            

        :param next_update_on: The next_update_on of this TransactionVoid.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionVoid.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TransactionVoid.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionVoid.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionVoid.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processor_reference(self):
        """Gets the processor_reference of this TransactionVoid.

            

        :return: The processor_reference of this TransactionVoid.
        :rtype: str
        """
        return self._processor_reference

    @processor_reference.setter
    def processor_reference(self, processor_reference):
        """Sets the processor_reference of this TransactionVoid.

            

        :param processor_reference: The processor_reference of this TransactionVoid.
        :type: str
        """

        self._processor_reference = processor_reference
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionVoid.

            

        :return: The space_view_id of this TransactionVoid.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionVoid.

            

        :param space_view_id: The space_view_id of this TransactionVoid.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this TransactionVoid.

            

        :return: The state of this TransactionVoid.
        :rtype: TransactionVoidState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionVoid.

            

        :param state: The state of this TransactionVoid.
        :type: TransactionVoidState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this TransactionVoid.

            

        :return: The succeeded_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this TransactionVoid.

            

        :param succeeded_on: The succeeded_on of this TransactionVoid.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this TransactionVoid.

            

        :return: The timeout_on of this TransactionVoid.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this TransactionVoid.

            

        :param timeout_on: The timeout_on of this TransactionVoid.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def transaction(self):
        """Gets the transaction of this TransactionVoid.

            

        :return: The transaction of this TransactionVoid.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionVoid.

            

        :param transaction: The transaction of this TransactionVoid.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this TransactionVoid.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TransactionVoid.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionVoid.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
