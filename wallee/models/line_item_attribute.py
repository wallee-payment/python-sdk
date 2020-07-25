# coding: utf-8
import pprint
import six
from enum import Enum



class LineItemAttribute:

    swagger_types = {
    
        'label': 'str',
        'value': 'str',
    }

    attribute_map = {
        'label': 'label','value': 'value',
    }

    
    _label = None
    _value = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.label = kwargs.get('label', None)
        self.value = kwargs.get('value', None)
        

    
    @property
    def label(self):
        """Gets the label of this LineItemAttribute.

            

        :return: The label of this LineItemAttribute.
        :rtype: str
        """
        return self._label

    @label.setter
    def label(self, label):
        """Sets the label of this LineItemAttribute.

            

        :param label: The label of this LineItemAttribute.
        :type: str
        """
        if label is not None and len(label) > 512:
            raise ValueError("Invalid value for `label`, length must be less than or equal to `512`")

        self._label = label
    
    @property
    def value(self):
        """Gets the value of this LineItemAttribute.

            

        :return: The value of this LineItemAttribute.
        :rtype: str
        """
        return self._value

    @value.setter
    def value(self, value):
        """Sets the value of this LineItemAttribute.

            

        :param value: The value of this LineItemAttribute.
        :type: str
        """
        if value is not None and len(value) > 512:
            raise ValueError("Invalid value for `value`, length must be less than or equal to `512`")

        self._value = value
    

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
        if issubclass(LineItemAttribute, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, LineItemAttribute):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
