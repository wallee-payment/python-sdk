# coding: utf-8
import pprint
import six
from enum import Enum



class WebAppConfirmationRequest:

    swagger_types = {
    
        'code': 'str',
    }

    attribute_map = {
        'code': 'code',
    }

    
    _code = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.code = kwargs.get('code', None)
        

    
    @property
    def code(self):
        """Gets the code of this WebAppConfirmationRequest.

            The user returns to the web app after granting the permission. The HTTP request contains the code. Provide it here to confirm the web app installation.

        :return: The code of this WebAppConfirmationRequest.
        :rtype: str
        """
        return self._code

    @code.setter
    def code(self, code):
        """Sets the code of this WebAppConfirmationRequest.

            The user returns to the web app after granting the permission. The HTTP request contains the code. Provide it here to confirm the web app installation.

        :param code: The code of this WebAppConfirmationRequest.
        :type: str
        """
        if code is not None and len(code) > 100:
            raise ValueError("Invalid value for `code`, length must be less than or equal to `100`")

        self._code = code
    

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
        if issubclass(WebAppConfirmationRequest, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebAppConfirmationRequest):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
