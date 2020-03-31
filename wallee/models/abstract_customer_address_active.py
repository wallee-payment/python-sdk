# coding: utf-8
import pprint
import six
from enum import Enum



class AbstractCustomerAddressActive:

    swagger_types = {
    
        'address': 'CustomerPostalAddressCreate',
        'address_type': 'CustomerAddressType',
    }

    attribute_map = {
        'address': 'address','address_type': 'addressType',
    }

    
    _address = None
    _address_type = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.address = kwargs.get('address', None)
        self.address_type = kwargs.get('address_type', None)
        

    
    @property
    def address(self):
        """Gets the address of this AbstractCustomerAddressActive.

            

        :return: The address of this AbstractCustomerAddressActive.
        :rtype: CustomerPostalAddressCreate
        """
        return self._address

    @address.setter
    def address(self, address):
        """Sets the address of this AbstractCustomerAddressActive.

            

        :param address: The address of this AbstractCustomerAddressActive.
        :type: CustomerPostalAddressCreate
        """

        self._address = address
    
    @property
    def address_type(self):
        """Gets the address_type of this AbstractCustomerAddressActive.

            

        :return: The address_type of this AbstractCustomerAddressActive.
        :rtype: CustomerAddressType
        """
        return self._address_type

    @address_type.setter
    def address_type(self, address_type):
        """Sets the address_type of this AbstractCustomerAddressActive.

            

        :param address_type: The address_type of this AbstractCustomerAddressActive.
        :type: CustomerAddressType
        """

        self._address_type = address_type
    

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
        if issubclass(AbstractCustomerAddressActive, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, AbstractCustomerAddressActive):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
