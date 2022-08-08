# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class InvoiceReconciliationRecord(TransactionAwareEntity):

    swagger_types = {
    
        'address': 'str',
        'amount': 'float',
        'city': 'str',
        'country': 'str',
        'created_on': 'datetime',
        'currency': 'str',
        'discarded_by': 'int',
        'discarded_on': 'datetime',
        'environment': 'ChargeAttemptEnvironment',
        'family_name': 'str',
        'given_name': 'str',
        'iban': 'str',
        'last_resolution_failure': 'FailureReason',
        'participant_number': 'str',
        'payment_fee_amount': 'float',
        'payment_fee_currency': 'str',
        'payment_reason': 'str',
        'planned_purge_date': 'datetime',
        'post_code': 'str',
        'reference_number': 'str',
        'rejection_status': 'InvoiceReconciliationRecordRejectionStatus',
        'resolved_by': 'int',
        'resolved_on': 'datetime',
        'sender_bank_account': 'str',
        'state': 'InvoiceReconciliationRecordState',
        'street': 'str',
        'type': 'InvoiceReconciliationRecordType',
        'unique_id': 'str',
        'value_date': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'address': 'address','amount': 'amount','city': 'city','country': 'country','created_on': 'createdOn','currency': 'currency','discarded_by': 'discardedBy','discarded_on': 'discardedOn','environment': 'environment','family_name': 'familyName','given_name': 'givenName','iban': 'iban','last_resolution_failure': 'lastResolutionFailure','participant_number': 'participantNumber','payment_fee_amount': 'paymentFeeAmount','payment_fee_currency': 'paymentFeeCurrency','payment_reason': 'paymentReason','planned_purge_date': 'plannedPurgeDate','post_code': 'postCode','reference_number': 'referenceNumber','rejection_status': 'rejectionStatus','resolved_by': 'resolvedBy','resolved_on': 'resolvedOn','sender_bank_account': 'senderBankAccount','state': 'state','street': 'street','type': 'type','unique_id': 'uniqueId','value_date': 'valueDate','version': 'version',
    }

    
    _address = None
    _amount = None
    _city = None
    _country = None
    _created_on = None
    _currency = None
    _discarded_by = None
    _discarded_on = None
    _environment = None
    _family_name = None
    _given_name = None
    _iban = None
    _last_resolution_failure = None
    _participant_number = None
    _payment_fee_amount = None
    _payment_fee_currency = None
    _payment_reason = None
    _planned_purge_date = None
    _post_code = None
    _reference_number = None
    _rejection_status = None
    _resolved_by = None
    _resolved_on = None
    _sender_bank_account = None
    _state = None
    _street = None
    _type = None
    _unique_id = None
    _value_date = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.address = kwargs.get('address', None)
        self.amount = kwargs.get('amount', None)
        self.city = kwargs.get('city', None)
        self.country = kwargs.get('country', None)
        self.created_on = kwargs.get('created_on', None)
        self.currency = kwargs.get('currency', None)
        self.discarded_by = kwargs.get('discarded_by', None)
        self.discarded_on = kwargs.get('discarded_on', None)
        self.environment = kwargs.get('environment', None)
        self.family_name = kwargs.get('family_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.iban = kwargs.get('iban', None)
        self.last_resolution_failure = kwargs.get('last_resolution_failure', None)
        self.participant_number = kwargs.get('participant_number', None)
        self.payment_fee_amount = kwargs.get('payment_fee_amount', None)
        self.payment_fee_currency = kwargs.get('payment_fee_currency', None)
        self.payment_reason = kwargs.get('payment_reason', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.post_code = kwargs.get('post_code', None)
        self.reference_number = kwargs.get('reference_number', None)
        self.rejection_status = kwargs.get('rejection_status', None)
        self.resolved_by = kwargs.get('resolved_by', None)
        self.resolved_on = kwargs.get('resolved_on', None)
        self.sender_bank_account = kwargs.get('sender_bank_account', None)
        self.state = kwargs.get('state', None)
        self.street = kwargs.get('street', None)
        self.type = kwargs.get('type', None)
        self.unique_id = kwargs.get('unique_id', None)
        self.value_date = kwargs.get('value_date', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def address(self):
        """Gets the address of this InvoiceReconciliationRecord.

            

        :return: The address of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this InvoiceReconciliationRecord.

            

        :param address: The address of this InvoiceReconciliationRecord.
        :type: str
        """

        self._address = address
    
    @property
    def amount(self):
        """Gets the amount of this InvoiceReconciliationRecord.

            

        :return: The amount of this InvoiceReconciliationRecord.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceReconciliationRecord.

            

        :param amount: The amount of this InvoiceReconciliationRecord.
        :type: float
        """

        self._amount = amount
    
    @property
    def city(self):
        """Gets the city of this InvoiceReconciliationRecord.

            

        :return: The city of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this InvoiceReconciliationRecord.

            

        :param city: The city of this InvoiceReconciliationRecord.
        :type: str
        """

        self._city = city
    
    @property
    def country(self):
        """Gets the country of this InvoiceReconciliationRecord.

            

        :return: The country of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this InvoiceReconciliationRecord.

            

        :param country: The country of this InvoiceReconciliationRecord.
        :type: str
        """

        self._country = country
    
    @property
    def created_on(self):
        """Gets the created_on of this InvoiceReconciliationRecord.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this InvoiceReconciliationRecord.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InvoiceReconciliationRecord.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this InvoiceReconciliationRecord.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def currency(self):
        """Gets the currency of this InvoiceReconciliationRecord.

            

        :return: The currency of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceReconciliationRecord.

            

        :param currency: The currency of this InvoiceReconciliationRecord.
        :type: str
        """

        self._currency = currency
    
    @property
    def discarded_by(self):
        """Gets the discarded_by of this InvoiceReconciliationRecord.

            

        :return: The discarded_by of this InvoiceReconciliationRecord.
        :rtype: int
        """
        return self._discarded_by

    @discarded_by.setter
    def discarded_by(self, discarded_by):
        """Sets the discarded_by of this InvoiceReconciliationRecord.

            

        :param discarded_by: The discarded_by of this InvoiceReconciliationRecord.
        :type: int
        """

        self._discarded_by = discarded_by
    
    @property
    def discarded_on(self):
        """Gets the discarded_on of this InvoiceReconciliationRecord.

            The discarded on date indicates when the bank transaction has been discarded.

        :return: The discarded_on of this InvoiceReconciliationRecord.
        :rtype: datetime
        """
        return self._discarded_on

    @discarded_on.setter
    def discarded_on(self, discarded_on):
        """Sets the discarded_on of this InvoiceReconciliationRecord.

            The discarded on date indicates when the bank transaction has been discarded.

        :param discarded_on: The discarded_on of this InvoiceReconciliationRecord.
        :type: datetime
        """

        self._discarded_on = discarded_on
    
    @property
    def environment(self):
        """Gets the environment of this InvoiceReconciliationRecord.

            

        :return: The environment of this InvoiceReconciliationRecord.
        :rtype: ChargeAttemptEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this InvoiceReconciliationRecord.

            

        :param environment: The environment of this InvoiceReconciliationRecord.
        :type: ChargeAttemptEnvironment
        """

        self._environment = environment
    
    @property
    def family_name(self):
        """Gets the family_name of this InvoiceReconciliationRecord.

            

        :return: The family_name of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this InvoiceReconciliationRecord.

            

        :param family_name: The family_name of this InvoiceReconciliationRecord.
        :type: str
        """

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this InvoiceReconciliationRecord.

            

        :return: The given_name of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this InvoiceReconciliationRecord.

            

        :param given_name: The given_name of this InvoiceReconciliationRecord.
        :type: str
        """

        self._given_name = given_name
    
    @property
    def iban(self):
        """Gets the iban of this InvoiceReconciliationRecord.

            

        :return: The iban of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._iban

    @iban.setter
    def iban(self, iban):
        """Sets the iban of this InvoiceReconciliationRecord.

            

        :param iban: The iban of this InvoiceReconciliationRecord.
        :type: str
        """
        if iban is not None and len(iban) > 100:
            raise ValueError("Invalid value for `iban`, length must be less than or equal to `100`")

        self._iban = iban
    
    @property
    def last_resolution_failure(self):
        """Gets the last_resolution_failure of this InvoiceReconciliationRecord.

            

        :return: The last_resolution_failure of this InvoiceReconciliationRecord.
        :rtype: FailureReason
        """
        return self._last_resolution_failure

    @last_resolution_failure.setter
    def last_resolution_failure(self, last_resolution_failure):
        """Sets the last_resolution_failure of this InvoiceReconciliationRecord.

            

        :param last_resolution_failure: The last_resolution_failure of this InvoiceReconciliationRecord.
        :type: FailureReason
        """

        self._last_resolution_failure = last_resolution_failure
    
    @property
    def participant_number(self):
        """Gets the participant_number of this InvoiceReconciliationRecord.

            

        :return: The participant_number of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._participant_number

    @participant_number.setter
    def participant_number(self, participant_number):
        """Sets the participant_number of this InvoiceReconciliationRecord.

            

        :param participant_number: The participant_number of this InvoiceReconciliationRecord.
        :type: str
        """
        if participant_number is not None and len(participant_number) > 100:
            raise ValueError("Invalid value for `participant_number`, length must be less than or equal to `100`")

        self._participant_number = participant_number
    
    @property
    def payment_fee_amount(self):
        """Gets the payment_fee_amount of this InvoiceReconciliationRecord.

            

        :return: The payment_fee_amount of this InvoiceReconciliationRecord.
        :rtype: float
        """
        return self._payment_fee_amount

    @payment_fee_amount.setter
    def payment_fee_amount(self, payment_fee_amount):
        """Sets the payment_fee_amount of this InvoiceReconciliationRecord.

            

        :param payment_fee_amount: The payment_fee_amount of this InvoiceReconciliationRecord.
        :type: float
        """

        self._payment_fee_amount = payment_fee_amount
    
    @property
    def payment_fee_currency(self):
        """Gets the payment_fee_currency of this InvoiceReconciliationRecord.

            

        :return: The payment_fee_currency of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._payment_fee_currency

    @payment_fee_currency.setter
    def payment_fee_currency(self, payment_fee_currency):
        """Sets the payment_fee_currency of this InvoiceReconciliationRecord.

            

        :param payment_fee_currency: The payment_fee_currency of this InvoiceReconciliationRecord.
        :type: str
        """

        self._payment_fee_currency = payment_fee_currency
    
    @property
    def payment_reason(self):
        """Gets the payment_reason of this InvoiceReconciliationRecord.

            

        :return: The payment_reason of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._payment_reason

    @payment_reason.setter
    def payment_reason(self, payment_reason):
        """Sets the payment_reason of this InvoiceReconciliationRecord.

            

        :param payment_reason: The payment_reason of this InvoiceReconciliationRecord.
        :type: str
        """

        self._payment_reason = payment_reason
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this InvoiceReconciliationRecord.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this InvoiceReconciliationRecord.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this InvoiceReconciliationRecord.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this InvoiceReconciliationRecord.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def post_code(self):
        """Gets the post_code of this InvoiceReconciliationRecord.

            

        :return: The post_code of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._post_code

    @post_code.setter
    def post_code(self, post_code):
        """Sets the post_code of this InvoiceReconciliationRecord.

            

        :param post_code: The post_code of this InvoiceReconciliationRecord.
        :type: str
        """

        self._post_code = post_code
    
    @property
    def reference_number(self):
        """Gets the reference_number of this InvoiceReconciliationRecord.

            

        :return: The reference_number of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._reference_number

    @reference_number.setter
    def reference_number(self, reference_number):
        """Sets the reference_number of this InvoiceReconciliationRecord.

            

        :param reference_number: The reference_number of this InvoiceReconciliationRecord.
        :type: str
        """
        if reference_number is not None and len(reference_number) > 255:
            raise ValueError("Invalid value for `reference_number`, length must be less than or equal to `255`")

        self._reference_number = reference_number
    
    @property
    def rejection_status(self):
        """Gets the rejection_status of this InvoiceReconciliationRecord.

            

        :return: The rejection_status of this InvoiceReconciliationRecord.
        :rtype: InvoiceReconciliationRecordRejectionStatus
        """
        return self._rejection_status

    @rejection_status.setter
    def rejection_status(self, rejection_status):
        """Sets the rejection_status of this InvoiceReconciliationRecord.

            

        :param rejection_status: The rejection_status of this InvoiceReconciliationRecord.
        :type: InvoiceReconciliationRecordRejectionStatus
        """

        self._rejection_status = rejection_status
    
    @property
    def resolved_by(self):
        """Gets the resolved_by of this InvoiceReconciliationRecord.

            

        :return: The resolved_by of this InvoiceReconciliationRecord.
        :rtype: int
        """
        return self._resolved_by

    @resolved_by.setter
    def resolved_by(self, resolved_by):
        """Sets the resolved_by of this InvoiceReconciliationRecord.

            

        :param resolved_by: The resolved_by of this InvoiceReconciliationRecord.
        :type: int
        """

        self._resolved_by = resolved_by
    
    @property
    def resolved_on(self):
        """Gets the resolved_on of this InvoiceReconciliationRecord.

            The resolved on date indicates when the bank transaction has been resolved.

        :return: The resolved_on of this InvoiceReconciliationRecord.
        :rtype: datetime
        """
        return self._resolved_on

    @resolved_on.setter
    def resolved_on(self, resolved_on):
        """Sets the resolved_on of this InvoiceReconciliationRecord.

            The resolved on date indicates when the bank transaction has been resolved.

        :param resolved_on: The resolved_on of this InvoiceReconciliationRecord.
        :type: datetime
        """

        self._resolved_on = resolved_on
    
    @property
    def sender_bank_account(self):
        """Gets the sender_bank_account of this InvoiceReconciliationRecord.

            

        :return: The sender_bank_account of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._sender_bank_account

    @sender_bank_account.setter
    def sender_bank_account(self, sender_bank_account):
        """Sets the sender_bank_account of this InvoiceReconciliationRecord.

            

        :param sender_bank_account: The sender_bank_account of this InvoiceReconciliationRecord.
        :type: str
        """

        self._sender_bank_account = sender_bank_account
    
    @property
    def state(self):
        """Gets the state of this InvoiceReconciliationRecord.

            

        :return: The state of this InvoiceReconciliationRecord.
        :rtype: InvoiceReconciliationRecordState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvoiceReconciliationRecord.

            

        :param state: The state of this InvoiceReconciliationRecord.
        :type: InvoiceReconciliationRecordState
        """

        self._state = state
    
    @property
    def street(self):
        """Gets the street of this InvoiceReconciliationRecord.

            

        :return: The street of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this InvoiceReconciliationRecord.

            

        :param street: The street of this InvoiceReconciliationRecord.
        :type: str
        """

        self._street = street
    
    @property
    def type(self):
        """Gets the type of this InvoiceReconciliationRecord.

            

        :return: The type of this InvoiceReconciliationRecord.
        :rtype: InvoiceReconciliationRecordType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this InvoiceReconciliationRecord.

            

        :param type: The type of this InvoiceReconciliationRecord.
        :type: InvoiceReconciliationRecordType
        """

        self._type = type
    
    @property
    def unique_id(self):
        """Gets the unique_id of this InvoiceReconciliationRecord.

            

        :return: The unique_id of this InvoiceReconciliationRecord.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this InvoiceReconciliationRecord.

            

        :param unique_id: The unique_id of this InvoiceReconciliationRecord.
        :type: str
        """
        if unique_id is not None and len(unique_id) > 500:
            raise ValueError("Invalid value for `unique_id`, length must be less than or equal to `500`")

        self._unique_id = unique_id
    
    @property
    def value_date(self):
        """Gets the value_date of this InvoiceReconciliationRecord.

            

        :return: The value_date of this InvoiceReconciliationRecord.
        :rtype: datetime
        """
        return self._value_date

    @value_date.setter
    def value_date(self, value_date):
        """Sets the value_date of this InvoiceReconciliationRecord.

            

        :param value_date: The value_date of this InvoiceReconciliationRecord.
        :type: datetime
        """

        self._value_date = value_date
    
    @property
    def version(self):
        """Gets the version of this InvoiceReconciliationRecord.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InvoiceReconciliationRecord.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InvoiceReconciliationRecord.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InvoiceReconciliationRecord.
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
        if issubclass(InvoiceReconciliationRecord, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceReconciliationRecord):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
