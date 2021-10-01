# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriberActive:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'email_address': 'str',
        'external_id': 'str',
        'phone_number': 'str',
    }

    attribute_map = {
        'id': 'id','version': 'version','email_address': 'emailAddress','external_id': 'externalId','phone_number': 'phoneNumber',
    }

    
    _id = None
    _version = None
    _email_address = None
    _external_id = None
    _phone_number = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.email_address = kwargs.get('email_address', None)
        self.external_id = kwargs.get('external_id', None)
        self.phone_number = kwargs.get('phone_number', None)
        

    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriberActive.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscriberActive.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriberActive.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscriberActive.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscriberActive.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscriberActive.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscriberActive.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscriberActive.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def email_address(self):
        """Gets the email_address of this ShopifySubscriberActive.

            

        :return: The email_address of this ShopifySubscriberActive.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ShopifySubscriberActive.

            

        :param email_address: The email_address of this ShopifySubscriberActive.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def external_id(self):
        """Gets the external_id of this ShopifySubscriberActive.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this ShopifySubscriberActive.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ShopifySubscriberActive.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this ShopifySubscriberActive.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def phone_number(self):
        """Gets the phone_number of this ShopifySubscriberActive.

            

        :return: The phone_number of this ShopifySubscriberActive.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ShopifySubscriberActive.

            

        :param phone_number: The phone_number of this ShopifySubscriberActive.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 254:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `254`")

        self._phone_number = phone_number
    

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
        if issubclass(ShopifySubscriberActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriberActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
