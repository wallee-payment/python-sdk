# coding: utf-8
import pprint
import six
from enum import Enum



class LineItem:

    swagger_types = {
    
        'aggregated_tax_rate': 'float',
        'amount_excluding_tax': 'float',
        'amount_including_tax': 'float',
        'attributes': 'dict(str, LineItemAttribute)',
        'discount_excluding_tax': 'float',
        'discount_including_tax': 'float',
        'name': 'str',
        'quantity': 'float',
        'shipping_required': 'bool',
        'sku': 'str',
        'tax_amount': 'float',
        'tax_amount_per_unit': 'float',
        'taxes': 'list[Tax]',
        'type': 'LineItemType',
        'undiscounted_amount_excluding_tax': 'float',
        'undiscounted_amount_including_tax': 'float',
        'undiscounted_unit_price_excluding_tax': 'float',
        'undiscounted_unit_price_including_tax': 'float',
        'unique_id': 'str',
        'unit_price_excluding_tax': 'float',
        'unit_price_including_tax': 'float',
    }

    attribute_map = {
        'aggregated_tax_rate': 'aggregatedTaxRate','amount_excluding_tax': 'amountExcludingTax','amount_including_tax': 'amountIncludingTax','attributes': 'attributes','discount_excluding_tax': 'discountExcludingTax','discount_including_tax': 'discountIncludingTax','name': 'name','quantity': 'quantity','shipping_required': 'shippingRequired','sku': 'sku','tax_amount': 'taxAmount','tax_amount_per_unit': 'taxAmountPerUnit','taxes': 'taxes','type': 'type','undiscounted_amount_excluding_tax': 'undiscountedAmountExcludingTax','undiscounted_amount_including_tax': 'undiscountedAmountIncludingTax','undiscounted_unit_price_excluding_tax': 'undiscountedUnitPriceExcludingTax','undiscounted_unit_price_including_tax': 'undiscountedUnitPriceIncludingTax','unique_id': 'uniqueId','unit_price_excluding_tax': 'unitPriceExcludingTax','unit_price_including_tax': 'unitPriceIncludingTax',
    }

    
    _aggregated_tax_rate = None
    _amount_excluding_tax = None
    _amount_including_tax = None
    _attributes = None
    _discount_excluding_tax = None
    _discount_including_tax = None
    _name = None
    _quantity = None
    _shipping_required = None
    _sku = None
    _tax_amount = None
    _tax_amount_per_unit = None
    _taxes = None
    _type = None
    _undiscounted_amount_excluding_tax = None
    _undiscounted_amount_including_tax = None
    _undiscounted_unit_price_excluding_tax = None
    _undiscounted_unit_price_including_tax = None
    _unique_id = None
    _unit_price_excluding_tax = None
    _unit_price_including_tax = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.aggregated_tax_rate = kwargs.get('aggregated_tax_rate', None)
        self.amount_excluding_tax = kwargs.get('amount_excluding_tax', None)
        self.amount_including_tax = kwargs.get('amount_including_tax', None)
        self.attributes = kwargs.get('attributes', None)
        self.discount_excluding_tax = kwargs.get('discount_excluding_tax', None)
        self.discount_including_tax = kwargs.get('discount_including_tax', None)
        self.name = kwargs.get('name', None)
        self.quantity = kwargs.get('quantity', None)
        self.shipping_required = kwargs.get('shipping_required', None)
        self.sku = kwargs.get('sku', None)
        self.tax_amount = kwargs.get('tax_amount', None)
        self.tax_amount_per_unit = kwargs.get('tax_amount_per_unit', None)
        self.taxes = kwargs.get('taxes', None)
        self.type = kwargs.get('type', None)
        self.undiscounted_amount_excluding_tax = kwargs.get('undiscounted_amount_excluding_tax', None)
        self.undiscounted_amount_including_tax = kwargs.get('undiscounted_amount_including_tax', None)
        self.undiscounted_unit_price_excluding_tax = kwargs.get('undiscounted_unit_price_excluding_tax', None)
        self.undiscounted_unit_price_including_tax = kwargs.get('undiscounted_unit_price_including_tax', None)
        self.unique_id = kwargs.get('unique_id', None)
        self.unit_price_excluding_tax = kwargs.get('unit_price_excluding_tax', None)
        self.unit_price_including_tax = kwargs.get('unit_price_including_tax', None)
        

    
    @property
    def aggregated_tax_rate(self):
        """Gets the aggregated_tax_rate of this LineItem.

            The aggregated tax rate is the sum of all tax rates of the line item.

        :return: The aggregated_tax_rate of this LineItem.
        :rtype: float
        """
        return self._aggregated_tax_rate

    @aggregated_tax_rate.setter
    def aggregated_tax_rate(self, aggregated_tax_rate):
        """Sets the aggregated_tax_rate of this LineItem.

            The aggregated tax rate is the sum of all tax rates of the line item.

        :param aggregated_tax_rate: The aggregated_tax_rate of this LineItem.
        :type: float
        """

        self._aggregated_tax_rate = aggregated_tax_rate
    
    @property
    def amount_excluding_tax(self):
        """Gets the amount_excluding_tax of this LineItem.

            

        :return: The amount_excluding_tax of this LineItem.
        :rtype: float
        """
        return self._amount_excluding_tax

    @amount_excluding_tax.setter
    def amount_excluding_tax(self, amount_excluding_tax):
        """Sets the amount_excluding_tax of this LineItem.

            

        :param amount_excluding_tax: The amount_excluding_tax of this LineItem.
        :type: float
        """

        self._amount_excluding_tax = amount_excluding_tax
    
    @property
    def amount_including_tax(self):
        """Gets the amount_including_tax of this LineItem.

            

        :return: The amount_including_tax of this LineItem.
        :rtype: float
        """
        return self._amount_including_tax

    @amount_including_tax.setter
    def amount_including_tax(self, amount_including_tax):
        """Sets the amount_including_tax of this LineItem.

            

        :param amount_including_tax: The amount_including_tax of this LineItem.
        :type: float
        """

        self._amount_including_tax = amount_including_tax
    
    @property
    def attributes(self):
        """Gets the attributes of this LineItem.

            

        :return: The attributes of this LineItem.
        :rtype: dict(str, LineItemAttribute)
        """
        return self._attributes

    @attributes.setter
    def attributes(self, attributes):
        """Sets the attributes of this LineItem.

            

        :param attributes: The attributes of this LineItem.
        :type: dict(str, LineItemAttribute)
        """

        self._attributes = attributes
    
    @property
    def discount_excluding_tax(self):
        """Gets the discount_excluding_tax of this LineItem.

            

        :return: The discount_excluding_tax of this LineItem.
        :rtype: float
        """
        return self._discount_excluding_tax

    @discount_excluding_tax.setter
    def discount_excluding_tax(self, discount_excluding_tax):
        """Sets the discount_excluding_tax of this LineItem.

            

        :param discount_excluding_tax: The discount_excluding_tax of this LineItem.
        :type: float
        """

        self._discount_excluding_tax = discount_excluding_tax
    
    @property
    def discount_including_tax(self):
        """Gets the discount_including_tax of this LineItem.

            

        :return: The discount_including_tax of this LineItem.
        :rtype: float
        """
        return self._discount_including_tax

    @discount_including_tax.setter
    def discount_including_tax(self, discount_including_tax):
        """Sets the discount_including_tax of this LineItem.

            

        :param discount_including_tax: The discount_including_tax of this LineItem.
        :type: float
        """

        self._discount_including_tax = discount_including_tax
    
    @property
    def name(self):
        """Gets the name of this LineItem.

            

        :return: The name of this LineItem.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this LineItem.

            

        :param name: The name of this LineItem.
        :type: str
        """
        if name is not None and len(name) > 150:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `150`")
        if name is not None and len(name) < 1:
            raise ValueError("Invalid value for `name`, length must be greater than or equal to `1`")

        self._name = name
    
    @property
    def quantity(self):
        """Gets the quantity of this LineItem.

            

        :return: The quantity of this LineItem.
        :rtype: float
        """
        return self._quantity

    @quantity.setter
    def quantity(self, quantity):
        """Sets the quantity of this LineItem.

            

        :param quantity: The quantity of this LineItem.
        :type: float
        """

        self._quantity = quantity
    
    @property
    def shipping_required(self):
        """Gets the shipping_required of this LineItem.

            

        :return: The shipping_required of this LineItem.
        :rtype: bool
        """
        return self._shipping_required

    @shipping_required.setter
    def shipping_required(self, shipping_required):
        """Sets the shipping_required of this LineItem.

            

        :param shipping_required: The shipping_required of this LineItem.
        :type: bool
        """

        self._shipping_required = shipping_required
    
    @property
    def sku(self):
        """Gets the sku of this LineItem.

            

        :return: The sku of this LineItem.
        :rtype: str
        """
        return self._sku

    @sku.setter
    def sku(self, sku):
        """Sets the sku of this LineItem.

            

        :param sku: The sku of this LineItem.
        :type: str
        """
        if sku is not None and len(sku) > 200:
            raise ValueError("Invalid value for `sku`, length must be less than or equal to `200`")

        self._sku = sku
    
    @property
    def tax_amount(self):
        """Gets the tax_amount of this LineItem.

            

        :return: The tax_amount of this LineItem.
        :rtype: float
        """
        return self._tax_amount

    @tax_amount.setter
    def tax_amount(self, tax_amount):
        """Sets the tax_amount of this LineItem.

            

        :param tax_amount: The tax_amount of this LineItem.
        :type: float
        """

        self._tax_amount = tax_amount
    
    @property
    def tax_amount_per_unit(self):
        """Gets the tax_amount_per_unit of this LineItem.

            

        :return: The tax_amount_per_unit of this LineItem.
        :rtype: float
        """
        return self._tax_amount_per_unit

    @tax_amount_per_unit.setter
    def tax_amount_per_unit(self, tax_amount_per_unit):
        """Sets the tax_amount_per_unit of this LineItem.

            

        :param tax_amount_per_unit: The tax_amount_per_unit of this LineItem.
        :type: float
        """

        self._tax_amount_per_unit = tax_amount_per_unit
    
    @property
    def taxes(self):
        """Gets the taxes of this LineItem.

            

        :return: The taxes of this LineItem.
        :rtype: list[Tax]
        """
        return self._taxes

    @taxes.setter
    def taxes(self, taxes):
        """Sets the taxes of this LineItem.

            

        :param taxes: The taxes of this LineItem.
        :type: list[Tax]
        """

        self._taxes = taxes
    
    @property
    def type(self):
        """Gets the type of this LineItem.

            

        :return: The type of this LineItem.
        :rtype: LineItemType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this LineItem.

            

        :param type: The type of this LineItem.
        :type: LineItemType
        """

        self._type = type
    
    @property
    def undiscounted_amount_excluding_tax(self):
        """Gets the undiscounted_amount_excluding_tax of this LineItem.

            

        :return: The undiscounted_amount_excluding_tax of this LineItem.
        :rtype: float
        """
        return self._undiscounted_amount_excluding_tax

    @undiscounted_amount_excluding_tax.setter
    def undiscounted_amount_excluding_tax(self, undiscounted_amount_excluding_tax):
        """Sets the undiscounted_amount_excluding_tax of this LineItem.

            

        :param undiscounted_amount_excluding_tax: The undiscounted_amount_excluding_tax of this LineItem.
        :type: float
        """

        self._undiscounted_amount_excluding_tax = undiscounted_amount_excluding_tax
    
    @property
    def undiscounted_amount_including_tax(self):
        """Gets the undiscounted_amount_including_tax of this LineItem.

            

        :return: The undiscounted_amount_including_tax of this LineItem.
        :rtype: float
        """
        return self._undiscounted_amount_including_tax

    @undiscounted_amount_including_tax.setter
    def undiscounted_amount_including_tax(self, undiscounted_amount_including_tax):
        """Sets the undiscounted_amount_including_tax of this LineItem.

            

        :param undiscounted_amount_including_tax: The undiscounted_amount_including_tax of this LineItem.
        :type: float
        """

        self._undiscounted_amount_including_tax = undiscounted_amount_including_tax
    
    @property
    def undiscounted_unit_price_excluding_tax(self):
        """Gets the undiscounted_unit_price_excluding_tax of this LineItem.

            

        :return: The undiscounted_unit_price_excluding_tax of this LineItem.
        :rtype: float
        """
        return self._undiscounted_unit_price_excluding_tax

    @undiscounted_unit_price_excluding_tax.setter
    def undiscounted_unit_price_excluding_tax(self, undiscounted_unit_price_excluding_tax):
        """Sets the undiscounted_unit_price_excluding_tax of this LineItem.

            

        :param undiscounted_unit_price_excluding_tax: The undiscounted_unit_price_excluding_tax of this LineItem.
        :type: float
        """

        self._undiscounted_unit_price_excluding_tax = undiscounted_unit_price_excluding_tax
    
    @property
    def undiscounted_unit_price_including_tax(self):
        """Gets the undiscounted_unit_price_including_tax of this LineItem.

            

        :return: The undiscounted_unit_price_including_tax of this LineItem.
        :rtype: float
        """
        return self._undiscounted_unit_price_including_tax

    @undiscounted_unit_price_including_tax.setter
    def undiscounted_unit_price_including_tax(self, undiscounted_unit_price_including_tax):
        """Sets the undiscounted_unit_price_including_tax of this LineItem.

            

        :param undiscounted_unit_price_including_tax: The undiscounted_unit_price_including_tax of this LineItem.
        :type: float
        """

        self._undiscounted_unit_price_including_tax = undiscounted_unit_price_including_tax
    
    @property
    def unique_id(self):
        """Gets the unique_id of this LineItem.

            The unique id identifies the line item within the set of line items associated with the transaction.

        :return: The unique_id of this LineItem.
        :rtype: str
        """
        return self._unique_id

    @unique_id.setter
    def unique_id(self, unique_id):
        """Sets the unique_id of this LineItem.

            The unique id identifies the line item within the set of line items associated with the transaction.

        :param unique_id: The unique_id of this LineItem.
        :type: str
        """
        if unique_id is not None and len(unique_id) > 200:
            raise ValueError("Invalid value for `unique_id`, length must be less than or equal to `200`")

        self._unique_id = unique_id
    
    @property
    def unit_price_excluding_tax(self):
        """Gets the unit_price_excluding_tax of this LineItem.

            

        :return: The unit_price_excluding_tax of this LineItem.
        :rtype: float
        """
        return self._unit_price_excluding_tax

    @unit_price_excluding_tax.setter
    def unit_price_excluding_tax(self, unit_price_excluding_tax):
        """Sets the unit_price_excluding_tax of this LineItem.

            

        :param unit_price_excluding_tax: The unit_price_excluding_tax of this LineItem.
        :type: float
        """

        self._unit_price_excluding_tax = unit_price_excluding_tax
    
    @property
    def unit_price_including_tax(self):
        """Gets the unit_price_including_tax of this LineItem.

            

        :return: The unit_price_including_tax of this LineItem.
        :rtype: float
        """
        return self._unit_price_including_tax

    @unit_price_including_tax.setter
    def unit_price_including_tax(self, unit_price_including_tax):
        """Sets the unit_price_including_tax of this LineItem.

            

        :param unit_price_including_tax: The unit_price_including_tax of this LineItem.
        :type: float
        """

        self._unit_price_including_tax = unit_price_including_tax
    

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
        if issubclass(LineItem, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LineItem):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
