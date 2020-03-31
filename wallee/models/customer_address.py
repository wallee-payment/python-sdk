# coding: utf-8
import pprint
import six
from enum import Enum



class CustomerAddress:

    swagger_types = {
    
        'address': 'CustomerPostalAddress',
        'address_type': 'CustomerAddressType',
        'created_on': 'datetime',
        'customer': 'Customer',
        'default_address': 'bool',
        'id': 'int',
        'linked_space_id': 'int',
        'version': 'int',
    }

    attribute_map = {
        'address': 'address','address_type': 'addressType','created_on': 'createdOn','customer': 'customer','default_address': 'defaultAddress','id': 'id','linked_space_id': 'linkedSpaceId','version': 'version',
    }

    
    _address = None
    _address_type = None
    _created_on = None
    _customer = None
    _default_address = None
    _id = None
    _linked_space_id = None
    _version = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.address = kwargs.get('address', None)
        self.address_type = kwargs.get('address_type', None)
        self.created_on = kwargs.get('created_on', None)
        self.customer = kwargs.get('customer', None)
        self.default_address = kwargs.get('default_address', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.version = kwargs.get('version', None)
        

    
    @property
    def address(self):
        """Gets the address of this CustomerAddress.

            

        :return: The address of this CustomerAddress.
        :rtype: CustomerPostalAddress
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this CustomerAddress.

            

        :param address: The address of this CustomerAddress.
        :type: CustomerPostalAddress
        """

        self._address = address
    
    @property
    def address_type(self):
        """Gets the address_type of this CustomerAddress.

            

        :return: The address_type of this CustomerAddress.
        :rtype: CustomerAddressType
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this CustomerAddress.

            

        :param address_type: The address_type of this CustomerAddress.
        :type: CustomerAddressType
        """

        self._address_type = address_type
    
    @property
    def created_on(self):
        """Gets the created_on of this CustomerAddress.

            The created on date indicates the date on which the entity was stored into the database.

        :return: The created_on of this CustomerAddress.
        :rtype: datetime
        """
        return self._created_on

    @created_on.setter
    def created_on(self, created_on):
        """Sets the created_on of this CustomerAddress.

            The created on date indicates the date on which the entity was stored into the database.

        :param created_on: The created_on of this CustomerAddress.
        :type: datetime
        """

        self._created_on = created_on
    
    @property
    def customer(self):
        """Gets the customer of this CustomerAddress.

            

        :return: The customer of this CustomerAddress.
        :rtype: Customer
        """
        return self._customer

    @customer.setter
    def customer(self, customer):
        """Sets the customer of this CustomerAddress.

            

        :param customer: The customer of this CustomerAddress.
        :type: Customer
        """

        self._customer = customer
    
    @property
    def default_address(self):
        """Gets the default_address of this CustomerAddress.

            

        :return: The default_address of this CustomerAddress.
        :rtype: bool
        """
        return self._default_address

    @default_address.setter
    def default_address(self, default_address):
        """Sets the default_address of this CustomerAddress.

            

        :param default_address: The default_address of this CustomerAddress.
        :type: bool
        """

        self._default_address = default_address
    
    @property
    def id(self):
        """Gets the id of this CustomerAddress.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :return: The id of this CustomerAddress.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this CustomerAddress.

            The ID is the primary key of the entity. The ID identifies the entity uniquely.

        :param id: The id of this CustomerAddress.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this CustomerAddress.

            The linked space id holds the ID of the space to which the entity belongs to.

        :return: The linked_space_id of this CustomerAddress.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this CustomerAddress.

            The linked space id holds the ID of the space to which the entity belongs to.

        :param linked_space_id: The linked_space_id of this CustomerAddress.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def version(self):
        """Gets the version of this CustomerAddress.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :return: The version of this CustomerAddress.
        :rtype: int
        """
        return self._version

    @version.setter
    def version(self, version):
        """Sets the version of this CustomerAddress.

            The version number indicates the version of the entity. The version is incremented whenever the entity is changed.

        :param version: The version of this CustomerAddress.
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
        if issubclass(CustomerAddress, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, CustomerAddress):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
