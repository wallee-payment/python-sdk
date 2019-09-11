# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionAwareEntity:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'linked_transaction': 'int',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','linked_transaction': 'linkedTransaction',
    }

    
    _id = None
    _linked_space_id = None
    _linked_transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.linked_transaction = kwargs.get('linked_transaction', None)
        

    
    @property
    def id(self):
        """Gets the id of this TransactionAwareEntity.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this TransactionAwareEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this TransactionAwareEntity.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this TransactionAwareEntity.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this TransactionAwareEntity.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this TransactionAwareEntity.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this TransactionAwareEntity.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this TransactionAwareEntity.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def linked_transaction(self):
        """Gets the linked_transaction of this TransactionAwareEntity.

            

        :return: The linked_transaction of this TransactionAwareEntity.
        :rtype: int
        """
        return self._linked_transaction

    @linked_transaction.setter
    def linked_transaction(self, linked_transaction):
        """Sets the linked_transaction of this TransactionAwareEntity.

            

        :param linked_transaction: The linked_transaction of this TransactionAwareEntity.
        :type: int
        """

        self._linked_transaction = linked_transaction
    

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
        if issubclass(TransactionAwareEntity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionAwareEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
