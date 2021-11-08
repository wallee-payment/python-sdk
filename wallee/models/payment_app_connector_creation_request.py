# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentAppConnectorCreationRequest:

    swagger_types = {
    
        'authorization_timeout_in_minutes': 'int',
        'completion_configuration': 'PaymentAppCompletionConfigurationCreate',
        'connector': 'int',
        'external_id': 'str',
        'name': 'str',
        'payment_page_endpoint': 'str',
        'processor_external_id': 'str',
        'refund_configuration': 'PaymentAppRefundConfigurationCreate',
    }

    attribute_map = {
        'authorization_timeout_in_minutes': 'authorizationTimeoutInMinutes','completion_configuration': 'completionConfiguration','connector': 'connector','external_id': 'externalId','name': 'name','payment_page_endpoint': 'paymentPageEndpoint','processor_external_id': 'processorExternalId','refund_configuration': 'refundConfiguration',
    }

    
    _authorization_timeout_in_minutes = None
    _completion_configuration = None
    _connector = None
    _external_id = None
    _name = None
    _payment_page_endpoint = None
    _processor_external_id = None
    _refund_configuration = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.authorization_timeout_in_minutes = kwargs.get('authorization_timeout_in_minutes')

        self.completion_configuration = kwargs.get('completion_configuration', None)
        self.connector = kwargs.get('connector')

        self.external_id = kwargs.get('external_id')

        self.name = kwargs.get('name')

        self.payment_page_endpoint = kwargs.get('payment_page_endpoint')

        self.processor_external_id = kwargs.get('processor_external_id')

        self.refund_configuration = kwargs.get('refund_configuration', None)
        

    
    @property
    def authorization_timeout_in_minutes(self):
        """Gets the authorization_timeout_in_minutes of this PaymentAppConnectorCreationRequest.

            When the transaction is not authorized within this timeout the transaction is considered as failed.

        :return: The authorization_timeout_in_minutes of this PaymentAppConnectorCreationRequest.
        :rtype: int
        """
        return self._authorization_timeout_in_minutes

    @authorization_timeout_in_minutes.setter
    def authorization_timeout_in_minutes(self, authorization_timeout_in_minutes):
        """Sets the authorization_timeout_in_minutes of this PaymentAppConnectorCreationRequest.

            When the transaction is not authorized within this timeout the transaction is considered as failed.

        :param authorization_timeout_in_minutes: The authorization_timeout_in_minutes of this PaymentAppConnectorCreationRequest.
        :type: int
        """
        if authorization_timeout_in_minutes is None:
            raise ValueError("Invalid value for `authorization_timeout_in_minutes`, must not be `None`")

        self._authorization_timeout_in_minutes = authorization_timeout_in_minutes
    
    @property
    def completion_configuration(self):
        """Gets the completion_configuration of this PaymentAppConnectorCreationRequest.

            The completion configuration allows the connector to support deferred completions on a transaction. If it is not provided the connector will not process transactions in deferred mode.

        :return: The completion_configuration of this PaymentAppConnectorCreationRequest.
        :rtype: PaymentAppCompletionConfigurationCreate
        """
        return self._completion_configuration

    @completion_configuration.setter
    def completion_configuration(self, completion_configuration):
        """Sets the completion_configuration of this PaymentAppConnectorCreationRequest.

            The completion configuration allows the connector to support deferred completions on a transaction. If it is not provided the connector will not process transactions in deferred mode.

        :param completion_configuration: The completion_configuration of this PaymentAppConnectorCreationRequest.
        :type: PaymentAppCompletionConfigurationCreate
        """

        self._completion_configuration = completion_configuration
    
    @property
    def connector(self):
        """Gets the connector of this PaymentAppConnectorCreationRequest.

            The ID of the connector identifies which connector that should be linked with this web app connector. The connector defines the payment method.

        :return: The connector of this PaymentAppConnectorCreationRequest.
        :rtype: int
        """
        return self._connector

    @connector.setter
    def connector(self, connector):
        """Sets the connector of this PaymentAppConnectorCreationRequest.

            The ID of the connector identifies which connector that should be linked with this web app connector. The connector defines the payment method.

        :param connector: The connector of this PaymentAppConnectorCreationRequest.
        :type: int
        """
        if connector is None:
            raise ValueError("Invalid value for `connector`, must not be `None`")

        self._connector = connector
    
    @property
    def external_id(self):
        """Gets the external_id of this PaymentAppConnectorCreationRequest.

            The external ID identifies the connector within the external system. It has to be unique per processor external ID and for any subsequent update the same ID must be sent.

        :return: The external_id of this PaymentAppConnectorCreationRequest.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this PaymentAppConnectorCreationRequest.

            The external ID identifies the connector within the external system. It has to be unique per processor external ID and for any subsequent update the same ID must be sent.

        :param external_id: The external_id of this PaymentAppConnectorCreationRequest.
        :type: str
        """
        if external_id is None:
            raise ValueError("Invalid value for `external_id`, must not be `None`")
        if external_id is not None and len(external_id) > 40:
            raise ValueError("Invalid value for `external_id`, length must be less than or equal to `40`")
        if external_id is not None and len(external_id) < 1:
            raise ValueError("Invalid value for `external_id`, length must be greater than or equal to `1`")

        self._external_id = external_id
    
    @property
    def name(self):
        """Gets the name of this PaymentAppConnectorCreationRequest.

            The name of the connector will be displayed within the user interfaces that the merchant is interacting with.

        :return: The name of this PaymentAppConnectorCreationRequest.
        :rtype: str
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentAppConnectorCreationRequest.

            The name of the connector will be displayed within the user interfaces that the merchant is interacting with.

        :param name: The name of this PaymentAppConnectorCreationRequest.
        :type: str
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")
        if name is not None and len(name) > 100:
            raise ValueError("Invalid value for `name`, length must be less than or equal to `100`")

        self._name = name
    
    @property
    def payment_page_endpoint(self):
        """Gets the payment_page_endpoint of this PaymentAppConnectorCreationRequest.

            The payment page endpoint URL will be invoked by the buyer to carry out the authorization of the payment.

        :return: The payment_page_endpoint of this PaymentAppConnectorCreationRequest.
        :rtype: str
        """
        return self._payment_page_endpoint

    @payment_page_endpoint.setter
    def payment_page_endpoint(self, payment_page_endpoint):
        """Sets the payment_page_endpoint of this PaymentAppConnectorCreationRequest.

            The payment page endpoint URL will be invoked by the buyer to carry out the authorization of the payment.

        :param payment_page_endpoint: The payment_page_endpoint of this PaymentAppConnectorCreationRequest.
        :type: str
        """
        if payment_page_endpoint is None:
            raise ValueError("Invalid value for `payment_page_endpoint`, must not be `None`")

        self._payment_page_endpoint = payment_page_endpoint
    
    @property
    def processor_external_id(self):
        """Gets the processor_external_id of this PaymentAppConnectorCreationRequest.

            The external ID of the processor identifies the processor to which this connector belongs to. The processor cannot be changed once it has been set on a connector.

        :return: The processor_external_id of this PaymentAppConnectorCreationRequest.
        :rtype: str
        """
        return self._processor_external_id

    @processor_external_id.setter
    def processor_external_id(self, processor_external_id):
        """Sets the processor_external_id of this PaymentAppConnectorCreationRequest.

            The external ID of the processor identifies the processor to which this connector belongs to. The processor cannot be changed once it has been set on a connector.

        :param processor_external_id: The processor_external_id of this PaymentAppConnectorCreationRequest.
        :type: str
        """
        if processor_external_id is None:
            raise ValueError("Invalid value for `processor_external_id`, must not be `None`")
        if processor_external_id is not None and len(processor_external_id) > 40:
            raise ValueError("Invalid value for `processor_external_id`, length must be less than or equal to `40`")
        if processor_external_id is not None and len(processor_external_id) < 1:
            raise ValueError("Invalid value for `processor_external_id`, length must be greater than or equal to `1`")

        self._processor_external_id = processor_external_id
    
    @property
    def refund_configuration(self):
        """Gets the refund_configuration of this PaymentAppConnectorCreationRequest.

            The refund configuration allows the connector to support refunds on transactions. In case no refund configuration is provided the connector will not support refunds.

        :return: The refund_configuration of this PaymentAppConnectorCreationRequest.
        :rtype: PaymentAppRefundConfigurationCreate
        """
        return self._refund_configuration

    @refund_configuration.setter
    def refund_configuration(self, refund_configuration):
        """Sets the refund_configuration of this PaymentAppConnectorCreationRequest.

            The refund configuration allows the connector to support refunds on transactions. In case no refund configuration is provided the connector will not support refunds.

        :param refund_configuration: The refund_configuration of this PaymentAppConnectorCreationRequest.
        :type: PaymentAppRefundConfigurationCreate
        """

        self._refund_configuration = refund_configuration
    

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
        if issubclass(PaymentAppConnectorCreationRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentAppConnectorCreationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
