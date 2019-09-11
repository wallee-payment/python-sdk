# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractRefundCommentActive


class RefundCommentCreate(AbstractRefundCommentActive):

    swagger_types = {
    
        'refund': 'int',
    }

    attribute_map = {
        'refund': 'refund',
    }

    
    _refund = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.refund = kwargs.get('refund')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def refund(self):
        """Gets the refund of this RefundCommentCreate.

            

        :return: The refund of this RefundCommentCreate.
        :rtype: int
        """
        return self._refund

    @refund.setter
    def refund(self, refund):
        """Sets the refund of this RefundCommentCreate.

            

        :param refund: The refund of this RefundCommentCreate.
        :type: int
        """
        if refund is None:
            raise ValueError("Invalid value for `refund`, must not be `None`")

        self._refund = refund
    

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
        if issubclass(RefundCommentCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RefundCommentCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
