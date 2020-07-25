# coding: utf-8
import pprint
import six
from enum import Enum



class LineItemReductionCreate:

    swagger_types = {
    
        'line_item_unique_id': 'str',
        'quantity_reduction': 'float',
        'unit_price_reduction': 'float',
    }

    attribute_map = {
        'line_item_unique_id': 'lineItemUniqueId','quantity_reduction': 'quantityReduction','unit_price_reduction': 'unitPriceReduction',
    }

    
    _line_item_unique_id = None
    _quantity_reduction = None
    _unit_price_reduction = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.line_item_unique_id = kwargs.get('line_item_unique_id')

        self.quantity_reduction = kwargs.get('quantity_reduction')

        self.unit_price_reduction = kwargs.get('unit_price_reduction')

        

    
    @property
    def line_item_unique_id(self):
        """Gets the line_item_unique_id of this LineItemReductionCreate.

            The unique id identifies the line item on which the reduction is applied on.

        :return: The line_item_unique_id of this LineItemReductionCreate.
        :rtype: str
        """
        return self._line_item_unique_id

    @line_item_unique_id.setter
    def line_item_unique_id(self, line_item_unique_id):
        """Sets the line_item_unique_id of this LineItemReductionCreate.

            The unique id identifies the line item on which the reduction is applied on.

        :param line_item_unique_id: The line_item_unique_id of this LineItemReductionCreate.
        :type: str
        """
        if line_item_unique_id is None:
            raise ValueError("Invalid value for `line_item_unique_id`, must not be `None`")
        if line_item_unique_id is not None and len(line_item_unique_id) > 200:
            raise ValueError("Invalid value for `line_item_unique_id`, length must be less than or equal to `200`")

        self._line_item_unique_id = line_item_unique_id
    
    @property
    def quantity_reduction(self):
        """Gets the quantity_reduction of this LineItemReductionCreate.

            

        :return: The quantity_reduction of this LineItemReductionCreate.
        :rtype: float
        """
        return self._quantity_reduction

    @quantity_reduction.setter
    def quantity_reduction(self, quantity_reduction):
        """Sets the quantity_reduction of this LineItemReductionCreate.

            

        :param quantity_reduction: The quantity_reduction of this LineItemReductionCreate.
        :type: float
        """
        if quantity_reduction is None:
            raise ValueError("Invalid value for `quantity_reduction`, must not be `None`")

        self._quantity_reduction = quantity_reduction
    
    @property
    def unit_price_reduction(self):
        """Gets the unit_price_reduction of this LineItemReductionCreate.

            

        :return: The unit_price_reduction of this LineItemReductionCreate.
        :rtype: float
        """
        return self._unit_price_reduction

    @unit_price_reduction.setter
    def unit_price_reduction(self, unit_price_reduction):
        """Sets the unit_price_reduction of this LineItemReductionCreate.

            

        :param unit_price_reduction: The unit_price_reduction of this LineItemReductionCreate.
        :type: float
        """
        if unit_price_reduction is None:
            raise ValueError("Invalid value for `unit_price_reduction`, must not be `None`")

        self._unit_price_reduction = unit_price_reduction
    

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
        if issubclass(LineItemReductionCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LineItemReductionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
