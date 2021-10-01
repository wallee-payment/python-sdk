# coding: utf-8
import pprint
import six
from enum import Enum



class DebtCollectionCase:

    swagger_types = {
    
        'amount': 'float',
        'billing_address': 'Address',
        'closed_on': 'datetime',
        'collector_configuration': 'DebtCollectorConfiguration',
        'contract_date': 'datetime',
        'created_on': 'datetime',
        'creator': 'int',
        'currency': 'str',
        'due_date': 'datetime',
        'environment': 'DebtCollectionEnvironment',
        'external_id': 'str',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'labels': 'list[Label]',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'next_attempt_on': 'datetime',
        'planned_purge_date': 'datetime',
        'processing_started_on': 'datetime',
        'processing_timeout_on': 'datetime',
        'reference': 'str',
        'review_started_on': 'datetime',
        'reviewed_on': 'datetime',
        'reviewer': 'int',
        'source': 'DebtCollectionCaseSource',
        'source_entity_id': 'int',
        'space_view_id': 'int',
        'state': 'DebtCollectionCaseState',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','billing_address': 'billingAddress','closed_on': 'closedOn','collector_configuration': 'collectorConfiguration','contract_date': 'contractDate','created_on': 'createdOn','creator': 'creator','currency': 'currency','due_date': 'dueDate','environment': 'environment','external_id': 'externalId','failed_on': 'failedOn','failure_reason': 'failureReason','id': 'id','labels': 'labels','language': 'language','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','next_attempt_on': 'nextAttemptOn','planned_purge_date': 'plannedPurgeDate','processing_started_on': 'processingStartedOn','processing_timeout_on': 'processingTimeoutOn','reference': 'reference','review_started_on': 'reviewStartedOn','reviewed_on': 'reviewedOn','reviewer': 'reviewer','source': 'source','source_entity_id': 'sourceEntityId','space_view_id': 'spaceViewId','state': 'state','version': 'version',
    }

    
    _amount = None
    _billing_address = None
    _closed_on = None
    _collector_configuration = None
    _contract_date = None
    _created_on = None
    _creator = None
    _currency = None
    _due_date = None
    _environment = None
    _external_id = None
    _failed_on = None
    _failure_reason = None
    _id = None
    _labels = None
    _language = None
    _line_items = None
    _linked_space_id = None
    _next_attempt_on = None
    _planned_purge_date = None
    _processing_started_on = None
    _processing_timeout_on = None
    _reference = None
    _review_started_on = None
    _reviewed_on = None
    _reviewer = None
    _source = None
    _source_entity_id = None
    _space_view_id = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.closed_on = kwargs.get('closed_on', None)
        self.collector_configuration = kwargs.get('collector_configuration', None)
        self.contract_date = kwargs.get('contract_date', None)
        self.created_on = kwargs.get('created_on', None)
        self.creator = kwargs.get('creator', None)
        self.currency = kwargs.get('currency', None)
        self.due_date = kwargs.get('due_date', None)
        self.environment = kwargs.get('environment', None)
        self.external_id = kwargs.get('external_id', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.next_attempt_on = kwargs.get('next_attempt_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_started_on = kwargs.get('processing_started_on', None)
        self.processing_timeout_on = kwargs.get('processing_timeout_on', None)
        self.reference = kwargs.get('reference', None)
        self.review_started_on = kwargs.get('review_started_on', None)
        self.reviewed_on = kwargs.get('reviewed_on', None)
        self.reviewer = kwargs.get('reviewer', None)
        self.source = kwargs.get('source', None)
        self.source_entity_id = kwargs.get('source_entity_id', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this DebtCollectionCase.

            The amount is the total amount of the not paid items. The amount cannot be change once the case is reviewed.

        :return: The amount of this DebtCollectionCase.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this DebtCollectionCase.

            The amount is the total amount of the not paid items. The amount cannot be change once the case is reviewed.

        :param amount: The amount of this DebtCollectionCase.
        :type: float
        """

        self._amount = amount
    
    @property
    def billing_address(self):
        """Gets the billing_address of this DebtCollectionCase.

            The billing address of the case identifies the debtor.

        :return: The billing_address of this DebtCollectionCase.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this DebtCollectionCase.

            The billing address of the case identifies the debtor.

        :param billing_address: The billing_address of this DebtCollectionCase.
        :type: Address
        """

        self._billing_address = billing_address
    
    @property
    def closed_on(self):
        """Gets the closed_on of this DebtCollectionCase.

            The closed on date indicates when the case is closed on.

        :return: The closed_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._closed_on

    @closed_on.setter
    def closed_on(self, closed_on):
        """Sets the closed_on of this DebtCollectionCase.

            The closed on date indicates when the case is closed on.

        :param closed_on: The closed_on of this DebtCollectionCase.
        :type: datetime
        """

        self._closed_on = closed_on
    
    @property
    def collector_configuration(self):
        """Gets the collector_configuration of this DebtCollectionCase.

            The collector configuration determines how the debt collection case is processed.

        :return: The collector_configuration of this DebtCollectionCase.
        :rtype: DebtCollectorConfiguration
        """
        return self._collector_configuration

    @collector_configuration.setter
    def collector_configuration(self, collector_configuration):
        """Sets the collector_configuration of this DebtCollectionCase.

            The collector configuration determines how the debt collection case is processed.

        :param collector_configuration: The collector_configuration of this DebtCollectionCase.
        :type: DebtCollectorConfiguration
        """

        self._collector_configuration = collector_configuration
    
    @property
    def contract_date(self):
        """Gets the contract_date of this DebtCollectionCase.

            The contract date is the date on which the contract with the debtor was signed on.

        :return: The contract_date of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._contract_date

    @contract_date.setter
    def contract_date(self, contract_date):
        """Sets the contract_date of this DebtCollectionCase.

            The contract date is the date on which the contract with the debtor was signed on.

        :param contract_date: The contract_date of this DebtCollectionCase.
        :type: datetime
        """

        self._contract_date = contract_date
    
    @property
    def created_on(self):
        """Gets the created_on of this DebtCollectionCase.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this DebtCollectionCase.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this DebtCollectionCase.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def creator(self):
        """Gets the creator of this DebtCollectionCase.

            The creator references the user which has created the debt collection case.

        :return: The creator of this DebtCollectionCase.
        :rtype: int
        """
        return self._creator

    @creator.setter
    def creator(self, creator):
        """Sets the creator of this DebtCollectionCase.

            The creator references the user which has created the debt collection case.

        :param creator: The creator of this DebtCollectionCase.
        :type: int
        """

        self._creator = creator
    
    @property
    def currency(self):
        """Gets the currency of this DebtCollectionCase.

            The currency defines the billing currency of the debt collection case.

        :return: The currency of this DebtCollectionCase.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this DebtCollectionCase.

            The currency defines the billing currency of the debt collection case.

        :param currency: The currency of this DebtCollectionCase.
        :type: str
        """

        self._currency = currency
    
    @property
    def due_date(self):
        """Gets the due_date of this DebtCollectionCase.

            The due date indicates the date on which the amount receivable was due. This date has to be always in the past.

        :return: The due_date of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._due_date

    @due_date.setter
    def due_date(self, due_date):
        """Sets the due_date of this DebtCollectionCase.

            The due date indicates the date on which the amount receivable was due. This date has to be always in the past.

        :param due_date: The due_date of this DebtCollectionCase.
        :type: datetime
        """

        self._due_date = due_date
    
    @property
    def environment(self):
        """Gets the environment of this DebtCollectionCase.

            The environment in which this case will be processed. There must be a debt collector configuration present which supports the chosen environment.

        :return: The environment of this DebtCollectionCase.
        :rtype: DebtCollectionEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this DebtCollectionCase.

            The environment in which this case will be processed. There must be a debt collector configuration present which supports the chosen environment.

        :param environment: The environment of this DebtCollectionCase.
        :type: DebtCollectionEnvironment
        """

        self._environment = environment
    
    @property
    def external_id(self):
        """Gets the external_id of this DebtCollectionCase.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this DebtCollectionCase.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this DebtCollectionCase.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this DebtCollectionCase.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def failed_on(self):
        """Gets the failed_on of this DebtCollectionCase.

            The failed on date indicates when the case is failed on.

        :return: The failed_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this DebtCollectionCase.

            The failed on date indicates when the case is failed on.

        :param failed_on: The failed_on of this DebtCollectionCase.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this DebtCollectionCase.

            

        :return: The failure_reason of this DebtCollectionCase.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this DebtCollectionCase.

            

        :param failure_reason: The failure_reason of this DebtCollectionCase.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this DebtCollectionCase.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DebtCollectionCase.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DebtCollectionCase.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DebtCollectionCase.
        :type: int
        """

        self._id = id
    
    @property
    def labels(self):
        """Gets the labels of this DebtCollectionCase.

            

        :return: The labels of this DebtCollectionCase.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this DebtCollectionCase.

            

        :param labels: The labels of this DebtCollectionCase.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this DebtCollectionCase.

            The language indicates the language to be used in the communication with the debtor.

        :return: The language of this DebtCollectionCase.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this DebtCollectionCase.

            The language indicates the language to be used in the communication with the debtor.

        :param language: The language of this DebtCollectionCase.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this DebtCollectionCase.

            The line items of the debt collection case will be shown on documents sent to the debtor and the total of them makes up total amount to collect.

        :return: The line_items of this DebtCollectionCase.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this DebtCollectionCase.

            The line items of the debt collection case will be shown on documents sent to the debtor and the total of them makes up total amount to collect.

        :param line_items: The line_items of this DebtCollectionCase.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this DebtCollectionCase.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this DebtCollectionCase.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this DebtCollectionCase.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this DebtCollectionCase.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def next_attempt_on(self):
        """Gets the next_attempt_on of this DebtCollectionCase.

            

        :return: The next_attempt_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._next_attempt_on

    @next_attempt_on.setter
    def next_attempt_on(self, next_attempt_on):
        """Sets the next_attempt_on of this DebtCollectionCase.

            

        :param next_attempt_on: The next_attempt_on of this DebtCollectionCase.
        :type: datetime
        """

        self._next_attempt_on = next_attempt_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this DebtCollectionCase.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this DebtCollectionCase.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this DebtCollectionCase.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_started_on(self):
        """Gets the processing_started_on of this DebtCollectionCase.

            The processing started on date indicates the date on which the processing of the case started on.

        :return: The processing_started_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._processing_started_on

    @processing_started_on.setter
    def processing_started_on(self, processing_started_on):
        """Sets the processing_started_on of this DebtCollectionCase.

            The processing started on date indicates the date on which the processing of the case started on.

        :param processing_started_on: The processing_started_on of this DebtCollectionCase.
        :type: datetime
        """

        self._processing_started_on = processing_started_on
    
    @property
    def processing_timeout_on(self):
        """Gets the processing_timeout_on of this DebtCollectionCase.

            

        :return: The processing_timeout_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._processing_timeout_on

    @processing_timeout_on.setter
    def processing_timeout_on(self, processing_timeout_on):
        """Sets the processing_timeout_on of this DebtCollectionCase.

            

        :param processing_timeout_on: The processing_timeout_on of this DebtCollectionCase.
        :type: datetime
        """

        self._processing_timeout_on = processing_timeout_on
    
    @property
    def reference(self):
        """Gets the reference of this DebtCollectionCase.

            The case reference is used in the communication with the debtor. It should be unique and it should be linkable with the source of the debt collection case.

        :return: The reference of this DebtCollectionCase.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this DebtCollectionCase.

            The case reference is used in the communication with the debtor. It should be unique and it should be linkable with the source of the debt collection case.

        :param reference: The reference of this DebtCollectionCase.
        :type: str
        """

        self._reference = reference
    
    @property
    def review_started_on(self):
        """Gets the review_started_on of this DebtCollectionCase.

            

        :return: The review_started_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._review_started_on

    @review_started_on.setter
    def review_started_on(self, review_started_on):
        """Sets the review_started_on of this DebtCollectionCase.

            

        :param review_started_on: The review_started_on of this DebtCollectionCase.
        :type: datetime
        """

        self._review_started_on = review_started_on
    
    @property
    def reviewed_on(self):
        """Gets the reviewed_on of this DebtCollectionCase.

            The reviewed on date indicates when the review of the case was conducted on.

        :return: The reviewed_on of this DebtCollectionCase.
        :rtype: datetime
        """
        return self._reviewed_on

    @reviewed_on.setter
    def reviewed_on(self, reviewed_on):
        """Sets the reviewed_on of this DebtCollectionCase.

            The reviewed on date indicates when the review of the case was conducted on.

        :param reviewed_on: The reviewed_on of this DebtCollectionCase.
        :type: datetime
        """

        self._reviewed_on = reviewed_on
    
    @property
    def reviewer(self):
        """Gets the reviewer of this DebtCollectionCase.

            The reviewer references the user which has reviewed the case.

        :return: The reviewer of this DebtCollectionCase.
        :rtype: int
        """
        return self._reviewer

    @reviewer.setter
    def reviewer(self, reviewer):
        """Sets the reviewer of this DebtCollectionCase.

            The reviewer references the user which has reviewed the case.

        :param reviewer: The reviewer of this DebtCollectionCase.
        :type: int
        """

        self._reviewer = reviewer
    
    @property
    def source(self):
        """Gets the source of this DebtCollectionCase.

            The source of the debt collection case indicates the origin of the amount receivable.

        :return: The source of this DebtCollectionCase.
        :rtype: DebtCollectionCaseSource
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this DebtCollectionCase.

            The source of the debt collection case indicates the origin of the amount receivable.

        :param source: The source of this DebtCollectionCase.
        :type: DebtCollectionCaseSource
        """

        self._source = source
    
    @property
    def source_entity_id(self):
        """Gets the source_entity_id of this DebtCollectionCase.

            The source entity ID points to the object which is the origin of the debt collection case. This ID is only set when the case was triggered by an internal process.

        :return: The source_entity_id of this DebtCollectionCase.
        :rtype: int
        """
        return self._source_entity_id

    @source_entity_id.setter
    def source_entity_id(self, source_entity_id):
        """Sets the source_entity_id of this DebtCollectionCase.

            The source entity ID points to the object which is the origin of the debt collection case. This ID is only set when the case was triggered by an internal process.

        :param source_entity_id: The source_entity_id of this DebtCollectionCase.
        :type: int
        """

        self._source_entity_id = source_entity_id
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this DebtCollectionCase.

            

        :return: The space_view_id of this DebtCollectionCase.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this DebtCollectionCase.

            

        :param space_view_id: The space_view_id of this DebtCollectionCase.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this DebtCollectionCase.

            

        :return: The state of this DebtCollectionCase.
        :rtype: DebtCollectionCaseState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this DebtCollectionCase.

            

        :param state: The state of this DebtCollectionCase.
        :type: DebtCollectionCaseState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this DebtCollectionCase.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this DebtCollectionCase.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this DebtCollectionCase.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this DebtCollectionCase.
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
        if issubclass(DebtCollectionCase, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DebtCollectionCase):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
