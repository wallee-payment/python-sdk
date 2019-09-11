# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentMethodBrand:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'gray_image_path': 'str',
        'id': 'int',
        'image_path': 'str',
        'name': 'dict(str, str)',
        'payment_method': 'int',
    }

    attribute_map = {
        'description': 'description','gray_image_path': 'grayImagePath','id': 'id','image_path': 'imagePath','name': 'name','payment_method': 'paymentMethod',
    }

    
    _description = None
    _gray_image_path = None
    _id = None
    _image_path = None
    _name = None
    _payment_method = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.gray_image_path = kwargs.get('gray_image_path', None)
        self.id = kwargs.get('id', None)
        self.image_path = kwargs.get('image_path', None)
        self.name = kwargs.get('name', None)
        self.payment_method = kwargs.get('payment_method', None)
        

    
    @property
    def description(self):
        """Gets the description of this PaymentMethodBrand.

            

        :return: The description of this PaymentMethodBrand.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this PaymentMethodBrand.

            

        :param description: The description of this PaymentMethodBrand.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def gray_image_path(self):
        """Gets the gray_image_path of this PaymentMethodBrand.

            

        :return: The gray_image_path of this PaymentMethodBrand.
        :rtype: str
        """
        return self._gray_image_path

    @gray_image_path.setter
    def gray_image_path(self, gray_image_path):
        """Sets the gray_image_path of this PaymentMethodBrand.

            

        :param gray_image_path: The gray_image_path of this PaymentMethodBrand.
        :type: str
        """

        self._gray_image_path = gray_image_path
    
    @property
    def id(self):
        """Gets the id of this PaymentMethodBrand.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this PaymentMethodBrand.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentMethodBrand.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this PaymentMethodBrand.
        :type: int
        """

        self._id = id
    
    @property
    def image_path(self):
        """Gets the image_path of this PaymentMethodBrand.

            

        :return: The image_path of this PaymentMethodBrand.
        :rtype: str
        """
        return self._image_path

    @image_path.setter
    def image_path(self, image_path):
        """Sets the image_path of this PaymentMethodBrand.

            

        :param image_path: The image_path of this PaymentMethodBrand.
        :type: str
        """

        self._image_path = image_path
    
    @property
    def name(self):
        """Gets the name of this PaymentMethodBrand.

            

        :return: The name of this PaymentMethodBrand.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this PaymentMethodBrand.

            

        :param name: The name of this PaymentMethodBrand.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def payment_method(self):
        """Gets the payment_method of this PaymentMethodBrand.

            

        :return: The payment_method of this PaymentMethodBrand.
        :rtype: int
        """
        return self._payment_method

    @payment_method.setter
    def payment_method(self, payment_method):
        """Sets the payment_method of this PaymentMethodBrand.

            

        :param payment_method: The payment_method of this PaymentMethodBrand.
        :type: int
        """

        self._payment_method = payment_method
    

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
        if issubclass(PaymentMethodBrand, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentMethodBrand):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
