# coding: utf-8
import pprint
import six
from enum import Enum



class Token:

    swagger_types = {
    
        'created_on': 'datetime',
        'customer_email_address': 'str',
        'customer_id': 'str',
        'enabled_for_one_click_payment': 'bool',
        'external_id': 'str',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'planned_purge_date': 'datetime',
        'state': 'CreationEntityState',
        'time_zone': 'str',
        'token_reference': 'str',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','customer_email_address': 'customerEmailAddress','customer_id': 'customerId','enabled_for_one_click_payment': 'enabledForOneClickPayment','external_id': 'externalId','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','planned_purge_date': 'plannedPurgeDate','state': 'state','time_zone': 'timeZone','token_reference': 'tokenReference','version': 'version',
    }

    
    _created_on = None
    _customer_email_address = None
    _customer_id = None
    _enabled_for_one_click_payment = None
    _external_id = None
    _id = None
    _language = None
    _linked_space_id = None
    _planned_purge_date = None
    _state = None
    _time_zone = None
    _token_reference = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.customer_email_address = kwargs.get('customer_email_address', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.enabled_for_one_click_payment = kwargs.get('enabled_for_one_click_payment', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.time_zone = kwargs.get('time_zone', None)
        self.token_reference = kwargs.get('token_reference', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this Token.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this Token.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Token.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this Token.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def customer_email_address(self):
        """Gets the customer_email_address of this Token.

            The customer email address is the email address of the customer.

        :return: The customer_email_address of this Token.
        :rtype: str
        """
        return self._customer_email_address

    @customer_email_address.setter
    def customer_email_address(self, customer_email_address):
        """Sets the customer_email_address of this Token.

            The customer email address is the email address of the customer.

        :param customer_email_address: The customer_email_address of this Token.
        :type: str
        """
        if customer_email_address is not None and len(customer_email_address) > 150:
            raise ValueError("Invalid value for `customer_email_address`, length must be less than or equal to `150`")

        self._customer_email_address = customer_email_address
    
    @property
    def customer_id(self):
        """Gets the customer_id of this Token.

            The customer ID identifies the customer in the merchant system. In case the customer ID has been provided it has to correspond with the customer ID provided on the transaction. The customer ID will not be changed automatically. The merchant system has to provide it.

        :return: The customer_id of this Token.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Token.

            The customer ID identifies the customer in the merchant system. In case the customer ID has been provided it has to correspond with the customer ID provided on the transaction. The customer ID will not be changed automatically. The merchant system has to provide it.

        :param customer_id: The customer_id of this Token.
        :type: str
        """

        self._customer_id = customer_id
    
    @property
    def enabled_for_one_click_payment(self):
        """Gets the enabled_for_one_click_payment of this Token.

            When a token is enabled for one-click payments the buyer will be able to select the token within the iFrame or on the payment page to pay with the token. The usage of the token will reduce the number of steps the buyer has to go through. The buyer is linked via the customer ID on the transaction with the token. Means the token will be visible for buyers with the same customer ID. Additionally the payment method has to be configured to allow the one-click payments.

        :return: The enabled_for_one_click_payment of this Token.
        :rtype: bool
        """
        return self._enabled_for_one_click_payment

    @enabled_for_one_click_payment.setter
    def enabled_for_one_click_payment(self, enabled_for_one_click_payment):
        """Sets the enabled_for_one_click_payment of this Token.

            When a token is enabled for one-click payments the buyer will be able to select the token within the iFrame or on the payment page to pay with the token. The usage of the token will reduce the number of steps the buyer has to go through. The buyer is linked via the customer ID on the transaction with the token. Means the token will be visible for buyers with the same customer ID. Additionally the payment method has to be configured to allow the one-click payments.

        :param enabled_for_one_click_payment: The enabled_for_one_click_payment of this Token.
        :type: bool
        """

        self._enabled_for_one_click_payment = enabled_for_one_click_payment
    
    @property
    def external_id(self):
        """Gets the external_id of this Token.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this Token.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Token.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this Token.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this Token.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Token.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Token.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Token.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this Token.

            

        :return: The language of this Token.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Token.

            

        :param language: The language of this Token.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Token.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Token.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Token.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Token.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Token.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Token.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Token.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Token.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this Token.

            

        :return: The state of this Token.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Token.

            

        :param state: The state of this Token.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def time_zone(self):
        """Gets the time_zone of this Token.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :return: The time_zone of this Token.
        :rtype: str
        """
        return self._time_zone

    @time_zone.setter
    def time_zone(self, time_zone):
        """Sets the time_zone of this Token.

            The time zone defines in which time zone the customer is located in. The time zone may affects how dates are formatted when interacting with the customer.

        :param time_zone: The time_zone of this Token.
        :type: str
        """

        self._time_zone = time_zone
    
    @property
    def token_reference(self):
        """Gets the token_reference of this Token.

            Use something that it is easy to identify and may help you find the token (e.g. customer id, email address).

        :return: The token_reference of this Token.
        :rtype: str
        """
        return self._token_reference

    @token_reference.setter
    def token_reference(self, token_reference):
        """Sets the token_reference of this Token.

            Use something that it is easy to identify and may help you find the token (e.g. customer id, email address).

        :param token_reference: The token_reference of this Token.
        :type: str
        """
        if token_reference is not None and len(token_reference) > 100:
            raise ValueError("Invalid value for `token_reference`, length must be less than or equal to `100`")

        self._token_reference = token_reference
    
    @property
    def version(self):
        """Gets the version of this Token.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Token.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Token.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Token.
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
        if issubclass(Token, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Token):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
