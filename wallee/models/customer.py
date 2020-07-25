# coding: utf-8
import pprint
import six
from enum import Enum



class Customer:

    swagger_types = {
    
        'created_on': 'datetime',
        'customer_id': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'meta_data': 'dict(str, str)',
        'preferred_currency': 'str',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','customer_id': 'customerId','email_address': 'emailAddress','family_name': 'familyName','given_name': 'givenName','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','meta_data': 'metaData','preferred_currency': 'preferredCurrency','version': 'version',
    }

    
    _created_on = None
    _customer_id = None
    _email_address = None
    _family_name = None
    _given_name = None
    _id = None
    _language = None
    _linked_space_id = None
    _meta_data = None
    _preferred_currency = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.customer_id = kwargs.get('customer_id', None)
        self.email_address = kwargs.get('email_address', None)
        self.family_name = kwargs.get('family_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.preferred_currency = kwargs.get('preferred_currency', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this Customer.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this Customer.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this Customer.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this Customer.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def customer_id(self):
        """Gets the customer_id of this Customer.

            

        :return: The customer_id of this Customer.
        :rtype: str
        """
        return self._customer_id

    @customer_id.setter
    def customer_id(self, customer_id):
        """Sets the customer_id of this Customer.

            

        :param customer_id: The customer_id of this Customer.
        :type: str
        """
        if customer_id is not None and len(customer_id) > 100:
            raise ValueError("Invalid value for `customer_id`, length must be less than or equal to `100`")

        self._customer_id = customer_id
    
    @property
    def email_address(self):
        """Gets the email_address of this Customer.

            

        :return: The email_address of this Customer.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Customer.

            

        :param email_address: The email_address of this Customer.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this Customer.

            

        :return: The family_name of this Customer.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this Customer.

            

        :param family_name: The family_name of this Customer.
        :type: str
        """
        if family_name is not None and len(family_name) > 100:
            raise ValueError("Invalid value for `family_name`, length must be less than or equal to `100`")

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this Customer.

            

        :return: The given_name of this Customer.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this Customer.

            

        :param given_name: The given_name of this Customer.
        :type: str
        """
        if given_name is not None and len(given_name) > 100:
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `100`")

        self._given_name = given_name
    
    @property
    def id(self):
        """Gets the id of this Customer.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Customer.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Customer.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Customer.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this Customer.

            

        :return: The language of this Customer.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Customer.

            

        :param language: The language of this Customer.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Customer.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Customer.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Customer.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Customer.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def meta_data(self):
        """Gets the meta_data of this Customer.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this Customer.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this Customer.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this Customer.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def preferred_currency(self):
        """Gets the preferred_currency of this Customer.

            

        :return: The preferred_currency of this Customer.
        :rtype: str
        """
        return self._preferred_currency

    @preferred_currency.setter
    def preferred_currency(self, preferred_currency):
        """Sets the preferred_currency of this Customer.

            

        :param preferred_currency: The preferred_currency of this Customer.
        :type: str
        """

        self._preferred_currency = preferred_currency
    
    @property
    def version(self):
        """Gets the version of this Customer.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Customer.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Customer.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Customer.
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
        if issubclass(Customer, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Customer):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
