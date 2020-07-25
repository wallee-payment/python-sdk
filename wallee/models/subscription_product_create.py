# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractSubscriptionProductActive


class SubscriptionProductCreate(AbstractSubscriptionProductActive):

    swagger_types = {
    
        'reference': 'str',
    }

    attribute_map = {
        'reference': 'reference',
    }

    
    _reference = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.reference = kwargs.get('reference')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def reference(self):
        """Gets the reference of this SubscriptionProductCreate.

            The product reference identifies the product for external systems. This field may contain the product's SKU.

        :return: The reference of this SubscriptionProductCreate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriptionProductCreate.

            The product reference identifies the product for external systems. This field may contain the product's SKU.

        :param reference: The reference of this SubscriptionProductCreate.
        :type: str
        """
        if reference is None:
            raise ValueError("Invalid value for `reference`, must not be `None`")
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    

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
        if issubclass(SubscriptionProductCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionProductCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
