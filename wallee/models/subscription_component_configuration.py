# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriptionComponentConfiguration:

    swagger_types = {
    
        'component': 'int',
        'id': 'int',
        'linked_space_id': 'int',
        'quantity': 'float',
        'version': 'int',
    }

    attribute_map = {
        'component': 'component','id': 'id','linked_space_id': 'linkedSpaceId','quantity': 'quantity','version': 'version',
    }

    
    _component = None
    _id = None
    _linked_space_id = None
    _quantity = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component = kwargs.get('component', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.quantity = kwargs.get('quantity', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def component(self):
        """Gets the component of this SubscriptionComponentConfiguration.

            

        :return: The component of this SubscriptionComponentConfiguration.
        :rtype: int
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this SubscriptionComponentConfiguration.

            

        :param component: The component of this SubscriptionComponentConfiguration.
        :type: int
        """

        self._component = component
    
    @property
    def id(self):
        """Gets the id of this SubscriptionComponentConfiguration.

            A unique identifier for the object.

        :return: The id of this SubscriptionComponentConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriptionComponentConfiguration.

            A unique identifier for the object.

        :param id: The id of this SubscriptionComponentConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this SubscriptionComponentConfiguration.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this SubscriptionComponentConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this SubscriptionComponentConfiguration.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this SubscriptionComponentConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def quantity(self):
        """Gets the quantity of this SubscriptionComponentConfiguration.

            

        :return: The quantity of this SubscriptionComponentConfiguration.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this SubscriptionComponentConfiguration.

            

        :param quantity: The quantity of this SubscriptionComponentConfiguration.
        :type: float
        """

        self._quantity = quantity
    
    @property
    def version(self):
        """Gets the version of this SubscriptionComponentConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this SubscriptionComponentConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriptionComponentConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this SubscriptionComponentConfiguration.
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
        if issubclass(SubscriptionComponentConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionComponentConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
