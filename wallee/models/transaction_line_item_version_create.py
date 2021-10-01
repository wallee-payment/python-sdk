# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionLineItemVersionCreate:

    swagger_types = {
    
        'external_id': 'str',
        'line_items': 'list[LineItemCreate]',
        'transaction': 'int',
    }

    attribute_map = {
        'external_id': 'externalId','line_items': 'lineItems','transaction': 'transaction',
    }

    
    _external_id = None
    _line_items = None
    _transaction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.external_id = kwargs.get('external_id')

        self.line_items = kwargs.get('line_items')

        self.transaction = kwargs.get('transaction')

        

    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionLineItemVersionCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this TransactionLineItemVersionCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionLineItemVersionCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this TransactionLineItemVersionCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionLineItemVersionCreate.

            

        :return: The line_items of this TransactionLineItemVersionCreate.
        :rtype: list[LineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionLineItemVersionCreate.

            

        :param line_items: The line_items of this TransactionLineItemVersionCreate.
        :type: list[LineItemCreate]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")

        self._line_items = line_items
    
    @property
    def transaction(self):
        """Gets the transaction of this TransactionLineItemVersionCreate.

            

        :return: The transaction of this TransactionLineItemVersionCreate.
        :rtype: int
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this TransactionLineItemVersionCreate.

            

        :param transaction: The transaction of this TransactionLineItemVersionCreate.
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
        if issubclass(TransactionLineItemVersionCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionLineItemVersionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
