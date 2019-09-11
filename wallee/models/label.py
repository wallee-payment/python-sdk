# coding: utf-8
import pprint
import six
from enum import Enum



class Label:

    swagger_types = {
    
        'content': 'object',
        'content_as_string': 'str',
        'descriptor': 'LabelDescriptor',
        'id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'content': 'content','content_as_string': 'contentAsString','descriptor': 'descriptor','id': 'id','version': 'version',
    }

    
    _content = None
    _content_as_string = None
    _descriptor = None
    _id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.content = kwargs.get('content', None)
        self.content_as_string = kwargs.get('content_as_string', None)
        self.descriptor = kwargs.get('descriptor', None)
        self.id = kwargs.get('id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def content(self):
        """Gets the content of this Label.

            

        :return: The content of this Label.
        :rtype: object
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this Label.

            

        :param content: The content of this Label.
        :type: object
        """

        self._content = content
    
    @property
    def content_as_string(self):
        """Gets the content_as_string of this Label.

            

        :return: The content_as_string of this Label.
        :rtype: str
        """
        return self._content_as_string

    @content_as_string.setter
    def content_as_string(self, content_as_string):
        """Sets the content_as_string of this Label.

            

        :param content_as_string: The content_as_string of this Label.
        :type: str
        """

        self._content_as_string = content_as_string
    
    @property
    def descriptor(self):
        """Gets the descriptor of this Label.

            

        :return: The descriptor of this Label.
        :rtype: LabelDescriptor
        """
        return self._descriptor

    @descriptor.setter
    def descriptor(self, descriptor):
        """Sets the descriptor of this Label.

            

        :param descriptor: The descriptor of this Label.
        :type: LabelDescriptor
        """

        self._descriptor = descriptor
    
    @property
    def id(self):
        """Gets the id of this Label.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Label.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Label.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Label.
        :type: int
        """

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this Label.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Label.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Label.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Label.
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
        if issubclass(Label, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Label):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
