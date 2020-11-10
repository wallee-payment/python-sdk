# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionCompletionRequest:

    swagger_types = {
    
        'external_id': 'str',
        'invoice_merchant_reference': 'str',
        'last_completion': 'bool',
        'line_items': 'list[CompletionLineItemCreate]',
        'transaction_id': 'int',
    }

    attribute_map = {
        'external_id': 'externalId','invoice_merchant_reference': 'invoiceMerchantReference','last_completion': 'lastCompletion','line_items': 'lineItems','transaction_id': 'transactionId',
    }

    
    _external_id = None
    _invoice_merchant_reference = None
    _last_completion = None
    _line_items = None
    _transaction_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.external_id = kwargs.get('external_id')

        self.invoice_merchant_reference = kwargs.get('invoice_merchant_reference', None)
        self.last_completion = kwargs.get('last_completion')

        self.line_items = kwargs.get('line_items', None)
        self.transaction_id = kwargs.get('transaction_id')

        

    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionCompletionRequest.

            The external ID helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this TransactionCompletionRequest.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionCompletionRequest.

            The external ID helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this TransactionCompletionRequest.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")
        if external_id is not None and len(external_id) > 100:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `100`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def invoice_merchant_reference(self):
        """Gets the invoice_merchant_reference of this TransactionCompletionRequest.

            

        :return: The invoice_merchant_reference of this TransactionCompletionRequest.
        :rtype: str
        """
        return self._invoice_merchant_reference

    @invoice_merchant_reference.setter
    def invoice_merchant_reference(self, invoice_merchant_reference):
        """Sets the invoice_merchant_reference of this TransactionCompletionRequest.

            

        :param invoice_merchant_reference: The invoice_merchant_reference of this TransactionCompletionRequest.
        :type: str
        """
        if invoice_merchant_reference is not None and len(invoice_merchant_reference) > 100:
            raise ValueError("Invalid value for `invoice_merchant_reference`, length must be less than or equal to `100`")

        self._invoice_merchant_reference = invoice_merchant_reference
    
    @property
    def last_completion(self):
        """Gets the last_completion of this TransactionCompletionRequest.

            The last completion flag indicates if this is the last completion. After the last completion is created no further completions can be issued.

        :return: The last_completion of this TransactionCompletionRequest.
        :rtype: bool
        """
        return self._last_completion

    @last_completion.setter
    def last_completion(self, last_completion):
        """Sets the last_completion of this TransactionCompletionRequest.

            The last completion flag indicates if this is the last completion. After the last completion is created no further completions can be issued.

        :param last_completion: The last_completion of this TransactionCompletionRequest.
        :type: bool
        """
        if last_completion is None:
            raise ValueError("Invalid value for `last_completion`, must not be `None`")

        self._last_completion = last_completion
    
    @property
    def line_items(self):
        """Gets the line_items of this TransactionCompletionRequest.

            The line items which will be used to complete the transaction.

        :return: The line_items of this TransactionCompletionRequest.
        :rtype: list[CompletionLineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionCompletionRequest.

            The line items which will be used to complete the transaction.

        :param line_items: The line_items of this TransactionCompletionRequest.
        :type: list[CompletionLineItemCreate]
        """

        self._line_items = line_items
    
    @property
    def transaction_id(self):
        """Gets the transaction_id of this TransactionCompletionRequest.

            The ID of the transaction which should be completed.

        :return: The transaction_id of this TransactionCompletionRequest.
        :rtype: int
        """
        return self._transaction_id

    @transaction_id.setter
    def transaction_id(self, transaction_id):
        """Sets the transaction_id of this TransactionCompletionRequest.

            The ID of the transaction which should be completed.

        :param transaction_id: The transaction_id of this TransactionCompletionRequest.
        :type: int
        """
        if transaction_id is None:
            raise ValueError("Invalid value for `transaction_id`, must not be `None`")

        self._transaction_id = transaction_id
    

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
        if issubclass(TransactionCompletionRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionCompletionRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
