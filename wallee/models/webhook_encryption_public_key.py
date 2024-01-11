# coding: utf-8
import pprint
import six
from enum import Enum



class WebhookEncryptionPublicKey:

    swagger_types = {
    
        'id': 'str',
        'public_key': 'str',
    }

    attribute_map = {
        'id': 'id','public_key': 'publicKey',
    }

    
    _id = None
    _public_key = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.public_key = kwargs.get('public_key', None)
        

    
    @property
    def id(self):
        """Gets the id of this WebhookEncryptionPublicKey.

            The ID of encryption key

        :return: The id of this WebhookEncryptionPublicKey.
        :rtype: str
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this WebhookEncryptionPublicKey.

            The ID of encryption key

        :param id: The id of this WebhookEncryptionPublicKey.
        :type: str
        """

        self._id = id
    
    @property
    def public_key(self):
        """Gets the public_key of this WebhookEncryptionPublicKey.

            The BASE64 encoded public key

        :return: The public_key of this WebhookEncryptionPublicKey.
        :rtype: str
        """
        return self._public_key

    @public_key.setter
    def public_key(self, public_key):
        """Sets the public_key of this WebhookEncryptionPublicKey.

            The BASE64 encoded public key

        :param public_key: The public_key of this WebhookEncryptionPublicKey.
        :type: str
        """

        self._public_key = public_key
    

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
        if issubclass(WebhookEncryptionPublicKey, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, WebhookEncryptionPublicKey):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
