# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifyTaxLine:

    swagger_types = {
    
        'fraction_rate': 'float',
        'id': 'int',
        'rate': 'float',
        'title': 'str',
        'version': 'int',
    }

    attribute_map = {
        'fraction_rate': 'fractionRate','id': 'id','rate': 'rate','title': 'title','version': 'version',
    }

    
    _fraction_rate = None
    _id = None
    _rate = None
    _title = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.fraction_rate = kwargs.get('fraction_rate', None)
        self.id = kwargs.get('id', None)
        self.rate = kwargs.get('rate', None)
        self.title = kwargs.get('title', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def fraction_rate(self):
        """Gets the fraction_rate of this ShopifyTaxLine.

            

        :return: The fraction_rate of this ShopifyTaxLine.
        :rtype: float
        """
        return self._fraction_rate

    @fraction_rate.setter
    def fraction_rate(self, fraction_rate):
        """Sets the fraction_rate of this ShopifyTaxLine.

            

        :param fraction_rate: The fraction_rate of this ShopifyTaxLine.
        :type: float
        """

        self._fraction_rate = fraction_rate
    
    @property
    def id(self):
        """Gets the id of this ShopifyTaxLine.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifyTaxLine.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifyTaxLine.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifyTaxLine.
        :type: int
        """

        self._id = id
    
    @property
    def rate(self):
        """Gets the rate of this ShopifyTaxLine.

            

        :return: The rate of this ShopifyTaxLine.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this ShopifyTaxLine.

            

        :param rate: The rate of this ShopifyTaxLine.
        :type: float
        """

        self._rate = rate
    
    @property
    def title(self):
        """Gets the title of this ShopifyTaxLine.

            

        :return: The title of this ShopifyTaxLine.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this ShopifyTaxLine.

            

        :param title: The title of this ShopifyTaxLine.
        :type: str
        """

        self._title = title
    
    @property
    def version(self):
        """Gets the version of this ShopifyTaxLine.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifyTaxLine.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifyTaxLine.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifyTaxLine.
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
        if issubclass(ShopifyTaxLine, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifyTaxLine):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
