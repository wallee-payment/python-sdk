# coding: utf-8
import pprint
import six
from enum import Enum



class BankTransaction:

    swagger_types = {
    
        'adjustments': 'list[PaymentAdjustment]',
        'created_by': 'int',
        'created_on': 'datetime',
        'currency_bank_account': 'CurrencyBankAccount',
        'external_id': 'str',
        'flow_direction': 'BankTransactionFlowDirection',
        'id': 'int',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'posting_amount': 'float',
        'reference': 'str',
        'source': 'int',
        'state': 'BankTransactionState',
        'total_adjustment_amount_including_tax': 'float',
        'type': 'int',
        'value_amount': 'float',
        'value_date': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'adjustments': 'adjustments','created_by': 'createdBy','created_on': 'createdOn','currency_bank_account': 'currencyBankAccount','external_id': 'externalId','flow_direction': 'flowDirection','id': 'id','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','posting_amount': 'postingAmount','reference': 'reference','source': 'source','state': 'state','total_adjustment_amount_including_tax': 'totalAdjustmentAmountIncludingTax','type': 'type','value_amount': 'valueAmount','value_date': 'valueDate','version': 'version',
    }

    
    _adjustments = None
    _created_by = None
    _created_on = None
    _currency_bank_account = None
    _external_id = None
    _flow_direction = None
    _id = None
    _linked_space_id = None
    _planned_purge_date = None
    _posting_amount = None
    _reference = None
    _source = None
    _state = None
    _total_adjustment_amount_including_tax = None
    _type = None
    _value_amount = None
    _value_date = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.adjustments = kwargs.get('adjustments', None)
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.currency_bank_account = kwargs.get('currency_bank_account', None)
        self.external_id = kwargs.get('external_id', None)
        self.flow_direction = kwargs.get('flow_direction', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.posting_amount = kwargs.get('posting_amount', None)
        self.reference = kwargs.get('reference', None)
        self.source = kwargs.get('source', None)
        self.state = kwargs.get('state', None)
        self.total_adjustment_amount_including_tax = kwargs.get('total_adjustment_amount_including_tax', None)
        self.type = kwargs.get('type', None)
        self.value_amount = kwargs.get('value_amount', None)
        self.value_date = kwargs.get('value_date', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def adjustments(self):
        """Gets the adjustments of this BankTransaction.

            The adjustments applied on this bank transaction.

        :return: The adjustments of this BankTransaction.
        :rtype: list[PaymentAdjustment]
        """
        return self._adjustments

    @adjustments.setter
    def adjustments(self, adjustments):
        """Sets the adjustments of this BankTransaction.

            The adjustments applied on this bank transaction.

        :param adjustments: The adjustments of this BankTransaction.
        :type: list[PaymentAdjustment]
        """

        self._adjustments = adjustments
    
    @property
    def created_by(self):
        """Gets the created_by of this BankTransaction.

            The created by indicates the user which has created the bank transaction.

        :return: The created_by of this BankTransaction.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this BankTransaction.

            The created by indicates the user which has created the bank transaction.

        :param created_by: The created_by of this BankTransaction.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this BankTransaction.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this BankTransaction.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this BankTransaction.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this BankTransaction.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def currency_bank_account(self):
        """Gets the currency_bank_account of this BankTransaction.

            The currency bank account which is used to handle money flow.

        :return: The currency_bank_account of this BankTransaction.
        :rtype: CurrencyBankAccount
        """
        return self._currency_bank_account

    @currency_bank_account.setter
    def currency_bank_account(self, currency_bank_account):
        """Sets the currency_bank_account of this BankTransaction.

            The currency bank account which is used to handle money flow.

        :param currency_bank_account: The currency_bank_account of this BankTransaction.
        :type: CurrencyBankAccount
        """

        self._currency_bank_account = currency_bank_account
    
    @property
    def external_id(self):
        """Gets the external_id of this BankTransaction.

            

        :return: The external_id of this BankTransaction.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this BankTransaction.

            

        :param external_id: The external_id of this BankTransaction.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def flow_direction(self):
        """Gets the flow_direction of this BankTransaction.

            

        :return: The flow_direction of this BankTransaction.
        :rtype: BankTransactionFlowDirection
        """
        return self._flow_direction

    @flow_direction.setter
    def flow_direction(self, flow_direction):
        """Sets the flow_direction of this BankTransaction.

            

        :param flow_direction: The flow_direction of this BankTransaction.
        :type: BankTransactionFlowDirection
        """

        self._flow_direction = flow_direction
    
    @property
    def id(self):
        """Gets the id of this BankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this BankTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this BankTransaction.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this BankTransaction.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this BankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this BankTransaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this BankTransaction.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this BankTransaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this BankTransaction.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this BankTransaction.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this BankTransaction.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this BankTransaction.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def posting_amount(self):
        """Gets the posting_amount of this BankTransaction.

            The posting amount indicates the amount including adjustments.

        :return: The posting_amount of this BankTransaction.
        :rtype: float
        """
        return self._posting_amount

    @posting_amount.setter
    def posting_amount(self, posting_amount):
        """Sets the posting_amount of this BankTransaction.

            The posting amount indicates the amount including adjustments.

        :param posting_amount: The posting_amount of this BankTransaction.
        :type: float
        """

        self._posting_amount = posting_amount
    
    @property
    def reference(self):
        """Gets the reference of this BankTransaction.

            

        :return: The reference of this BankTransaction.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this BankTransaction.

            

        :param reference: The reference of this BankTransaction.
        :type: str
        """

        self._reference = reference
    
    @property
    def source(self):
        """Gets the source of this BankTransaction.

            

        :return: The source of this BankTransaction.
        :rtype: int
        """
        return self._source

    @source.setter
    def source(self, source):
        """Sets the source of this BankTransaction.

            

        :param source: The source of this BankTransaction.
        :type: int
        """

        self._source = source
    
    @property
    def state(self):
        """Gets the state of this BankTransaction.

            

        :return: The state of this BankTransaction.
        :rtype: BankTransactionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this BankTransaction.

            

        :param state: The state of this BankTransaction.
        :type: BankTransactionState
        """

        self._state = state
    
    @property
    def total_adjustment_amount_including_tax(self):
        """Gets the total_adjustment_amount_including_tax of this BankTransaction.

            

        :return: The total_adjustment_amount_including_tax of this BankTransaction.
        :rtype: float
        """
        return self._total_adjustment_amount_including_tax

    @total_adjustment_amount_including_tax.setter
    def total_adjustment_amount_including_tax(self, total_adjustment_amount_including_tax):
        """Sets the total_adjustment_amount_including_tax of this BankTransaction.

            

        :param total_adjustment_amount_including_tax: The total_adjustment_amount_including_tax of this BankTransaction.
        :type: float
        """

        self._total_adjustment_amount_including_tax = total_adjustment_amount_including_tax
    
    @property
    def type(self):
        """Gets the type of this BankTransaction.

            

        :return: The type of this BankTransaction.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this BankTransaction.

            

        :param type: The type of this BankTransaction.
        :type: int
        """

        self._type = type
    
    @property
    def value_amount(self):
        """Gets the value_amount of this BankTransaction.

            

        :return: The value_amount of this BankTransaction.
        :rtype: float
        """
        return self._value_amount

    @value_amount.setter
    def value_amount(self, value_amount):
        """Sets the value_amount of this BankTransaction.

            

        :param value_amount: The value_amount of this BankTransaction.
        :type: float
        """

        self._value_amount = value_amount
    
    @property
    def value_date(self):
        """Gets the value_date of this BankTransaction.

            The value date describes the date the amount is effective on the account.

        :return: The value_date of this BankTransaction.
        :rtype: datetime
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this BankTransaction.

            The value date describes the date the amount is effective on the account.

        :param value_date: The value_date of this BankTransaction.
        :type: datetime
        """

        self._value_date = value_date
    
    @property
    def version(self):
        """Gets the version of this BankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this BankTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this BankTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this BankTransaction.
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
        if issubclass(BankTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, BankTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
