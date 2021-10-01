# coding: utf-8
import pprint
import six
from enum import Enum



class Subscriber:

    swagger_types = {
    
        'additional_allowed_payment_method_configurations': 'list[int]',
        'billing_address': 'Address',
        'description': 'str',
        'disallowed_payment_method_configurations': 'list[int]',
        'email_address': 'str',
        'external_id': 'str',
        'id': 'int',
        'language': 'str',
        'linked_space_id': 'int',
        'meta_data': 'dict(str, str)',
        'planned_purge_date': 'datetime',
        'reference': 'str',
        'shipping_address': 'Address',
        'state': 'CreationEntityState',
        'version': 'int',
    }

    attribute_map = {
        'additional_allowed_payment_method_configurations': 'additionalAllowedPaymentMethodConfigurations','billing_address': 'billingAddress','description': 'description','disallowed_payment_method_configurations': 'disallowedPaymentMethodConfigurations','email_address': 'emailAddress','external_id': 'externalId','id': 'id','language': 'language','linked_space_id': 'linkedSpaceId','meta_data': 'metaData','planned_purge_date': 'plannedPurgeDate','reference': 'reference','shipping_address': 'shippingAddress','state': 'state','version': 'version',
    }

    
    _additional_allowed_payment_method_configurations = None
    _billing_address = None
    _description = None
    _disallowed_payment_method_configurations = None
    _email_address = None
    _external_id = None
    _id = None
    _language = None
    _linked_space_id = None
    _meta_data = None
    _planned_purge_date = None
    _reference = None
    _shipping_address = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.additional_allowed_payment_method_configurations = kwargs.get('additional_allowed_payment_method_configurations', None)
        self.billing_address = kwargs.get('billing_address', None)
        self.description = kwargs.get('description', None)
        self.disallowed_payment_method_configurations = kwargs.get('disallowed_payment_method_configurations', None)
        self.email_address = kwargs.get('email_address', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.language = kwargs.get('language', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.meta_data = kwargs.get('meta_data', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.reference = kwargs.get('reference', None)
        self.shipping_address = kwargs.get('shipping_address', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def additional_allowed_payment_method_configurations(self):
        """Gets the additional_allowed_payment_method_configurations of this Subscriber.

            Those payment methods which are allowed additionally will be available even when the product does not allow those methods.

        :return: The additional_allowed_payment_method_configurations of this Subscriber.
        :rtype: list[int]
        """
        return self._additional_allowed_payment_method_configurations

    @additional_allowed_payment_method_configurations.setter
    def additional_allowed_payment_method_configurations(self, additional_allowed_payment_method_configurations):
        """Sets the additional_allowed_payment_method_configurations of this Subscriber.

            Those payment methods which are allowed additionally will be available even when the product does not allow those methods.

        :param additional_allowed_payment_method_configurations: The additional_allowed_payment_method_configurations of this Subscriber.
        :type: list[int]
        """

        self._additional_allowed_payment_method_configurations = additional_allowed_payment_method_configurations
    
    @property
    def billing_address(self):
        """Gets the billing_address of this Subscriber.

            

        :return: The billing_address of this Subscriber.
        :rtype: Address
        """
        return self._billing_address

    @billing_address.setter
    def billing_address(self, billing_address):
        """Sets the billing_address of this Subscriber.

            

        :param billing_address: The billing_address of this Subscriber.
        :type: Address
        """

        self._billing_address = billing_address
    
    @property
    def description(self):
        """Gets the description of this Subscriber.

            The subscriber description can be used to add a description to the subscriber. This is used in the back office to identify the subscriber.

        :return: The description of this Subscriber.
        :rtype: str
        """
        return self._description

    @description.setter
    def description(self, description):
        """Sets the description of this Subscriber.

            The subscriber description can be used to add a description to the subscriber. This is used in the back office to identify the subscriber.

        :param description: The description of this Subscriber.
        :type: str
        """
        if description is not None and len(description) > 200:
            raise ValueError("Invalid value for `description`, length must be less than or equal to `200`")

        self._description = description
    
    @property
    def disallowed_payment_method_configurations(self):
        """Gets the disallowed_payment_method_configurations of this Subscriber.

            Those payment methods which are disallowed will not be available to the subscriber even if the product allows those methods.

        :return: The disallowed_payment_method_configurations of this Subscriber.
        :rtype: list[int]
        """
        return self._disallowed_payment_method_configurations

    @disallowed_payment_method_configurations.setter
    def disallowed_payment_method_configurations(self, disallowed_payment_method_configurations):
        """Sets the disallowed_payment_method_configurations of this Subscriber.

            Those payment methods which are disallowed will not be available to the subscriber even if the product allows those methods.

        :param disallowed_payment_method_configurations: The disallowed_payment_method_configurations of this Subscriber.
        :type: list[int]
        """

        self._disallowed_payment_method_configurations = disallowed_payment_method_configurations
    
    @property
    def email_address(self):
        """Gets the email_address of this Subscriber.

            The email address is used to communicate with the subscriber. There can be only one subscriber per space with the same email address.

        :return: The email_address of this Subscriber.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this Subscriber.

            The email address is used to communicate with the subscriber. There can be only one subscriber per space with the same email address.

        :param email_address: The email_address of this Subscriber.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def external_id(self):
        """Gets the external_id of this Subscriber.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this Subscriber.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this Subscriber.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this Subscriber.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this Subscriber.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this Subscriber.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this Subscriber.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this Subscriber.
        :type: int
        """

        self._id = id
    
    @property
    def language(self):
        """Gets the language of this Subscriber.

            The subscriber language determines the language which is used to communicate with the subscriber in emails and documents (e.g. invoices).

        :return: The language of this Subscriber.
        :rtype: str
        """
        return self._language

    @language.setter
    def language(self, language):
        """Sets the language of this Subscriber.

            The subscriber language determines the language which is used to communicate with the subscriber in emails and documents (e.g. invoices).

        :param language: The language of this Subscriber.
        :type: str
        """

        self._language = language
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this Subscriber.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this Subscriber.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this Subscriber.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this Subscriber.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def meta_data(self):
        """Gets the meta_data of this Subscriber.

            Meta data allow to store additional data along the object.

        :return: The meta_data of this Subscriber.
        :rtype: dict(str, str)
        """
        return self._meta_data

    @meta_data.setter
    def meta_data(self, meta_data):
        """Sets the meta_data of this Subscriber.

            Meta data allow to store additional data along the object.

        :param meta_data: The meta_data of this Subscriber.
        :type: dict(str, str)
        """

        self._meta_data = meta_data
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this Subscriber.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this Subscriber.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this Subscriber.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this Subscriber.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def reference(self):
        """Gets the reference of this Subscriber.

            The subscriber reference identifies the subscriber in administrative interfaces (e.g. customer id).

        :return: The reference of this Subscriber.
        :rtype: str
        """
        return self._reference

    @reference.setter
    def reference(self, reference):
        """Sets the reference of this Subscriber.

            The subscriber reference identifies the subscriber in administrative interfaces (e.g. customer id).

        :param reference: The reference of this Subscriber.
        :type: str
        """
        if reference is not None and len(reference) > 100:
            raise ValueError("Invalid value for `reference`, length must be less than or equal to `100`")

        self._reference = reference
    
    @property
    def shipping_address(self):
        """Gets the shipping_address of this Subscriber.

            

        :return: The shipping_address of this Subscriber.
        :rtype: Address
        """
        return self._shipping_address

    @shipping_address.setter
    def shipping_address(self, shipping_address):
        """Sets the shipping_address of this Subscriber.

            

        :param shipping_address: The shipping_address of this Subscriber.
        :type: Address
        """

        self._shipping_address = shipping_address
    
    @property
    def state(self):
        """Gets the state of this Subscriber.

            

        :return: The state of this Subscriber.
        :rtype: CreationEntityState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this Subscriber.

            

        :param state: The state of this Subscriber.
        :type: CreationEntityState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this Subscriber.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this Subscriber.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this Subscriber.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this Subscriber.
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
        if issubclass(Subscriber, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, Subscriber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
