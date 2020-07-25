# coding: utf-8
import pprint
import six
from enum import Enum



class SpaceAddress:

    swagger_types = {
    
        'city': 'str',
        'country': 'str',
        'dependent_locality': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'organization_name': 'str',
        'postal_state': 'str',
        'postcode': 'str',
        'sales_tax_number': 'str',
        'salutation': 'str',
        'sorting_code': 'str',
        'street': 'str',
    }

    attribute_map = {
        'city': 'city','country': 'country','dependent_locality': 'dependentLocality','email_address': 'emailAddress','family_name': 'familyName','given_name': 'givenName','organization_name': 'organizationName','postal_state': 'postalState','postcode': 'postcode','sales_tax_number': 'salesTaxNumber','salutation': 'salutation','sorting_code': 'sortingCode','street': 'street',
    }

    
    _city = None
    _country = None
    _dependent_locality = None
    _email_address = None
    _family_name = None
    _given_name = None
    _organization_name = None
    _postal_state = None
    _postcode = None
    _sales_tax_number = None
    _salutation = None
    _sorting_code = None
    _street = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.city = kwargs.get('city', None)
        self.country = kwargs.get('country', None)
        self.dependent_locality = kwargs.get('dependent_locality', None)
        self.email_address = kwargs.get('email_address', None)
        self.family_name = kwargs.get('family_name', None)
        self.given_name = kwargs.get('given_name', None)
        self.organization_name = kwargs.get('organization_name', None)
        self.postal_state = kwargs.get('postal_state', None)
        self.postcode = kwargs.get('postcode', None)
        self.sales_tax_number = kwargs.get('sales_tax_number', None)
        self.salutation = kwargs.get('salutation', None)
        self.sorting_code = kwargs.get('sorting_code', None)
        self.street = kwargs.get('street', None)
        

    
    @property
    def city(self):
        """Gets the city of this SpaceAddress.

            

        :return: The city of this SpaceAddress.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SpaceAddress.

            

        :param city: The city of this SpaceAddress.
        :type: str
        """

        self._city = city
    
    @property
    def country(self):
        """Gets the country of this SpaceAddress.

            

        :return: The country of this SpaceAddress.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SpaceAddress.

            

        :param country: The country of this SpaceAddress.
        :type: str
        """

        self._country = country
    
    @property
    def dependent_locality(self):
        """Gets the dependent_locality of this SpaceAddress.

            

        :return: The dependent_locality of this SpaceAddress.
        :rtype: str
        """
        return self._dependent_locality

    @dependent_locality.setter
    def dependent_locality(self, dependent_locality):
        """Sets the dependent_locality of this SpaceAddress.

            

        :param dependent_locality: The dependent_locality of this SpaceAddress.
        :type: str
        """
        if dependent_locality is not None and len(dependent_locality) > 100:
            raise ValueError("Invalid value for `dependent_locality`, length must be less than or equal to `100`")

        self._dependent_locality = dependent_locality
    
    @property
    def email_address(self):
        """Gets the email_address of this SpaceAddress.

            The email address is used within emails and as reply to address.

        :return: The email_address of this SpaceAddress.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SpaceAddress.

            The email address is used within emails and as reply to address.

        :param email_address: The email_address of this SpaceAddress.
        :type: str
        """

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this SpaceAddress.

            

        :return: The family_name of this SpaceAddress.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this SpaceAddress.

            

        :param family_name: The family_name of this SpaceAddress.
        :type: str
        """
        if family_name is not None and len(family_name) > 100:
            raise ValueError("Invalid value for `family_name`, length must be less than or equal to `100`")

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this SpaceAddress.

            

        :return: The given_name of this SpaceAddress.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this SpaceAddress.

            

        :param given_name: The given_name of this SpaceAddress.
        :type: str
        """
        if given_name is not None and len(given_name) > 100:
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `100`")

        self._given_name = given_name
    
    @property
    def organization_name(self):
        """Gets the organization_name of this SpaceAddress.

            

        :return: The organization_name of this SpaceAddress.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this SpaceAddress.

            

        :param organization_name: The organization_name of this SpaceAddress.
        :type: str
        """
        if organization_name is not None and len(organization_name) > 100:
            raise ValueError("Invalid value for `organization_name`, length must be less than or equal to `100`")

        self._organization_name = organization_name
    
    @property
    def postal_state(self):
        """Gets the postal_state of this SpaceAddress.

            

        :return: The postal_state of this SpaceAddress.
        :rtype: str
        """
        return self._postal_state

    @postal_state.setter
    def postal_state(self, postal_state):
        """Sets the postal_state of this SpaceAddress.

            

        :param postal_state: The postal_state of this SpaceAddress.
        :type: str
        """

        self._postal_state = postal_state
    
    @property
    def postcode(self):
        """Gets the postcode of this SpaceAddress.

            

        :return: The postcode of this SpaceAddress.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this SpaceAddress.

            

        :param postcode: The postcode of this SpaceAddress.
        :type: str
        """

        self._postcode = postcode
    
    @property
    def sales_tax_number(self):
        """Gets the sales_tax_number of this SpaceAddress.

            

        :return: The sales_tax_number of this SpaceAddress.
        :rtype: str
        """
        return self._sales_tax_number

    @sales_tax_number.setter
    def sales_tax_number(self, sales_tax_number):
        """Sets the sales_tax_number of this SpaceAddress.

            

        :param sales_tax_number: The sales_tax_number of this SpaceAddress.
        :type: str
        """
        if sales_tax_number is not None and len(sales_tax_number) > 100:
            raise ValueError("Invalid value for `sales_tax_number`, length must be less than or equal to `100`")

        self._sales_tax_number = sales_tax_number
    
    @property
    def salutation(self):
        """Gets the salutation of this SpaceAddress.

            

        :return: The salutation of this SpaceAddress.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """Sets the salutation of this SpaceAddress.

            

        :param salutation: The salutation of this SpaceAddress.
        :type: str
        """
        if salutation is not None and len(salutation) > 20:
            raise ValueError("Invalid value for `salutation`, length must be less than or equal to `20`")

        self._salutation = salutation
    
    @property
    def sorting_code(self):
        """Gets the sorting_code of this SpaceAddress.

            The sorting code identifies the post office at which the post box is located in.

        :return: The sorting_code of this SpaceAddress.
        :rtype: str
        """
        return self._sorting_code

    @sorting_code.setter
    def sorting_code(self, sorting_code):
        """Sets the sorting_code of this SpaceAddress.

            The sorting code identifies the post office at which the post box is located in.

        :param sorting_code: The sorting_code of this SpaceAddress.
        :type: str
        """
        if sorting_code is not None and len(sorting_code) > 100:
            raise ValueError("Invalid value for `sorting_code`, length must be less than or equal to `100`")

        self._sorting_code = sorting_code
    
    @property
    def street(self):
        """Gets the street of this SpaceAddress.

            

        :return: The street of this SpaceAddress.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this SpaceAddress.

            

        :param street: The street of this SpaceAddress.
        :type: str
        """

        self._street = street
    

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
        if issubclass(SpaceAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SpaceAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
