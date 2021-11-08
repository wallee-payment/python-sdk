# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppConnector:

    swagger_types = {
    
        'authorization_timeout': 'str',
        'completion_configuration': 'PaymentAppCompletionConfiguration',
        'connector_configuration': 'PaymentConnectorConfiguration',
        'created_on': 'datetime',
        'external_id': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'name': 'str',
        'payment_page_endpoint': 'str',
        'processor': 'PaymentAppProcessor',
        'refund_configuration': 'PaymentAppRefundConfiguration',
        'state': 'PaymentAppConnectorState',
        'updated_on': 'datetime',
        'version': 'int',
    }

    attribute_map = {
        'authorization_timeout': 'authorizationTimeout','completion_configuration': 'completionConfiguration','connector_configuration': 'connectorConfiguration','created_on': 'createdOn','external_id': 'externalId','id': 'id','linked_space_id': 'linkedSpaceId','name': 'name','payment_page_endpoint': 'paymentPageEndpoint','processor': 'processor','refund_configuration': 'refundConfiguration','state': 'state','updated_on': 'updatedOn','version': 'version',
    }

    
    _authorization_timeout = None
    _completion_configuration = None
    _connector_configuration = None
    _created_on = None
    _external_id = None
    _id = None
    _linked_space_id = None
    _name = None
    _payment_page_endpoint = None
    _processor = None
    _refund_configuration = None
    _state = None
    _updated_on = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.authorization_timeout = kwargs.get('authorization_timeout', None)
        self.completion_configuration = kwargs.get('completion_configuration', None)
        self.connector_configuration = kwargs.get('connector_configuration', None)
        self.created_on = kwargs.get('created_on', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.name = kwargs.get('name', None)
        self.payment_page_endpoint = kwargs.get('payment_page_endpoint', None)
        self.processor = kwargs.get('processor', None)
        self.refund_configuration = kwargs.get('refund_configuration', None)
        self.state = kwargs.get('state', None)
        self.updated_on = kwargs.get('updated_on', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def authorization_timeout(self):
        """Gets the authorization_timeout of this PaymentAppConnector.

            

        :return: The authorization_timeout of this PaymentAppConnector.
        :rtype: str
        """
        return self._authorization_timeout

    @authorization_timeout.setter
    def authorization_timeout(self, authorization_timeout):
        """Sets the authorization_timeout of this PaymentAppConnector.

            

        :param authorization_timeout: The authorization_timeout of this PaymentAppConnector.
        :type: str
        """

        self._authorization_timeout = authorization_timeout
    
    @property
    def completion_configuration(self):
        """Gets the completion_configuration of this PaymentAppConnector.

            The completion configuration defines how the deferred completion is processed. If it is not present it means that deferred completion is not supported by this connector.

        :return: The completion_configuration of this PaymentAppConnector.
        :rtype: PaymentAppCompletionConfiguration
        """
        return self._completion_configuration

    @completion_configuration.setter
    def completion_configuration(self, completion_configuration):
        """Sets the completion_configuration of this PaymentAppConnector.

            The completion configuration defines how the deferred completion is processed. If it is not present it means that deferred completion is not supported by this connector.

        :param completion_configuration: The completion_configuration of this PaymentAppConnector.
        :type: PaymentAppCompletionConfiguration
        """

        self._completion_configuration = completion_configuration
    
    @property
    def connector_configuration(self):
        """Gets the connector_configuration of this PaymentAppConnector.

            The connector configuration references the configuration that was created as part of this connector within the space. The connector configuration is referenced within transactions created with this connector.

        :return: The connector_configuration of this PaymentAppConnector.
        :rtype: PaymentConnectorConfiguration
        """
        return self._connector_configuration

    @connector_configuration.setter
    def connector_configuration(self, connector_configuration):
        """Sets the connector_configuration of this PaymentAppConnector.

            The connector configuration references the configuration that was created as part of this connector within the space. The connector configuration is referenced within transactions created with this connector.

        :param connector_configuration: The connector_configuration of this PaymentAppConnector.
        :type: PaymentConnectorConfiguration
        """

        self._connector_configuration = connector_configuration
    
    @property
    def created_on(self):
        """Gets the created_on of this PaymentAppConnector.

            The created on date indicates when the connector was added.

        :return: The created_on of this PaymentAppConnector.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this PaymentAppConnector.

            The created on date indicates when the connector was added.

        :param created_on: The created_on of this PaymentAppConnector.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentAppConnector.

            The external ID corresponds to the ID provided during inserting of the processor.

        :return: The external_id of this PaymentAppConnector.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentAppConnector.

            The external ID corresponds to the ID provided during inserting of the processor.

        :param external_id: The external_id of this PaymentAppConnector.
        :type: str
        """
        if external_id is not None and len(external_id) > 40:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `40`")

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this PaymentAppConnector.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentAppConnector.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentAppConnector.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentAppConnector.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentAppConnector.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this PaymentAppConnector.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentAppConnector.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this PaymentAppConnector.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def name(self):
        """Gets the name of this PaymentAppConnector.

            The name of the connector will be displayed within the user interfaces that the merchant is interacting with.

        :return: The name of this PaymentAppConnector.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentAppConnector.

            The name of the connector will be displayed within the user interfaces that the merchant is interacting with.

        :param name: The name of this PaymentAppConnector.
        :type: str
        """
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def payment_page_endpoint(self):
        """Gets the payment_page_endpoint of this PaymentAppConnector.

            The payment page endpoint is invoked to process the transaction. The endpoint is defined by the external service provider.

        :return: The payment_page_endpoint of this PaymentAppConnector.
        :rtype: str
        """
        return self._payment_page_endpoint

    @payment_page_endpoint.setter
    def payment_page_endpoint(self, payment_page_endpoint):
        """Sets the payment_page_endpoint of this PaymentAppConnector.

            The payment page endpoint is invoked to process the transaction. The endpoint is defined by the external service provider.

        :param payment_page_endpoint: The payment_page_endpoint of this PaymentAppConnector.
        :type: str
        """

        self._payment_page_endpoint = payment_page_endpoint
    
    @property
    def processor(self):
        """Gets the processor of this PaymentAppConnector.

            The processor references the app processor to which this connector belongs to. The relationship is established during the creation of the connector.

        :return: The processor of this PaymentAppConnector.
        :rtype: PaymentAppProcessor
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this PaymentAppConnector.

            The processor references the app processor to which this connector belongs to. The relationship is established during the creation of the connector.

        :param processor: The processor of this PaymentAppConnector.
        :type: PaymentAppProcessor
        """

        self._processor = processor
    
    @property
    def refund_configuration(self):
        """Gets the refund_configuration of this PaymentAppConnector.

            The refund configuration defines how refunds are processed. If it is not present it means that refunds are not supported by this connector.

        :return: The refund_configuration of this PaymentAppConnector.
        :rtype: PaymentAppRefundConfiguration
        """
        return self._refund_configuration

    @refund_configuration.setter
    def refund_configuration(self, refund_configuration):
        """Sets the refund_configuration of this PaymentAppConnector.

            The refund configuration defines how refunds are processed. If it is not present it means that refunds are not supported by this connector.

        :param refund_configuration: The refund_configuration of this PaymentAppConnector.
        :type: PaymentAppRefundConfiguration
        """

        self._refund_configuration = refund_configuration
    
    @property
    def state(self):
        """Gets the state of this PaymentAppConnector.

            

        :return: The state of this PaymentAppConnector.
        :rtype: PaymentAppConnectorState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this PaymentAppConnector.

            

        :param state: The state of this PaymentAppConnector.
        :type: PaymentAppConnectorState
        """

        self._state = state
    
    @property
    def updated_on(self):
        """Gets the updated_on of this PaymentAppConnector.

            The updated on date indicates when the last time the connector was updated on.

        :return: The updated_on of this PaymentAppConnector.
        :rtype: datetime
        """
        return self._updated_on

    @updated_on.setter
    def updated_on(self, updated_on):
        """Sets the updated_on of this PaymentAppConnector.

            The updated on date indicates when the last time the connector was updated on.

        :param updated_on: The updated_on of this PaymentAppConnector.
        :type: datetime
        """

        self._updated_on = updated_on
    
    @property
    def version(self):
        """Gets the version of this PaymentAppConnector.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this PaymentAppConnector.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this PaymentAppConnector.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this PaymentAppConnector.
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
        if issubclass(PaymentAppConnector, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
