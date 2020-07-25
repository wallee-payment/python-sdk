# coding: utf-8
import pprint
import six
from enum import Enum



class Tax:

    swagger_types = {
    
        'rate': 'float',
        'title': 'str',
    }

    attribute_map = {
        'rate': 'rate','title': 'title',
    }

    
    _rate = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.rate = kwargs.get('rate', None)
        self.title = kwargs.get('title', None)
        

    
    @property
    def rate(self):
        """Gets the rate of this Tax.

            

        :return: The rate of this Tax.
        :rtype: float
        """
        return self._rate

    @rate.setter
    def rate(self, rate):
        """Sets the rate of this Tax.

            

        :param rate: The rate of this Tax.
        :type: float
        """

        self._rate = rate
    
    @property
    def title(self):
        """Gets the title of this Tax.

            

        :return: The title of this Tax.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this Tax.

            

        :param title: The title of this Tax.
        :type: str
        """
        if title is not None and len(title) > 40:
            raise ValueError("Invalid value for `title`, length must be less than or equal to `40`")
        if title is not None and len(title) < 2:
            raise ValueError("Invalid value for `title`, length must be greater than or equal to `2`")

        self._title = title
    

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
        if issubclass(Tax, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Tax):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
