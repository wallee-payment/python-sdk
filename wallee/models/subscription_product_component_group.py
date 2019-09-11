# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductComponentGroup:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'DatabaseTranslatedString',
        'optional': 'bool',
        'product_version': 'SubscriptionProductVersion',
        'sort_order': 'int',
        'version': 'int',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','optional': 'optional','product_version': 'productVersion','sort_order': 'sortOrder','version': 'version',
    }

    
    _id = None
    _linked_space_id = None
    _name = None
    _optional = None
    _product_version = None
    _sort_order = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.optional = kwargs.get('optional', None)
        self.product_version = kwargs.get('product_version', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductComponentGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductComponentGroup.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductComponentGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductComponentGroup.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionProductComponentGroup.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this SubscriptionProductComponentGroup.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionProductComponentGroup.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionProductComponentGroup.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductComponentGroup.

            The component group name will be shown when the components are selected. This can be visible to the subscriber.

        :return: The name of this SubscriptionProductComponentGroup.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductComponentGroup.

            The component group name will be shown when the components are selected. This can be visible to the subscriber.

        :param name: The name of this SubscriptionProductComponentGroup.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def optional(self):
        """Gets the optional of this SubscriptionProductComponentGroup.

            The component group can be optional. This means no component has to be selected by the subscriber.

        :return: The optional of this SubscriptionProductComponentGroup.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this SubscriptionProductComponentGroup.

            The component group can be optional. This means no component has to be selected by the subscriber.

        :param optional: The optional of this SubscriptionProductComponentGroup.
        :type: bool
        """

        self._optional = optional
    
    @property
    def product_version(self):
        """Gets the product_version of this SubscriptionProductComponentGroup.

            

        :return: The product_version of this SubscriptionProductComponentGroup.
        :rtype: SubscriptionProductVersion
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this SubscriptionProductComponentGroup.

            

        :param product_version: The product_version of this SubscriptionProductComponentGroup.
        :type: SubscriptionProductVersion
        """

        self._product_version = product_version
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SubscriptionProductComponentGroup.

            The sort order controls in which order the component group is listed. The sort order is used to order the component groups in ascending order.

        :return: The sort_order of this SubscriptionProductComponentGroup.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SubscriptionProductComponentGroup.

            The sort order controls in which order the component group is listed. The sort order is used to order the component groups in ascending order.

        :param sort_order: The sort_order of this SubscriptionProductComponentGroup.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductComponentGroup.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductComponentGroup.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductComponentGroup.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductComponentGroup.
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
        if issubclass(SubscriptionProductComponentGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductComponentGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
