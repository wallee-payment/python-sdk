# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractCustomerActive:

    swagger_types = {
    
        'customer_id': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'language': 'str',
        'meta_data': 'dict(str, str)',
        'preferred_currency': 'str',
    }

    attribute_map = {
        'customer_id': 'customerId','email_address': 'emailAddress','family_name': 'familyName','given_name': 'givenName','language': 'language','meta_data': 'metaData','preferred_currency': 'preferredCurrency',
    }

    
    _customer_id = None
    _email_address = None
    _family_name = None
    _given_name = None
    _language = None
    _meta_data = None
    _preferred_currency = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.customer_id = kwargs.get('customer_id', None)
        self.email_address = kwargs.get('email_address', None)
        self.family_name = kwargs.get('family_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.language = kwargs.get('language', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.preferred_currency = kwargs.get('preferred_currency', None)
        

    
    @property
    def customer_id(self):
        """Gets the customer_id of this AbstractCustomerActive.

            

        :return: The customer_id of this AbstractCustomerActive.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this AbstractCustomerActive.

            

        :param customer_id: The customer_id of this AbstractCustomerActive.
        :type: str
        """
        if customer_id is not None and len(customer_id) > 100:
            raise ValueError("Invalid value for `customer_id`, length must be less than or equal to `100`")

        self._customer_id = customer_id
    
    @property
    def email_address(self):
        """Gets the email_address of this AbstractCustomerActive.

            

        :return: The email_address of this AbstractCustomerActive.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this AbstractCustomerActive.

            

        :param email_address: The email_address of this AbstractCustomerActive.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this AbstractCustomerActive.

            

        :return: The family_name of this AbstractCustomerActive.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this AbstractCustomerActive.

            

        :param family_name: The family_name of this AbstractCustomerActive.
        :type: str
        """
        if family_name is not None and len(family_name) > 100:
            raise ValueError("Invalid value for `family_name`, length must be less than or equal to `100`")

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this AbstractCustomerActive.

            

        :return: The given_name of this AbstractCustomerActive.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this AbstractCustomerActive.

            

        :param given_name: The given_name of this AbstractCustomerActive.
        :type: str
        """
        if given_name is not None and len(given_name) > 100:
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `100`")

        self._given_name = given_name
    
    @property
    def language(self):
        """Gets the language of this AbstractCustomerActive.

            

        :return: The language of this AbstractCustomerActive.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this AbstractCustomerActive.

            

        :param language: The language of this AbstractCustomerActive.
        :type: str
        """

        self._language = language
    
    @property
    def meta_data(self):
        """Gets the meta_data of this AbstractCustomerActive.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this AbstractCustomerActive.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this AbstractCustomerActive.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this AbstractCustomerActive.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def preferred_currency(self):
        """Gets the preferred_currency of this AbstractCustomerActive.

            

        :return: The preferred_currency of this AbstractCustomerActive.
        :rtype: str
        """
        return self._preferred_currency

    @preferred_currency.setter
    def preferred_currency(self, preferred_currency):
        """Sets the preferred_currency of this AbstractCustomerActive.

            

        :param preferred_currency: The preferred_currency of this AbstractCustomerActive.
        :type: str
        """

        self._preferred_currency = preferred_currency
    

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
        if issubclass(AbstractCustomerActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractCustomerActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
