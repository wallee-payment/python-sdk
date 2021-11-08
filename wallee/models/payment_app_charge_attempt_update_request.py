# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppChargeAttemptUpdateRequest:

    swagger_types = {
    
        'charge_attempt_id': 'int',
        'end_user_failure_message': 'str',
        'failure_reason_id': 'int',
        'reference': 'str',
        'target_state': 'PaymentAppChargeAttemptTargetState',
    }

    attribute_map = {
        'charge_attempt_id': 'chargeAttemptId','end_user_failure_message': 'endUserFailureMessage','failure_reason_id': 'failureReasonId','reference': 'reference','target_state': 'targetState',
    }

    
    _charge_attempt_id = None
    _end_user_failure_message = None
    _failure_reason_id = None
    _reference = None
    _target_state = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.charge_attempt_id = kwargs.get('charge_attempt_id', None)
        self.end_user_failure_message = kwargs.get('end_user_failure_message', None)
        self.failure_reason_id = kwargs.get('failure_reason_id', None)
        self.reference = kwargs.get('reference', None)
        self.target_state = kwargs.get('target_state', None)
        

    
    @property
    def charge_attempt_id(self):
        """Gets the charge_attempt_id of this PaymentAppChargeAttemptUpdateRequest.

            This is the ID of the charge attempt that should be updated.

        :return: The charge_attempt_id of this PaymentAppChargeAttemptUpdateRequest.
        :rtype: int
        """
        return self._charge_attempt_id

    @charge_attempt_id.setter
    def charge_attempt_id(self, charge_attempt_id):
        """Sets the charge_attempt_id of this PaymentAppChargeAttemptUpdateRequest.

            This is the ID of the charge attempt that should be updated.

        :param charge_attempt_id: The charge_attempt_id of this PaymentAppChargeAttemptUpdateRequest.
        :type: int
        """

        self._charge_attempt_id = charge_attempt_id
    
    @property
    def end_user_failure_message(self):
        """Gets the end_user_failure_message of this PaymentAppChargeAttemptUpdateRequest.

            The end user failure message indicates to the end user (buyer) why the payment failed. The message has to be in the language of the end user. The language is provided within the payment page invocation URL.

        :return: The end_user_failure_message of this PaymentAppChargeAttemptUpdateRequest.
        :rtype: str
        """
        return self._end_user_failure_message

    @end_user_failure_message.setter
    def end_user_failure_message(self, end_user_failure_message):
        """Sets the end_user_failure_message of this PaymentAppChargeAttemptUpdateRequest.

            The end user failure message indicates to the end user (buyer) why the payment failed. The message has to be in the language of the end user. The language is provided within the payment page invocation URL.

        :param end_user_failure_message: The end_user_failure_message of this PaymentAppChargeAttemptUpdateRequest.
        :type: str
        """
        if end_user_failure_message is not None and len(end_user_failure_message) > 2000:
            raise ValueError("Invalid value for `end_user_failure_message`, length must be less than or equal to `2000`")

        self._end_user_failure_message = end_user_failure_message
    
    @property
    def failure_reason_id(self):
        """Gets the failure_reason_id of this PaymentAppChargeAttemptUpdateRequest.

            The failure reason indicates why the charge attempt failed. It is required when the target state is FAILED.

        :return: The failure_reason_id of this PaymentAppChargeAttemptUpdateRequest.
        :rtype: int
        """
        return self._failure_reason_id

    @failure_reason_id.setter
    def failure_reason_id(self, failure_reason_id):
        """Sets the failure_reason_id of this PaymentAppChargeAttemptUpdateRequest.

            The failure reason indicates why the charge attempt failed. It is required when the target state is FAILED.

        :param failure_reason_id: The failure_reason_id of this PaymentAppChargeAttemptUpdateRequest.
        :type: int
        """

        self._failure_reason_id = failure_reason_id
    
    @property
    def reference(self):
        """Gets the reference of this PaymentAppChargeAttemptUpdateRequest.

            The reference identifies the charge attempt within the systems of the external service provider. It is required when the target state is SUCCESSFUL.

        :return: The reference of this PaymentAppChargeAttemptUpdateRequest.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this PaymentAppChargeAttemptUpdateRequest.

            The reference identifies the charge attempt within the systems of the external service provider. It is required when the target state is SUCCESSFUL.

        :param reference: The reference of this PaymentAppChargeAttemptUpdateRequest.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def target_state(self):
        """Gets the target_state of this PaymentAppChargeAttemptUpdateRequest.

            The target state defines the state into which the charge attempt should be switched into. Once the charge attempt changed the state it will not be possible to change it again.

        :return: The target_state of this PaymentAppChargeAttemptUpdateRequest.
        :rtype: PaymentAppChargeAttemptTargetState
        """
        return self._target_state

    @target_state.setter
    def target_state(self, target_state):
        """Sets the target_state of this PaymentAppChargeAttemptUpdateRequest.

            The target state defines the state into which the charge attempt should be switched into. Once the charge attempt changed the state it will not be possible to change it again.

        :param target_state: The target_state of this PaymentAppChargeAttemptUpdateRequest.
        :type: PaymentAppChargeAttemptTargetState
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
        if issubclass(PaymentAppChargeAttemptUpdateRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppChargeAttemptUpdateRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
