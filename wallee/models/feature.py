# coding: utf-8
import pprint
import six
from enum import Enum



class Feature:

    swagger_types = {
    
        'beta': 'bool',
        'category': 'FeatureCategory',
        'description': 'dict(str, str)',
        'id': 'int',
        'logo_path': 'str',
        'name': 'dict(str, str)',
        'required_features': 'list[int]',
        'sort_order': 'int',
        'visible': 'bool',
    }

    attribute_map = {
        'beta': 'beta','category': 'category','description': 'description','id': 'id','logo_path': 'logoPath','name': 'name','required_features': 'requiredFeatures','sort_order': 'sortOrder','visible': 'visible',
    }

    
    _beta = None
    _category = None
    _description = None
    _id = None
    _logo_path = None
    _name = None
    _required_features = None
    _sort_order = None
    _visible = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.beta = kwargs.get('beta', None)
        self.category = kwargs.get('category', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.logo_path = kwargs.get('logo_path', None)
        self.name = kwargs.get('name', None)
        self.required_features = kwargs.get('required_features', None)
        self.sort_order = kwargs.get('sort_order', None)
        self.visible = kwargs.get('visible', None)
        

    
    @property
    def beta(self):
        """Gets the beta of this Feature.

            Whether the feature is in beta stage and there may still be some issues.

        :return: The beta of this Feature.
        :rtype: bool
        """
        return self._beta

    @beta.setter
    def beta(self, beta):
        """Sets the beta of this Feature.

            Whether the feature is in beta stage and there may still be some issues.

        :param beta: The beta of this Feature.
        :type: bool
        """

        self._beta = beta
    
    @property
    def category(self):
        """Gets the category of this Feature.

            The category that the feature belongs to.

        :return: The category of this Feature.
        :rtype: FeatureCategory
        """
        return self._category

    @category.setter
    def category(self, category):
        """Sets the category of this Feature.

            The category that the feature belongs to.

        :param category: The category of this Feature.
        :type: FeatureCategory
        """

        self._category = category
    
    @property
    def description(self):
        """Gets the description of this Feature.

            The localized description of the object.

        :return: The description of this Feature.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Feature.

            The localized description of the object.

        :param description: The description of this Feature.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this Feature.

            A unique identifier for the object.

        :return: The id of this Feature.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Feature.

            A unique identifier for the object.

        :param id: The id of this Feature.
        :type: int
        """

        self._id = id
    
    @property
    def logo_path(self):
        """Gets the logo_path of this Feature.

            The path to the feature's logo image.

        :return: The logo_path of this Feature.
        :rtype: str
        """
        return self._logo_path

    @logo_path.setter
    def logo_path(self, logo_path):
        """Sets the logo_path of this Feature.

            The path to the feature's logo image.

        :param logo_path: The logo_path of this Feature.
        :type: str
        """

        self._logo_path = logo_path
    
    @property
    def name(self):
        """Gets the name of this Feature.

            The localized name of the object.

        :return: The name of this Feature.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this Feature.

            The localized name of the object.

        :param name: The name of this Feature.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def required_features(self):
        """Gets the required_features of this Feature.

            The features that must be enabled for this feature to work properly.

        :return: The required_features of this Feature.
        :rtype: list[int]
        """
        return self._required_features

    @required_features.setter
    def required_features(self, required_features):
        """Sets the required_features of this Feature.

            The features that must be enabled for this feature to work properly.

        :param required_features: The required_features of this Feature.
        :type: list[int]
        """

        self._required_features = required_features
    
    @property
    def sort_order(self):
        """Gets the sort_order of this Feature.

            When listing features, they can be sorted by this number.

        :return: The sort_order of this Feature.
        :rtype: int
        """
        return self._sort_order

    @sort_order.setter
    def sort_order(self, sort_order):
        """Sets the sort_order of this Feature.

            When listing features, they can be sorted by this number.

        :param sort_order: The sort_order of this Feature.
        :type: int
        """

        self._sort_order = sort_order
    
    @property
    def visible(self):
        """Gets the visible of this Feature.

            

        :return: The visible of this Feature.
        :rtype: bool
        """
        return self._visible

    @visible.setter
    def visible(self, visible):
        """Sets the visible of this Feature.

            

        :param visible: The visible of this Feature.
        :type: bool
        """

        self._visible = visible
    

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
        if issubclass(Feature, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Feature):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
