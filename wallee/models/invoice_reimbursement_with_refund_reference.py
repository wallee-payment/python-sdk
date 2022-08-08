# coding: utf-8
import pprint
import six
from enum import Enum
from . import InvoiceReimbursement


class InvoiceReimbursementWithRefundReference(InvoiceReimbursement):

    swagger_types = {
    
        'refund_merchant_reference': 'str',
    }

    attribute_map = {
        'refund_merchant_reference': 'refundMerchantReference',
    }

    
    _refund_merchant_reference = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.refund_merchant_reference = kwargs.get('refund_merchant_reference', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def refund_merchant_reference(self):
        """Gets the refund_merchant_reference of this InvoiceReimbursementWithRefundReference.

            

        :return: The refund_merchant_reference of this InvoiceReimbursementWithRefundReference.
        :rtype: str
        """
        return self._refund_merchant_reference

    @refund_merchant_reference.setter
    def refund_merchant_reference(self, refund_merchant_reference):
        """Sets the refund_merchant_reference of this InvoiceReimbursementWithRefundReference.

            

        :param refund_merchant_reference: The refund_merchant_reference of this InvoiceReimbursementWithRefundReference.
        :type: str
        """

        self._refund_merchant_reference = refund_merchant_reference
    

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
        if issubclass(InvoiceReimbursementWithRefundReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, InvoiceReimbursementWithRefundReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
