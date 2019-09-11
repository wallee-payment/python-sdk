# coding: utf-8
import pprint
import six
from enum import Enum



class DocumentTemplateType:

    swagger_types = {
    
        'description': 'dict(str, str)',
        'feature': 'int',
        'group': 'DocumentTemplateTypeGroup',
        'id': 'int',
        'title': 'dict(str, str)',
    }

    attribute_map = {
        'description': 'description','feature': 'feature','group': 'group','id': 'id','title': 'title',
    }

    
    _description = None
    _feature = None
    _group = None
    _id = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.description = kwargs.get('description', None)
        self.feature = kwargs.get('feature', None)
        self.group = kwargs.get('group', None)
        self.id = kwargs.get('id', None)
        self.title = kwargs.get('title', None)
        

    
    @property
    def description(self):
        """Gets the description of this DocumentTemplateType.

            

        :return: The description of this DocumentTemplateType.
        :rtype: dict(str, str)
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this DocumentTemplateType.

            

        :param description: The description of this DocumentTemplateType.
        :type: dict(str, str)
        """

        self._description = description
    
    @property
    def feature(self):
        """Gets the feature of this DocumentTemplateType.

            

        :return: The feature of this DocumentTemplateType.
        :rtype: int
        """
        return self._feature

    @feature.setter
    def feature(self, feature):
        """Sets the feature of this DocumentTemplateType.

            

        :param feature: The feature of this DocumentTemplateType.
        :type: int
        """

        self._feature = feature
    
    @property
    def group(self):
        """Gets the group of this DocumentTemplateType.

            

        :return: The group of this DocumentTemplateType.
        :rtype: DocumentTemplateTypeGroup
        """
        return self._group

    @group.setter
    def group(self, group):
        """Sets the group of this DocumentTemplateType.

            

        :param group: The group of this DocumentTemplateType.
        :type: DocumentTemplateTypeGroup
        """

        self._group = group
    
    @property
    def id(self):
        """Gets the id of this DocumentTemplateType.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this DocumentTemplateType.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this DocumentTemplateType.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this DocumentTemplateType.
        :type: int
        """

        self._id = id
    
    @property
    def title(self):
        """Gets the title of this DocumentTemplateType.

            

        :return: The title of this DocumentTemplateType.
        :rtype: dict(str, str)
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this DocumentTemplateType.

            

        :param title: The title of this DocumentTemplateType.
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
        if issubclass(DocumentTemplateType, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, DocumentTemplateType):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
