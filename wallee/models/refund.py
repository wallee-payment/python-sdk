# coding: utf-8
import pprint
import six
from enum import Enum



class Refund:

    swagger_types = {
    
        'amount': 'float',
        'base_line_items': 'list[LineItem]',
        'completion': 'int',
        'created_by': 'int',
        'created_on': 'datetime',
        'environment': 'Environment',
        'external_id': 'str',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'labels': 'list[Label]',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'merchant_reference': 'str',
        'next_update_on': 'datetime',
        'planned_purge_date': 'datetime',
        'processing_on': 'datetime',
        'processor_reference': 'str',
        'reduced_line_items': 'list[LineItem]',
        'reductions': 'list[LineItemReduction]',
        'state': 'RefundState',
        'succeeded_on': 'datetime',
        'taxes': 'list[Tax]',
        'time_zone': 'str',
        'timeout_on': 'datetime',
        'total_applied_fees': 'float',
        'total_settled_amount': 'float',
        'transaction': 'Transaction',
        'type': 'RefundType',
        'updated_invoice': 'int',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','base_line_items': 'baseLineItems','completion': 'completion','created_by': 'createdBy','created_on': 'createdOn','environment': 'environment','external_id': 'externalId','failed_on': 'failedOn','failure_reason': 'failureReason','id': 'id','labels': 'labels','language': 'language','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','merchant_reference': 'merchantReference','next_update_on': 'nextUpdateOn','planned_purge_date': 'plannedPurgeDate','processing_on': 'processingOn','processor_reference': 'processorReference','reduced_line_items': 'reducedLineItems','reductions': 'reductions','state': 'state','succeeded_on': 'succeededOn','taxes': 'taxes','time_zone': 'timeZone','timeout_on': 'timeoutOn','total_applied_fees': 'totalAppliedFees','total_settled_amount': 'totalSettledAmount','transaction': 'transaction','type': 'type','updated_invoice': 'updatedInvoice','version': 'version',
    }

    
    _amount = None
    _base_line_items = None
    _completion = None
    _created_by = None
    _created_on = None
    _environment = None
    _external_id = None
    _failed_on = None
    _failure_reason = None
    _id = None
    _labels = None
    _language = None
    _line_items = None
    _linked_space_id = None
    _merchant_reference = None
    _next_update_on = None
    _planned_purge_date = None
    _processing_on = None
    _processor_reference = None
    _reduced_line_items = None
    _reductions = None
    _state = None
    _succeeded_on = None
    _taxes = None
    _time_zone = None
    _timeout_on = None
    _total_applied_fees = None
    _total_settled_amount = None
    _transaction = None
    _type = None
    _updated_invoice = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.base_line_items = kwargs.get('base_line_items', None)
        self.completion = kwargs.get('completion', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.environment = kwargs.get('environment', None)
        self.external_id = kwargs.get('external_id', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.next_update_on = kwargs.get('next_update_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_on = kwargs.get('processing_on', None)
        self.processor_reference = kwargs.get('processor_reference', None)
        self.reduced_line_items = kwargs.get('reduced_line_items', None)
        self.reductions = kwargs.get('reductions', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.taxes = kwargs.get('taxes', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.total_applied_fees = kwargs.get('total_applied_fees', None)
        self.total_settled_amount = kwargs.get('total_settled_amount', None)
        self.transaction = kwargs.get('transaction', None)
        self.type = kwargs.get('type', None)
        self.updated_invoice = kwargs.get('updated_invoice', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this Refund.

            

        :return: The amount of this Refund.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this Refund.

            

        :param amount: The amount of this Refund.
        :type: float
        """

        self._amount = amount
    
    @property
    def base_line_items(self):
        """Gets the base_line_items of this Refund.

            

        :return: The base_line_items of this Refund.
        :rtype: list[LineItem]
        """
        return self._base_line_items

    @base_line_items.setter
    def base_line_items(self, base_line_items):
        """Sets the base_line_items of this Refund.

            

        :param base_line_items: The base_line_items of this Refund.
        :type: list[LineItem]
        """

        self._base_line_items = base_line_items
    
    @property
    def completion(self):
        """Gets the completion of this Refund.

            

        :return: The completion of this Refund.
        :rtype: int
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this Refund.

            

        :param completion: The completion of this Refund.
        :type: int
        """

        self._completion = completion
    
    @property
    def created_by(self):
        """Gets the created_by of this Refund.

            

        :return: The created_by of this Refund.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this Refund.

            

        :param created_by: The created_by of this Refund.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this Refund.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this Refund.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Refund.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this Refund.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def environment(self):
        """Gets the environment of this Refund.

            

        :return: The environment of this Refund.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this Refund.

            

        :param environment: The environment of this Refund.
        :type: Environment
        """

        self._environment = environment
    
    @property
    def external_id(self):
        """Gets the external_id of this Refund.

            The external id helps to identify duplicate calls to the refund service. As such the external ID has to be unique per transaction.

        :return: The external_id of this Refund.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Refund.

            The external id helps to identify duplicate calls to the refund service. As such the external ID has to be unique per transaction.

        :param external_id: The external_id of this Refund.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def failed_on(self):
        """Gets the failed_on of this Refund.

            

        :return: The failed_on of this Refund.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this Refund.

            

        :param failed_on: The failed_on of this Refund.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this Refund.

            

        :return: The failure_reason of this Refund.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this Refund.

            

        :param failure_reason: The failure_reason of this Refund.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this Refund.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Refund.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Refund.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Refund.
        :type: int
        """

        self._id = id
    
    @property
    def labels(self):
        """Gets the labels of this Refund.

            

        :return: The labels of this Refund.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this Refund.

            

        :param labels: The labels of this Refund.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this Refund.

            

        :return: The language of this Refund.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Refund.

            

        :param language: The language of this Refund.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this Refund.

            

        :return: The line_items of this Refund.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this Refund.

            

        :param line_items: The line_items of this Refund.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Refund.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Refund.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Refund.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Refund.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this Refund.

            

        :return: The merchant_reference of this Refund.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this Refund.

            

        :param merchant_reference: The merchant_reference of this Refund.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this Refund.

            

        :return: The next_update_on of this Refund.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this Refund.

            

        :param next_update_on: The next_update_on of this Refund.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Refund.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Refund.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Refund.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Refund.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_on(self):
        """Gets the processing_on of this Refund.

            

        :return: The processing_on of this Refund.
        :rtype: datetime
        """
        return self._processing_on

    @processing_on.setter
    def processing_on(self, processing_on):
        """Sets the processing_on of this Refund.

            

        :param processing_on: The processing_on of this Refund.
        :type: datetime
        """

        self._processing_on = processing_on
    
    @property
    def processor_reference(self):
        """Gets the processor_reference of this Refund.

            

        :return: The processor_reference of this Refund.
        :rtype: str
        """
        return self._processor_reference

    @processor_reference.setter
    def processor_reference(self, processor_reference):
        """Sets the processor_reference of this Refund.

            

        :param processor_reference: The processor_reference of this Refund.
        :type: str
        """
        if processor_reference is not None and len(processor_reference) > 150:
            raise ValueError("Invalid value for `processor_reference`, length must be less than or equal to `150`")

        self._processor_reference = processor_reference
    
    @property
    def reduced_line_items(self):
        """Gets the reduced_line_items of this Refund.

            

        :return: The reduced_line_items of this Refund.
        :rtype: list[LineItem]
        """
        return self._reduced_line_items

    @reduced_line_items.setter
    def reduced_line_items(self, reduced_line_items):
        """Sets the reduced_line_items of this Refund.

            

        :param reduced_line_items: The reduced_line_items of this Refund.
        :type: list[LineItem]
        """

        self._reduced_line_items = reduced_line_items
    
    @property
    def reductions(self):
        """Gets the reductions of this Refund.

            

        :return: The reductions of this Refund.
        :rtype: list[LineItemReduction]
        """
        return self._reductions

    @reductions.setter
    def reductions(self, reductions):
        """Sets the reductions of this Refund.

            

        :param reductions: The reductions of this Refund.
        :type: list[LineItemReduction]
        """

        self._reductions = reductions
    
    @property
    def state(self):
        """Gets the state of this Refund.

            

        :return: The state of this Refund.
        :rtype: RefundState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Refund.

            

        :param state: The state of this Refund.
        :type: RefundState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this Refund.

            

        :return: The succeeded_on of this Refund.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this Refund.

            

        :param succeeded_on: The succeeded_on of this Refund.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def taxes(self):
        """Gets the taxes of this Refund.

            

        :return: The taxes of this Refund.
        :rtype: list[Tax]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this Refund.

            

        :param taxes: The taxes of this Refund.
        :type: list[Tax]
        """

        self._taxes = taxes
    
    @property
    def time_zone(self):
        """Gets the time_zone of this Refund.

            

        :return: The time_zone of this Refund.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Refund.

            

        :param time_zone: The time_zone of this Refund.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this Refund.

            

        :return: The timeout_on of this Refund.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this Refund.

            

        :param timeout_on: The timeout_on of this Refund.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def total_applied_fees(self):
        """Gets the total_applied_fees of this Refund.

            The total applied fees is the sum of all fees that have been applied so far.

        :return: The total_applied_fees of this Refund.
        :rtype: float
        """
        return self._total_applied_fees

    @total_applied_fees.setter
    def total_applied_fees(self, total_applied_fees):
        """Sets the total_applied_fees of this Refund.

            The total applied fees is the sum of all fees that have been applied so far.

        :param total_applied_fees: The total_applied_fees of this Refund.
        :type: float
        """

        self._total_applied_fees = total_applied_fees
    
    @property
    def total_settled_amount(self):
        """Gets the total_settled_amount of this Refund.

            The total settled amount is the total amount which has been settled so far.

        :return: The total_settled_amount of this Refund.
        :rtype: float
        """
        return self._total_settled_amount

    @total_settled_amount.setter
    def total_settled_amount(self, total_settled_amount):
        """Sets the total_settled_amount of this Refund.

            The total settled amount is the total amount which has been settled so far.

        :param total_settled_amount: The total_settled_amount of this Refund.
        :type: float
        """

        self._total_settled_amount = total_settled_amount
    
    @property
    def transaction(self):
        """Gets the transaction of this Refund.

            

        :return: The transaction of this Refund.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this Refund.

            

        :param transaction: The transaction of this Refund.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def type(self):
        """Gets the type of this Refund.

            

        :return: The type of this Refund.
        :rtype: RefundType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this Refund.

            

        :param type: The type of this Refund.
        :type: RefundType
        """

        self._type = type
    
    @property
    def updated_invoice(self):
        """Gets the updated_invoice of this Refund.

            

        :return: The updated_invoice of this Refund.
        :rtype: int
        """
        return self._updated_invoice

    @updated_invoice.setter
    def updated_invoice(self, updated_invoice):
        """Sets the updated_invoice of this Refund.

            

        :param updated_invoice: The updated_invoice of this Refund.
        :type: int
        """

        self._updated_invoice = updated_invoice
    
    @property
    def version(self):
        """Gets the version of this Refund.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Refund.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Refund.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Refund.
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
        if issubclass(Refund, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Refund):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
