# coding: utf-8
import pprint
import six
from enum import Enum



class LineItemCreate:

    swagger_types = {
    
        'amount_including_tax': 'float',
        'attributes': 'dict(str, LineItemAttributeCreate)',
        'discount_including_tax': 'float',
        'name': 'str',
        'quantity': 'float',
        'shipping_required': 'bool',
        'sku': 'str',
        'taxes': 'list[TaxCreate]',
        'type': 'LineItemType',
        'unique_id': 'str',
    }

    attribute_map = {
        'amount_including_tax': 'amountIncludingTax','attributes': 'attributes','discount_including_tax': 'discountIncludingTax','name': 'name','quantity': 'quantity','shipping_required': 'shippingRequired','sku': 'sku','taxes': 'taxes','type': 'type','unique_id': 'uniqueId',
    }

    
    _amount_including_tax = None
    _attributes = None
    _discount_including_tax = None
    _name = None
    _quantity = None
    _shipping_required = None
    _sku = None
    _taxes = None
    _type = None
    _unique_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.amount_including_tax = kwargs.get('amount_including_tax')

        self.attributes = kwargs.get('attributes', None)
        self.discount_including_tax = kwargs.get('discount_including_tax', None)
        self.name = kwargs.get('name')

        self.quantity = kwargs.get('quantity')

        self.shipping_required = kwargs.get('shipping_required', None)
        self.sku = kwargs.get('sku', None)
        self.taxes = kwargs.get('taxes', None)
        self.type = kwargs.get('type')

        self.unique_id = kwargs.get('unique_id')

        

    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this LineItemCreate.

            

        :return: The amount_including_tax of this LineItemCreate.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this LineItemCreate.

            

        :param amount_including_tax: The amount_including_tax of this LineItemCreate.
        :type: float
        """
        if amount_including_tax is None:
            raise ValueError("Invalid value for `amount_including_tax`, must not be `None`")

        self._amount_including_tax = amount_including_tax
    
    @property
    def attributes(self):
        """Gets the attributes of this LineItemCreate.

            

        :return: The attributes of this LineItemCreate.
        :rtype: dict(str, LineItemAttributeCreate)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LineItemCreate.

            

        :param attributes: The attributes of this LineItemCreate.
        :type: dict(str, LineItemAttributeCreate)
        """

        self._attributes = attributes
    
    @property
    def discount_including_tax(self):
        """Gets the discount_including_tax of this LineItemCreate.

            

        :return: The discount_including_tax of this LineItemCreate.
        :rtype: float
        """
        return self._discount_including_tax

    @discount_including_tax.setter
    def discount_including_tax(self, discount_including_tax):
        """Sets the discount_including_tax of this LineItemCreate.

            

        :param discount_including_tax: The discount_including_tax of this LineItemCreate.
        :type: float
        """

        self._discount_including_tax = discount_including_tax
    
    @property
    def name(self):
        """Gets the name of this LineItemCreate.

            

        :return: The name of this LineItemCreate.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LineItemCreate.

            

        :param name: The name of this LineItemCreate.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 150:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name
    
    @property
    def quantity(self):
        """Gets the quantity of this LineItemCreate.

            

        :return: The quantity of this LineItemCreate.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItemCreate.

            

        :param quantity: The quantity of this LineItemCreate.
        :type: float
        """
        if quantity is None:
            raise ValueError("Invalid value for `quantity`, must not be `None`")

        self._quantity = quantity
    
    @property
    def shipping_required(self):
        """Gets the shipping_required of this LineItemCreate.

            

        :return: The shipping_required of this LineItemCreate.
        :rtype: bool
        """
        return self._shipping_required

    @shipping_required.setter
    def shipping_required(self, shipping_required):
        """Sets the shipping_required of this LineItemCreate.

            

        :param shipping_required: The shipping_required of this LineItemCreate.
        :type: bool
        """

        self._shipping_required = shipping_required
    
    @property
    def sku(self):
        """Gets the sku of this LineItemCreate.

            

        :return: The sku of this LineItemCreate.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this LineItemCreate.

            

        :param sku: The sku of this LineItemCreate.
        :type: str
        """
        if sku is not None and len(sku) > 200:
            raise ValueError("Invalid value for `sku`, length must be less than or equal to `200`")

        self._sku = sku
    
    @property
    def taxes(self):
        """Gets the taxes of this LineItemCreate.

            

        :return: The taxes of this LineItemCreate.
        :rtype: list[TaxCreate]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this LineItemCreate.

            

        :param taxes: The taxes of this LineItemCreate.
        :type: list[TaxCreate]
        """

        self._taxes = taxes
    
    @property
    def type(self):
        """Gets the type of this LineItemCreate.

            

        :return: The type of this LineItemCreate.
        :rtype: LineItemType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LineItemCreate.

            

        :param type: The type of this LineItemCreate.
        :type: LineItemType
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type
    
    @property
    def unique_id(self):
        """Gets the unique_id of this LineItemCreate.

            The unique id identifies the line item within the set of line items associated with the transaction.

        :return: The unique_id of this LineItemCreate.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this LineItemCreate.

            The unique id identifies the line item within the set of line items associated with the transaction.

        :param unique_id: The unique_id of this LineItemCreate.
        :type: str
        """
        if unique_id is None:
            raise ValueError("Invalid value for `unique_id`, must not be `None`")
        if unique_id is not None and len(unique_id) > 200:
            raise ValueError("Invalid value for `unique_id`, length must be less than or equal to `200`")

        self._unique_id = unique_id
    

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
        if issubclass(LineItemCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LineItemCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
