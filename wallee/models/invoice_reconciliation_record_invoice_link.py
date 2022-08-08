# coding: utf-8
import pprint
import six
from enum import Enum



class InvoiceReconciliationRecordInvoiceLink:

    swagger_types = {
    
        'amount': 'float',
        'created_on': 'datetime',
        'id': 'int',
        'invoice': 'TransactionInvoice',
        'linked_space_id': 'int',
        'record': 'InvoiceReconciliationRecord',
    }

    attribute_map = {
        'amount': 'amount','created_on': 'createdOn','id': 'id','invoice': 'invoice','linked_space_id': 'linkedSpaceId','record': 'record',
    }

    
    _amount = None
    _created_on = None
    _id = None
    _invoice = None
    _linked_space_id = None
    _record = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount = kwargs.get('amount', None)
        self.created_on = kwargs.get('created_on', None)
        self.id = kwargs.get('id', None)
        self.invoice = kwargs.get('invoice', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.record = kwargs.get('record', None)
        

    
    @property
    def amount(self):
        """Gets the amount of this InvoiceReconciliationRecordInvoiceLink.

            

        :return: The amount of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: float
        """
        return self._amount

    @amount.setter
    def amount(self, amount):
        """Sets the amount of this InvoiceReconciliationRecordInvoiceLink.

            

        :param amount: The amount of this InvoiceReconciliationRecordInvoiceLink.
        :type: float
        """

        self._amount = amount
    
    @property
    def created_on(self):
        """Gets the created_on of this InvoiceReconciliationRecordInvoiceLink.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this InvoiceReconciliationRecordInvoiceLink.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this InvoiceReconciliationRecordInvoiceLink.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def id(self):
        """Gets the id of this InvoiceReconciliationRecordInvoiceLink.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this InvoiceReconciliationRecordInvoiceLink.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this InvoiceReconciliationRecordInvoiceLink.
        :type: int
        """

        self._id = id
    
    @property
    def invoice(self):
        """Gets the invoice of this InvoiceReconciliationRecordInvoiceLink.

            

        :return: The invoice of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: TransactionInvoice
        """
        return self._invoice

    @invoice.setter
    def invoice(self, invoice):
        """Sets the invoice of this InvoiceReconciliationRecordInvoiceLink.

            

        :param invoice: The invoice of this InvoiceReconciliationRecordInvoiceLink.
        :type: TransactionInvoice
        """

        self._invoice = invoice
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this InvoiceReconciliationRecordInvoiceLink.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this InvoiceReconciliationRecordInvoiceLink.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this InvoiceReconciliationRecordInvoiceLink.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def record(self):
        """Gets the record of this InvoiceReconciliationRecordInvoiceLink.

            

        :return: The record of this InvoiceReconciliationRecordInvoiceLink.
        :rtype: InvoiceReconciliationRecord
        """
        return self._record

    @record.setter
    def record(self, record):
        """Sets the record of this InvoiceReconciliationRecordInvoiceLink.

            

        :param record: The record of this InvoiceReconciliationRecordInvoiceLink.
        :type: InvoiceReconciliationRecord
        """

        self._record = record
    

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
        if issubclass(InvoiceReconciliationRecordInvoiceLink, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceReconciliationRecordInvoiceLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
