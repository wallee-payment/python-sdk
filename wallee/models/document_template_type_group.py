# coding: utf-8
import pprint
import six
from enum import Enum



class DocumentTemplateTypeGroup:

    swagger_types = {
    
        'id': 'int',
        'title': 'dict(str, str)',
    }

    attribute_map = {
        'id': 'id','title': 'title',
    }

    
    _id = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        

    
    @property
    def id(self):
        """Gets the id of this DocumentTemplateTypeGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DocumentTemplateTypeGroup.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentTemplateTypeGroup.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DocumentTemplateTypeGroup.
        :type: int
        """

        self._id = id
    
    @property
    def title(self):
        """Gets the title of this DocumentTemplateTypeGroup.

            

        :return: The title of this DocumentTemplateTypeGroup.
        :rtype: dict(str, str)
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentTemplateTypeGroup.

            

        :param title: The title of this DocumentTemplateTypeGroup.
        :type: dict(str, str)
        """

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
        if issubclass(DocumentTemplateTypeGroup, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DocumentTemplateTypeGroup):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
