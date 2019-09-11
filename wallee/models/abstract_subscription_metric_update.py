# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractSubscriptionMetricUpdate:

    swagger_types = {
    
        'description': 'DatabaseTranslatedStringCreate',
        'name': 'DatabaseTranslatedStringCreate',
    }

    attribute_map = {
        'description': 'description','name': 'name',
    }

    
    _description = None
    _name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.name = kwargs.get('name', None)
        

    
    @property
    def description(self):
        """Gets the description of this AbstractSubscriptionMetricUpdate.

            

        :return: The description of this AbstractSubscriptionMetricUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this AbstractSubscriptionMetricUpdate.

            

        :param description: The description of this AbstractSubscriptionMetricUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._description = description
    
    @property
    def name(self):
        """Gets the name of this AbstractSubscriptionMetricUpdate.

            

        :return: The name of this AbstractSubscriptionMetricUpdate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this AbstractSubscriptionMetricUpdate.

            

        :param name: The name of this AbstractSubscriptionMetricUpdate.
        :type: DatabaseTranslatedStringCreate
        """

        self._name = name
    

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
        if issubclass(AbstractSubscriptionMetricUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractSubscriptionMetricUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
