# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProduct:

    swagger_types = {
    
        'allowed_payment_method_configurations': 'list[int]',
        'failed_payment_suspension_period': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'product_locked': 'bool',
        'reference': 'str',
        'sort_order': 'int',
        'space_id': 'int',
        'state': 'SubscriptionProductState',
        'version': 'int',
    }

    attribute_map = {
        'allowed_payment_method_configurations': 'allowedPaymentMethodConfigurations','failed_payment_suspension_period': 'failedPaymentSuspensionPeriod','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','product_locked': 'productLocked','reference': 'reference','sort_order': 'sortOrder','space_id': 'spaceId','state': 'state','version': 'version',
    }

    
    _allowed_payment_method_configurations = None
    _failed_payment_suspension_period = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _product_locked = None
    _reference = None
    _sort_order = None
    _space_id = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.allowed_payment_method_configurations = kwargs.get('allowed_payment_method_configurations', None)
        self.failed_payment_suspension_period = kwargs.get('failed_payment_suspension_period', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.product_locked = kwargs.get('product_locked', None)
        self.reference = kwargs.get('reference', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.space_id = kwargs.get('space_id', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def allowed_payment_method_configurations(self):
        """Gets the allowed_payment_method_configurations of this SubscriptionProduct.

            The allowed payment method configurations control which payment methods can be used with this product. When none is selected all methods will be allowed.

        :return: The allowed_payment_method_configurations of this SubscriptionProduct.
        :rtype: list[int]
        """
        return self._allowed_payment_method_configurations

    @allowed_payment_method_configurations.setter
    def allowed_payment_method_configurations(self, allowed_payment_method_configurations):
        """Sets the allowed_payment_method_configurations of this SubscriptionProduct.

            The allowed payment method configurations control which payment methods can be used with this product. When none is selected all methods will be allowed.

        :param allowed_payment_method_configurations: The allowed_payment_method_configurations of this SubscriptionProduct.
        :type: list[int]
        """

        self._allowed_payment_method_configurations = allowed_payment_method_configurations
    
    @property
    def failed_payment_suspension_period(self):
        """Gets the failed_payment_suspension_period of this SubscriptionProduct.

            When a payment fails, the subscription to which the payment belongs to will be suspended. When the suspension is not removed within the specified period the subscription will be terminated. A payment is considered as failed when the subscriber issues a refund or when a subscription charge fails.

        :return: The failed_payment_suspension_period of this SubscriptionProduct.
        :rtype: str
        """
        return self._failed_payment_suspension_period

    @failed_payment_suspension_period.setter
    def failed_payment_suspension_period(self, failed_payment_suspension_period):
        """Sets the failed_payment_suspension_period of this SubscriptionProduct.

            When a payment fails, the subscription to which the payment belongs to will be suspended. When the suspension is not removed within the specified period the subscription will be terminated. A payment is considered as failed when the subscriber issues a refund or when a subscription charge fails.

        :param failed_payment_suspension_period: The failed_payment_suspension_period of this SubscriptionProduct.
        :type: str
        """

        self._failed_payment_suspension_period = failed_payment_suspension_period
    
    @property
    def id(self):
        """Gets the id of this SubscriptionProduct.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProduct.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProduct.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProduct.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionProduct.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionProduct.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionProduct.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionProduct.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProduct.

            The product name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this SubscriptionProduct.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProduct.

            The product name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this SubscriptionProduct.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this SubscriptionProduct.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this SubscriptionProduct.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this SubscriptionProduct.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this SubscriptionProduct.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def product_locked(self):
        """Gets the product_locked of this SubscriptionProduct.

            Marks the product as locked. Meaning that customer can not change away from this product or change to this product later on.

        :return: The product_locked of this SubscriptionProduct.
        :rtype: bool
        """
        return self._product_locked

    @product_locked.setter
    def product_locked(self, product_locked):
        """Sets the product_locked of this SubscriptionProduct.

            Marks the product as locked. Meaning that customer can not change away from this product or change to this product later on.

        :param product_locked: The product_locked of this SubscriptionProduct.
        :type: bool
        """

        self._product_locked = product_locked
    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionProduct.

            The product reference identifies the product for external systems. This field may contain the product's SKU.

        :return: The reference of this SubscriptionProduct.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionProduct.

            The product reference identifies the product for external systems. This field may contain the product's SKU.

        :param reference: The reference of this SubscriptionProduct.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SubscriptionProduct.

            The sort order controls in which order the product is listed. The sort order is used to order the products in ascending order.

        :return: The sort_order of this SubscriptionProduct.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SubscriptionProduct.

            The sort order controls in which order the product is listed. The sort order is used to order the products in ascending order.

        :param sort_order: The sort_order of this SubscriptionProduct.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def space_id(self):
        """Gets the space_id of this SubscriptionProduct.

            

        :return: The space_id of this SubscriptionProduct.
        :rtype: int
        """
        return self._space_id

    @space_id.setter
    def space_id(self, space_id):
        """Sets the space_id of this SubscriptionProduct.

            

        :param space_id: The space_id of this SubscriptionProduct.
        :type: int
        """

        self._space_id = space_id
    
    @property
    def state(self):
        """Gets the state of this SubscriptionProduct.

            

        :return: The state of this SubscriptionProduct.
        :rtype: SubscriptionProductState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this SubscriptionProduct.

            

        :param state: The state of this SubscriptionProduct.
        :type: SubscriptionProductState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProduct.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProduct.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProduct.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProduct.
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
        if issubclass(SubscriptionProduct, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProduct):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
