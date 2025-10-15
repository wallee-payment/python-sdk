# coding: utf-8
import pprint
import six
from enum import Enum



class ChargeFlowLevelPaymentLink:

    swagger_types = {
    
        'charge_flow_level': 'ChargeFlowLevel',
        'id': 'int',
        'linked_space_id': 'int',
        'payment_link': 'str',
    }

    attribute_map = {
        'charge_flow_level': 'chargeFlowLevel','id': 'id','linked_space_id': 'linkedSpaceId','payment_link': 'paymentLink',
    }

    
    _charge_flow_level = None
    _id = None
    _linked_space_id = None
    _payment_link = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.charge_flow_level = kwargs.get('charge_flow_level', None)
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.payment_link = kwargs.get('payment_link', None)
        

    
    @property
    def charge_flow_level(self):
        """Gets the charge_flow_level of this ChargeFlowLevelPaymentLink.

            The charge flow level that the payment link belongs to.

        :return: The charge_flow_level of this ChargeFlowLevelPaymentLink.
        :rtype: ChargeFlowLevel
        """
        return self._charge_flow_level

    @charge_flow_level.setter
    def charge_flow_level(self, charge_flow_level):
        """Sets the charge_flow_level of this ChargeFlowLevelPaymentLink.

            The charge flow level that the payment link belongs to.

        :param charge_flow_level: The charge_flow_level of this ChargeFlowLevelPaymentLink.
        :type: ChargeFlowLevel
        """

        self._charge_flow_level = charge_flow_level
    
    @property
    def id(self):
        """Gets the id of this ChargeFlowLevelPaymentLink.

            A unique identifier for the object.

        :return: The id of this ChargeFlowLevelPaymentLink.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this ChargeFlowLevelPaymentLink.

            A unique identifier for the object.

        :param id: The id of this ChargeFlowLevelPaymentLink.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this ChargeFlowLevelPaymentLink.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this ChargeFlowLevelPaymentLink.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this ChargeFlowLevelPaymentLink.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this ChargeFlowLevelPaymentLink.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def payment_link(self):
        """Gets the payment_link of this ChargeFlowLevelPaymentLink.

            The URL provided to the customer for entering their payment details and completing the transaction.

        :return: The payment_link of this ChargeFlowLevelPaymentLink.
        :rtype: str
        """
        return self._payment_link

    @payment_link.setter
    def payment_link(self, payment_link):
        """Sets the payment_link of this ChargeFlowLevelPaymentLink.

            The URL provided to the customer for entering their payment details and completing the transaction.

        :param payment_link: The payment_link of this ChargeFlowLevelPaymentLink.
        :type: str
        """

        self._payment_link = payment_link
    

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
        if issubclass(ChargeFlowLevelPaymentLink, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, ChargeFlowLevelPaymentLink):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
