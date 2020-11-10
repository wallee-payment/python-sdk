# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class TransactionCompletion(TransactionAwareEntity):

    swagger_types = {
    
        'amount': 'float',
        'base_line_items': 'list[LineItem]',
        'created_by': 'int',
        'created_on': 'datetime',
        'external_id': 'str',
        'failed_on': 'datetime',
        'failure_reason': 'FailureReason',
        'invoice_merchant_reference': 'str',
        'labels': 'list[Label]',
        'language': 'str',
        'last_completion': 'bool',
        'line_item_version': 'TransactionLineItemVersion',
        'line_items': 'list[LineItem]',
        'mode': 'TransactionCompletionMode',
        'next_update_on': 'datetime',
        'payment_information': 'str',
        'planned_purge_date': 'datetime',
        'processing_on': 'datetime',
        'processor_reference': 'str',
        'remaining_line_items': 'list[LineItem]',
        'space_view_id': 'int',
        'state': 'TransactionCompletionState',
        'succeeded_on': 'datetime',
        'tax_amount': 'float',
        'time_zone': 'str',
        'timeout_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','base_line_items': 'baseLineItems','created_by': 'createdBy','created_on': 'createdOn','external_id': 'externalId','failed_on': 'failedOn','failure_reason': 'failureReason','invoice_merchant_reference': 'invoiceMerchantReference','labels': 'labels','language': 'language','last_completion': 'lastCompletion','line_item_version': 'lineItemVersion','line_items': 'lineItems','mode': 'mode','next_update_on': 'nextUpdateOn','payment_information': 'paymentInformation','planned_purge_date': 'plannedPurgeDate','processing_on': 'processingOn','processor_reference': 'processorReference','remaining_line_items': 'remainingLineItems','space_view_id': 'spaceViewId','state': 'state','succeeded_on': 'succeededOn','tax_amount': 'taxAmount','time_zone': 'timeZone','timeout_on': 'timeoutOn','version': 'version',
    }

    
    _amount = None
    _base_line_items = None
    _created_by = None
    _created_on = None
    _external_id = None
    _failed_on = None
    _failure_reason = None
    _invoice_merchant_reference = None
    _labels = None
    _language = None
    _last_completion = None
    _line_item_version = None
    _line_items = None
    _mode = None
    _next_update_on = None
    _payment_information = None
    _planned_purge_date = None
    _processing_on = None
    _processor_reference = None
    _remaining_line_items = None
    _space_view_id = None
    _state = None
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
        self.invoice_merchant_reference = kwargs.get('invoice_merchant_reference', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.last_completion = kwargs.get('last_completion', None)
        self.line_item_version = kwargs.get('line_item_version', None)
        self.line_items = kwargs.get('line_items', None)
        self.mode = kwargs.get('mode', None)
        self.next_update_on = kwargs.get('next_update_on', None)
        self.payment_information = kwargs.get('payment_information', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processing_on = kwargs.get('processing_on', None)
        self.processor_reference = kwargs.get('processor_reference', None)
        self.remaining_line_items = kwargs.get('remaining_line_items', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.succeeded_on = kwargs.get('succeeded_on', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def amount(self):
        """Gets the amount of this TransactionCompletion.

            The amount which is captured. The amount represents sum of line items including taxes.

        :return: The amount of this TransactionCompletion.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionCompletion.

            The amount which is captured. The amount represents sum of line items including taxes.

        :param amount: The amount of this TransactionCompletion.
        :type: float
        """

        self._amount = amount
    
    @property
    def base_line_items(self):
        """Gets the base_line_items of this TransactionCompletion.

            The base line items on which the completion is applied on.

        :return: The base_line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._base_line_items

    @base_line_items.setter
    def base_line_items(self, base_line_items):
        """Sets the base_line_items of this TransactionCompletion.

            The base line items on which the completion is applied on.

        :param base_line_items: The base_line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._base_line_items = base_line_items
    
    @property
    def created_by(self):
        """Gets the created_by of this TransactionCompletion.

            

        :return: The created_by of this TransactionCompletion.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this TransactionCompletion.

            

        :param created_by: The created_by of this TransactionCompletion.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionCompletion.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionCompletion.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this TransactionCompletion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionCompletion.

            The external ID helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this TransactionCompletion.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionCompletion.

            The external ID helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

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

            

        :return: The failed_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._failed_on

    @failed_on.setter
    def failed_on(self, failed_on):
        """Sets the failed_on of this TransactionCompletion.

            

        :param failed_on: The failed_on of this TransactionCompletion.
        :type: datetime
        """

        self._failed_on = failed_on
    
    @property
    def failure_reason(self):
        """Gets the failure_reason of this TransactionCompletion.

            

        :return: The failure_reason of this TransactionCompletion.
        :rtype: FailureReason
        """
        return self._failure_reason

    @failure_reason.setter
    def failure_reason(self, failure_reason):
        """Sets the failure_reason of this TransactionCompletion.

            

        :param failure_reason: The failure_reason of this TransactionCompletion.
        :type: FailureReason
        """

        self._failure_reason = failure_reason
    
    @property
    def invoice_merchant_reference(self):
        """Gets the invoice_merchant_reference of this TransactionCompletion.

            

        :return: The invoice_merchant_reference of this TransactionCompletion.
        :rtype: str
        """
        return self._invoice_merchant_reference

    @invoice_merchant_reference.setter
    def invoice_merchant_reference(self, invoice_merchant_reference):
        """Sets the invoice_merchant_reference of this TransactionCompletion.

            

        :param invoice_merchant_reference: The invoice_merchant_reference of this TransactionCompletion.
        :type: str
        """
        if invoice_merchant_reference is not None and len(invoice_merchant_reference) > 100:
            raise ValueError("Invalid value for `invoice_merchant_reference`, length must be less than or equal to `100`")

        self._invoice_merchant_reference = invoice_merchant_reference
    
    @property
    def labels(self):
        """Gets the labels of this TransactionCompletion.

            

        :return: The labels of this TransactionCompletion.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TransactionCompletion.

            

        :param labels: The labels of this TransactionCompletion.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this TransactionCompletion.

            

        :return: The language of this TransactionCompletion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionCompletion.

            

        :param language: The language of this TransactionCompletion.
        :type: str
        """

        self._language = language
    
    @property
    def last_completion(self):
        """Gets the last_completion of this TransactionCompletion.

            Indicates if this is the last completion. After the last completion is created the transaction cannot be completed anymore.

        :return: The last_completion of this TransactionCompletion.
        :rtype: bool
        """
        return self._last_completion

    @last_completion.setter
    def last_completion(self, last_completion):
        """Sets the last_completion of this TransactionCompletion.

            Indicates if this is the last completion. After the last completion is created the transaction cannot be completed anymore.

        :param last_completion: The last_completion of this TransactionCompletion.
        :type: bool
        """

        self._last_completion = last_completion
    
    @property
    def line_item_version(self):
        """Gets the line_item_version of this TransactionCompletion.

            

        :return: The line_item_version of this TransactionCompletion.
        :rtype: TransactionLineItemVersion
        """
        return self._line_item_version

    @line_item_version.setter
    def line_item_version(self, line_item_version):
        """Sets the line_item_version of this TransactionCompletion.

            

        :param line_item_version: The line_item_version of this TransactionCompletion.
        :type: TransactionLineItemVersion
        """

        self._line_item_version = line_item_version
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionCompletion.

            The line items which are captured.

        :return: The line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionCompletion.

            The line items which are captured.

        :param line_items: The line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def mode(self):
        """Gets the mode of this TransactionCompletion.

            

        :return: The mode of this TransactionCompletion.
        :rtype: TransactionCompletionMode
        """
        return self._mode

    @mode.setter
    def mode(self, mode):
        """Sets the mode of this TransactionCompletion.

            

        :param mode: The mode of this TransactionCompletion.
        :type: TransactionCompletionMode
        """

        self._mode = mode
    
    @property
    def next_update_on(self):
        """Gets the next_update_on of this TransactionCompletion.

            

        :return: The next_update_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._next_update_on

    @next_update_on.setter
    def next_update_on(self, next_update_on):
        """Sets the next_update_on of this TransactionCompletion.

            

        :param next_update_on: The next_update_on of this TransactionCompletion.
        :type: datetime
        """

        self._next_update_on = next_update_on
    
    @property
    def payment_information(self):
        """Gets the payment_information of this TransactionCompletion.

            

        :return: The payment_information of this TransactionCompletion.
        :rtype: str
        """
        return self._payment_information

    @payment_information.setter
    def payment_information(self, payment_information):
        """Sets the payment_information of this TransactionCompletion.

            

        :param payment_information: The payment_information of this TransactionCompletion.
        :type: str
        """

        self._payment_information = payment_information
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionCompletion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TransactionCompletion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionCompletion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionCompletion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processing_on(self):
        """Gets the processing_on of this TransactionCompletion.

            

        :return: The processing_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._processing_on

    @processing_on.setter
    def processing_on(self, processing_on):
        """Sets the processing_on of this TransactionCompletion.

            

        :param processing_on: The processing_on of this TransactionCompletion.
        :type: datetime
        """

        self._processing_on = processing_on
    
    @property
    def processor_reference(self):
        """Gets the processor_reference of this TransactionCompletion.

            

        :return: The processor_reference of this TransactionCompletion.
        :rtype: str
        """
        return self._processor_reference

    @processor_reference.setter
    def processor_reference(self, processor_reference):
        """Sets the processor_reference of this TransactionCompletion.

            

        :param processor_reference: The processor_reference of this TransactionCompletion.
        :type: str
        """

        self._processor_reference = processor_reference
    
    @property
    def remaining_line_items(self):
        """Gets the remaining_line_items of this TransactionCompletion.

            

        :return: The remaining_line_items of this TransactionCompletion.
        :rtype: list[LineItem]
        """
        return self._remaining_line_items

    @remaining_line_items.setter
    def remaining_line_items(self, remaining_line_items):
        """Sets the remaining_line_items of this TransactionCompletion.

            

        :param remaining_line_items: The remaining_line_items of this TransactionCompletion.
        :type: list[LineItem]
        """

        self._remaining_line_items = remaining_line_items
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionCompletion.

            

        :return: The space_view_id of this TransactionCompletion.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionCompletion.

            

        :param space_view_id: The space_view_id of this TransactionCompletion.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this TransactionCompletion.

            

        :return: The state of this TransactionCompletion.
        :rtype: TransactionCompletionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionCompletion.

            

        :param state: The state of this TransactionCompletion.
        :type: TransactionCompletionState
        """

        self._state = state
    
    @property
    def succeeded_on(self):
        """Gets the succeeded_on of this TransactionCompletion.

            

        :return: The succeeded_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._succeeded_on

    @succeeded_on.setter
    def succeeded_on(self, succeeded_on):
        """Sets the succeeded_on of this TransactionCompletion.

            

        :param succeeded_on: The succeeded_on of this TransactionCompletion.
        :type: datetime
        """

        self._succeeded_on = succeeded_on
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this TransactionCompletion.

            The total sum of all taxes of line items.

        :return: The tax_amount of this TransactionCompletion.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TransactionCompletion.

            The total sum of all taxes of line items.

        :param tax_amount: The tax_amount of this TransactionCompletion.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def time_zone(self):
        """Gets the time_zone of this TransactionCompletion.

            

        :return: The time_zone of this TransactionCompletion.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this TransactionCompletion.

            

        :param time_zone: The time_zone of this TransactionCompletion.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this TransactionCompletion.

            

        :return: The timeout_on of this TransactionCompletion.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this TransactionCompletion.

            

        :param timeout_on: The timeout_on of this TransactionCompletion.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def version(self):
        """Gets the version of this TransactionCompletion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TransactionCompletion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionCompletion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
