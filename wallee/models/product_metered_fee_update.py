# coding: utf-8
import pprint
import six
from enum import Enum



class ProductMeteredFeeUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'component': 'int',
        'description': 'DatabaseTranslatedStringCreate',
        'metric': 'int',
        'name': 'DatabaseTranslatedStringCreate',
        'tier_pricing': 'ProductMeteredTierPricing',
    }

    attribute_map = {
        'id': 'id','version': 'version','component': 'component','description': 'description','metric': 'metric','name': 'name','tier_pricing': 'tierPricing',
    }

    
    _id = None
    _version = None
    _component = None
    _description = None
    _metric = None
    _name = None
    _tier_pricing = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.component = kwargs.get('component', None)
        self.description = kwargs.get('description', None)
        self.metric = kwargs.get('metric', None)
        self.name = kwargs.get('name', None)
        self.tier_pricing = kwargs.get('tier_pricing', None)
        

    
    @property
    def id(self):
        """Gets the id of this ProductMeteredFeeUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ProductMeteredFeeUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ProductMeteredFeeUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ProductMeteredFeeUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this ProductMeteredFeeUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ProductMeteredFeeUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ProductMeteredFeeUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ProductMeteredFeeUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def component(self):
        """Gets the component of this ProductMeteredFeeUpdate.

            

        :return: The component of this ProductMeteredFeeUpdate.
        :rtype: int
        """
        return self._component

    @component.setter
    def component(self, component):
        """Sets the component of this ProductMeteredFeeUpdate.

            

        :param component: The component of this ProductMeteredFeeUpdate.
        :type: int
        """

        self._component = component
    
    @property
    def description(self):
        """Gets the description of this ProductMeteredFeeUpdate.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :return: The description of this ProductMeteredFeeUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this ProductMeteredFeeUpdate.

            The description of a component fee describes the fee to the subscriber. The description may be shown in documents or on certain user interfaces.

        :param description: The description of this ProductMeteredFeeUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._description = description
    
    @property
    def metric(self):
        """Gets the metric of this ProductMeteredFeeUpdate.

            

        :return: The metric of this ProductMeteredFeeUpdate.
        :rtype: int
        """
        return self._metric

    @metric.setter
    def metric(self, metric):
        """Sets the metric of this ProductMeteredFeeUpdate.

            

        :param metric: The metric of this ProductMeteredFeeUpdate.
        :type: int
        """

        self._metric = metric
    
    @property
    def name(self):
        """Gets the name of this ProductMeteredFeeUpdate.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :return: The name of this ProductMeteredFeeUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this ProductMeteredFeeUpdate.

            The name of the fee should describe for the subscriber in few words for what the fee is for.

        :param name: The name of this ProductMeteredFeeUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._name = name
    
    @property
    def tier_pricing(self):
        """Gets the tier_pricing of this ProductMeteredFeeUpdate.

            The tier pricing determines the calculation method of the tiers. The prices of the different tiers can be applied in different ways. The tier pricing controls this calculation.

        :return: The tier_pricing of this ProductMeteredFeeUpdate.
        :rtype: ProductMeteredTierPricing
        """
        return self._tier_pricing

    @tier_pricing.setter
    def tier_pricing(self, tier_pricing):
        """Sets the tier_pricing of this ProductMeteredFeeUpdate.

            The tier pricing determines the calculation method of the tiers. The prices of the different tiers can be applied in different ways. The tier pricing controls this calculation.

        :param tier_pricing: The tier_pricing of this ProductMeteredFeeUpdate.
        :type: ProductMeteredTierPricing
        """

        self._tier_pricing = tier_pricing
    

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
        if issubclass(ProductMeteredFeeUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ProductMeteredFeeUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
