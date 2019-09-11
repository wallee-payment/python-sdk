# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractTransactionCommentActive


class TransactionCommentCreate(AbstractTransactionCommentActive):

    swagger_types = {
    
        'transaction': 'int',
    }

    attribute_map = {
        'transaction': 'transaction',
    }

    
    _transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.transaction = kwargs.get('transaction')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def transaction(self):
        """Gets the transaction of this TransactionCommentCreate.

            

        :return: The transaction of this TransactionCommentCreate.
        :rtype: int
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionCommentCreate.

            

        :param transaction: The transaction of this TransactionCommentCreate.
        :type: int
        """
        if transaction is None:
            raise ValueError("Invalid value for `transaction`, must not be `None`")

        self._transaction = transaction
    

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
        if issubclass(TransactionCommentCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionCommentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
