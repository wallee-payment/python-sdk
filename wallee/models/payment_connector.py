# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentConnector:

    swagger_types = {
    
        'data_collection_type': 'DataCollectionType',
        'deprecated': 'bool',
        'deprecation_reason': 'dict(str, str)',
        'description': 'dict(str, str)',
        'feature': 'Feature',
        'id': 'int',
        'name': 'dict(str, str)',
        'payment_method': 'int',
        'payment_method_brand': 'PaymentMethodBrand',
        'primary_risk_taker': 'PaymentPrimaryRiskTaker',
        'processor': 'int',
        'supported_customers_presences': 'list[CustomersPresence]',
        'supported_features': 'list[int]',
    }

    attribute_map = {
        'data_collection_type': 'dataCollectionType','deprecated': 'deprecated','deprecation_reason': 'deprecationReason','description': 'description','feature': 'feature','id': 'id','name': 'name','payment_method': 'paymentMethod','payment_method_brand': 'paymentMethodBrand','primary_risk_taker': 'primaryRiskTaker','processor': 'processor','supported_customers_presences': 'supportedCustomersPresences','supported_features': 'supportedFeatures',
    }

    
    _data_collection_type = None
    _deprecated = None
    _deprecation_reason = None
    _description = None
    _feature = None
    _id = None
    _name = None
    _payment_method = None
    _payment_method_brand = None
    _primary_risk_taker = None
    _processor = None
    _supported_customers_presences = None
    _supported_features = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.data_collection_type = kwargs.get('data_collection_type', None)
        self.deprecated = kwargs.get('deprecated', None)
        self.deprecation_reason = kwargs.get('deprecation_reason', None)
        self.description = kwargs.get('description', None)
        self.feature = kwargs.get('feature', None)
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.payment_method = kwargs.get('payment_method', None)
        self.payment_method_brand = kwargs.get('payment_method_brand', None)
        self.primary_risk_taker = kwargs.get('primary_risk_taker', None)
        self.processor = kwargs.get('processor', None)
        self.supported_customers_presences = kwargs.get('supported_customers_presences', None)
        self.supported_features = kwargs.get('supported_features', None)
        

    
    @property
    def data_collection_type(self):
        """Gets the data_collection_type of this PaymentConnector.

            

        :return: The data_collection_type of this PaymentConnector.
        :rtype: DataCollectionType
        """
        return self._data_collection_type

    @data_collection_type.setter
    def data_collection_type(self, data_collection_type):
        """Sets the data_collection_type of this PaymentConnector.

            

        :param data_collection_type: The data_collection_type of this PaymentConnector.
        :type: DataCollectionType
        """

        self._data_collection_type = data_collection_type
    
    @property
    def deprecated(self):
        """Gets the deprecated of this PaymentConnector.

            

        :return: The deprecated of this PaymentConnector.
        :rtype: bool
        """
        return self._deprecated

    @deprecated.setter
    def deprecated(self, deprecated):
        """Sets the deprecated of this PaymentConnector.

            

        :param deprecated: The deprecated of this PaymentConnector.
        :type: bool
        """

        self._deprecated = deprecated
    
    @property
    def deprecation_reason(self):
        """Gets the deprecation_reason of this PaymentConnector.

            

        :return: The deprecation_reason of this PaymentConnector.
        :rtype: dict(str, str)
        """
        return self._deprecation_reason

    @deprecation_reason.setter
    def deprecation_reason(self, deprecation_reason):
        """Sets the deprecation_reason of this PaymentConnector.

            

        :param deprecation_reason: The deprecation_reason of this PaymentConnector.
        :type: dict(str, str)
        """

        self._deprecation_reason = deprecation_reason
    
    @property
    def description(self):
        """Gets the description of this PaymentConnector.

            

        :return: The description of this PaymentConnector.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentConnector.

            

        :param description: The description of this PaymentConnector.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def feature(self):
        """Gets the feature of this PaymentConnector.

            

        :return: The feature of this PaymentConnector.
        :rtype: Feature
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this PaymentConnector.

            

        :param feature: The feature of this PaymentConnector.
        :type: Feature
        """

        self._feature = feature
    
    @property
    def id(self):
        """Gets the id of this PaymentConnector.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentConnector.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentConnector.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentConnector.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this PaymentConnector.

            

        :return: The name of this PaymentConnector.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentConnector.

            

        :param name: The name of this PaymentConnector.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentConnector.

            

        :return: The payment_method of this PaymentConnector.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentConnector.

            

        :param payment_method: The payment_method of this PaymentConnector.
        :type: int
        """

        self._payment_method = payment_method
    
    @property
    def payment_method_brand(self):
        """Gets the payment_method_brand of this PaymentConnector.

            

        :return: The payment_method_brand of this PaymentConnector.
        :rtype: PaymentMethodBrand
        """
        return self._payment_method_brand

    @payment_method_brand.setter
    def payment_method_brand(self, payment_method_brand):
        """Sets the payment_method_brand of this PaymentConnector.

            

        :param payment_method_brand: The payment_method_brand of this PaymentConnector.
        :type: PaymentMethodBrand
        """

        self._payment_method_brand = payment_method_brand
    
    @property
    def primary_risk_taker(self):
        """Gets the primary_risk_taker of this PaymentConnector.

            

        :return: The primary_risk_taker of this PaymentConnector.
        :rtype: PaymentPrimaryRiskTaker
        """
        return self._primary_risk_taker

    @primary_risk_taker.setter
    def primary_risk_taker(self, primary_risk_taker):
        """Sets the primary_risk_taker of this PaymentConnector.

            

        :param primary_risk_taker: The primary_risk_taker of this PaymentConnector.
        :type: PaymentPrimaryRiskTaker
        """

        self._primary_risk_taker = primary_risk_taker
    
    @property
    def processor(self):
        """Gets the processor of this PaymentConnector.

            

        :return: The processor of this PaymentConnector.
        :rtype: int
        """
        return self._processor

    @processor.setter
    def processor(self, processor):
        """Sets the processor of this PaymentConnector.

            

        :param processor: The processor of this PaymentConnector.
        :type: int
        """

        self._processor = processor
    
    @property
    def supported_customers_presences(self):
        """Gets the supported_customers_presences of this PaymentConnector.

            

        :return: The supported_customers_presences of this PaymentConnector.
        :rtype: list[CustomersPresence]
        """
        return self._supported_customers_presences

    @supported_customers_presences.setter
    def supported_customers_presences(self, supported_customers_presences):
        """Sets the supported_customers_presences of this PaymentConnector.

            

        :param supported_customers_presences: The supported_customers_presences of this PaymentConnector.
        :type: list[CustomersPresence]
        """

        self._supported_customers_presences = supported_customers_presences
    
    @property
    def supported_features(self):
        """Gets the supported_features of this PaymentConnector.

            

        :return: The supported_features of this PaymentConnector.
        :rtype: list[int]
        """
        return self._supported_features

    @supported_features.setter
    def supported_features(self, supported_features):
        """Sets the supported_features of this PaymentConnector.

            

        :param supported_features: The supported_features of this PaymentConnector.
        :type: list[int]
        """

        self._supported_features = supported_features
    

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
        if issubclass(PaymentConnector, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentConnector):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
