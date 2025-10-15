# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractTransactionPending


class TransactionCreate(AbstractTransactionPending):

    swagger_types = {
    
        'auto_confirmation_enabled': 'bool',
        'charge_retry_enabled': 'bool',
        'customers_presence': 'CustomersPresence',
        'device_session_identifier': 'str',
        'emails_disabled': 'bool',
        'environment': 'Environment',
        'environment_selection_strategy': 'TransactionEnvironmentSelectionStrategy',
        'space_view_id': 'int',
    }

    attribute_map = {
        'auto_confirmation_enabled': 'autoConfirmationEnabled','charge_retry_enabled': 'chargeRetryEnabled','customers_presence': 'customersPresence','device_session_identifier': 'deviceSessionIdentifier','emails_disabled': 'emailsDisabled','environment': 'environment','environment_selection_strategy': 'environmentSelectionStrategy','space_view_id': 'spaceViewId',
    }

    
    _auto_confirmation_enabled = None
    _charge_retry_enabled = None
    _customers_presence = None
    _device_session_identifier = None
    _emails_disabled = None
    _environment = None
    _environment_selection_strategy = None
    _space_view_id = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.auto_confirmation_enabled = kwargs.get('auto_confirmation_enabled', None)
        self.charge_retry_enabled = kwargs.get('charge_retry_enabled', None)
        self.customers_presence = kwargs.get('customers_presence', None)
        self.device_session_identifier = kwargs.get('device_session_identifier', None)
        self.emails_disabled = kwargs.get('emails_disabled', None)
        self.environment = kwargs.get('environment', None)
        self.environment_selection_strategy = kwargs.get('environment_selection_strategy', None)
        self.space_view_id = kwargs.get('space_view_id', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def auto_confirmation_enabled(self):
        """Gets the auto_confirmation_enabled of this TransactionCreate.

            Whether the transaction can be confirmed automatically or whether this must be done explicitly via the API. Default is true.

        :return: The auto_confirmation_enabled of this TransactionCreate.
        :rtype: bool
        """
        return self._auto_confirmation_enabled

    @auto_confirmation_enabled.setter
    def auto_confirmation_enabled(self, auto_confirmation_enabled):
        """Sets the auto_confirmation_enabled of this TransactionCreate.

            Whether the transaction can be confirmed automatically or whether this must be done explicitly via the API. Default is true.

        :param auto_confirmation_enabled: The auto_confirmation_enabled of this TransactionCreate.
        :type: bool
        """

        self._auto_confirmation_enabled = auto_confirmation_enabled
    
    @property
    def charge_retry_enabled(self):
        """Gets the charge_retry_enabled of this TransactionCreate.

            Whether the customer can make further payment attempts if the first one has failed. Default is true.

        :return: The charge_retry_enabled of this TransactionCreate.
        :rtype: bool
        """
        return self._charge_retry_enabled

    @charge_retry_enabled.setter
    def charge_retry_enabled(self, charge_retry_enabled):
        """Sets the charge_retry_enabled of this TransactionCreate.

            Whether the customer can make further payment attempts if the first one has failed. Default is true.

        :param charge_retry_enabled: The charge_retry_enabled of this TransactionCreate.
        :type: bool
        """

        self._charge_retry_enabled = charge_retry_enabled
    
    @property
    def customers_presence(self):
        """Gets the customers_presence of this TransactionCreate.

            The customer's presence indicates whether and in what way the transaction's customer is present. Default is VIRTUAL_PRESENT.

        :return: The customers_presence of this TransactionCreate.
        :rtype: CustomersPresence
        """
        return self._customers_presence

    @customers_presence.setter
    def customers_presence(self, customers_presence):
        """Sets the customers_presence of this TransactionCreate.

            The customer's presence indicates whether and in what way the transaction's customer is present. Default is VIRTUAL_PRESENT.

        :param customers_presence: The customers_presence of this TransactionCreate.
        :type: CustomersPresence
        """

        self._customers_presence = customers_presence
    
    @property
    def device_session_identifier(self):
        """Gets the device_session_identifier of this TransactionCreate.

            Allows to link the transaction to the data collected from the customer's device.

        :return: The device_session_identifier of this TransactionCreate.
        :rtype: str
        """
        return self._device_session_identifier

    @device_session_identifier.setter
    def device_session_identifier(self, device_session_identifier):
        """Sets the device_session_identifier of this TransactionCreate.

            Allows to link the transaction to the data collected from the customer's device.

        :param device_session_identifier: The device_session_identifier of this TransactionCreate.
        :type: str
        """
        if device_session_identifier is not None and len(device_session_identifier) > 40:
            raise ValueError("Invalid value for `device_session_identifier`, length must be less than or equal to `40`")
        if device_session_identifier is not None and len(device_session_identifier) < 10:
            raise ValueError("Invalid value for `device_session_identifier`, length must be greater than or equal to `10`")

        self._device_session_identifier = device_session_identifier
    
    @property
    def emails_disabled(self):
        """Gets the emails_disabled of this TransactionCreate.

            Whether email sending is deactivated for the transaction. Default is false.

        :return: The emails_disabled of this TransactionCreate.
        :rtype: bool
        """
        return self._emails_disabled

    @emails_disabled.setter
    def emails_disabled(self, emails_disabled):
        """Sets the emails_disabled of this TransactionCreate.

            Whether email sending is deactivated for the transaction. Default is false.

        :param emails_disabled: The emails_disabled of this TransactionCreate.
        :type: bool
        """

        self._emails_disabled = emails_disabled
    
    @property
    def environment(self):
        """Gets the environment of this TransactionCreate.

            The environment used when rendering resources.

        :return: The environment of this TransactionCreate.
        :rtype: Environment
        """
        return self._environment

    @environment.setter
    def environment(self, environment):
        """Sets the environment of this TransactionCreate.

            The environment used when rendering resources.

        :param environment: The environment of this TransactionCreate.
        :type: Environment
        """

        self._environment = environment
    
    @property
    def environment_selection_strategy(self):
        """Gets the environment_selection_strategy of this TransactionCreate.

            The strategy for determining whether the transaction is to be processed in the test or production environment.

        :return: The environment_selection_strategy of this TransactionCreate.
        :rtype: TransactionEnvironmentSelectionStrategy
        """
        return self._environment_selection_strategy

    @environment_selection_strategy.setter
    def environment_selection_strategy(self, environment_selection_strategy):
        """Sets the environment_selection_strategy of this TransactionCreate.

            The strategy for determining whether the transaction is to be processed in the test or production environment.

        :param environment_selection_strategy: The environment_selection_strategy of this TransactionCreate.
        :type: TransactionEnvironmentSelectionStrategy
        """

        self._environment_selection_strategy = environment_selection_strategy
    
    @property
    def space_view_id(self):
        """Gets the space_view_id of this TransactionCreate.

            The ID of the space view this object is linked to.

        :return: The space_view_id of this TransactionCreate.
        :rtype: int
        """
        return self._space_view_id

    @space_view_id.setter
    def space_view_id(self, space_view_id):
        """Sets the space_view_id of this TransactionCreate.

            The ID of the space view this object is linked to.

        :param space_view_id: The space_view_id of this TransactionCreate.
        :type: int
        """

        self._space_view_id = space_view_id
    

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
        if issubclass(TransactionCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, TransactionCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
