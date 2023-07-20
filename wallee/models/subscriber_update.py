# coding: utf-8
import pprint
import six
from enum import Enum



class SubscriberUpdate:

    swagger_types = {
    
        'id': 'int',
        'version': 'int',
        'additional_allowed_payment_method_configurations': 'list[int]',
        'billing_address': 'AddressCreate',
        'description': 'str',
        'disallowed_payment_method_configurations': 'list[int]',
        'email_address': 'str',
        'language': 'str',
        'meta_data': 'dict(str, str)',
        'reference': 'str',
        'shipping_address': 'AddressCreate',
    }

    attribute_map = {
        'id': 'id','version': 'version','additional_allowed_payment_method_configurations': 'additionalAllowedPaymentMethodConfigurations','billing_address': 'billingAddress','description': 'description','disallowed_payment_method_configurations': 'disallowedPaymentMethodConfigurations','email_address': 'emailAddress','language': 'language','meta_data': 'metaData','reference': 'reference','shipping_address': 'shippingAddress',
    }

    
    _id = None
    _version = None
    _additional_allowed_payment_method_configurations = None
    _billing_address = None
    _description = None
    _disallowed_payment_method_configurations = None
    _email_address = None
    _language = None
    _meta_data = None
    _reference = None
    _shipping_address = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id')

        self.version = kwargs.get('version')

        self.additional_allowed_payment_method_configurations = kwargs.get('additional_allowed_payment_method_configurations', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.description = kwargs.get('description', None)
        self.disallowed_payment_method_configurations = kwargs.get('disallowed_payment_method_configurations', None)
        self.email_address = kwargs.get('email_address', None)
        self.language = kwargs.get('language', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.reference = kwargs.get('reference', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        

    
    @property
    def id(self):
        """Gets the id of this SubscriberUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this SubscriberUpdate.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this SubscriberUpdate.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this SubscriberUpdate.
        :type: int
        """
        if id is None:
            raise ValueError("Invalid value for `id`, must not be `None`")

        self._id = id
    
    @property
    def version(self):
        """Gets the version of this SubscriberUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this SubscriberUpdate.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this SubscriberUpdate.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this SubscriberUpdate.
        :type: int
        """
        if version is None:
            raise ValueError("Invalid value for `version`, must not be `None`")

        self._version = version
    
    @property
    def additional_allowed_payment_method_configurations(self):
        """Gets the additional_allowed_payment_method_configurations of this SubscriberUpdate.

            Those payment methods which are allowed additionally will be available even when the product does not allow those methods.

        :return: The additional_allowed_payment_method_configurations of this SubscriberUpdate.
        :rtype: list[int]
        """
        return self._additional_allowed_payment_method_configurations

    @additional_allowed_payment_method_configurations.setter
    def additional_allowed_payment_method_configurations(self, additional_allowed_payment_method_configurations):
        """Sets the additional_allowed_payment_method_configurations of this SubscriberUpdate.

            Those payment methods which are allowed additionally will be available even when the product does not allow those methods.

        :param additional_allowed_payment_method_configurations: The additional_allowed_payment_method_configurations of this SubscriberUpdate.
        :type: list[int]
        """

        self._additional_allowed_payment_method_configurations = additional_allowed_payment_method_configurations
    
    @property
    def billing_address(self):
        """Gets the billing_address of this SubscriberUpdate.

            

        :return: The billing_address of this SubscriberUpdate.
        :rtype: AddressCreate
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this SubscriberUpdate.

            

        :param billing_address: The billing_address of this SubscriberUpdate.
        :type: AddressCreate
        """

        self._billing_address = billing_address
    
    @property
    def description(self):
        """Gets the description of this SubscriberUpdate.

            The subscriber description can be used to add a description to the subscriber. This is used in the back office to identify the subscriber.

        :return: The description of this SubscriberUpdate.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this SubscriberUpdate.

            The subscriber description can be used to add a description to the subscriber. This is used in the back office to identify the subscriber.

        :param description: The description of this SubscriberUpdate.
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")

        self._description = description
    
    @property
    def disallowed_payment_method_configurations(self):
        """Gets the disallowed_payment_method_configurations of this SubscriberUpdate.

            Those payment methods which are disallowed will not be available to the subscriber even if the product allows those methods.

        :return: The disallowed_payment_method_configurations of this SubscriberUpdate.
        :rtype: list[int]
        """
        return self._disallowed_payment_method_configurations

    @disallowed_payment_method_configurations.setter
    def disallowed_payment_method_configurations(self, disallowed_payment_method_configurations):
        """Sets the disallowed_payment_method_configurations of this SubscriberUpdate.

            Those payment methods which are disallowed will not be available to the subscriber even if the product allows those methods.

        :param disallowed_payment_method_configurations: The disallowed_payment_method_configurations of this SubscriberUpdate.
        :type: list[int]
        """

        self._disallowed_payment_method_configurations = disallowed_payment_method_configurations
    
    @property
    def email_address(self):
        """Gets the email_address of this SubscriberUpdate.

            The email address is used to communicate with the subscriber. There can be only one subscriber per space with the same email address.

        :return: The email_address of this SubscriberUpdate.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this SubscriberUpdate.

            The email address is used to communicate with the subscriber. There can be only one subscriber per space with the same email address.

        :param email_address: The email_address of this SubscriberUpdate.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def language(self):
        """Gets the language of this SubscriberUpdate.

            The subscriber language determines the language which is used to communicate with the subscriber in emails and documents (e.g. invoices).

        :return: The language of this SubscriberUpdate.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this SubscriberUpdate.

            The subscriber language determines the language which is used to communicate with the subscriber in emails and documents (e.g. invoices).

        :param language: The language of this SubscriberUpdate.
        :type: str
        """

        self._language = language
    
    @property
    def meta_data(self):
        """Gets the meta_data of this SubscriberUpdate.

            Allow to store additional information about the object.

        :return: The meta_data of this SubscriberUpdate.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this SubscriberUpdate.

            Allow to store additional information about the object.

        :param meta_data: The meta_data of this SubscriberUpdate.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def reference(self):
        """Gets the reference of this SubscriberUpdate.

            The subscriber reference identifies the subscriber in administrative interfaces (e.g. customer id).

        :return: The reference of this SubscriberUpdate.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this SubscriberUpdate.

            The subscriber reference identifies the subscriber in administrative interfaces (e.g. customer id).

        :param reference: The reference of this SubscriberUpdate.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this SubscriberUpdate.

            

        :return: The shipping_address of this SubscriberUpdate.
        :rtype: AddressCreate
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this SubscriberUpdate.

            

        :param shipping_address: The shipping_address of this SubscriberUpdate.
        :type: AddressCreate
        """

        self._shipping_address = shipping_address
    

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
        if issubclass(SubscriberUpdate, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, SubscriberUpdate):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
