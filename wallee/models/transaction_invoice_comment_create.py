# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractTransactionInvoiceCommentActive


class TransactionInvoiceCommentCreate(AbstractTransactionInvoiceCommentActive):

    swagger_types = {
    
        'transaction_invoice': 'int',
    }

    attribute_map = {
        'transaction_invoice': 'transactionInvoice',
    }

    
    _transaction_invoice = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.transaction_invoice = kwargs.get('transaction_invoice')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def transaction_invoice(self):
        """Gets the transaction_invoice of this TransactionInvoiceCommentCreate.

            

        :return: The transaction_invoice of this TransactionInvoiceCommentCreate.
        :rtype: int
        """
        return self._transaction_invoice

    @transaction_invoice.setter
    def transaction_invoice(self, transaction_invoice):
        """Sets the transaction_invoice of this TransactionInvoiceCommentCreate.

            

        :param transaction_invoice: The transaction_invoice of this TransactionInvoiceCommentCreate.
        :type: int
        """
        if transaction_invoice is None:
            raise ValueError("Invalid value for `transaction_invoice`, must not be `None`")

        self._transaction_invoice = transaction_invoice
    

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
        if issubclass(TransactionInvoiceCommentCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionInvoiceCommentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
