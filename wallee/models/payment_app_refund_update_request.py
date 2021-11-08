# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppRefundUpdateRequest:

    swagger_types = {
    
        'failure_reason_id': 'int',
        'reference': 'str',
        'refund_id': 'int',
        'target_state': 'PaymentAppRefundTargetState',
    }

    attribute_map = {
        'failure_reason_id': 'failureReasonId','reference': 'reference','refund_id': 'refundId','target_state': 'targetState',
    }

    
    _failure_reason_id = None
    _reference = None
    _refund_id = None
    _target_state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.failure_reason_id = kwargs.get('failure_reason_id', None)
        self.reference = kwargs.get('reference', None)
        self.refund_id = kwargs.get('refund_id', None)
        self.target_state = kwargs.get('target_state', None)
        

    
    @property
    def failure_reason_id(self):
        """Gets the failure_reason_id of this PaymentAppRefundUpdateRequest.

            The failure reason indicates why the refund failed. It is required when the target state is FAILED.

        :return: The failure_reason_id of this PaymentAppRefundUpdateRequest.
        :rtype: int
        """
        return self._failure_reason_id

    @failure_reason_id.setter
    def failure_reason_id(self, failure_reason_id):
        """Sets the failure_reason_id of this PaymentAppRefundUpdateRequest.

            The failure reason indicates why the refund failed. It is required when the target state is FAILED.

        :param failure_reason_id: The failure_reason_id of this PaymentAppRefundUpdateRequest.
        :type: int
        """

        self._failure_reason_id = failure_reason_id
    
    @property
    def reference(self):
        """Gets the reference of this PaymentAppRefundUpdateRequest.

            The reference identifies the refund within the systems of the external service provider. It is required when the target state is SUCCESSFUL.

        :return: The reference of this PaymentAppRefundUpdateRequest.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentAppRefundUpdateRequest.

            The reference identifies the refund within the systems of the external service provider. It is required when the target state is SUCCESSFUL.

        :param reference: The reference of this PaymentAppRefundUpdateRequest.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def refund_id(self):
        """Gets the refund_id of this PaymentAppRefundUpdateRequest.

            This is the ID of the refund that should be updated.

        :return: The refund_id of this PaymentAppRefundUpdateRequest.
        :rtype: int
        """
        return self._refund_id

    @refund_id.setter
    def refund_id(self, refund_id):
        """Sets the refund_id of this PaymentAppRefundUpdateRequest.

            This is the ID of the refund that should be updated.

        :param refund_id: The refund_id of this PaymentAppRefundUpdateRequest.
        :type: int
        """

        self._refund_id = refund_id
    
    @property
    def target_state(self):
        """Gets the target_state of this PaymentAppRefundUpdateRequest.

            The target state defines the state into which the refund should be switched into. Once the refund changed the state it will not be possible to change it again.

        :return: The target_state of this PaymentAppRefundUpdateRequest.
        :rtype: PaymentAppRefundTargetState
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this PaymentAppRefundUpdateRequest.

            The target state defines the state into which the refund should be switched into. Once the refund changed the state it will not be possible to change it again.

        :param target_state: The target_state of this PaymentAppRefundUpdateRequest.
        :type: PaymentAppRefundTargetState
        """

        self._target_state = target_state
    

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
        if issubclass(PaymentAppRefundUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppRefundUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
