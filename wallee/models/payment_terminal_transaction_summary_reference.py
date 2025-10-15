# coding: utf-8
import pprint
import six
from enum import Enum



class PaymentTerminalTransactionSummaryReference:

    swagger_types = {
    
        'id': 'int',
        'linked_space_id': 'int',
        'terminal_id': 'int',
        'terminal_identifier': 'str',
    }

    attribute_map = {
        'id': 'id','linked_space_id': 'linkedSpaceId','terminal_id': 'terminalId','terminal_identifier': 'terminalIdentifier',
    }

    
    _id = None
    _linked_space_id = None
    _terminal_id = None
    _terminal_identifier = None

    def __init__(self, **kwargs):
        self.discriminator = None
        
        self.id = kwargs.get('id', None)
        self.linked_space_id = kwargs.get('linked_space_id', None)
        self.terminal_id = kwargs.get('terminal_id', None)
        self.terminal_identifier = kwargs.get('terminal_identifier', None)
        

    
    @property
    def id(self):
        """Gets the id of this PaymentTerminalTransactionSummaryReference.

            A unique identifier for the object.

        :return: The id of this PaymentTerminalTransactionSummaryReference.
        :rtype: int
        """
        return self._id

    @id.setter
    def id(self, id):
        """Sets the id of this PaymentTerminalTransactionSummaryReference.

            A unique identifier for the object.

        :param id: The id of this PaymentTerminalTransactionSummaryReference.
        :type: int
        """

        self._id = id
    
    @property
    def linked_space_id(self):
        """Gets the linked_space_id of this PaymentTerminalTransactionSummaryReference.

            The ID of the space this object belongs to.

        :return: The linked_space_id of this PaymentTerminalTransactionSummaryReference.
        :rtype: int
        """
        return self._linked_space_id

    @linked_space_id.setter
    def linked_space_id(self, linked_space_id):
        """Sets the linked_space_id of this PaymentTerminalTransactionSummaryReference.

            The ID of the space this object belongs to.

        :param linked_space_id: The linked_space_id of this PaymentTerminalTransactionSummaryReference.
        :type: int
        """

        self._linked_space_id = linked_space_id
    
    @property
    def terminal_id(self):
        """Gets the terminal_id of this PaymentTerminalTransactionSummaryReference.

            The unique identifier of the terminal.

        :return: The terminal_id of this PaymentTerminalTransactionSummaryReference.
        :rtype: int
        """
        return self._terminal_id

    @terminal_id.setter
    def terminal_id(self, terminal_id):
        """Sets the terminal_id of this PaymentTerminalTransactionSummaryReference.

            The unique identifier of the terminal.

        :param terminal_id: The terminal_id of this PaymentTerminalTransactionSummaryReference.
        :type: int
        """

        self._terminal_id = terminal_id
    
    @property
    def terminal_identifier(self):
        """Gets the terminal_identifier of this PaymentTerminalTransactionSummaryReference.

            The unique identifier of the terminal, that is displayed on the device.

        :return: The terminal_identifier of this PaymentTerminalTransactionSummaryReference.
        :rtype: str
        """
        return self._terminal_identifier

    @terminal_identifier.setter
    def terminal_identifier(self, terminal_identifier):
        """Sets the terminal_identifier of this PaymentTerminalTransactionSummaryReference.

            The unique identifier of the terminal, that is displayed on the device.

        :param terminal_identifier: The terminal_identifier of this PaymentTerminalTransactionSummaryReference.
        :type: str
        """

        self._terminal_identifier = terminal_identifier
    

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
        if issubclass(PaymentTerminalTransactionSummaryReference, dict):
            for key, value in self.items():
                result[key] = value

        return result

    def to_str(self):
        return pprint.pformat(self.to_dict())

    def __repr__(self):
        return self.to_str()

    def __eq__(self, other):
        if not isinstance(other, PaymentTerminalTransactionSummaryReference):
            return False

        return self.__dict__ == other.__dict__

    def __ne__(self, other):
        return not self == other
