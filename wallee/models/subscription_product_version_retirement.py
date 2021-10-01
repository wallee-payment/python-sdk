# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductVersionRetirement:

    swagger_types = {
    
        'created_on': 'datetime',
        'id': 'int',
        'linked_space_id': 'int',
        'product_version': 'SubscriptionProductVersion',
        'respect_terminiation_periods_enabled': 'bool',
        'target_product': 'SubscriptionProduct',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','id': 'id','linked_space_id': 'linkedSpaceId','product_version': 'productVersion','respect_terminiation_periods_enabled': 'respectTerminiationPeriodsEnabled','target_product': 'targetProduct','version': 'version',
    }

    
    _created_on = None
    _id = None
    _linked_space_id = None
    _product_version = None
    _respect_terminiation_periods_enabled = None
    _target_product = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.product_version = kwargs.get('product_version', None)
        self.respect_terminiation_periods_enabled = kwargs.get('respect_terminiation_periods_enabled', None)
        self.target_product = kwargs.get('target_product', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this SubscriptionProductVersionRetirement.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this SubscriptionProductVersionRetirement.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this SubscriptionProductVersionRetirement.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this SubscriptionProductVersionRetirement.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductVersionRetirement.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductVersionRetirement.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductVersionRetirement.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductVersionRetirement.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionProductVersionRetirement.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionProductVersionRetirement.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionProductVersionRetirement.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionProductVersionRetirement.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def product_version(self):
        """Gets the product_version of this SubscriptionProductVersionRetirement.

            

        :return: The product_version of this SubscriptionProductVersionRetirement.
        :rtype: SubscriptionProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this SubscriptionProductVersionRetirement.

            

        :param product_version: The product_version of this SubscriptionProductVersionRetirement.
        :type: SubscriptionProductVersion
        """

        self._product_version = product_version
    
    @property
    def respect_terminiation_periods_enabled(self):
        """Gets the respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirement.

            

        :return: The respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirement.
        :rtype: bool
        """
        return self._respect_terminiation_periods_enabled

    @respect_terminiation_periods_enabled.setter
    def respect_terminiation_periods_enabled(self, respect_terminiation_periods_enabled):
        """Sets the respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirement.

            

        :param respect_terminiation_periods_enabled: The respect_terminiation_periods_enabled of this SubscriptionProductVersionRetirement.
        :type: bool
        """

        self._respect_terminiation_periods_enabled = respect_terminiation_periods_enabled
    
    @property
    def target_product(self):
        """Gets the target_product of this SubscriptionProductVersionRetirement.

            When a target product is not chosen, all customers with the retired product will be terminated.

        :return: The target_product of this SubscriptionProductVersionRetirement.
        :rtype: SubscriptionProduct
        """
        return self._target_product

    @target_product.setter
    def target_product(self, target_product):
        """Sets the target_product of this SubscriptionProductVersionRetirement.

            When a target product is not chosen, all customers with the retired product will be terminated.

        :param target_product: The target_product of this SubscriptionProductVersionRetirement.
        :type: SubscriptionProduct
        """

        self._target_product = target_product
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductVersionRetirement.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductVersionRetirement.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductVersionRetirement.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductVersionRetirement.
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
        if issubclass(SubscriptionProductVersionRetirement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductVersionRetirement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
