# coding: utf-8
import pprint
import six
from enum import Enum



class CustomerPostalAddressCreate:

    swagger_types = {
    
        'city': 'str',
        'commercial_register_number': 'str',
        'country': 'str',
        'date_of_birth': 'date',
        'dependent_locality': 'str',
        'email_address': 'str',
        'family_name': 'str',
        'gender': 'Gender',
        'given_name': 'str',
        'legal_organization_form': 'int',
        'mobile_phone_number': 'str',
        'organization_name': 'str',
        'phone_number': 'str',
        'postal_state': 'str',
        'postcode': 'str',
        'sales_tax_number': 'str',
        'salutation': 'str',
        'social_security_number': 'str',
        'sorting_code': 'str',
        'street': 'str',
    }

    attribute_map = {
        'city': 'city','commercial_register_number': 'commercialRegisterNumber','country': 'country','date_of_birth': 'dateOfBirth','dependent_locality': 'dependentLocality','email_address': 'emailAddress','family_name': 'familyName','gender': 'gender','given_name': 'givenName','legal_organization_form': 'legalOrganizationForm','mobile_phone_number': 'mobilePhoneNumber','organization_name': 'organizationName','phone_number': 'phoneNumber','postal_state': 'postalState','postcode': 'postcode','sales_tax_number': 'salesTaxNumber','salutation': 'salutation','social_security_number': 'socialSecurityNumber','sorting_code': 'sortingCode','street': 'street',
    }

    
    _city = None
    _commercial_register_number = None
    _country = None
    _date_of_birth = None
    _dependent_locality = None
    _email_address = None
    _family_name = None
    _gender = None
    _given_name = None
    _legal_organization_form = None
    _mobile_phone_number = None
    _organization_name = None
    _phone_number = None
    _postal_state = None
    _postcode = None
    _sales_tax_number = None
    _salutation = None
    _social_security_number = None
    _sorting_code = None
    _street = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.city = kwargs.get('city', None)
        self.commercial_register_number = kwargs.get('commercial_register_number', None)
        self.country = kwargs.get('country', None)
        self.date_of_birth = kwargs.get('date_of_birth', None)
        self.dependent_locality = kwargs.get('dependent_locality', None)
        self.email_address = kwargs.get('email_address', None)
        self.family_name = kwargs.get('family_name', None)
        self.gender = kwargs.get('gender', None)
        self.given_name = kwargs.get('given_name', None)
        self.legal_organization_form = kwargs.get('legal_organization_form', None)
        self.mobile_phone_number = kwargs.get('mobile_phone_number', None)
        self.organization_name = kwargs.get('organization_name', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.postal_state = kwargs.get('postal_state', None)
        self.postcode = kwargs.get('postcode', None)
        self.sales_tax_number = kwargs.get('sales_tax_number', None)
        self.salutation = kwargs.get('salutation', None)
        self.social_security_number = kwargs.get('social_security_number', None)
        self.sorting_code = kwargs.get('sorting_code', None)
        self.street = kwargs.get('street', None)
        

    
    @property
    def city(self):
        """Gets the city of this CustomerPostalAddressCreate.

            

        :return: The city of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._city

    @city.setter
    def city(self, city):
        """Sets the city of this CustomerPostalAddressCreate.

            

        :param city: The city of this CustomerPostalAddressCreate.
        :type: str
        """
        if city is not None and len(city) > 100:
            raise ValueError("Invalid value for `city`, length must be less than or equal to `100`")

        self._city = city
    
    @property
    def commercial_register_number(self):
        """Gets the commercial_register_number of this CustomerPostalAddressCreate.

            

        :return: The commercial_register_number of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._commercial_register_number

    @commercial_register_number.setter
    def commercial_register_number(self, commercial_register_number):
        """Sets the commercial_register_number of this CustomerPostalAddressCreate.

            

        :param commercial_register_number: The commercial_register_number of this CustomerPostalAddressCreate.
        :type: str
        """
        if commercial_register_number is not None and len(commercial_register_number) > 100:
            raise ValueError("Invalid value for `commercial_register_number`, length must be less than or equal to `100`")

        self._commercial_register_number = commercial_register_number
    
    @property
    def country(self):
        """Gets the country of this CustomerPostalAddressCreate.

            

        :return: The country of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._country

    @country.setter
    def country(self, country):
        """Sets the country of this CustomerPostalAddressCreate.

            

        :param country: The country of this CustomerPostalAddressCreate.
        :type: str
        """

        self._country = country
    
    @property
    def date_of_birth(self):
        """Gets the date_of_birth of this CustomerPostalAddressCreate.

            

        :return: The date_of_birth of this CustomerPostalAddressCreate.
        :rtype: date
        """
        return self._date_of_birth

    @date_of_birth.setter
    def date_of_birth(self, date_of_birth):
        """Sets the date_of_birth of this CustomerPostalAddressCreate.

            

        :param date_of_birth: The date_of_birth of this CustomerPostalAddressCreate.
        :type: date
        """

        self._date_of_birth = date_of_birth
    
    @property
    def dependent_locality(self):
        """Gets the dependent_locality of this CustomerPostalAddressCreate.

            

        :return: The dependent_locality of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._dependent_locality

    @dependent_locality.setter
    def dependent_locality(self, dependent_locality):
        """Sets the dependent_locality of this CustomerPostalAddressCreate.

            

        :param dependent_locality: The dependent_locality of this CustomerPostalAddressCreate.
        :type: str
        """
        if dependent_locality is not None and len(dependent_locality) > 100:
            raise ValueError("Invalid value for `dependent_locality`, length must be less than or equal to `100`")

        self._dependent_locality = dependent_locality
    
    @property
    def email_address(self):
        """Gets the email_address of this CustomerPostalAddressCreate.

            

        :return: The email_address of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this CustomerPostalAddressCreate.

            

        :param email_address: The email_address of this CustomerPostalAddressCreate.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def family_name(self):
        """Gets the family_name of this CustomerPostalAddressCreate.

            

        :return: The family_name of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._family_name

    @family_name.setter
    def family_name(self, family_name):
        """Sets the family_name of this CustomerPostalAddressCreate.

            

        :param family_name: The family_name of this CustomerPostalAddressCreate.
        :type: str
        """
        if family_name is not None and len(family_name) > 100:
            raise ValueError("Invalid value for `family_name`, length must be less than or equal to `100`")

        self._family_name = family_name
    
    @property
    def gender(self):
        """Gets the gender of this CustomerPostalAddressCreate.

            

        :return: The gender of this CustomerPostalAddressCreate.
        :rtype: Gender
        """
        return self._gender

    @gender.setter
    def gender(self, gender):
        """Sets the gender of this CustomerPostalAddressCreate.

            

        :param gender: The gender of this CustomerPostalAddressCreate.
        :type: Gender
        """

        self._gender = gender
    
    @property
    def given_name(self):
        """Gets the given_name of this CustomerPostalAddressCreate.

            

        :return: The given_name of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._given_name

    @given_name.setter
    def given_name(self, given_name):
        """Sets the given_name of this CustomerPostalAddressCreate.

            

        :param given_name: The given_name of this CustomerPostalAddressCreate.
        :type: str
        """
        if given_name is not None and len(given_name) > 100:
            raise ValueError("Invalid value for `given_name`, length must be less than or equal to `100`")

        self._given_name = given_name
    
    @property
    def legal_organization_form(self):
        """Gets the legal_organization_form of this CustomerPostalAddressCreate.

            

        :return: The legal_organization_form of this CustomerPostalAddressCreate.
        :rtype: int
        """
        return self._legal_organization_form

    @legal_organization_form.setter
    def legal_organization_form(self, legal_organization_form):
        """Sets the legal_organization_form of this CustomerPostalAddressCreate.

            

        :param legal_organization_form: The legal_organization_form of this CustomerPostalAddressCreate.
        :type: int
        """

        self._legal_organization_form = legal_organization_form
    
    @property
    def mobile_phone_number(self):
        """Gets the mobile_phone_number of this CustomerPostalAddressCreate.

            

        :return: The mobile_phone_number of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._mobile_phone_number

    @mobile_phone_number.setter
    def mobile_phone_number(self, mobile_phone_number):
        """Sets the mobile_phone_number of this CustomerPostalAddressCreate.

            

        :param mobile_phone_number: The mobile_phone_number of this CustomerPostalAddressCreate.
        :type: str
        """
        if mobile_phone_number is not None and len(mobile_phone_number) > 100:
            raise ValueError("Invalid value for `mobile_phone_number`, length must be less than or equal to `100`")

        self._mobile_phone_number = mobile_phone_number
    
    @property
    def organization_name(self):
        """Gets the organization_name of this CustomerPostalAddressCreate.

            

        :return: The organization_name of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._organization_name

    @organization_name.setter
    def organization_name(self, organization_name):
        """Sets the organization_name of this CustomerPostalAddressCreate.

            

        :param organization_name: The organization_name of this CustomerPostalAddressCreate.
        :type: str
        """
        if organization_name is not None and len(organization_name) > 100:
            raise ValueError("Invalid value for `organization_name`, length must be less than or equal to `100`")

        self._organization_name = organization_name
    
    @property
    def phone_number(self):
        """Gets the phone_number of this CustomerPostalAddressCreate.

            

        :return: The phone_number of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this CustomerPostalAddressCreate.

            

        :param phone_number: The phone_number of this CustomerPostalAddressCreate.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 100:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `100`")

        self._phone_number = phone_number
    
    @property
    def postal_state(self):
        """Gets the postal_state of this CustomerPostalAddressCreate.

            

        :return: The postal_state of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._postal_state

    @postal_state.setter
    def postal_state(self, postal_state):
        """Sets the postal_state of this CustomerPostalAddressCreate.

            

        :param postal_state: The postal_state of this CustomerPostalAddressCreate.
        :type: str
        """

        self._postal_state = postal_state
    
    @property
    def postcode(self):
        """Gets the postcode of this CustomerPostalAddressCreate.

            

        :return: The postcode of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._postcode

    @postcode.setter
    def postcode(self, postcode):
        """Sets the postcode of this CustomerPostalAddressCreate.

            

        :param postcode: The postcode of this CustomerPostalAddressCreate.
        :type: str
        """
        if postcode is not None and len(postcode) > 40:
            raise ValueError("Invalid value for `postcode`, length must be less than or equal to `40`")

        self._postcode = postcode
    
    @property
    def sales_tax_number(self):
        """Gets the sales_tax_number of this CustomerPostalAddressCreate.

            

        :return: The sales_tax_number of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._sales_tax_number

    @sales_tax_number.setter
    def sales_tax_number(self, sales_tax_number):
        """Sets the sales_tax_number of this CustomerPostalAddressCreate.

            

        :param sales_tax_number: The sales_tax_number of this CustomerPostalAddressCreate.
        :type: str
        """
        if sales_tax_number is not None and len(sales_tax_number) > 100:
            raise ValueError("Invalid value for `sales_tax_number`, length must be less than or equal to `100`")

        self._sales_tax_number = sales_tax_number
    
    @property
    def salutation(self):
        """Gets the salutation of this CustomerPostalAddressCreate.

            

        :return: The salutation of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._salutation

    @salutation.setter
    def salutation(self, salutation):
        """Sets the salutation of this CustomerPostalAddressCreate.

            

        :param salutation: The salutation of this CustomerPostalAddressCreate.
        :type: str
        """
        if salutation is not None and len(salutation) > 20:
            raise ValueError("Invalid value for `salutation`, length must be less than or equal to `20`")

        self._salutation = salutation
    
    @property
    def social_security_number(self):
        """Gets the social_security_number of this CustomerPostalAddressCreate.

            

        :return: The social_security_number of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._social_security_number

    @social_security_number.setter
    def social_security_number(self, social_security_number):
        """Sets the social_security_number of this CustomerPostalAddressCreate.

            

        :param social_security_number: The social_security_number of this CustomerPostalAddressCreate.
        :type: str
        """
        if social_security_number is not None and len(social_security_number) > 100:
            raise ValueError("Invalid value for `social_security_number`, length must be less than or equal to `100`")

        self._social_security_number = social_security_number
    
    @property
    def sorting_code(self):
        """Gets the sorting_code of this CustomerPostalAddressCreate.

            The sorting code identifies the post office at which the post box is located in.

        :return: The sorting_code of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._sorting_code

    @sorting_code.setter
    def sorting_code(self, sorting_code):
        """Sets the sorting_code of this CustomerPostalAddressCreate.

            The sorting code identifies the post office at which the post box is located in.

        :param sorting_code: The sorting_code of this CustomerPostalAddressCreate.
        :type: str
        """
        if sorting_code is not None and len(sorting_code) > 100:
            raise ValueError("Invalid value for `sorting_code`, length must be less than or equal to `100`")

        self._sorting_code = sorting_code
    
    @property
    def street(self):
        """Gets the street of this CustomerPostalAddressCreate.

            

        :return: The street of this CustomerPostalAddressCreate.
        :rtype: str
        """
        return self._street

    @street.setter
    def street(self, street):
        """Sets the street of this CustomerPostalAddressCreate.

            

        :param street: The street of this CustomerPostalAddressCreate.
        :type: str
        """
        if street is not None and len(street) > 300:
            raise ValueError("Invalid value for `street`, length must be less than or equal to `300`")

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
        if issubclass(CustomerPostalAddressCreate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CustomerPostalAddressCreate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
