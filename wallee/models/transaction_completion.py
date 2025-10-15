# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionCompletion:

    swagger_types = {
    
        'amount': 'float',
        'base_line_items': 'list[LineItem]',
        'created_by': 'int',
        'created_on': 'datetime',
        'external_id': 'str',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'id': 'int',
        'invoice_merchant_reference': 'str',
        'labels': 'list[Label]',
        'language': 'str',
        'last_completion': 'bool',
        'line_item_version': 'TransactionLineItemVersion',
        'line_items': 'list[LineItem]',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'mode': 'TransactionCompletionMode',
        'next_update_on': 'datetime',
        'payment_information': 'str',
        'planned_purge_date': 'datetime',
        'processing_on': 'datetime',
        'processor_reference': 'str',
        'remaining_line_items': 'list[LineItem]',
        'space_view_id': 'int',
        'state': 'TransactionCompletionState',
        'statement_descriptor': 'str',
        'succeeded_on': 'datetime',
        'tax_amount': 'float',
        'time_zone': 'str',
        'timeout_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','base_line_items': 'baseLineItems','created_by': 'createdBy','created_on': 'createdOn','external_id': 'externalId','failed_on': 'failedOn','failure_reason': 'failureReason','id': 'id','invoice_merchant_reference': 'invoiceMerchantReference','labels': 'labels','language': 'language','last_completion': 'lastCompletion','line_item_version': 'lineItemVersion','line_items': 'lineItems','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','mode': 'mode','next_update_on': 'nextUpdateOn','payment_information': 'paymentInformation','planned_purge_date': 'plannedPurgeDate','processing_on': 'processingOn','processor_reference': 'processorReference','remaining_line_items': 'remainingLineItems','space_view_id': 'spaceViewId','state': 'state','statement_descriptor': 'statementDescriptor','succeeded_on': 'succeededOn','tax_amount': 'taxAmount','time_zone': 'timeZone','timeout_on': 'timeoutOn','version': 'version',
    }

    
    _amount = None
    _base_line_items = None
    _created_by = None
    _created_on = None
    _external_id = None
    _failed_on = None
    _failure_reason = None
    _id = None
    _invoice_merchant_reference = None
    _labels = None
    _language = None
    _last_completion = None
    _line_item_version = None
    _line_items = None
    _linked_space_id = None
    _linked_transaction = None
    _mode = None
    _next_update_on = None
    _payment_information = None
    _planned_purge_date = None
    _processing_on = None
    _processor_reference = None
    _remaining_line_items = None
    _space_view_id = None
    _state = None
    _statement_descriptor = None
    _succeeded_on = None
    _tax_amount = None
    _time_zone = None
    _timeout_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.base_line_items = kwargs.get('base_line_items', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.external_id = kwargs.get('external_id', None)
        self.failed_on = kwargs.get('failed_on', None)
        self.failure_reason = kwargs.get('failure_reason', None)
        self.id = kwargs.get('id', None)
        self.invoice_merchant_reference = kwargs.get('invoice_merchant_reference', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.last_completion = kwargs.get('last_completion', None)
        self.line_item_version = kwargs.get('line_item_version', None)
        self.line_items = kwargs.get('line_items', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.mode = kwargs.get('mode', None)
        self.next_update_on = kwargs.get('next_update_on', None)
        self.payment_information = kwargs.get('payment_information', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_on = kwargs.get('processing_on', None)
        self.processor_reference = kwargs.get('processor_reference', None)
        self.remaining_line_items = kwargs.get('remaining_line_items', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.statement_descriptor = kwargs.get('statement_descriptor', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this TransactionCompletion.

            The total amount to be captured in this completion, including taxes.

        :return: The amount of this TransactionCompletion.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCompletion.

            The total amount to be captured in this completion, including taxes.

        :param amount: The amount of this TransactionCompletion.
        :type: float
        """

        self._amount = amount
    
    @property
    def base_line_items(self):
        """Gets the base_line_items of this TransactionCompletion.

            The original line items from the transaction that serve as the baseline for this completion.

        :return: The base_line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._base_line_items

    @base_line_items.setter
    def base_line_items(self, base_line_items):
        """Sets the base_line_items of this TransactionCompletion.

            The original line items from the transaction that serve as the baseline for this completion.

        :param base_line_items: The base_line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._base_line_items = base_line_items
    
    @property
    def created_by(self):
        """Gets the created_by of this TransactionCompletion.

            The ID of the user the transaction completion was created by.

        :return: The created_by of this TransactionCompletion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransactionCompletion.

            The ID of the user the transaction completion was created by.

        :param created_by: The created_by of this TransactionCompletion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionCompletion.

            The date and time when the object was created.

        :return: The created_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionCompletion.

            The date and time when the object was created.

        :param created_on: The created_on of this TransactionCompletion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionCompletion.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :return: The external_id of this TransactionCompletion.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionCompletion.

            A client-generated nonce which uniquely identifies some action to be executed. Subsequent requests with the same external ID do not execute the action again, but return the original result.

        :param external_id: The external_id of this TransactionCompletion.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def failed_on(self):
        """Gets the failed_on of this TransactionCompletion.

            The date and time when the transaction completion failed.

        :return: The failed_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this TransactionCompletion.

            The date and time when the transaction completion failed.

        :param failed_on: The failed_on of this TransactionCompletion.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this TransactionCompletion.

            The reason for the failure of the transaction completion.

        :return: The failure_reason of this TransactionCompletion.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this TransactionCompletion.

            The reason for the failure of the transaction completion.

        :param failure_reason: The failure_reason of this TransactionCompletion.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def id(self):
        """Gets the id of this TransactionCompletion.

            A unique identifier for the object.

        :return: The id of this TransactionCompletion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionCompletion.

            A unique identifier for the object.

        :param id: The id of this TransactionCompletion.
        :type: int
        """

        self._id = id
    
    @property
    def invoice_merchant_reference(self):
        """Gets the invoice_merchant_reference of this TransactionCompletion.

            The merchant's reference used to identify the invoice.

        :return: The invoice_merchant_reference of this TransactionCompletion.
        :rtype: str
        """
        return self._invoice_merchant_reference

    @invoice_merchant_reference.setter
    def invoice_merchant_reference(self, invoice_merchant_reference):
        """Sets the invoice_merchant_reference of this TransactionCompletion.

            The merchant's reference used to identify the invoice.

        :param invoice_merchant_reference: The invoice_merchant_reference of this TransactionCompletion.
        :type: str
        """
        if invoice_merchant_reference is not None and len(invoice_merchant_reference) > 100:
            raise ValueError("Invalid value for `invoice_merchant_reference`, length must be less than or equal to `100`")

        self._invoice_merchant_reference = invoice_merchant_reference
    
    @property
    def labels(self):
        """Gets the labels of this TransactionCompletion.

            The labels providing additional information about the object.

        :return: The labels of this TransactionCompletion.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TransactionCompletion.

            The labels providing additional information about the object.

        :param labels: The labels of this TransactionCompletion.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this TransactionCompletion.

            The language that is linked to the object.

        :return: The language of this TransactionCompletion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionCompletion.

            The language that is linked to the object.

        :param language: The language of this TransactionCompletion.
        :type: str
        """

        self._language = language
    
    @property
    def last_completion(self):
        """Gets the last_completion of this TransactionCompletion.

            Whether this is the final completion for the transaction. After the last completion is successfully created, the transaction enters its final state, and no further completions can occur.

        :return: The last_completion of this TransactionCompletion.
        :rtype: bool
        """
        return self._last_completion

    @last_completion.setter
    def last_completion(self, last_completion):
        """Sets the last_completion of this TransactionCompletion.

            Whether this is the final completion for the transaction. After the last completion is successfully created, the transaction enters its final state, and no further completions can occur.

        :param last_completion: The last_completion of this TransactionCompletion.
        :type: bool
        """

        self._last_completion = last_completion
    
    @property
    def line_item_version(self):
        """Gets the line_item_version of this TransactionCompletion.

            The specific version of the line items that are being used for this completion.

        :return: The line_item_version of this TransactionCompletion.
        :rtype: TransactionLineItemVersion
        """
        return self._line_item_version

    @line_item_version.setter
    def line_item_version(self, line_item_version):
        """Sets the line_item_version of this TransactionCompletion.

            The specific version of the line items that are being used for this completion.

        :param line_item_version: The line_item_version of this TransactionCompletion.
        :type: TransactionLineItemVersion
        """

        self._line_item_version = line_item_version
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionCompletion.

            The line items captured in this transaction completion.

        :return: The line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionCompletion.

            The line items captured in this transaction completion.

        :param line_items: The line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this TransactionCompletion.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this TransactionCompletion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this TransactionCompletion.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this TransactionCompletion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this TransactionCompletion.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this TransactionCompletion.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this TransactionCompletion.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this TransactionCompletion.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def mode(self):
        """Gets the mode of this TransactionCompletion.

            The mode of transaction completion, such as online or offline, determining how the completion process is executed.

        :return: The mode of this TransactionCompletion.
        :rtype: TransactionCompletionMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TransactionCompletion.

            The mode of transaction completion, such as online or offline, determining how the completion process is executed.

        :param mode: The mode of this TransactionCompletion.
        :type: TransactionCompletionMode
        """

        self._mode = mode
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this TransactionCompletion.

            The date and time when the next update of the object's state is planned.

        :return: The next_update_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this TransactionCompletion.

            The date and time when the next update of the object's state is planned.

        :param next_update_on: The next_update_on of this TransactionCompletion.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def payment_information(self):
        """Gets the payment_information of this TransactionCompletion.

            Payment-specific details related to this transaction completion such as payment instructions or references needed for processing.

        :return: The payment_information of this TransactionCompletion.
        :rtype: str
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """Sets the payment_information of this TransactionCompletion.

            Payment-specific details related to this transaction completion such as payment instructions or references needed for processing.

        :param payment_information: The payment_information of this TransactionCompletion.
        :type: str
        """

        self._payment_information = payment_information
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionCompletion.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this TransactionCompletion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionCompletion.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionCompletion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_on(self):
        """Gets the processing_on of this TransactionCompletion.

            The date and time when the processing of the transaction completion was started.

        :return: The processing_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._processing_on

    @processing_on.setter
    def processing_on(self, processing_on):
        """Sets the processing_on of this TransactionCompletion.

            The date and time when the processing of the transaction completion was started.

        :param processing_on: The processing_on of this TransactionCompletion.
        :type: datetime
        """

        self._processing_on = processing_on
    
    @property
    def processor_reference(self):
        """Gets the processor_reference of this TransactionCompletion.

            The reference ID provided by the payment processor, used to trace the completion through the external payment system.

        :return: The processor_reference of this TransactionCompletion.
        :rtype: str
        """
        return self._processor_reference

    @processor_reference.setter
    def processor_reference(self, processor_reference):
        """Sets the processor_reference of this TransactionCompletion.

            The reference ID provided by the payment processor, used to trace the completion through the external payment system.

        :param processor_reference: The processor_reference of this TransactionCompletion.
        :type: str
        """

        self._processor_reference = processor_reference
    
    @property
    def remaining_line_items(self):
        """Gets the remaining_line_items of this TransactionCompletion.

            The line items yet to be captured in the transaction.

        :return: The remaining_line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._remaining_line_items

    @remaining_line_items.setter
    def remaining_line_items(self, remaining_line_items):
        """Sets the remaining_line_items of this TransactionCompletion.

            The line items yet to be captured in the transaction.

        :param remaining_line_items: The remaining_line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._remaining_line_items = remaining_line_items
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionCompletion.

            The ID of the space view this object is linked to.

        :return: The space_view_id of this TransactionCompletion.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionCompletion.

            The ID of the space view this object is linked to.

        :param space_view_id: The space_view_id of this TransactionCompletion.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this TransactionCompletion.

            The object's current state.

        :return: The state of this TransactionCompletion.
        :rtype: TransactionCompletionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionCompletion.

            The object's current state.

        :param state: The state of this TransactionCompletion.
        :type: TransactionCompletionState
        """

        self._state = state
    
    @property
    def statement_descriptor(self):
        """Gets the statement_descriptor of this TransactionCompletion.

            The statement descriptor that appears on a customer's bank statement, providing an explanation for charges or payments, helping customers identify the transaction.

        :return: The statement_descriptor of this TransactionCompletion.
        :rtype: str
        """
        return self._statement_descriptor

    @statement_descriptor.setter
    def statement_descriptor(self, statement_descriptor):
        """Sets the statement_descriptor of this TransactionCompletion.

            The statement descriptor that appears on a customer's bank statement, providing an explanation for charges or payments, helping customers identify the transaction.

        :param statement_descriptor: The statement_descriptor of this TransactionCompletion.
        :type: str
        """
        if statement_descriptor is not None and len(statement_descriptor) > 80:
            raise ValueError("Invalid value for `statement_descriptor`, length must be less than or equal to `80`")

        self._statement_descriptor = statement_descriptor
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this TransactionCompletion.

            The date and time when the transaction completion succeeded.

        :return: The succeeded_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this TransactionCompletion.

            The date and time when the transaction completion succeeded.

        :param succeeded_on: The succeeded_on of this TransactionCompletion.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this TransactionCompletion.

            The portion of the captured amount that corresponds to taxes.

        :return: The tax_amount of this TransactionCompletion.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TransactionCompletion.

            The portion of the captured amount that corresponds to taxes.

        :param tax_amount: The tax_amount of this TransactionCompletion.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def time_zone(self):
        """Gets the time_zone of this TransactionCompletion.

            The time zone that this object is associated with.

        :return: The time_zone of this TransactionCompletion.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this TransactionCompletion.

            The time zone that this object is associated with.

        :param time_zone: The time_zone of this TransactionCompletion.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this TransactionCompletion.

            The date and time when the object will expire.

        :return: The timeout_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this TransactionCompletion.

            The date and time when the object will expire.

        :param timeout_on: The timeout_on of this TransactionCompletion.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def version(self):
        """Gets the version of this TransactionCompletion.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this TransactionCompletion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionCompletion.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this TransactionCompletion.
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
        if issubclass(TransactionCompletion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionCompletion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
