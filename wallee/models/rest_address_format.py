# coding: utf-8
import pprint
import six
from enum import Enum



class RestAddressFormat:

    swagger_types = {
    
        'post_code_examples': 'list[str]',
        'post_code_regex': 'str',
        'required_fields': 'list[RestAddressFormatField]',
        'used_fields': 'list[RestAddressFormatField]',
    }

    attribute_map = {
        'post_code_examples': 'postCodeExamples','post_code_regex': 'postCodeRegex','required_fields': 'requiredFields','used_fields': 'usedFields',
    }

    
    _post_code_examples = None
    _post_code_regex = None
    _required_fields = None
    _used_fields = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.post_code_examples = kwargs.get('post_code_examples', None)
        self.post_code_regex = kwargs.get('post_code_regex', None)
        self.required_fields = kwargs.get('required_fields', None)
        self.used_fields = kwargs.get('used_fields', None)
        

    
    @property
    def post_code_examples(self):
        """Gets the post_code_examples of this RestAddressFormat.

            The example post codes allow the user to understand what we expect here.

        :return: The post_code_examples of this RestAddressFormat.
        :rtype: list[str]
        """
        return self._post_code_examples

    @post_code_examples.setter
    def post_code_examples(self, post_code_examples):
        """Sets the post_code_examples of this RestAddressFormat.

            The example post codes allow the user to understand what we expect here.

        :param post_code_examples: The post_code_examples of this RestAddressFormat.
        :type: list[str]
        """

        self._post_code_examples = post_code_examples
    
    @property
    def post_code_regex(self):
        """Gets the post_code_regex of this RestAddressFormat.

            The post code regex is a regular expression which can validates the input of the post code.

        :return: The post_code_regex of this RestAddressFormat.
        :rtype: str
        """
        return self._post_code_regex

    @post_code_regex.setter
    def post_code_regex(self, post_code_regex):
        """Sets the post_code_regex of this RestAddressFormat.

            The post code regex is a regular expression which can validates the input of the post code.

        :param post_code_regex: The post_code_regex of this RestAddressFormat.
        :type: str
        """

        self._post_code_regex = post_code_regex
    
    @property
    def required_fields(self):
        """Gets the required_fields of this RestAddressFormat.

            The required fields indicate what fields are required within an address to comply with the address format.

        :return: The required_fields of this RestAddressFormat.
        :rtype: list[RestAddressFormatField]
        """
        return self._required_fields

    @required_fields.setter
    def required_fields(self, required_fields):
        """Sets the required_fields of this RestAddressFormat.

            The required fields indicate what fields are required within an address to comply with the address format.

        :param required_fields: The required_fields of this RestAddressFormat.
        :type: list[RestAddressFormatField]
        """

        self._required_fields = required_fields
    
    @property
    def used_fields(self):
        """Gets the used_fields of this RestAddressFormat.

            The used fields indicate what fields are used within this address format.

        :return: The used_fields of this RestAddressFormat.
        :rtype: list[RestAddressFormatField]
        """
        return self._used_fields

    @used_fields.setter
    def used_fields(self, used_fields):
        """Sets the used_fields of this RestAddressFormat.

            The used fields indicate what fields are used within this address format.

        :param used_fields: The used_fields of this RestAddressFormat.
        :type: list[RestAddressFormatField]
        """

        self._used_fields = used_fields
    

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
        if issubclass(RestAddressFormat, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, RestAddressFormat):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
