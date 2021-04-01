# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscription:

    swagger_types = {
    
        'created_by': 'int',
        'created_on': 'datetime',
        'external_id': 'str',
        'id': 'int',
        'initial_execution_date': 'datetime',
        'initial_payment_transaction': 'int',
        'initial_shopify_transaction': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'order_recurrence_number': 'int',
        'shop': 'int',
        'state': 'ShopifySubscriptionState',
        'subscriber': 'ShopifySubscriber',
        'terminated_by': 'int',
        'terminated_on': 'datetime',
        'termination_request_date': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'created_by': 'createdBy','created_on': 'createdOn','external_id': 'externalId','id': 'id','initial_execution_date': 'initialExecutionDate','initial_payment_transaction': 'initialPaymentTransaction','initial_shopify_transaction': 'initialShopifyTransaction','language': 'language','linked_space_id': 'linkedSpaceId','order_recurrence_number': 'orderRecurrenceNumber','shop': 'shop','state': 'state','subscriber': 'subscriber','terminated_by': 'terminatedBy','terminated_on': 'terminatedOn','termination_request_date': 'terminationRequestDate','version': 'version',
    }

    
    _created_by = None
    _created_on = None
    _external_id = None
    _id = None
    _initial_execution_date = None
    _initial_payment_transaction = None
    _initial_shopify_transaction = None
    _language = None
    _linked_space_id = None
    _order_recurrence_number = None
    _shop = None
    _state = None
    _subscriber = None
    _terminated_by = None
    _terminated_on = None
    _termination_request_date = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_by = kwargs.get('created_by', None)
        self.created_on = kwargs.get('created_on', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.initial_execution_date = kwargs.get('initial_execution_date', None)
        self.initial_payment_transaction = kwargs.get('initial_payment_transaction', None)
        self.initial_shopify_transaction = kwargs.get('initial_shopify_transaction', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.order_recurrence_number = kwargs.get('order_recurrence_number', None)
        self.shop = kwargs.get('shop', None)
        self.state = kwargs.get('state', None)
        self.subscriber = kwargs.get('subscriber', None)
        self.terminated_by = kwargs.get('terminated_by', None)
        self.terminated_on = kwargs.get('terminated_on', None)
        self.termination_request_date = kwargs.get('termination_request_date', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_by(self):
        """Gets the created_by of this ShopifySubscription.

            

        :return: The created_by of this ShopifySubscription.
        :rtype: int
        """
        return self._created_by

    @created_by.setter
    def created_by(self, created_by):
        """Sets the created_by of this ShopifySubscription.

            

        :param created_by: The created_by of this ShopifySubscription.
        :type: int
        """

        self._created_by = created_by
    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifySubscription.

            

        :return: The created_on of this ShopifySubscription.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifySubscription.

            

        :param created_on: The created_on of this ShopifySubscription.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def external_id(self):
        """Gets the external_id of this ShopifySubscription.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this ShopifySubscription.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ShopifySubscription.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this ShopifySubscription.
        :type: str
        """
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscription.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscription.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscription.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscription.
        :type: int
        """

        self._id = id
    
    @property
    def initial_execution_date(self):
        """Gets the initial_execution_date of this ShopifySubscription.

            

        :return: The initial_execution_date of this ShopifySubscription.
        :rtype: datetime
        """
        return self._initial_execution_date

    @initial_execution_date.setter
    def initial_execution_date(self, initial_execution_date):
        """Sets the initial_execution_date of this ShopifySubscription.

            

        :param initial_execution_date: The initial_execution_date of this ShopifySubscription.
        :type: datetime
        """

        self._initial_execution_date = initial_execution_date
    
    @property
    def initial_payment_transaction(self):
        """Gets the initial_payment_transaction of this ShopifySubscription.

            

        :return: The initial_payment_transaction of this ShopifySubscription.
        :rtype: int
        """
        return self._initial_payment_transaction

    @initial_payment_transaction.setter
    def initial_payment_transaction(self, initial_payment_transaction):
        """Sets the initial_payment_transaction of this ShopifySubscription.

            

        :param initial_payment_transaction: The initial_payment_transaction of this ShopifySubscription.
        :type: int
        """

        self._initial_payment_transaction = initial_payment_transaction
    
    @property
    def initial_shopify_transaction(self):
        """Gets the initial_shopify_transaction of this ShopifySubscription.

            

        :return: The initial_shopify_transaction of this ShopifySubscription.
        :rtype: int
        """
        return self._initial_shopify_transaction

    @initial_shopify_transaction.setter
    def initial_shopify_transaction(self, initial_shopify_transaction):
        """Sets the initial_shopify_transaction of this ShopifySubscription.

            

        :param initial_shopify_transaction: The initial_shopify_transaction of this ShopifySubscription.
        :type: int
        """

        self._initial_shopify_transaction = initial_shopify_transaction
    
    @property
    def language(self):
        """Gets the language of this ShopifySubscription.

            

        :return: The language of this ShopifySubscription.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this ShopifySubscription.

            

        :param language: The language of this ShopifySubscription.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifySubscription.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ShopifySubscription.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifySubscription.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ShopifySubscription.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def order_recurrence_number(self):
        """Gets the order_recurrence_number of this ShopifySubscription.

            

        :return: The order_recurrence_number of this ShopifySubscription.
        :rtype: int
        """
        return self._order_recurrence_number

    @order_recurrence_number.setter
    def order_recurrence_number(self, order_recurrence_number):
        """Sets the order_recurrence_number of this ShopifySubscription.

            

        :param order_recurrence_number: The order_recurrence_number of this ShopifySubscription.
        :type: int
        """

        self._order_recurrence_number = order_recurrence_number
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscription.

            

        :return: The shop of this ShopifySubscription.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscription.

            

        :param shop: The shop of this ShopifySubscription.
        :type: int
        """

        self._shop = shop
    
    @property
    def state(self):
        """Gets the state of this ShopifySubscription.

            

        :return: The state of this ShopifySubscription.
        :rtype: ShopifySubscriptionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifySubscription.

            

        :param state: The state of this ShopifySubscription.
        :type: ShopifySubscriptionState
        """

        self._state = state
    
    @property
    def subscriber(self):
        """Gets the subscriber of this ShopifySubscription.

            

        :return: The subscriber of this ShopifySubscription.
        :rtype: ShopifySubscriber
        """
        return self._subscriber

    @subscriber.setter
    def subscriber(self, subscriber):
        """Sets the subscriber of this ShopifySubscription.

            

        :param subscriber: The subscriber of this ShopifySubscription.
        :type: ShopifySubscriber
        """

        self._subscriber = subscriber
    
    @property
    def terminated_by(self):
        """Gets the terminated_by of this ShopifySubscription.

            

        :return: The terminated_by of this ShopifySubscription.
        :rtype: int
        """
        return self._terminated_by

    @terminated_by.setter
    def terminated_by(self, terminated_by):
        """Sets the terminated_by of this ShopifySubscription.

            

        :param terminated_by: The terminated_by of this ShopifySubscription.
        :type: int
        """

        self._terminated_by = terminated_by
    
    @property
    def terminated_on(self):
        """Gets the terminated_on of this ShopifySubscription.

            

        :return: The terminated_on of this ShopifySubscription.
        :rtype: datetime
        """
        return self._terminated_on

    @terminated_on.setter
    def terminated_on(self, terminated_on):
        """Sets the terminated_on of this ShopifySubscription.

            

        :param terminated_on: The terminated_on of this ShopifySubscription.
        :type: datetime
        """

        self._terminated_on = terminated_on
    
    @property
    def termination_request_date(self):
        """Gets the termination_request_date of this ShopifySubscription.

            

        :return: The termination_request_date of this ShopifySubscription.
        :rtype: datetime
        """
        return self._termination_request_date

    @termination_request_date.setter
    def termination_request_date(self, termination_request_date):
        """Sets the termination_request_date of this ShopifySubscription.

            

        :param termination_request_date: The termination_request_date of this ShopifySubscription.
        :type: datetime
        """

        self._termination_request_date = termination_request_date
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscription.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscription.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscription.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscription.
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
        if issubclass(ShopifySubscription, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscription):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
