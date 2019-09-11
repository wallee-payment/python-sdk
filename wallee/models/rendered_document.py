# coding: utf-8
import pprint
import six
from enum import Enum



class RenderedDocument:

    swagger_types = {
    
        'data': 'list[str]',
        'document_template_type': 'int',
        'mime_type': 'str',
        'title': 'str',
    }

    attribute_map = {
        'data': 'data','document_template_type': 'documentTemplateType','mime_type': 'mimeType','title': 'title',
    }

    
    _data = None
    _document_template_type = None
    _mime_type = None
    _title = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.data = kwargs.get('data', None)
        self.document_template_type = kwargs.get('document_template_type', None)
        self.mime_type = kwargs.get('mime_type', None)
        self.title = kwargs.get('title', None)
        

    
    @property
    def data(self):
        """Gets the data of this RenderedDocument.

            

        :return: The data of this RenderedDocument.
        :rtype: list[str]
        """
        return self._data

    @data.setter
    def data(self, data):
        """Sets the data of this RenderedDocument.

            

        :param data: The data of this RenderedDocument.
        :type: list[str]
        """

        self._data = data
    
    @property
    def document_template_type(self):
        """Gets the document_template_type of this RenderedDocument.

            

        :return: The document_template_type of this RenderedDocument.
        :rtype: int
        """
        return self._document_template_type

    @document_template_type.setter
    def document_template_type(self, document_template_type):
        """Sets the document_template_type of this RenderedDocument.

            

        :param document_template_type: The document_template_type of this RenderedDocument.
        :type: int
        """

        self._document_template_type = document_template_type
    
    @property
    def mime_type(self):
        """Gets the mime_type of this RenderedDocument.

            

        :return: The mime_type of this RenderedDocument.
        :rtype: str
        """
        return self._mime_type

    @mime_type.setter
    def mime_type(self, mime_type):
        """Sets the mime_type of this RenderedDocument.

            

        :param mime_type: The mime_type of this RenderedDocument.
        :type: str
        """

        self._mime_type = mime_type
    
    @property
    def title(self):
        """Gets the title of this RenderedDocument.

            

        :return: The title of this RenderedDocument.
        :rtype: str
        """
        return self._title

    @title.setter
    def title(self, title):
        """Sets the title of this RenderedDocument.

            

        :param title: The title of this RenderedDocument.
        :type: str
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
        if issubclass(RenderedDocument, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RenderedDocument):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
