# coding: utf-8
import pprint
import six
from enum import Enum



class TransactionInvoiceReplacement:

    swagger_types = {
    
        'billing_address': 'AddressCreate',
        'due_on': 'datetime',
        'external_id': 'str',
        'line_items': 'list[LineItemCreate]',
        'merchant_reference': 'str',
        'sent_to_customer': 'bool',
    }

    attribute_map = {
        'billing_address': 'billingAddress','due_on': 'dueOn','external_id': 'externalId','line_items': 'lineItems','merchant_reference': 'merchantReference','sent_to_customer': 'sentToCustomer',
    }

    
    _billing_address = None
    _due_on = None
    _external_id = None
    _line_items = None
    _merchant_reference = None
    _sent_to_customer = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.billing_address = kwargs.get('billing_address', None)
        self.due_on = kwargs.get('due_on', None)
        self.external_id = kwargs.get('external_id')

        self.line_items = kwargs.get('line_items')

        self.merchant_reference = kwargs.get('merchant_reference', None)
        self.sent_to_customer = kwargs.get('sent_to_customer', None)
        

    
    @property
    def billing_address(self):
        """Gets the billing_address of this TransactionInvoiceReplacement.

            

        :return: The billing_address of this TransactionInvoiceReplacement.
        :rtype: AddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this TransactionInvoiceReplacement.

            

        :param billing_address: The billing_address of this TransactionInvoiceReplacement.
        :type: AddressCreate
        """

        self._billing_address = billing_address
    
    @property
    def due_on(self):
        """Gets the due_on of this TransactionInvoiceReplacement.

            The date on which the invoice should be paid on.

        :return: The due_on of this TransactionInvoiceReplacement.
        :rtype: datetime
        """
        return self._due_on

    @due_on.setter
    def due_on(self, due_on):
        """Sets the due_on of this TransactionInvoiceReplacement.

            The date on which the invoice should be paid on.

        :param due_on: The due_on of this TransactionInvoiceReplacement.
        :type: datetime
        """

        self._due_on = due_on
    
    @property
    def external_id(self):
        """Gets the external_id of this TransactionInvoiceReplacement.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :return: The external_id of this TransactionInvoiceReplacement.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this TransactionInvoiceReplacement.

            The external id helps to identify the entity and a subsequent creation of an entity with the same ID will not create a new entity.

        :param external_id: The external_id of this TransactionInvoiceReplacement.
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
    def line_items(self):
        """Gets the line_items of this TransactionInvoiceReplacement.

            

        :return: The line_items of this TransactionInvoiceReplacement.
        :rtype: list[LineItemCreate]
        """
        return self._line_items

    @line_items.setter
    def line_items(self, line_items):
        """Sets the line_items of this TransactionInvoiceReplacement.

            

        :param line_items: The line_items of this TransactionInvoiceReplacement.
        :type: list[LineItemCreate]
        """
        if line_items is None:
            raise ValueError("Invalid value for `line_items`, must not be `None`")

        self._line_items = line_items
    
    @property
    def merchant_reference(self):
        """Gets the merchant_reference of this TransactionInvoiceReplacement.

            

        :return: The merchant_reference of this TransactionInvoiceReplacement.
        :rtype: str
        """
        return self._merchant_reference

    @merchant_reference.setter
    def merchant_reference(self, merchant_reference):
        """Sets the merchant_reference of this TransactionInvoiceReplacement.

            

        :param merchant_reference: The merchant_reference of this TransactionInvoiceReplacement.
        :type: str
        """
        if merchant_reference is not None and len(merchant_reference) > 100:
            raise ValueError("Invalid value for `merchant_reference`, length must be less than or equal to `100`")

        self._merchant_reference = merchant_reference
    
    @property
    def sent_to_customer(self):
        """Gets the sent_to_customer of this TransactionInvoiceReplacement.

            When the connector is configured to send the invoice to the customer and this property is true the customer will receive an email with the updated invoice. When this property is false no invoice is sent.

        :return: The sent_to_customer of this TransactionInvoiceReplacement.
        :rtype: bool
        """
        return self._sent_to_customer

    @sent_to_customer.setter
    def sent_to_customer(self, sent_to_customer):
        """Sets the sent_to_customer of this TransactionInvoiceReplacement.

            When the connector is configured to send the invoice to the customer and this property is true the customer will receive an email with the updated invoice. When this property is false no invoice is sent.

        :param sent_to_customer: The sent_to_customer of this TransactionInvoiceReplacement.
        :type: bool
        """

        self._sent_to_customer = sent_to_customer
    

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
        if issubclass(TransactionInvoiceReplacement, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionInvoiceReplacement):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
