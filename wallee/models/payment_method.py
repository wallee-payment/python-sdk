# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentMethod:

    swagger_types = {
    
        'data_collection_types': 'list[DataCollectionType]',
        'description': 'dict(str, str)',
        'id': 'int',
        'image_path': 'str',
        'merchant_description': 'dict(str, str)',
        'name': 'dict(str, str)',
        'supported_currencies': 'list[str]',
    }

    attribute_map = {
        'data_collection_types': 'dataCollectionTypes','description': 'description','id': 'id','image_path': 'imagePath','merchant_description': 'merchantDescription','name': 'name','supported_currencies': 'supportedCurrencies',
    }

    
    _data_collection_types = None
    _description = None
    _id = None
    _image_path = None
    _merchant_description = None
    _name = None
    _supported_currencies = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.data_collection_types = kwargs.get('data_collection_types', None)
        self.description = kwargs.get('description', None)
        self.id = kwargs.get('id', None)
        self.image_path = kwargs.get('image_path', None)
        self.merchant_description = kwargs.get('merchant_description', None)
        self.name = kwargs.get('name', None)
        self.supported_currencies = kwargs.get('supported_currencies', None)
        

    
    @property
    def data_collection_types(self):
        """Gets the data_collection_types of this PaymentMethod.

            

        :return: The data_collection_types of this PaymentMethod.
        :rtype: list[DataCollectionType]
        """
        return self._data_collection_types

    @data_collection_types.setter
    def data_collection_types(self, data_collection_types):
        """Sets the data_collection_types of this PaymentMethod.

            

        :param data_collection_types: The data_collection_types of this PaymentMethod.
        :type: list[DataCollectionType]
        """

        self._data_collection_types = data_collection_types
    
    @property
    def description(self):
        """Gets the description of this PaymentMethod.

            

        :return: The description of this PaymentMethod.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentMethod.

            

        :param description: The description of this PaymentMethod.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def id(self):
        """Gets the id of this PaymentMethod.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentMethod.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethod.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentMethod.
        :type: int
        """

        self._id = id
    
    @property
    def image_path(self):
        """Gets the image_path of this PaymentMethod.

            

        :return: The image_path of this PaymentMethod.
        :rtype: str
        """
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        """Sets the image_path of this PaymentMethod.

            

        :param image_path: The image_path of this PaymentMethod.
        :type: str
        """

        self._image_path = image_path
    
    @property
    def merchant_description(self):
        """Gets the merchant_description of this PaymentMethod.

            

        :return: The merchant_description of this PaymentMethod.
        :rtype: dict(str, str)
        """
        return self._merchant_description

    @merchant_description.setter
    def merchant_description(self, merchant_description):
        """Sets the merchant_description of this PaymentMethod.

            

        :param merchant_description: The merchant_description of this PaymentMethod.
        :type: dict(str, str)
        """

        self._merchant_description = merchant_description
    
    @property
    def name(self):
        """Gets the name of this PaymentMethod.

            

        :return: The name of this PaymentMethod.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentMethod.

            

        :param name: The name of this PaymentMethod.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def supported_currencies(self):
        """Gets the supported_currencies of this PaymentMethod.

            

        :return: The supported_currencies of this PaymentMethod.
        :rtype: list[str]
        """
        return self._supported_currencies

    @supported_currencies.setter
    def supported_currencies(self, supported_currencies):
        """Sets the supported_currencies of this PaymentMethod.

            

        :param supported_currencies: The supported_currencies of this PaymentMethod.
        :type: list[str]
        """

        self._supported_currencies = supported_currencies
    

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
        if issubclass(PaymentMethod, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentMethod):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
