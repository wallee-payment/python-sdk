# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionProductComponentGroupUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'name': 'DatabaseTranslatedStringCreate',
        'optional': 'bool',
        'product_version': 'int',
        'sort_order': 'int',
    }

    attribute_map = {
        'id': 'id','version': 'version','name': 'name','optional': 'optional','product_version': 'productVersion','sort_order': 'sortOrder',
    }

    
    _id = None
    _version = None
    _name = None
    _optional = None
    _product_version = None
    _sort_order = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.name = kwargs.get('name', None)
        self.optional = kwargs.get('optional', None)
        self.product_version = kwargs.get('product_version', None)
        self.sort_order = kwargs.get('sort_order', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriptionProductComponentGroupUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriptionProductComponentGroupUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionProductComponentGroupUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriptionProductComponentGroupUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this SubscriptionProductComponentGroupUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriptionProductComponentGroupUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionProductComponentGroupUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriptionProductComponentGroupUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def name(self):
        """Gets the name of this SubscriptionProductComponentGroupUpdate.

            The component group name will be shown when the components are selected. This can be visible to the subscriber.

        :return: The name of this SubscriptionProductComponentGroupUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionProductComponentGroupUpdate.

            The component group name will be shown when the components are selected. This can be visible to the subscriber.

        :param name: The name of this SubscriptionProductComponentGroupUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._name = name
    
    @property
    def optional(self):
        """Gets the optional of this SubscriptionProductComponentGroupUpdate.

            The component group can be optional. This means no component has to be selected by the subscriber.

        :return: The optional of this SubscriptionProductComponentGroupUpdate.
        :rtype: bool
        """
        return self._optional

    @optional.setter
    def optional(self, optional):
        """Sets the optional of this SubscriptionProductComponentGroupUpdate.

            The component group can be optional. This means no component has to be selected by the subscriber.

        :param optional: The optional of this SubscriptionProductComponentGroupUpdate.
        :type: bool
        """

        self._optional = optional
    
    @property
    def product_version(self):
        """Gets the product_version of this SubscriptionProductComponentGroupUpdate.

            

        :return: The product_version of this SubscriptionProductComponentGroupUpdate.
        :rtype: int
        """
        return self._product_version

    @product_version.setter
    def product_version(self, product_version):
        """Sets the product_version of this SubscriptionProductComponentGroupUpdate.

            

        :param product_version: The product_version of this SubscriptionProductComponentGroupUpdate.
        :type: int
        """

        self._product_version = product_version
    
    @property
    def sort_order(self):
        """Gets the sort_order of this SubscriptionProductComponentGroupUpdate.

            The sort order controls in which order the component group is listed. The sort order is used to order the component groups in ascending order.

        :return: The sort_order of this SubscriptionProductComponentGroupUpdate.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this SubscriptionProductComponentGroupUpdate.

            The sort order controls in which order the component group is listed. The sort order is used to order the component groups in ascending order.

        :param sort_order: The sort_order of this SubscriptionProductComponentGroupUpdate.
        :type: int
        """

        self._sort_order = sort_order
    

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
        if issubclass(SubscriptionProductComponentGroupUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductComponentGroupUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
