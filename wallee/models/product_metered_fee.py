# coding: utf-8
import pprint
import six
from enum import Enum



class ProductMeteredFee:

    swagger_types = {
    
        'component': 'SubscriptionProductComponent',
        'description': 'DatabaseTranslatedString',
        'id': 'int',
        'linked_space_id': 'int',
        'metric': 'SubscriptionMetric',
        'name': 'DatabaseTranslatedString',
        'tier_pricing': 'ProductMeteredTierPricing',
        'type': 'ProductFeeType',
        'version': 'int',
    }

    attribute_map = {
        'component': 'component','description': 'description','id': 'id','linked_space_id': 'linkedSpaceId','metric': 'metric','name': 'name','tier_pricing': 'tierPricing','type': 'type','version': 'version',
    }

    
    _component = None
    _description = None
    _id = None
    _linked_space_id = None
    _metric = None
    _name = None
    _tier_pricing = None
    _type = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.component = kwargs.get('component', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.metric = kwargs.get('metric', None)
        self.name = kwargs.get('name', None)
        self.tier_pricing = kwargs.get('tier_pricing', None)
        self.type = kwargs.get('type', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def component(self):
        """Gets the component of this ProductMeteredFee.

            

        :return: The component of this ProductMeteredFee.
        :rtype: SubscriptionProductComponent
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductMeteredFee.

            

        :param component: The component of this ProductMeteredFee.
        :type: SubscriptionProductComponent
        """

        self._component = component
    
    @property
    def description(self):
        """Gets the description of this ProductMeteredFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :return: The description of this ProductMeteredFee.
        :rtype: DatabaseTranslatedString
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductMeteredFee.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :param description: The description of this ProductMeteredFee.
        :type: DatabaseTranslatedString
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this ProductMeteredFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductMeteredFee.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductMeteredFee.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductMeteredFee.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ProductMeteredFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ProductMeteredFee.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ProductMeteredFee.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ProductMeteredFee.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def metric(self):
        """Gets the metric of this ProductMeteredFee.

            

        :return: The metric of this ProductMeteredFee.
        :rtype: SubscriptionMetric
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ProductMeteredFee.

            

        :param metric: The metric of this ProductMeteredFee.
        :type: SubscriptionMetric
        """

        self._metric = metric
    
    @property
    def name(self):
        """Gets the name of this ProductMeteredFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :return: The name of this ProductMeteredFee.
        :rtype: DatabaseTranslatedString
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductMeteredFee.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :param name: The name of this ProductMeteredFee.
        :type: DatabaseTranslatedString
        """

        self._name = name
    
    @property
    def tier_pricing(self):
        """Gets the tier_pricing of this ProductMeteredFee.

            The tier pricing determines the calculation method of the tiers. The prices of the different tiers can be applied in different ways. The tier pricing controls this calculation.

        :return: The tier_pricing of this ProductMeteredFee.
        :rtype: ProductMeteredTierPricing
        """
        return self._tier_pricing

    @tier_pricing.setter
    def tier_pricing(self, tier_pricing):
        """Sets the tier_pricing of this ProductMeteredFee.

            The tier pricing determines the calculation method of the tiers. The prices of the different tiers can be applied in different ways. The tier pricing controls this calculation.

        :param tier_pricing: The tier_pricing of this ProductMeteredFee.
        :type: ProductMeteredTierPricing
        """

        self._tier_pricing = tier_pricing
    
    @property
    def type(self):
        """Gets the type of this ProductMeteredFee.

            

        :return: The type of this ProductMeteredFee.
        :rtype: ProductFeeType
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this ProductMeteredFee.

            

        :param type: The type of this ProductMeteredFee.
        :type: ProductFeeType
        """

        self._type = type
    
    @property
    def version(self):
        """Gets the version of this ProductMeteredFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductMeteredFee.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductMeteredFee.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductMeteredFee.
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
        if issubclass(ProductMeteredFee, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductMeteredFee):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
