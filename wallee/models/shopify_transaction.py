# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifyTransaction:

    swagger_types = {
    
        'checkout_id': 'str',
        'created_on': 'datetime',
        'draft_order_id': 'str',
        'draft_order_legacy_id': 'str',
        'id': 'int',
        'integration': 'ShopifyV1Integration',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
        'order_legacy_id': 'str',
        'order_name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'ShopifyTransactionState',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'checkout_id': 'checkoutId','created_on': 'createdOn','draft_order_id': 'draftOrderId','draft_order_legacy_id': 'draftOrderLegacyId','id': 'id','integration': 'integration','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction','order_legacy_id': 'orderLegacyId','order_name': 'orderName','planned_purge_date': 'plannedPurgeDate','state': 'state','transaction': 'transaction','version': 'version',
    }

    
    _checkout_id = None
    _created_on = None
    _draft_order_id = None
    _draft_order_legacy_id = None
    _id = None
    _integration = None
    _linked_space_id = None
    _linked_transaction = None
    _order_legacy_id = None
    _order_name = None
    _planned_purge_date = None
    _state = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.checkout_id = kwargs.get('checkout_id', None)
        self.created_on = kwargs.get('created_on', None)
        self.draft_order_id = kwargs.get('draft_order_id', None)
        self.draft_order_legacy_id = kwargs.get('draft_order_legacy_id', None)
        self.id = kwargs.get('id', None)
        self.integration = kwargs.get('integration', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        self.order_legacy_id = kwargs.get('order_legacy_id', None)
        self.order_name = kwargs.get('order_name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def checkout_id(self):
        """Gets the checkout_id of this ShopifyTransaction.

            

        :return: The checkout_id of this ShopifyTransaction.
        :rtype: str
        """
        return self._checkout_id

    @checkout_id.setter
    def checkout_id(self, checkout_id):
        """Sets the checkout_id of this ShopifyTransaction.

            

        :param checkout_id: The checkout_id of this ShopifyTransaction.
        :type: str
        """

        self._checkout_id = checkout_id
    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifyTransaction.

            The date and time when the object was created.

        :return: The created_on of this ShopifyTransaction.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifyTransaction.

            The date and time when the object was created.

        :param created_on: The created_on of this ShopifyTransaction.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def draft_order_id(self):
        """Gets the draft_order_id of this ShopifyTransaction.

            

        :return: The draft_order_id of this ShopifyTransaction.
        :rtype: str
        """
        return self._draft_order_id

    @draft_order_id.setter
    def draft_order_id(self, draft_order_id):
        """Sets the draft_order_id of this ShopifyTransaction.

            

        :param draft_order_id: The draft_order_id of this ShopifyTransaction.
        :type: str
        """

        self._draft_order_id = draft_order_id
    
    @property
    def draft_order_legacy_id(self):
        """Gets the draft_order_legacy_id of this ShopifyTransaction.

            

        :return: The draft_order_legacy_id of this ShopifyTransaction.
        :rtype: str
        """
        return self._draft_order_legacy_id

    @draft_order_legacy_id.setter
    def draft_order_legacy_id(self, draft_order_legacy_id):
        """Sets the draft_order_legacy_id of this ShopifyTransaction.

            

        :param draft_order_legacy_id: The draft_order_legacy_id of this ShopifyTransaction.
        :type: str
        """

        self._draft_order_legacy_id = draft_order_legacy_id
    
    @property
    def id(self):
        """Gets the id of this ShopifyTransaction.

            A unique identifier for the object.

        :return: The id of this ShopifyTransaction.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifyTransaction.

            A unique identifier for the object.

        :param id: The id of this ShopifyTransaction.
        :type: int
        """

        self._id = id
    
    @property
    def integration(self):
        """Gets the integration of this ShopifyTransaction.

            

        :return: The integration of this ShopifyTransaction.
        :rtype: ShopifyV1Integration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ShopifyTransaction.

            

        :param integration: The integration of this ShopifyTransaction.
        :type: ShopifyV1Integration
        """

        self._integration = integration
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifyTransaction.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this ShopifyTransaction.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifyTransaction.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this ShopifyTransaction.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this ShopifyTransaction.

            The payment transaction this object is linked to.

        :return: The linked_transaction of this ShopifyTransaction.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this ShopifyTransaction.

            The payment transaction this object is linked to.

        :param linked_transaction: The linked_transaction of this ShopifyTransaction.
        :type: int
        """

        self._linked_transaction = linked_transaction
    
    @property
    def order_legacy_id(self):
        """Gets the order_legacy_id of this ShopifyTransaction.

            

        :return: The order_legacy_id of this ShopifyTransaction.
        :rtype: str
        """
        return self._order_legacy_id

    @order_legacy_id.setter
    def order_legacy_id(self, order_legacy_id):
        """Sets the order_legacy_id of this ShopifyTransaction.

            

        :param order_legacy_id: The order_legacy_id of this ShopifyTransaction.
        :type: str
        """

        self._order_legacy_id = order_legacy_id
    
    @property
    def order_name(self):
        """Gets the order_name of this ShopifyTransaction.

            

        :return: The order_name of this ShopifyTransaction.
        :rtype: str
        """
        return self._order_name

    @order_name.setter
    def order_name(self, order_name):
        """Sets the order_name of this ShopifyTransaction.

            

        :param order_name: The order_name of this ShopifyTransaction.
        :type: str
        """

        self._order_name = order_name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ShopifyTransaction.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this ShopifyTransaction.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifyTransaction.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this ShopifyTransaction.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this ShopifyTransaction.

            

        :return: The state of this ShopifyTransaction.
        :rtype: ShopifyTransactionState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifyTransaction.

            

        :param state: The state of this ShopifyTransaction.
        :type: ShopifyTransactionState
        """

        self._state = state
    
    @property
    def transaction(self):
        """Gets the transaction of this ShopifyTransaction.

            

        :return: The transaction of this ShopifyTransaction.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ShopifyTransaction.

            

        :param transaction: The transaction of this ShopifyTransaction.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this ShopifyTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this ShopifyTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifyTransaction.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this ShopifyTransaction.
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
        if issubclass(ShopifyTransaction, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifyTransaction):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
