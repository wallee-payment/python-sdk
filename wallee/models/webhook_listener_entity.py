# coding: utf-8
import pprint
import six
from enum import Enum



class WebhookListenerEntity:

    swagger_types = {
    
        'id': 'int',
        'name': 'dict(str, str)',
        'technical_name': 'str',
    }

    attribute_map = {
        'id': 'id','name': 'name','technical_name': 'technicalName',
    }

    
    _id = None
    _name = None
    _technical_name = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.name = kwargs.get('name', None)
        self.technical_name = kwargs.get('technical_name', None)
        

    
    @property
    def id(self):
        """Gets the id of this WebhookListenerEntity.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this WebhookListenerEntity.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookListenerEntity.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this WebhookListenerEntity.
        :type: int
        """

        self._id = id
    
    @property
    def name(self):
        """Gets the name of this WebhookListenerEntity.

            

        :return: The name of this WebhookListenerEntity.
        :rtype: dict(str, str)
        """
        return self._name

    @name.setter
    def name(self, name):
        """Sets the name of this WebhookListenerEntity.

            

        :param name: The name of this WebhookListenerEntity.
        :type: dict(str, str)
        """

        self._name = name
    
    @property
    def technical_name(self):
        """Gets the technical_name of this WebhookListenerEntity.

            

        :return: The technical_name of this WebhookListenerEntity.
        :rtype: str
        """
        return self._technical_name

    @technical_name.setter
    def technical_name(self, technical_name):
        """Sets the technical_name of this WebhookListenerEntity.

            

        :param technical_name: The technical_name of this WebhookListenerEntity.
        :type: str
        """

        self._technical_name = technical_name
    

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
        if issubclass(WebhookListenerEntity, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebhookListenerEntity):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
