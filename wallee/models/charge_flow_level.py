# coding: utf-8
import pprint
import six
from enum import Enum
from . import TransactionAwareEntity


class ChargeFlowLevel(TransactionAwareEntity):

    swagger_types = {
    
        'asynchronous_charge': 'int',
        'configuration': 'ChargeFlowLevelConfiguration',
        'created_on': 'datetime',
        'planned_purge_date': 'datetime',
        'state': 'ChargeFlowLevelState',
        'synchronous_charge': 'int',
        'timeout_on': 'datetime',
        'token_charge': 'int',
        'transaction': 'Transaction',
        'version': 'int',
    }

    attribute_map = {
        'asynchronous_charge': 'asynchronousCharge','configuration': 'configuration','created_on': 'createdOn','planned_purge_date': 'plannedPurgeDate','state': 'state','synchronous_charge': 'synchronousCharge','timeout_on': 'timeoutOn','token_charge': 'tokenCharge','transaction': 'transaction','version': 'version',
    }

    
    _asynchronous_charge = None
    _configuration = None
    _created_on = None
    _planned_purge_date = None
    _state = None
    _synchronous_charge = None
    _timeout_on = None
    _token_charge = None
    _transaction = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.asynchronous_charge = kwargs.get('asynchronous_charge', None)
        self.configuration = kwargs.get('configuration', None)
        self.created_on = kwargs.get('created_on', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.state = kwargs.get('state', None)
        self.synchronous_charge = kwargs.get('synchronous_charge', None)
        self.timeout_on = kwargs.get('timeout_on', None)
        self.token_charge = kwargs.get('token_charge', None)
        self.transaction = kwargs.get('transaction', None)
        self.version = kwargs.get('version', None)
        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    
    @property
    def asynchronous_charge(self):
        """Gets the asynchronous_charge of this ChargeFlowLevel.

            

        :return: The asynchronous_charge of this ChargeFlowLevel.
        :rtype: int
        """
        return self._asynchronous_charge

    @asynchronous_charge.setter
    def asynchronous_charge(self, asynchronous_charge):
        """Sets the asynchronous_charge of this ChargeFlowLevel.

            

        :param asynchronous_charge: The asynchronous_charge of this ChargeFlowLevel.
        :type: int
        """

        self._asynchronous_charge = asynchronous_charge
    
    @property
    def configuration(self):
        """Gets the configuration of this ChargeFlowLevel.

            

        :return: The configuration of this ChargeFlowLevel.
        :rtype: ChargeFlowLevelConfiguration
        """
        return self._configuration

    @configuration.setter
    def configuration(self, configuration):
        """Sets the configuration of this ChargeFlowLevel.

            

        :param configuration: The configuration of this ChargeFlowLevel.
        :type: ChargeFlowLevelConfiguration
        """

        self._configuration = configuration
    
    @property
    def created_on(self):
        """Gets the created_on of this ChargeFlowLevel.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this ChargeFlowLevel.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ChargeFlowLevel.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this ChargeFlowLevel.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ChargeFlowLevel.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ChargeFlowLevel.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ChargeFlowLevel.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ChargeFlowLevel.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def state(self):
        """Gets the state of this ChargeFlowLevel.

            

        :return: The state of this ChargeFlowLevel.
        :rtype: ChargeFlowLevelState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ChargeFlowLevel.

            

        :param state: The state of this ChargeFlowLevel.
        :type: ChargeFlowLevelState
        """

        self._state = state
    
    @property
    def synchronous_charge(self):
        """Gets the synchronous_charge of this ChargeFlowLevel.

            

        :return: The synchronous_charge of this ChargeFlowLevel.
        :rtype: int
        """
        return self._synchronous_charge

    @synchronous_charge.setter
    def synchronous_charge(self, synchronous_charge):
        """Sets the synchronous_charge of this ChargeFlowLevel.

            

        :param synchronous_charge: The synchronous_charge of this ChargeFlowLevel.
        :type: int
        """

        self._synchronous_charge = synchronous_charge
    
    @property
    def timeout_on(self):
        """Gets the timeout_on of this ChargeFlowLevel.

            

        :return: The timeout_on of this ChargeFlowLevel.
        :rtype: datetime
        """
        return self._timeout_on

    @timeout_on.setter
    def timeout_on(self, timeout_on):
        """Sets the timeout_on of this ChargeFlowLevel.

            

        :param timeout_on: The timeout_on of this ChargeFlowLevel.
        :type: datetime
        """

        self._timeout_on = timeout_on
    
    @property
    def token_charge(self):
        """Gets the token_charge of this ChargeFlowLevel.

            

        :return: The token_charge of this ChargeFlowLevel.
        :rtype: int
        """
        return self._token_charge

    @token_charge.setter
    def token_charge(self, token_charge):
        """Sets the token_charge of this ChargeFlowLevel.

            

        :param token_charge: The token_charge of this ChargeFlowLevel.
        :type: int
        """

        self._token_charge = token_charge
    
    @property
    def transaction(self):
        """Gets the transaction of this ChargeFlowLevel.

            

        :return: The transaction of this ChargeFlowLevel.
        :rtype: Transaction
        """
        return self._transaction

    @transaction.setter
    def transaction(self, transaction):
        """Sets the transaction of this ChargeFlowLevel.

            

        :param transaction: The transaction of this ChargeFlowLevel.
        :type: Transaction
        """

        self._transaction = transaction
    
    @property
    def version(self):
        """Gets the version of this ChargeFlowLevel.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ChargeFlowLevel.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ChargeFlowLevel.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ChargeFlowLevel.
        :type: int
        """

        self._version = version
    

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
        if issubclass(ChargeFlowLevel, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeFlowLevel):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
