# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ShopifyTransaction(TransactionAwareEntity):

    swagger_types = {
    
        'checkout_id': 'str',
        'created_on': 'datetime',
        'integration': 'ShopifyIntegration',
        'order_id': 'str',
        'order_name': 'str',
        'planned_purge_date': 'datetime',
        'state': 'ShopifyTransactionState',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'checkout_id': 'checkoutId','created_on': 'createdOn','integration': 'integration','order_id': 'orderId','order_name': 'orderName','planned_purge_date': 'plannedPurgeDate','state': 'state','transaction': 'transaction','version': 'version',
    }

    
    _checkout_id = None
    _created_on = None
    _integration = None
    _order_id = None
    _order_name = None
    _planned_purge_date = None
    _state = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.checkout_id = kwargs.get('checkout_id', None)
        self.created_on = kwargs.get('created_on', None)
        self.integration = kwargs.get('integration', None)
        self.order_id = kwargs.get('order_id', None)
        self.order_name = kwargs.get('order_name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
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

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this ShopifyTransaction.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifyTransaction.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this ShopifyTransaction.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def integration(self):
        """Gets the integration of this ShopifyTransaction.

            

        :return: The integration of this ShopifyTransaction.
        :rtype: ShopifyIntegration
        """
        return self._integration

    @integration.setter
    def integration(self, integration):
        """Sets the integration of this ShopifyTransaction.

            

        :param integration: The integration of this ShopifyTransaction.
        :type: ShopifyIntegration
        """

        self._integration = integration
    
    @property
    def order_id(self):
        """Gets the order_id of this ShopifyTransaction.

            

        :return: The order_id of this ShopifyTransaction.
        :rtype: str
        """
        return self._order_id

    @order_id.setter
    def order_id(self, order_id):
        """Sets the order_id of this ShopifyTransaction.

            

        :param order_id: The order_id of this ShopifyTransaction.
        :type: str
        """

        self._order_id = order_id
    
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

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ShopifyTransaction.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifyTransaction.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

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

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifyTransaction.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifyTransaction.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

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
