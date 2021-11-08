# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppProcessor:

    swagger_types = {
    
        'configured_environment': 'ChargeAttemptEnvironment',
        'created_on': 'datetime',
        'documentation_url': 'str',
        'external_id': 'str',
        'id': 'int',
        'installation_id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'processor_configuration': 'PaymentProcessorConfiguration',
        'production_mode_url': 'str',
        'state': 'PaymentAppProcessorState',
        'svg_icon': 'str',
        'updated_on': 'datetime',
        'usable_in_production': 'bool',
        'usable_in_production_since': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'configured_environment': 'configuredEnvironment','created_on': 'createdOn','documentation_url': 'documentationUrl','external_id': 'externalId','id': 'id','installation_id': 'installationId','linked_space_id': 'linkedSpaceId','name': 'name','processor_configuration': 'processorConfiguration','production_mode_url': 'productionModeUrl','state': 'state','svg_icon': 'svgIcon','updated_on': 'updatedOn','usable_in_production': 'usableInProduction','usable_in_production_since': 'usableInProductionSince','version': 'version',
    }

    
    _configured_environment = None
    _created_on = None
    _documentation_url = None
    _external_id = None
    _id = None
    _installation_id = None
    _linked_space_id = None
    _name = None
    _processor_configuration = None
    _production_mode_url = None
    _state = None
    _svg_icon = None
    _updated_on = None
    _usable_in_production = None
    _usable_in_production_since = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.configured_environment = kwargs.get('configured_environment', None)
        self.created_on = kwargs.get('created_on', None)
        self.documentation_url = kwargs.get('documentation_url', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.installation_id = kwargs.get('installation_id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.processor_configuration = kwargs.get('processor_configuration', None)
        self.production_mode_url = kwargs.get('production_mode_url', None)
        self.state = kwargs.get('state', None)
        self.svg_icon = kwargs.get('svg_icon', None)
        self.updated_on = kwargs.get('updated_on', None)
        self.usable_in_production = kwargs.get('usable_in_production', None)
        self.usable_in_production_since = kwargs.get('usable_in_production_since', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def configured_environment(self):
        """Gets the configured_environment of this PaymentAppProcessor.

            

        :return: The configured_environment of this PaymentAppProcessor.
        :rtype: ChargeAttemptEnvironment
        """
        return self._configured_environment

    @configured_environment.setter
    def configured_environment(self, configured_environment):
        """Sets the configured_environment of this PaymentAppProcessor.

            

        :param configured_environment: The configured_environment of this PaymentAppProcessor.
        :type: ChargeAttemptEnvironment
        """

        self._configured_environment = configured_environment
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentAppProcessor.

            The created on date is the date when this processor has been added.

        :return: The created_on of this PaymentAppProcessor.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentAppProcessor.

            The created on date is the date when this processor has been added.

        :param created_on: The created_on of this PaymentAppProcessor.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def documentation_url(self):
        """Gets the documentation_url of this PaymentAppProcessor.

            The documentation URL points to a web site that describes how to configure and use the processor.

        :return: The documentation_url of this PaymentAppProcessor.
        :rtype: str
        """
        return self._documentation_url

    @documentation_url.setter
    def documentation_url(self, documentation_url):
        """Sets the documentation_url of this PaymentAppProcessor.

            The documentation URL points to a web site that describes how to configure and use the processor.

        :param documentation_url: The documentation_url of this PaymentAppProcessor.
        :type: str
        """

        self._documentation_url = documentation_url
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentAppProcessor.

            The external ID corresponds to the ID that was provided during creation of the processor.

        :return: The external_id of this PaymentAppProcessor.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentAppProcessor.

            The external ID corresponds to the ID that was provided during creation of the processor.

        :param external_id: The external_id of this PaymentAppProcessor.
        :type: str
        """
        if external_id is not None and len(external_id) > 40:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `40`")

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this PaymentAppProcessor.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentAppProcessor.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentAppProcessor.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentAppProcessor.
        :type: int
        """

        self._id = id
    
    @property
    def installation_id(self):
        """Gets the installation_id of this PaymentAppProcessor.

            The installation ID identifies the Web App installation.

        :return: The installation_id of this PaymentAppProcessor.
        :rtype: int
        """
        return self._installation_id

    @installation_id.setter
    def installation_id(self, installation_id):
        """Sets the installation_id of this PaymentAppProcessor.

            The installation ID identifies the Web App installation.

        :param installation_id: The installation_id of this PaymentAppProcessor.
        :type: int
        """

        self._installation_id = installation_id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentAppProcessor.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentAppProcessor.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentAppProcessor.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentAppProcessor.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentAppProcessor.

            The name of the processor will be displayed within the user interfaces that the merchant is interacting with.

        :return: The name of this PaymentAppProcessor.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentAppProcessor.

            The name of the processor will be displayed within the user interfaces that the merchant is interacting with.

        :param name: The name of this PaymentAppProcessor.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def processor_configuration(self):
        """Gets the processor_configuration of this PaymentAppProcessor.

            This processor configuration is created as part of the app processor. Any transaction created with the processor is linked with this processor configuration.

        :return: The processor_configuration of this PaymentAppProcessor.
        :rtype: PaymentProcessorConfiguration
        """
        return self._processor_configuration

    @processor_configuration.setter
    def processor_configuration(self, processor_configuration):
        """Sets the processor_configuration of this PaymentAppProcessor.

            This processor configuration is created as part of the app processor. Any transaction created with the processor is linked with this processor configuration.

        :param processor_configuration: The processor_configuration of this PaymentAppProcessor.
        :type: PaymentProcessorConfiguration
        """

        self._processor_configuration = processor_configuration
    
    @property
    def production_mode_url(self):
        """Gets the production_mode_url of this PaymentAppProcessor.

            When the user sets the processor into the production mode the user will be forwarded to this URL to configure the production environment. When no URL is provided no redirection will happen.

        :return: The production_mode_url of this PaymentAppProcessor.
        :rtype: str
        """
        return self._production_mode_url

    @production_mode_url.setter
    def production_mode_url(self, production_mode_url):
        """Sets the production_mode_url of this PaymentAppProcessor.

            When the user sets the processor into the production mode the user will be forwarded to this URL to configure the production environment. When no URL is provided no redirection will happen.

        :param production_mode_url: The production_mode_url of this PaymentAppProcessor.
        :type: str
        """

        self._production_mode_url = production_mode_url
    
    @property
    def state(self):
        """Gets the state of this PaymentAppProcessor.

            

        :return: The state of this PaymentAppProcessor.
        :rtype: PaymentAppProcessorState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentAppProcessor.

            

        :param state: The state of this PaymentAppProcessor.
        :type: PaymentAppProcessorState
        """

        self._state = state
    
    @property
    def svg_icon(self):
        """Gets the svg_icon of this PaymentAppProcessor.

            

        :return: The svg_icon of this PaymentAppProcessor.
        :rtype: str
        """
        return self._svg_icon

    @svg_icon.setter
    def svg_icon(self, svg_icon):
        """Sets the svg_icon of this PaymentAppProcessor.

            

        :param svg_icon: The svg_icon of this PaymentAppProcessor.
        :type: str
        """
        if svg_icon is not None and len(svg_icon) > 10000:
            raise ValueError("Invalid value for `svg_icon`, length must be less than or equal to `10000`")

        self._svg_icon = svg_icon
    
    @property
    def updated_on(self):
        """Gets the updated_on of this PaymentAppProcessor.

            The updated on date indicates when the last update on the processor occurred.

        :return: The updated_on of this PaymentAppProcessor.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this PaymentAppProcessor.

            The updated on date indicates when the last update on the processor occurred.

        :param updated_on: The updated_on of this PaymentAppProcessor.
        :type: datetime
        """

        self._updated_on = updated_on
    
    @property
    def usable_in_production(self):
        """Gets the usable_in_production of this PaymentAppProcessor.

            When the processor is ready to be used for transactions in the production environment this flag is set to true.

        :return: The usable_in_production of this PaymentAppProcessor.
        :rtype: bool
        """
        return self._usable_in_production

    @usable_in_production.setter
    def usable_in_production(self, usable_in_production):
        """Sets the usable_in_production of this PaymentAppProcessor.

            When the processor is ready to be used for transactions in the production environment this flag is set to true.

        :param usable_in_production: The usable_in_production of this PaymentAppProcessor.
        :type: bool
        """

        self._usable_in_production = usable_in_production
    
    @property
    def usable_in_production_since(self):
        """Gets the usable_in_production_since of this PaymentAppProcessor.

            

        :return: The usable_in_production_since of this PaymentAppProcessor.
        :rtype: datetime
        """
        return self._usable_in_production_since

    @usable_in_production_since.setter
    def usable_in_production_since(self, usable_in_production_since):
        """Sets the usable_in_production_since of this PaymentAppProcessor.

            

        :param usable_in_production_since: The usable_in_production_since of this PaymentAppProcessor.
        :type: datetime
        """

        self._usable_in_production_since = usable_in_production_since
    
    @property
    def version(self):
        """Gets the version of this PaymentAppProcessor.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentAppProcessor.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentAppProcessor.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentAppProcessor.
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
        if issubclass(PaymentAppProcessor, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppProcessor):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
