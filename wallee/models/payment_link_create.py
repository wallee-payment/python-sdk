# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractPaymentLinkUpdate


class PaymentLinkCreate(AbstractPaymentLinkUpdate):

    swagger_types = {
    
        'state': 'CreationEntityState',
        'external_id': 'str',
        'protection_mode': 'PaymentLinkProtectionMode',
    }

    attribute_map = {
        'state': 'state','external_id': 'externalId','protection_mode': 'protectionMode',
    }

    
    _state = None
    _external_id = None
    _protection_mode = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.state = kwargs.get('state', None)
        self.external_id = kwargs.get('external_id')

        self.protection_mode = kwargs.get('protection_mode', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def state(self):
        """Gets the state of this PaymentLinkCreate.

            

        :return: The state of this PaymentLinkCreate.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentLinkCreate.

            

        :param state: The state of this PaymentLinkCreate.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentLinkCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this PaymentLinkCreate.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentLinkCreate.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this PaymentLinkCreate.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")

        self._external_id = external_id
    
    @property
    def protection_mode(self):
        """Gets the protection_mode of this PaymentLinkCreate.

            The protection mode determines if the payment link is protected against tampering and in what way.

        :return: The protection_mode of this PaymentLinkCreate.
        :rtype: PaymentLinkProtectionMode
        """
        return self._protection_mode

    @protection_mode.setter
    def protection_mode(self, protection_mode):
        """Sets the protection_mode of this PaymentLinkCreate.

            The protection mode determines if the payment link is protected against tampering and in what way.

        :param protection_mode: The protection_mode of this PaymentLinkCreate.
        :type: PaymentLinkProtectionMode
        """

        self._protection_mode = protection_mode
    

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
        if issubclass(PaymentLinkCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentLinkCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
