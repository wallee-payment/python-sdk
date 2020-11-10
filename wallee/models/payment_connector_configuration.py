# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentConnectorConfiguration:

    swagger_types = {
    
        'applicable_for_transaction_processing': 'bool',
        'conditions': 'list[int]',
        'connector': 'int',
        'enabled_sales_channels': 'list[SalesChannel]',
        'enabled_space_views': 'list[int]',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'payment_method_configuration': 'PaymentMethodConfiguration',
        'planned_purge_date': 'datetime',
        'priority': 'int',
        'processor_configuration': 'PaymentProcessorConfiguration',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'applicable_for_transaction_processing': 'applicableForTransactionProcessing','conditions': 'conditions','connector': 'connector','enabled_sales_channels': 'enabledSalesChannels','enabled_space_views': 'enabledSpaceViews','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','payment_method_configuration': 'paymentMethodConfiguration','planned_purge_date': 'plannedPurgeDate','priority': 'priority','processor_configuration': 'processorConfiguration','state': 'state','version': 'version',
    }

    
    _applicable_for_transaction_processing = None
    _conditions = None
    _connector = None
    _enabled_sales_channels = None
    _enabled_space_views = None
    _id = None
    _linked_space_id = None
    _name = None
    _payment_method_configuration = None
    _planned_purge_date = None
    _priority = None
    _processor_configuration = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.applicable_for_transaction_processing = kwargs.get('applicable_for_transaction_processing', None)
        self.conditions = kwargs.get('conditions', None)
        self.connector = kwargs.get('connector', None)
        self.enabled_sales_channels = kwargs.get('enabled_sales_channels', None)
        self.enabled_space_views = kwargs.get('enabled_space_views', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.payment_method_configuration = kwargs.get('payment_method_configuration', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.priority = kwargs.get('priority', None)
        self.processor_configuration = kwargs.get('processor_configuration', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def applicable_for_transaction_processing(self):
        """Gets the applicable_for_transaction_processing of this PaymentConnectorConfiguration.

            This property indicates if the connector is currently used for processing transactions. In case either the payment method configuration or the processor configuration is not active the connector will not be used even though the connector state is active.

        :return: The applicable_for_transaction_processing of this PaymentConnectorConfiguration.
        :rtype: bool
        """
        return self._applicable_for_transaction_processing

    @applicable_for_transaction_processing.setter
    def applicable_for_transaction_processing(self, applicable_for_transaction_processing):
        """Sets the applicable_for_transaction_processing of this PaymentConnectorConfiguration.

            This property indicates if the connector is currently used for processing transactions. In case either the payment method configuration or the processor configuration is not active the connector will not be used even though the connector state is active.

        :param applicable_for_transaction_processing: The applicable_for_transaction_processing of this PaymentConnectorConfiguration.
        :type: bool
        """

        self._applicable_for_transaction_processing = applicable_for_transaction_processing
    
    @property
    def conditions(self):
        """Gets the conditions of this PaymentConnectorConfiguration.

            If a transaction meet all selected conditions the connector configuration will be used to process the transaction otherwise the next connector configuration in line will be chosen according to the priorities.

        :return: The conditions of this PaymentConnectorConfiguration.
        :rtype: list[int]
        """
        return self._conditions

    @conditions.setter
    def conditions(self, conditions):
        """Sets the conditions of this PaymentConnectorConfiguration.

            If a transaction meet all selected conditions the connector configuration will be used to process the transaction otherwise the next connector configuration in line will be chosen according to the priorities.

        :param conditions: The conditions of this PaymentConnectorConfiguration.
        :type: list[int]
        """

        self._conditions = conditions
    
    @property
    def connector(self):
        """Gets the connector of this PaymentConnectorConfiguration.

            

        :return: The connector of this PaymentConnectorConfiguration.
        :rtype: int
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this PaymentConnectorConfiguration.

            

        :param connector: The connector of this PaymentConnectorConfiguration.
        :type: int
        """

        self._connector = connector
    
    @property
    def enabled_sales_channels(self):
        """Gets the enabled_sales_channels of this PaymentConnectorConfiguration.

            Defines the sales channels the connector configuration is enabled for. In case the set is empty, the connector configuration is enabled for all sales channels.

        :return: The enabled_sales_channels of this PaymentConnectorConfiguration.
        :rtype: list[SalesChannel]
        """
        return self._enabled_sales_channels

    @enabled_sales_channels.setter
    def enabled_sales_channels(self, enabled_sales_channels):
        """Sets the enabled_sales_channels of this PaymentConnectorConfiguration.

            Defines the sales channels the connector configuration is enabled for. In case the set is empty, the connector configuration is enabled for all sales channels.

        :param enabled_sales_channels: The enabled_sales_channels of this PaymentConnectorConfiguration.
        :type: list[SalesChannel]
        """

        self._enabled_sales_channels = enabled_sales_channels
    
    @property
    def enabled_space_views(self):
        """Gets the enabled_space_views of this PaymentConnectorConfiguration.

            The connector configuration is only enabled for the selected space views. In case the set is empty the connector configuration is enabled for all space views.

        :return: The enabled_space_views of this PaymentConnectorConfiguration.
        :rtype: list[int]
        """
        return self._enabled_space_views

    @enabled_space_views.setter
    def enabled_space_views(self, enabled_space_views):
        """Sets the enabled_space_views of this PaymentConnectorConfiguration.

            The connector configuration is only enabled for the selected space views. In case the set is empty the connector configuration is enabled for all space views.

        :param enabled_space_views: The enabled_space_views of this PaymentConnectorConfiguration.
        :type: list[int]
        """

        self._enabled_space_views = enabled_space_views
    
    @property
    def id(self):
        """Gets the id of this PaymentConnectorConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentConnectorConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentConnectorConfiguration.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentConnectorConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentConnectorConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentConnectorConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentConnectorConfiguration.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentConnectorConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentConnectorConfiguration.

            The connector configuration name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentConnectorConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentConnectorConfiguration.

            The connector configuration name is used internally to identify the configuration in administrative interfaces. For example it is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentConnectorConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def payment_method_configuration(self):
        """Gets the payment_method_configuration of this PaymentConnectorConfiguration.

            

        :return: The payment_method_configuration of this PaymentConnectorConfiguration.
        :rtype: PaymentMethodConfiguration
        """
        return self._payment_method_configuration

    @payment_method_configuration.setter
    def payment_method_configuration(self, payment_method_configuration):
        """Sets the payment_method_configuration of this PaymentConnectorConfiguration.

            

        :param payment_method_configuration: The payment_method_configuration of this PaymentConnectorConfiguration.
        :type: PaymentMethodConfiguration
        """

        self._payment_method_configuration = payment_method_configuration
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentConnectorConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this PaymentConnectorConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentConnectorConfiguration.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentConnectorConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def priority(self):
        """Gets the priority of this PaymentConnectorConfiguration.

            The priority will define the order of choice of the connector configurations. The lower the value, the higher the priority is going to be. This value can also be a negative number in case you are adding a new configuration that you want to have a high priority and you dont want to change the priority of all the other configurations.

        :return: The priority of this PaymentConnectorConfiguration.
        :rtype: int
        """
        return self._priority

    @priority.setter
    def priority(self, priority):
        """Sets the priority of this PaymentConnectorConfiguration.

            The priority will define the order of choice of the connector configurations. The lower the value, the higher the priority is going to be. This value can also be a negative number in case you are adding a new configuration that you want to have a high priority and you dont want to change the priority of all the other configurations.

        :param priority: The priority of this PaymentConnectorConfiguration.
        :type: int
        """

        self._priority = priority
    
    @property
    def processor_configuration(self):
        """Gets the processor_configuration of this PaymentConnectorConfiguration.

            

        :return: The processor_configuration of this PaymentConnectorConfiguration.
        :rtype: PaymentProcessorConfiguration
        """
        return self._processor_configuration

    @processor_configuration.setter
    def processor_configuration(self, processor_configuration):
        """Sets the processor_configuration of this PaymentConnectorConfiguration.

            

        :param processor_configuration: The processor_configuration of this PaymentConnectorConfiguration.
        :type: PaymentProcessorConfiguration
        """

        self._processor_configuration = processor_configuration
    
    @property
    def state(self):
        """Gets the state of this PaymentConnectorConfiguration.

            

        :return: The state of this PaymentConnectorConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentConnectorConfiguration.

            

        :param state: The state of this PaymentConnectorConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this PaymentConnectorConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentConnectorConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentConnectorConfiguration.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentConnectorConfiguration.
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
        if issubclass(PaymentConnectorConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentConnectorConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
