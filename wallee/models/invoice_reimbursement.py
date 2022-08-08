# coding: utf-8
import pprint
import six
from enum import Enum



class InvoiceReimbursement:

    swagger_types = {
    
        'amount': 'float',
        'created_on': 'datetime',
        'currency': 'str',
        'discarded_by': 'int',
        'discarded_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'payment_connector_configuration': 'PaymentConnectorConfiguration',
        'payment_initiation_advice_file': 'PaymentInitiationAdviceFile',
        'processed_by': 'int',
        'processed_on': 'datetime',
        'recipient_city': 'str',
        'recipient_country': 'str',
        'recipient_family_name': 'str',
        'recipient_given_name': 'str',
        'recipient_iban': 'str',
        'recipient_postcode': 'str',
        'recipient_street': 'str',
        'sender_iban': 'str',
        'state': 'InvoiceReimbursementState',
        'version': 'int',
    }

    attribute_map = {
        'amount': 'amount','created_on': 'createdOn','currency': 'currency','discarded_by': 'discardedBy','discarded_on': 'discardedOn','id': 'id','linked_space_id': 'linkedSpaceId','payment_connector_configuration': 'paymentConnectorConfiguration','payment_initiation_advice_file': 'paymentInitiationAdviceFile','processed_by': 'processedBy','processed_on': 'processedOn','recipient_city': 'recipientCity','recipient_country': 'recipientCountry','recipient_family_name': 'recipientFamilyName','recipient_given_name': 'recipientGivenName','recipient_iban': 'recipientIban','recipient_postcode': 'recipientPostcode','recipient_street': 'recipientStreet','sender_iban': 'senderIban','state': 'state','version': 'version',
    }

    
    _amount = None
    _created_on = None
    _currency = None
    _discarded_by = None
    _discarded_on = None
    _id = None
    _linked_space_id = None
    _payment_connector_configuration = None
    _payment_initiation_advice_file = None
    _processed_by = None
    _processed_on = None
    _recipient_city = None
    _recipient_country = None
    _recipient_family_name = None
    _recipient_given_name = None
    _recipient_iban = None
    _recipient_postcode = None
    _recipient_street = None
    _sender_iban = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.created_on = kwargs.get('created_on', None)
        self.currency = kwargs.get('currency', None)
        self.discarded_by = kwargs.get('discarded_by', None)
        self.discarded_on = kwargs.get('discarded_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.payment_connector_configuration = kwargs.get('payment_connector_configuration', None)
        self.payment_initiation_advice_file = kwargs.get('payment_initiation_advice_file', None)
        self.processed_by = kwargs.get('processed_by', None)
        self.processed_on = kwargs.get('processed_on', None)
        self.recipient_city = kwargs.get('recipient_city', None)
        self.recipient_country = kwargs.get('recipient_country', None)
        self.recipient_family_name = kwargs.get('recipient_family_name', None)
        self.recipient_given_name = kwargs.get('recipient_given_name', None)
        self.recipient_iban = kwargs.get('recipient_iban', None)
        self.recipient_postcode = kwargs.get('recipient_postcode', None)
        self.recipient_street = kwargs.get('recipient_street', None)
        self.sender_iban = kwargs.get('sender_iban', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this InvoiceReimbursement.

            

        :return: The amount of this InvoiceReimbursement.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceReimbursement.

            

        :param amount: The amount of this InvoiceReimbursement.
        :type: float
        """

        self._amount = amount
    
    @property
    def created_on(self):
        """Gets the created_on of this InvoiceReimbursement.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this InvoiceReimbursement.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InvoiceReimbursement.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this InvoiceReimbursement.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def currency(self):
        """Gets the currency of this InvoiceReimbursement.

            

        :return: The currency of this InvoiceReimbursement.
        :rtype: str
        """
        return self._currency

    @currency.setter
    def currency(self, currency):
        """Sets the currency of this InvoiceReimbursement.

            

        :param currency: The currency of this InvoiceReimbursement.
        :type: str
        """

        self._currency = currency
    
    @property
    def discarded_by(self):
        """Gets the discarded_by of this InvoiceReimbursement.

            

        :return: The discarded_by of this InvoiceReimbursement.
        :rtype: int
        """
        return self._discarded_by

    @discarded_by.setter
    def discarded_by(self, discarded_by):
        """Sets the discarded_by of this InvoiceReimbursement.

            

        :param discarded_by: The discarded_by of this InvoiceReimbursement.
        :type: int
        """

        self._discarded_by = discarded_by
    
    @property
    def discarded_on(self):
        """Gets the discarded_on of this InvoiceReimbursement.

            

        :return: The discarded_on of this InvoiceReimbursement.
        :rtype: datetime
        """
        return self._discarded_on

    @discarded_on.setter
    def discarded_on(self, discarded_on):
        """Sets the discarded_on of this InvoiceReimbursement.

            

        :param discarded_on: The discarded_on of this InvoiceReimbursement.
        :type: datetime
        """

        self._discarded_on = discarded_on
    
    @property
    def id(self):
        """Gets the id of this InvoiceReimbursement.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InvoiceReimbursement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceReimbursement.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InvoiceReimbursement.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InvoiceReimbursement.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InvoiceReimbursement.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InvoiceReimbursement.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InvoiceReimbursement.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def payment_connector_configuration(self):
        """Gets the payment_connector_configuration of this InvoiceReimbursement.

            

        :return: The payment_connector_configuration of this InvoiceReimbursement.
        :rtype: PaymentConnectorConfiguration
        """
        return self._payment_connector_configuration

    @payment_connector_configuration.setter
    def payment_connector_configuration(self, payment_connector_configuration):
        """Sets the payment_connector_configuration of this InvoiceReimbursement.

            

        :param payment_connector_configuration: The payment_connector_configuration of this InvoiceReimbursement.
        :type: PaymentConnectorConfiguration
        """

        self._payment_connector_configuration = payment_connector_configuration
    
    @property
    def payment_initiation_advice_file(self):
        """Gets the payment_initiation_advice_file of this InvoiceReimbursement.

            

        :return: The payment_initiation_advice_file of this InvoiceReimbursement.
        :rtype: PaymentInitiationAdviceFile
        """
        return self._payment_initiation_advice_file

    @payment_initiation_advice_file.setter
    def payment_initiation_advice_file(self, payment_initiation_advice_file):
        """Sets the payment_initiation_advice_file of this InvoiceReimbursement.

            

        :param payment_initiation_advice_file: The payment_initiation_advice_file of this InvoiceReimbursement.
        :type: PaymentInitiationAdviceFile
        """

        self._payment_initiation_advice_file = payment_initiation_advice_file
    
    @property
    def processed_by(self):
        """Gets the processed_by of this InvoiceReimbursement.

            

        :return: The processed_by of this InvoiceReimbursement.
        :rtype: int
        """
        return self._processed_by

    @processed_by.setter
    def processed_by(self, processed_by):
        """Sets the processed_by of this InvoiceReimbursement.

            

        :param processed_by: The processed_by of this InvoiceReimbursement.
        :type: int
        """

        self._processed_by = processed_by
    
    @property
    def processed_on(self):
        """Gets the processed_on of this InvoiceReimbursement.

            

        :return: The processed_on of this InvoiceReimbursement.
        :rtype: datetime
        """
        return self._processed_on

    @processed_on.setter
    def processed_on(self, processed_on):
        """Sets the processed_on of this InvoiceReimbursement.

            

        :param processed_on: The processed_on of this InvoiceReimbursement.
        :type: datetime
        """

        self._processed_on = processed_on
    
    @property
    def recipient_city(self):
        """Gets the recipient_city of this InvoiceReimbursement.

            

        :return: The recipient_city of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_city

    @recipient_city.setter
    def recipient_city(self, recipient_city):
        """Sets the recipient_city of this InvoiceReimbursement.

            

        :param recipient_city: The recipient_city of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_city = recipient_city
    
    @property
    def recipient_country(self):
        """Gets the recipient_country of this InvoiceReimbursement.

            

        :return: The recipient_country of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_country

    @recipient_country.setter
    def recipient_country(self, recipient_country):
        """Sets the recipient_country of this InvoiceReimbursement.

            

        :param recipient_country: The recipient_country of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_country = recipient_country
    
    @property
    def recipient_family_name(self):
        """Gets the recipient_family_name of this InvoiceReimbursement.

            

        :return: The recipient_family_name of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_family_name

    @recipient_family_name.setter
    def recipient_family_name(self, recipient_family_name):
        """Sets the recipient_family_name of this InvoiceReimbursement.

            

        :param recipient_family_name: The recipient_family_name of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_family_name = recipient_family_name
    
    @property
    def recipient_given_name(self):
        """Gets the recipient_given_name of this InvoiceReimbursement.

            

        :return: The recipient_given_name of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_given_name

    @recipient_given_name.setter
    def recipient_given_name(self, recipient_given_name):
        """Sets the recipient_given_name of this InvoiceReimbursement.

            

        :param recipient_given_name: The recipient_given_name of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_given_name = recipient_given_name
    
    @property
    def recipient_iban(self):
        """Gets the recipient_iban of this InvoiceReimbursement.

            

        :return: The recipient_iban of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_iban

    @recipient_iban.setter
    def recipient_iban(self, recipient_iban):
        """Sets the recipient_iban of this InvoiceReimbursement.

            

        :param recipient_iban: The recipient_iban of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_iban = recipient_iban
    
    @property
    def recipient_postcode(self):
        """Gets the recipient_postcode of this InvoiceReimbursement.

            

        :return: The recipient_postcode of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_postcode

    @recipient_postcode.setter
    def recipient_postcode(self, recipient_postcode):
        """Sets the recipient_postcode of this InvoiceReimbursement.

            

        :param recipient_postcode: The recipient_postcode of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_postcode = recipient_postcode
    
    @property
    def recipient_street(self):
        """Gets the recipient_street of this InvoiceReimbursement.

            

        :return: The recipient_street of this InvoiceReimbursement.
        :rtype: str
        """
        return self._recipient_street

    @recipient_street.setter
    def recipient_street(self, recipient_street):
        """Sets the recipient_street of this InvoiceReimbursement.

            

        :param recipient_street: The recipient_street of this InvoiceReimbursement.
        :type: str
        """

        self._recipient_street = recipient_street
    
    @property
    def sender_iban(self):
        """Gets the sender_iban of this InvoiceReimbursement.

            

        :return: The sender_iban of this InvoiceReimbursement.
        :rtype: str
        """
        return self._sender_iban

    @sender_iban.setter
    def sender_iban(self, sender_iban):
        """Sets the sender_iban of this InvoiceReimbursement.

            

        :param sender_iban: The sender_iban of this InvoiceReimbursement.
        :type: str
        """

        self._sender_iban = sender_iban
    
    @property
    def state(self):
        """Gets the state of this InvoiceReimbursement.

            

        :return: The state of this InvoiceReimbursement.
        :rtype: InvoiceReimbursementState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this InvoiceReimbursement.

            

        :param state: The state of this InvoiceReimbursement.
        :type: InvoiceReimbursementState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this InvoiceReimbursement.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this InvoiceReimbursement.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this InvoiceReimbursement.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this InvoiceReimbursement.
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
        if issubclass(InvoiceReimbursement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceReimbursement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
