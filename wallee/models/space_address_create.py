# coding: utf-8
import pprint
import six
from enum import Enum



class SpaceAddressCreate:

    swagger_types = {
    
        'city': 'str',
        'country': 'str',
        'dependent_locality': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'given_name': 'str',
        'mobile_phone_number': 'str',
        'organization_name': 'str',
        'phone_number': 'str',
        'postal_state': 'str',
        'postcode': 'str',
        'sales_tax_number': 'str',
        'salutation': 'str',
        'sorting_code': 'str',
        'street': 'str',
    }

    attribute_map = {
        'city': 'city','country': 'country','dependent_locality': 'dependentLocality','email_address': 'emailAddress','family_name': 'familyName','given_name': 'givenName','mobile_phone_number': 'mobilePhoneNumber','organization_name': 'organizationName','phone_number': 'phoneNumber','postal_state': 'postalState','postcode': 'postcode','sales_tax_number': 'salesTaxNumber','salutation': 'salutation','sorting_code': 'sortingCode','street': 'street',
    }

    
    _city = None
    _country = None
    _dependent_locality = None
    _email_address = None
    _family_name = None
    _given_name = None
    _mobile_phone_number = None
    _organization_name = None
    _phone_number = None
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
        self.mobile_phone_number = kwargs.get('mobile_phone_number', None)
        self.organization_name = kwargs.get('organization_name', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.postal_state = kwargs.get('postal_state', None)
        self.postcode = kwargs.get('postcode', None)
        self.sales_tax_number = kwargs.get('sales_tax_number', None)
        self.salutation = kwargs.get('salutation', None)
        self.sorting_code = kwargs.get('sorting_code', None)
        self.street = kwargs.get('street', None)
        

    
    @property
    def city(self):
        """Gets the city of this SpaceAddressCreate.

            The city, town or village.

        :return: The city of this SpaceAddressCreate.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this SpaceAddressCreate.

            The city, town or village.

        :param city: The city of this SpaceAddressCreate.
        :type: str
        """

        self._city = city
    
    @property
    def country(self):
        """Gets the country of this SpaceAddressCreate.

            The two-letter country code (ISO 3166 format).

        :return: The country of this SpaceAddressCreate.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this SpaceAddressCreate.

            The two-letter country code (ISO 3166 format).

        :param country: The country of this SpaceAddressCreate.
        :type: str
        """

        self._country = country
    
    @property
    def dependent_locality(self):
        """Gets the dependent_locality of this SpaceAddressCreate.

            The dependent locality which is a sub-division of the state.

        :return: The dependent_locality of this SpaceAddressCreate.
        :rtype: str
        """
        return self._dependent_locality

    @dependent_locality.setter
    def dependent_locality(self, dependent_locality):
        """Sets the dependent_locality of this SpaceAddressCreate.

            The dependent locality which is a sub-division of the state.

        :param dependent_locality: The dependent_locality of this SpaceAddressCreate.
        :type: str
        """
        if dependent_locality is not None and len(dependent_locality) > 100:
            raise ValueError("Invalid value for `dependent_locality`, length must be less than or equal to `100`")

        self._dependent_locality = dependent_locality
    
    @property
    def email_address(self):
        """Gets the email_address of this SpaceAddressCreate.

            The email address used for communication with clients.

        :return: The email_address of this SpaceAddressCreate.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SpaceAddressCreate.

            The email address used for communication with clients.

        :param email_address: The email_address of this SpaceAddressCreate.
        :type: str
        """

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this SpaceAddressCreate.

            The family or last name.

        :return: The family_name of this SpaceAddressCreate.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this SpaceAddressCreate.

            The family or last name.

        :param family_name: The family_name of this SpaceAddressCreate.
        :type: str
        """
        if family_name is not None and len(family_name) > 100:
            raise ValueError("Invalid value for `family_name`, length must be less than or equal to `100`")

        self._family_name = family_name
    
    @property
    def given_name(self):
        """Gets the given_name of this SpaceAddressCreate.

            The given or first name.

        :return: The given_name of this SpaceAddressCreate.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this SpaceAddressCreate.

            The given or first name.

        :param given_name: The given_name of this SpaceAddressCreate.
        :type: str
        """
        if given_name is not None and len(given_name) > 100:
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `100`")

        self._given_name = given_name
    
    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this SpaceAddressCreate.

            The phone number of a mobile phone.

        :return: The mobile_phone_number of this SpaceAddressCreate.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this SpaceAddressCreate.

            The phone number of a mobile phone.

        :param mobile_phone_number: The mobile_phone_number of this SpaceAddressCreate.
        :type: str
        """
        if mobile_phone_number is not None and len(mobile_phone_number) > 100:
            raise ValueError("Invalid value for `mobile_phone_number`, length must be less than or equal to `100`")

        self._mobile_phone_number = mobile_phone_number
    
    @property
    def organization_name(self):
        """Gets the organization_name of this SpaceAddressCreate.

            The organization's name.

        :return: The organization_name of this SpaceAddressCreate.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this SpaceAddressCreate.

            The organization's name.

        :param organization_name: The organization_name of this SpaceAddressCreate.
        :type: str
        """
        if organization_name is not None and len(organization_name) > 100:
            raise ValueError("Invalid value for `organization_name`, length must be less than or equal to `100`")

        self._organization_name = organization_name
    
    @property
    def phone_number(self):
        """Gets the phone_number of this SpaceAddressCreate.

            The phone number.

        :return: The phone_number of this SpaceAddressCreate.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this SpaceAddressCreate.

            The phone number.

        :param phone_number: The phone_number of this SpaceAddressCreate.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 100:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `100`")

        self._phone_number = phone_number
    
    @property
    def postal_state(self):
        """Gets the postal_state of this SpaceAddressCreate.

            The name of the region, typically a state, county, province or prefecture.

        :return: The postal_state of this SpaceAddressCreate.
        :rtype: str
        """
        return self._postal_state

    @postal_state.setter
    def postal_state(self, postal_state):
        """Sets the postal_state of this SpaceAddressCreate.

            The name of the region, typically a state, county, province or prefecture.

        :param postal_state: The postal_state of this SpaceAddressCreate.
        :type: str
        """

        self._postal_state = postal_state
    
    @property
    def postcode(self):
        """Gets the postcode of this SpaceAddressCreate.

            The postal code, also known as ZIP, postcode, etc.

        :return: The postcode of this SpaceAddressCreate.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this SpaceAddressCreate.

            The postal code, also known as ZIP, postcode, etc.

        :param postcode: The postcode of this SpaceAddressCreate.
        :type: str
        """

        self._postcode = postcode
    
    @property
    def sales_tax_number(self):
        """Gets the sales_tax_number of this SpaceAddressCreate.

            The sales tax number of the organization.

        :return: The sales_tax_number of this SpaceAddressCreate.
        :rtype: str
        """
        return self._sales_tax_number

    @sales_tax_number.setter
    def sales_tax_number(self, sales_tax_number):
        """Sets the sales_tax_number of this SpaceAddressCreate.

            The sales tax number of the organization.

        :param sales_tax_number: The sales_tax_number of this SpaceAddressCreate.
        :type: str
        """
        if sales_tax_number is not None and len(sales_tax_number) > 100:
            raise ValueError("Invalid value for `sales_tax_number`, length must be less than or equal to `100`")

        self._sales_tax_number = sales_tax_number
    
    @property
    def salutation(self):
        """Gets the salutation of this SpaceAddressCreate.

            The salutation e.g. Mrs, Mr, Dr.

        :return: The salutation of this SpaceAddressCreate.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """Sets the salutation of this SpaceAddressCreate.

            The salutation e.g. Mrs, Mr, Dr.

        :param salutation: The salutation of this SpaceAddressCreate.
        :type: str
        """
        if salutation is not None and len(salutation) > 20:
            raise ValueError("Invalid value for `salutation`, length must be less than or equal to `20`")

        self._salutation = salutation
    
    @property
    def sorting_code(self):
        """Gets the sorting_code of this SpaceAddressCreate.

            The sorting code identifying the post office where the PO Box is located.

        :return: The sorting_code of this SpaceAddressCreate.
        :rtype: str
        """
        return self._sorting_code

    @sorting_code.setter
    def sorting_code(self, sorting_code):
        """Sets the sorting_code of this SpaceAddressCreate.

            The sorting code identifying the post office where the PO Box is located.

        :param sorting_code: The sorting_code of this SpaceAddressCreate.
        :type: str
        """
        if sorting_code is not None and len(sorting_code) > 100:
            raise ValueError("Invalid value for `sorting_code`, length must be less than or equal to `100`")

        self._sorting_code = sorting_code
    
    @property
    def street(self):
        """Gets the street of this SpaceAddressCreate.

            The street or PO Box.

        :return: The street of this SpaceAddressCreate.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this SpaceAddressCreate.

            The street or PO Box.

        :param street: The street of this SpaceAddressCreate.
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
        if issubclass(SpaceAddressCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SpaceAddressCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
