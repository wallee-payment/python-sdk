# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class TransactionInvoice(TransactionAwareEntity):

    swagger_types = {
    
        'amount': 'float',
        'billing_address': 'Address',
        'completion': 'TransactionCompletion',
        'created_on': 'datetime',
        'derecognized_by': 'int',
        'derecognized_on': 'datetime',
        'due_on': 'datetime',
        'environment': 'Environment',
        'external_id': 'str',
        'language': 'str',
        'line_items': 'list[LineItem]',
        'merchant_reference': 'str',
        'outstanding_amount': 'float',
        'paid_on': 'datetime',
        'planned_purge_date': 'datetime',
        'space_view_id': 'int',
        'state': 'TransactionInvoiceState',
        'tax_amount': 'float',
        'time_zone': 'str',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','billing_address': 'billingAddress','completion': 'completion','created_on': 'createdOn','derecognized_by': 'derecognizedBy','derecognized_on': 'derecognizedOn','due_on': 'dueOn','environment': 'environment','external_id': 'externalId','language': 'language','line_items': 'lineItems','merchant_reference': 'merchantReference','outstanding_amount': 'outstandingAmount','paid_on': 'paidOn','planned_purge_date': 'plannedPurgeDate','space_view_id': 'spaceViewId','state': 'state','tax_amount': 'taxAmount','time_zone': 'timeZone','version': 'version',
    }

    
    _amount = None
    _billing_address = None
    _completion = None
    _created_on = None
    _derecognized_by = None
    _derecognized_on = None
    _due_on = None
    _environment = None
    _external_id = None
    _language = None
    _line_items = None
    _merchant_reference = None
    _outstanding_amount = None
    _paid_on = None
    _planned_purge_date = None
    _space_view_id = None
    _state = None
    _tax_amount = None
    _time_zone = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.completion = kwargs.get('completion', None)
        self.created_on = kwargs.get('created_on', None)
        self.derecognized_by = kwargs.get('derecognized_by', None)
        self.derecognized_on = kwargs.get('derecognized_on', None)
        self.due_on = kwargs.get('due_on', None)
        self.environment = kwargs.get('environment', None)
        self.external_id = kwargs.get('external_id', None)
        self.language = kwargs.get('language', None)
        self.line_items = kwargs.get('line_items', None)
        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.outstanding_amount = kwargs.get('outstanding_amount', None)
        self.paid_on = kwargs.get('paid_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        self.state = kwargs.get('state', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def amount(self):
        """Gets the amount of this TransactionInvoice.

            

        :return: The amount of this TransactionInvoice.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this TransactionInvoice.

            

        :param amount: The amount of this TransactionInvoice.
        :type: float
        """

        self._amount = amount
    
    @property
    def billing_address(self):
        """Gets the billing_address of this TransactionInvoice.

            

        :return: The billing_address of this TransactionInvoice.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this TransactionInvoice.

            

        :param billing_address: The billing_address of this TransactionInvoice.
        :type: Address
        """

        self._billing_address = billing_address
    
    @property
    def completion(self):
        """Gets the completion of this TransactionInvoice.

            

        :return: The completion of this TransactionInvoice.
        :rtype: TransactionCompletion
        """
        return self._completion

    @completion.setter
    def completion(self, completion):
        """Sets the completion of this TransactionInvoice.

            

        :param completion: The completion of this TransactionInvoice.
        :type: TransactionCompletion
        """

        self._completion = completion
    
    @property
    def created_on(self):
        """Gets the created_on of this TransactionInvoice.

            The date on which the invoice is created on.

        :return: The created_on of this TransactionInvoice.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TransactionInvoice.

            The date on which the invoice is created on.

        :param created_on: The created_on of this TransactionInvoice.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def derecognized_by(self):
        """Gets the derecognized_by of this TransactionInvoice.

            The id of the user which marked the invoice as derecognized.

        :return: The derecognized_by of this TransactionInvoice.
        :rtype: int
        """
        return self._derecognized_by

    @derecognized_by.setter
    def derecognized_by(self, derecognized_by):
        """Sets the derecognized_by of this TransactionInvoice.

            The id of the user which marked the invoice as derecognized.

        :param derecognized_by: The derecognized_by of this TransactionInvoice.
        :type: int
        """

        self._derecognized_by = derecognized_by
    
    @property
    def derecognized_on(self):
        """Gets the derecognized_on of this TransactionInvoice.

            The date on which the invoice is marked as derecognized.

        :return: The derecognized_on of this TransactionInvoice.
        :rtype: datetime
        """
        return self._derecognized_on

    @derecognized_on.setter
    def derecognized_on(self, derecognized_on):
        """Sets the derecognized_on of this TransactionInvoice.

            The date on which the invoice is marked as derecognized.

        :param derecognized_on: The derecognized_on of this TransactionInvoice.
        :type: datetime
        """

        self._derecognized_on = derecognized_on
    
    @property
    def due_on(self):
        """Gets the due_on of this TransactionInvoice.

            The date on which the invoice should be paid on.

        :return: The due_on of this TransactionInvoice.
        :rtype: datetime
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this TransactionInvoice.

            The date on which the invoice should be paid on.

        :param due_on: The due_on of this TransactionInvoice.
        :type: datetime
        """

        self._due_on = due_on
    
    @property
    def environment(self):
        """Gets the environment of this TransactionInvoice.

            

        :return: The environment of this TransactionInvoice.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this TransactionInvoice.

            

        :param environment: The environment of this TransactionInvoice.
        :type: Environment
        """

        self._environment = environment
    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionInvoice.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this TransactionInvoice.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionInvoice.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this TransactionInvoice.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def language(self):
        """Gets the language of this TransactionInvoice.

            

        :return: The language of this TransactionInvoice.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TransactionInvoice.

            

        :param language: The language of this TransactionInvoice.
        :type: str
        """

        self._language = language
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionInvoice.

            

        :return: The line_items of this TransactionInvoice.
        :rtype: list[LineItem]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionInvoice.

            

        :param line_items: The line_items of this TransactionInvoice.
        :type: list[LineItem]
        """

        self._line_items = line_items
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this TransactionInvoice.

            

        :return: The merchant_reference of this TransactionInvoice.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this TransactionInvoice.

            

        :param merchant_reference: The merchant_reference of this TransactionInvoice.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def outstanding_amount(self):
        """Gets the outstanding_amount of this TransactionInvoice.

            The outstanding amount indicates how much the buyer owes the merchant. A negative amount indicates that the invoice is overpaid.

        :return: The outstanding_amount of this TransactionInvoice.
        :rtype: float
        """
        return self._outstanding_amount

    @outstanding_amount.setter
    def outstanding_amount(self, outstanding_amount):
        """Sets the outstanding_amount of this TransactionInvoice.

            The outstanding amount indicates how much the buyer owes the merchant. A negative amount indicates that the invoice is overpaid.

        :param outstanding_amount: The outstanding_amount of this TransactionInvoice.
        :type: float
        """

        self._outstanding_amount = outstanding_amount
    
    @property
    def paid_on(self):
        """Gets the paid_on of this TransactionInvoice.

            The date on which the invoice is marked as paid. Eventually this date lags behind of the actual paid date.

        :return: The paid_on of this TransactionInvoice.
        :rtype: datetime
        """
        return self._paid_on

    @paid_on.setter
    def paid_on(self, paid_on):
        """Sets the paid_on of this TransactionInvoice.

            The date on which the invoice is marked as paid. Eventually this date lags behind of the actual paid date.

        :param paid_on: The paid_on of this TransactionInvoice.
        :type: datetime
        """

        self._paid_on = paid_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TransactionInvoice.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TransactionInvoice.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TransactionInvoice.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TransactionInvoice.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionInvoice.

            

        :return: The space_view_id of this TransactionInvoice.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionInvoice.

            

        :param space_view_id: The space_view_id of this TransactionInvoice.
        :type: int
        """

        self._space_view_id = space_view_id
    
    @property
    def state(self):
        """Gets the state of this TransactionInvoice.

            

        :return: The state of this TransactionInvoice.
        :rtype: TransactionInvoiceState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TransactionInvoice.

            

        :param state: The state of this TransactionInvoice.
        :type: TransactionInvoiceState
        """

        self._state = state
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this TransactionInvoice.

            

        :return: The tax_amount of this TransactionInvoice.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this TransactionInvoice.

            

        :param tax_amount: The tax_amount of this TransactionInvoice.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def time_zone(self):
        """Gets the time_zone of this TransactionInvoice.

            

        :return: The time_zone of this TransactionInvoice.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this TransactionInvoice.

            

        :param time_zone: The time_zone of this TransactionInvoice.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def version(self):
        """Gets the version of this TransactionInvoice.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TransactionInvoice.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TransactionInvoice.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this TransactionInvoice.
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
        if issubclass(TransactionInvoice, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionInvoice):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
