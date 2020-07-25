# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractTransactionCommentActive:

    swagger_types = {
    
        'content': 'str',
    }

    attribute_map = {
        'content': 'content',
    }

    
    _content = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.content = kwargs.get('content', None)
        

    
    @property
    def content(self):
        """Gets the content of this AbstractTransactionCommentActive.

            

        :return: The content of this AbstractTransactionCommentActive.
        :rtype: str
        """
        return self._content

    @content.setter
    def content(self, content):
        """Sets the content of this AbstractTransactionCommentActive.

            

        :param content: The content of this AbstractTransactionCommentActive.
        :type: str
        """
        if content is not None and len(content) > 262144:
            raise ValueError("Invalid value for `content`, length must be less than or equal to `262144`")

        self._content = content
    

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
        if issubclass(AbstractTransactionCommentActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractTransactionCommentActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
