# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentProcessorConfiguration:

    swagger_types = {
    
        'application_managed': 'bool',
        'contract_id': 'int',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'planned_purge_date': 'datetime',
        'processor': 'int',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'application_managed': 'applicationManaged','contract_id': 'contractId','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','planned_purge_date': 'plannedPurgeDate','processor': 'processor','state': 'state','version': 'version',
    }

    
    _application_managed = None
    _contract_id = None
    _id = None
    _linked_space_id = None
    _name = None
    _planned_purge_date = None
    _processor = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.application_managed = kwargs.get('application_managed', None)
        self.contract_id = kwargs.get('contract_id', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.processor = kwargs.get('processor', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def application_managed(self):
        """Gets the application_managed of this PaymentProcessorConfiguration.

            The configuration is managed by the application and cannot be changed via the user interface.

        :return: The application_managed of this PaymentProcessorConfiguration.
        :rtype: bool
        """
        return self._application_managed

    @application_managed.setter
    def application_managed(self, application_managed):
        """Sets the application_managed of this PaymentProcessorConfiguration.

            The configuration is managed by the application and cannot be changed via the user interface.

        :param application_managed: The application_managed of this PaymentProcessorConfiguration.
        :type: bool
        """

        self._application_managed = application_managed
    
    @property
    def contract_id(self):
        """Gets the contract_id of this PaymentProcessorConfiguration.

            The contract links the processor configuration with the contract that is used to process payments.

        :return: The contract_id of this PaymentProcessorConfiguration.
        :rtype: int
        """
        return self._contract_id

    @contract_id.setter
    def contract_id(self, contract_id):
        """Sets the contract_id of this PaymentProcessorConfiguration.

            The contract links the processor configuration with the contract that is used to process payments.

        :param contract_id: The contract_id of this PaymentProcessorConfiguration.
        :type: int
        """

        self._contract_id = contract_id
    
    @property
    def id(self):
        """Gets the id of this PaymentProcessorConfiguration.

            A unique identifier for the object.

        :return: The id of this PaymentProcessorConfiguration.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentProcessorConfiguration.

            A unique identifier for the object.

        :param id: The id of this PaymentProcessorConfiguration.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentProcessorConfiguration.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this PaymentProcessorConfiguration.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentProcessorConfiguration.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this PaymentProcessorConfiguration.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentProcessorConfiguration.

            The processor configuration name is used internally to identify a specific processor configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :return: The name of this PaymentProcessorConfiguration.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentProcessorConfiguration.

            The processor configuration name is used internally to identify a specific processor configuration. For example the name is used within search fields and hence it should be distinct and descriptive.

        :param name: The name of this PaymentProcessorConfiguration.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this PaymentProcessorConfiguration.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :return: The planned_purge_date of this PaymentProcessorConfiguration.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this PaymentProcessorConfiguration.

            The date and time when the object is planned to be permanently removed. If the value is empty, the object will not be removed.

        :param planned_purge_date: The planned_purge_date of this PaymentProcessorConfiguration.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def processor(self):
        """Gets the processor of this PaymentProcessorConfiguration.

            A processor handles the connection to a third part company (a Payment Service Provider) that technically manages the transaction and therefore processes the payment. For the same processor multiple processor configuration can be setup.

        :return: The processor of this PaymentProcessorConfiguration.
        :rtype: int
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this PaymentProcessorConfiguration.

            A processor handles the connection to a third part company (a Payment Service Provider) that technically manages the transaction and therefore processes the payment. For the same processor multiple processor configuration can be setup.

        :param processor: The processor of this PaymentProcessorConfiguration.
        :type: int
        """

        self._processor = processor
    
    @property
    def state(self):
        """Gets the state of this PaymentProcessorConfiguration.

            The object's current state.

        :return: The state of this PaymentProcessorConfiguration.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentProcessorConfiguration.

            The object's current state.

        :param state: The state of this PaymentProcessorConfiguration.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this PaymentProcessorConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :return: The version of this PaymentProcessorConfiguration.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentProcessorConfiguration.

            The version is used for optimistic locking and incremented whenever the object is updated.

        :param version: The version of this PaymentProcessorConfiguration.
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
        if issubclass(PaymentProcessorConfiguration, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentProcessorConfiguration):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
