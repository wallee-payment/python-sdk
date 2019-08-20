# coding: utf-8
import pprint
import six
from enum import Enum
from . import AbstractSubscriptionMetricUpdate


class SubscriptionMetricCreate(AbstractSubscriptionMetricUpdate):

    swagger_types = {
        'description': 'DatabaseTranslatedStringCreate',
        'name': 'DatabaseTranslatedStringCreate',
        'type': 'int',
    }

    attribute_map = {
        'description': 'description',
        'name': 'name',
        'type': 'type',
    }

    
    _description = None
    _name = None
    _type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.name = kwargs.get('name')
        self.type = kwargs.get('type')

        super().__init__(**kwargs)
        self.swagger_types.update(super().swagger_types)
        self.attribute_map.update(super().attribute_map)

    @property
    def description(self):
        """Gets the description of this SubscriptionMetricCreate.

            

        :return: The description of this SubscriptionMetricCreate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriptionMetricCreate.

            

        :param description: The description of this SubscriptionMetricCreate.
        :type: DatabaseTranslatedStringCreate
        """

        self._description = description

    @property
    def name(self):
        """Gets the name of this SubscriptionMetricCreate.

            

        :return: The name of this SubscriptionMetricCreate.
        :rtype: DatabaseTranslatedStringCreate
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this SubscriptionMetricCreate.

            

        :param name: The name of this SubscriptionMetricCreate.
        :type: DatabaseTranslatedStringCreate
        """
        if name is None:
            raise ValueError("Invalid value for `name`, must not be `None`")

        self._name = name

    @property
    def type(self):
        """Gets the type of this SubscriptionMetricCreate.

            

        :return: The type of this SubscriptionMetricCreate.
        :rtype: int
        """
        return self._type

    @type.setter
    def type(self, type):
        """Sets the type of this SubscriptionMetricCreate.

            

        :param type: The type of this SubscriptionMetricCreate.
        :type: int
        """
        if type is None:
            raise ValueError("Invalid value for `type`, must not be `None`")

        self._type = type

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
        if issubclass(SubscriptionMetricCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriptionMetricCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
