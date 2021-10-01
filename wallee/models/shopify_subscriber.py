# coding: utf-8
import pprint
import six
from enum import Enum



class ShopifySubscriber:

    swagger_types = {
    
        'created_on': 'datetime',
        'email_address': 'str',
        'external_id': 'str',
        'id': 'int',
        'linked_space_id': 'int',
        'phone_number': 'str',
        'planned_purge_date': 'datetime',
        'shop': 'int',
        'state': 'ShopifySubscriberState',
        'version': 'int',
    }

    attribute_map = {
        'created_on': 'createdOn','email_address': 'emailAddress','external_id': 'externalId','id': 'id','linked_space_id': 'linkedSpaceId','phone_number': 'phoneNumber','planned_purge_date': 'plannedPurgeDate','shop': 'shop','state': 'state','version': 'version',
    }

    
    _created_on = None
    _email_address = None
    _external_id = None
    _id = None
    _linked_space_id = None
    _phone_number = None
    _planned_purge_date = None
    _shop = None
    _state = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.created_on = kwargs.get('created_on', None)
        self.email_address = kwargs.get('email_address', None)
        self.external_id = kwargs.get('external_id', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.phone_number = kwargs.get('phone_number', None)
        self.planned_purge_date = kwargs.get('planned_purge_date', None)
        self.shop = kwargs.get('shop', None)
        self.state = kwargs.get('state', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def created_on(self):
        """Gets the created_on of this ShopifySubscriber.

            

        :return: The created_on of this ShopifySubscriber.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this ShopifySubscriber.

            

        :param created_on: The created_on of this ShopifySubscriber.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def email_address(self):
        """Gets the email_address of this ShopifySubscriber.

            

        :return: The email_address of this ShopifySubscriber.
        :rtype: str
        """
        return self._email_address

    @email_address.setter
    def email_address(self, email_address):
        """Sets the email_address of this ShopifySubscriber.

            

        :param email_address: The email_address of this ShopifySubscriber.
        :type: str
        """
        if email_address is not None and len(email_address) > 254:
            raise ValueError("Invalid value for `email_address`, length must be less than or equal to `254`")

        self._email_address = email_address
    
    @property
    def external_id(self):
        """Gets the external_id of this ShopifySubscriber.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :return: The external_id of this ShopifySubscriber.
        :rtype: str
        """
        return self._external_id

    @external_id.setter
    def external_id(self, external_id):
        """Sets the external_id of this ShopifySubscriber.

            A client generated nonce which identifies the entity to be created. Subsequent creation requests with the same external ID will not create new entities but return the initially created entity instead.

        :param external_id: The external_id of this ShopifySubscriber.
        :type: str
        """

        self._external_id = external_id
    
    @property
    def id(self):
        """Gets the id of this ShopifySubscriber.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this ShopifySubscriber.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ShopifySubscriber.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this ShopifySubscriber.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ShopifySubscriber.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this ShopifySubscriber.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ShopifySubscriber.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this ShopifySubscriber.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def phone_number(self):
        """Gets the phone_number of this ShopifySubscriber.

            

        :return: The phone_number of this ShopifySubscriber.
        :rtype: str
        """
        return self._phone_number

    @phone_number.setter
    def phone_number(self, phone_number):
        """Sets the phone_number of this ShopifySubscriber.

            

        :param phone_number: The phone_number of this ShopifySubscriber.
        :type: str
        """
        if phone_number is not None and len(phone_number) > 254:
            raise ValueError("Invalid value for `phone_number`, length must be less than or equal to `254`")

        self._phone_number = phone_number
    
    @property
    def planned_purge_date(self):
        """Gets the planned_purge_date of this ShopifySubscriber.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :return: The planned_purge_date of this ShopifySubscriber.
        :rtype: datetime
        """
        return self._planned_purge_date

    @planned_purge_date.setter
    def planned_purge_date(self, planned_purge_date):
        """Sets the planned_purge_date of this ShopifySubscriber.

            The planned purge date indicates when the entity is permanently removed. When the date is null the entity is not planned to be removed.

        :param planned_purge_date: The planned_purge_date of this ShopifySubscriber.
        :type: datetime
        """

        self._planned_purge_date = planned_purge_date
    
    @property
    def shop(self):
        """Gets the shop of this ShopifySubscriber.

            

        :return: The shop of this ShopifySubscriber.
        :rtype: int
        """
        return self._shop

    @shop.setter
    def shop(self, shop):
        """Sets the shop of this ShopifySubscriber.

            

        :param shop: The shop of this ShopifySubscriber.
        :type: int
        """

        self._shop = shop
    
    @property
    def state(self):
        """Gets the state of this ShopifySubscriber.

            

        :return: The state of this ShopifySubscriber.
        :rtype: ShopifySubscriberState
        """
        return self._state

    @state.setter
    def state(self, state):
        """Sets the state of this ShopifySubscriber.

            

        :param state: The state of this ShopifySubscriber.
        :type: ShopifySubscriberState
        """

        self._state = state
    
    @property
    def version(self):
        """Gets the version of this ShopifySubscriber.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this ShopifySubscriber.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this ShopifySubscriber.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this ShopifySubscriber.
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
        if issubclass(ShopifySubscriber, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ShopifySubscriber):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
