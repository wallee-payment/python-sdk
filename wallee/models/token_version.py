# coding: utf-8
import pprint
import six
from enum import Enum



class TokenVersion:

    swagger_types = {
    
        'activated_on': 'datetime',
        'billing_address': 'Address',
        'created_on': 'datetime',
        'environment': 'ChargeAttemptEnvironment',
        'expires_on': 'datetime',
        'icon_url': 'str',
        'id': 'int',
        'labels': 'list[Label]',
        'language': 'str',
        'linked_space_id': 'int',
        'name': 'str',
        'obsoleted_on': 'datetime',
        'payment_connector_configuration': 'PaymentConnectorConfiguration',
        'payment_information_hashes': 'list[PaymentInformationHash]',
        'payment_method': 'int',
        'payment_method_brand': 'int',
        'planned_purge_date': 'datetime',
        'processor_token': 'str',
        'shipping_address': 'Address',
        'state': 'TokenVersionState',
        'token': 'Token',
        'type': 'TokenVersionType',
        'version': 'int',
    }

    attribute_map = {
        'activated_on': 'activatedOn','billing_address': 'billingAddress','created_on': 'createdOn','environment': 'environment','expires_on': 'expiresOn','icon_url': 'iconUrl','id': 'id','labels': 'labels','language': 'language','linked_space_id': 'linkedSpaceId','name': 'name','obsoleted_on': 'obsoletedOn','payment_connector_configuration': 'paymentConnectorConfiguration','payment_information_hashes': 'paymentInformationHashes','payment_method': 'paymentMethod','payment_method_brand': 'paymentMethodBrand','planned_purge_date': 'plannedPurgeDate','processor_token': 'processorToken','shipping_address': 'shippingAddress','state': 'state','token': 'token','type': 'type','version': 'version',
    }

    
    _activated_on = None
    _billing_address = None
    _created_on = None
    _environment = None
    _expires_on = None
    _icon_url = None
    _id = None
    _labels = None
    _language = None
    _linked_space_id = None
    _name = None
    _obsoleted_on = None
    _payment_connector_configuration = None
    _payment_information_hashes = None
    _payment_method = None
    _payment_method_brand = None
    _planned_purge_date = None
    _processor_token = None
    _shipping_address = None
    _state = None
    _token = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.activated_on = kwargs.get('activated_on', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.created_on = kwargs.get('created_on', None)
        self.environment = kwargs.get('environment', None)
        self.expires_on = kwargs.get('expires_on', None)
        self.icon_url = kwargs.get('icon_url', None)
        self.id = kwargs.get('id', None)
        self.labels = kwargs.get('labels', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.obsoleted_on = kwargs.get('obsoleted_on', None)
        self.payment_connector_configuration = kwargs.get('payment_connector_configuration', None)
        self.payment_information_hashes = kwargs.get('payment_information_hashes', None)
        self.payment_method = kwargs.get('payment_method', None)
        self.payment_method_brand = kwargs.get('payment_method_brand', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processor_token = kwargs.get('processor_token', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.state = kwargs.get('state', None)
        self.token = kwargs.get('token', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def activated_on(self):
        """Gets the activated_on of this TokenVersion.

            

        :return: The activated_on of this TokenVersion.
        :rtype: datetime
        """
        return self._activated_on

    @activated_on.setter
    def activated_on(self, activated_on):
        """Sets the activated_on of this TokenVersion.

            

        :param activated_on: The activated_on of this TokenVersion.
        :type: datetime
        """

        self._activated_on = activated_on
    
    @property
    def billing_address(self):
        """Gets the billing_address of this TokenVersion.

            

        :return: The billing_address of this TokenVersion.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this TokenVersion.

            

        :param billing_address: The billing_address of this TokenVersion.
        :type: Address
        """

        self._billing_address = billing_address
    
    @property
    def created_on(self):
        """Gets the created_on of this TokenVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this TokenVersion.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this TokenVersion.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this TokenVersion.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def environment(self):
        """Gets the environment of this TokenVersion.

            

        :return: The environment of this TokenVersion.
        :rtype: ChargeAttemptEnvironment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this TokenVersion.

            

        :param environment: The environment of this TokenVersion.
        :type: ChargeAttemptEnvironment
        """

        self._environment = environment
    
    @property
    def expires_on(self):
        """Gets the expires_on of this TokenVersion.

            The expires on date indicates when token version expires. Once this date is reached the token version is marked as obsolete.

        :return: The expires_on of this TokenVersion.
        :rtype: datetime
        """
        return self._expires_on

    @expires_on.setter
    def expires_on(self, expires_on):
        """Sets the expires_on of this TokenVersion.

            The expires on date indicates when token version expires. Once this date is reached the token version is marked as obsolete.

        :param expires_on: The expires_on of this TokenVersion.
        :type: datetime
        """

        self._expires_on = expires_on
    
    @property
    def icon_url(self):
        """Gets the icon_url of this TokenVersion.

            

        :return: The icon_url of this TokenVersion.
        :rtype: str
        """
        return self._icon_url

    @icon_url.setter
    def icon_url(self, icon_url):
        """Sets the icon_url of this TokenVersion.

            

        :param icon_url: The icon_url of this TokenVersion.
        :type: str
        """

        self._icon_url = icon_url
    
    @property
    def id(self):
        """Gets the id of this TokenVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this TokenVersion.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TokenVersion.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this TokenVersion.
        :type: int
        """

        self._id = id
    
    @property
    def labels(self):
        """Gets the labels of this TokenVersion.

            

        :return: The labels of this TokenVersion.
        :rtype: list[Label]
        """
        return self._labels

    @labels.setter
    def labels(self, labels):
        """Sets the labels of this TokenVersion.

            

        :param labels: The labels of this TokenVersion.
        :type: list[Label]
        """

        self._labels = labels
    
    @property
    def language(self):
        """Gets the language of this TokenVersion.

            

        :return: The language of this TokenVersion.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this TokenVersion.

            

        :param language: The language of this TokenVersion.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this TokenVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this TokenVersion.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this TokenVersion.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this TokenVersion.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this TokenVersion.

            

        :return: The name of this TokenVersion.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this TokenVersion.

            

        :param name: The name of this TokenVersion.
        :type: str
        """
        if name is not None and len(name) > 150:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")

        self._name = name
    
    @property
    def obsoleted_on(self):
        """Gets the obsoleted_on of this TokenVersion.

            

        :return: The obsoleted_on of this TokenVersion.
        :rtype: datetime
        """
        return self._obsoleted_on

    @obsoleted_on.setter
    def obsoleted_on(self, obsoleted_on):
        """Sets the obsoleted_on of this TokenVersion.

            

        :param obsoleted_on: The obsoleted_on of this TokenVersion.
        :type: datetime
        """

        self._obsoleted_on = obsoleted_on
    
    @property
    def payment_connector_configuration(self):
        """Gets the payment_connector_configuration of this TokenVersion.

            

        :return: The payment_connector_configuration of this TokenVersion.
        :rtype: PaymentConnectorConfiguration
        """
        return self._payment_connector_configuration

    @payment_connector_configuration.setter
    def payment_connector_configuration(self, payment_connector_configuration):
        """Sets the payment_connector_configuration of this TokenVersion.

            

        :param payment_connector_configuration: The payment_connector_configuration of this TokenVersion.
        :type: PaymentConnectorConfiguration
        """

        self._payment_connector_configuration = payment_connector_configuration
    
    @property
    def payment_information_hashes(self):
        """Gets the payment_information_hashes of this TokenVersion.

            The payment information hash set contains hashes of the payment information represented by this token version.

        :return: The payment_information_hashes of this TokenVersion.
        :rtype: list[PaymentInformationHash]
        """
        return self._payment_information_hashes

    @payment_information_hashes.setter
    def payment_information_hashes(self, payment_information_hashes):
        """Sets the payment_information_hashes of this TokenVersion.

            The payment information hash set contains hashes of the payment information represented by this token version.

        :param payment_information_hashes: The payment_information_hashes of this TokenVersion.
        :type: list[PaymentInformationHash]
        """

        self._payment_information_hashes = payment_information_hashes
    
    @property
    def payment_method(self):
        """Gets the payment_method of this TokenVersion.

            

        :return: The payment_method of this TokenVersion.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this TokenVersion.

            

        :param payment_method: The payment_method of this TokenVersion.
        :type: int
        """

        self._payment_method = payment_method
    
    @property
    def payment_method_brand(self):
        """Gets the payment_method_brand of this TokenVersion.

            

        :return: The payment_method_brand of this TokenVersion.
        :rtype: int
        """
        return self._payment_method_brand

    @payment_method_brand.setter
    def payment_method_brand(self, payment_method_brand):
        """Sets the payment_method_brand of this TokenVersion.

            

        :param payment_method_brand: The payment_method_brand of this TokenVersion.
        :type: int
        """

        self._payment_method_brand = payment_method_brand
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this TokenVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this TokenVersion.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this TokenVersion.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this TokenVersion.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processor_token(self):
        """Gets the processor_token of this TokenVersion.

            

        :return: The processor_token of this TokenVersion.
        :rtype: str
        """
        return self._processor_token

    @processor_token.setter
    def processor_token(self, processor_token):
        """Sets the processor_token of this TokenVersion.

            

        :param processor_token: The processor_token of this TokenVersion.
        :type: str
        """
        if processor_token is not None and len(processor_token) > 150:
            raise ValueError("Invalid value for `processor_token`, length must be less than or equal to `150`")

        self._processor_token = processor_token
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this TokenVersion.

            

        :return: The shipping_address of this TokenVersion.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this TokenVersion.

            

        :param shipping_address: The shipping_address of this TokenVersion.
        :type: Address
        """

        self._shipping_address = shipping_address
    
    @property
    def state(self):
        """Gets the state of this TokenVersion.

            

        :return: The state of this TokenVersion.
        :rtype: TokenVersionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this TokenVersion.

            

        :param state: The state of this TokenVersion.
        :type: TokenVersionState
        """

        self._state = state
    
    @property
    def token(self):
        """Gets the token of this TokenVersion.

            

        :return: The token of this TokenVersion.
        :rtype: Token
        """
        return self._token

    @token.setter
    def token(self, token):
        """Sets the token of this TokenVersion.

            

        :param token: The token of this TokenVersion.
        :type: Token
        """

        self._token = token
    
    @property
    def type(self):
        """Gets the type of this TokenVersion.

            The token version type determines what kind of token it is and by which payment connector the token can be processed by.

        :return: The type of this TokenVersion.
        :rtype: TokenVersionType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this TokenVersion.

            The token version type determines what kind of token it is and by which payment connector the token can be processed by.

        :param type: The type of this TokenVersion.
        :type: TokenVersionType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this TokenVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this TokenVersion.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this TokenVersion.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this TokenVersion.
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
        if issubclass(TokenVersion, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TokenVersion):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
